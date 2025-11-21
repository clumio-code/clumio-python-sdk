#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
import re
from typing import Any, Iterator, Optional, Union
import urllib.parse

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import aws_ec2_instances_types
from clumioapi.controllers.types import aws_s3_buckets_v1_bucket_matcher_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_ec2_instances_response
from clumioapi.models import read_ec2_instance_response
import requests
import retrying


class AwsEc2InstancesV1Controller:
    """A Controller to access Endpoints for aws-ec2-instances resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.aws-ec2-instances=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_aws_ec2_instances(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: aws_ec2_instances_types.ListAwsEc2InstancesV1FilterT | None = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> list_ec2_instances_response.ListEc2InstancesResponse:
        """Returns a list of EC2 instances.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following
                table lists the supported filter fields for this resource and the filter
                conditions that can
                be applied on those fields:

                +---------------------------+------------------+-------------------------------+
                |           Field           | Filter Condition |          Description          |
                +===========================+==================+===============================+
                | environment_id            | $eq              | The Clumio-assigned ID of the |
                |                           |                  | AWS environment.              |
                +---------------------------+------------------+-------------------------------+
                | name                      | $contains, $eq   | The AWS-assigned name of this |
                |                           |                  | resource to conditionalize    |
                |                           |                  | on. For example,              |
                |                           |                  | filter={"name":{"$contains":" |
                |                           |                  | dev"}} retrieves all EC2      |
                |                           |                  | instances with "dev" in       |
                |                           |                  | their name.                   |
                |                           |                  | filter={"name":{"$eq":"dev"}} |
                |                           |                  | retrieves only EC2 instances  |
                |                           |                  | with names that               |
                |                           |                  | exactly match "dev"           |
                +---------------------------+------------------+-------------------------------+
                | instance_native_id        | $eq, $contains   | The AWS-assigned ID of the    |
                |                           |                  | EC2 instance.                 |
                |                           |                  | For example, filter={"instanc |
                |                           |                  | e_native_id":{"$eq":"i-       |
                |                           |                  | 07aa02a849fe376d0"}} or       |
                |                           |                  | filter={"instance_native_id": |
                |                           |                  | {"$contains":"2a849fe37"}}    |
                |                           |                  | Both filter operations cannot |
                |                           |                  | be used simultaneously.       |
                |                           |                  |                               |
                +---------------------------+------------------+-------------------------------+
                | account_native_id         | $eq              | The AWS-assigned ID of the    |
                |                           |                  | AWS account. For example,     |
                |                           |                  | filter={"account_native_id":{ |
                |                           |                  | "$eq":"789901323485"}}        |
                +---------------------------+------------------+-------------------------------+
                | aws_region                | $eq              | The AWS region of a given     |
                |                           |                  | account to which this         |
                |                           |                  | resource belongs. For         |
                |                           |                  | example,                      |
                |                           |                  | filter={"aws_region":{"$eq":" |
                |                           |                  | us-east-1"}}                  |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $in              | The protection status of the  |
                |                           |                  | EC2 instance. Possible values |
                |                           |                  | include "protected",          |
                |                           |                  | "unprotected", and            |
                |                           |                  | "unsupported". For example,   |
                |                           |                  | filter={"protection_status":{ |
                |                           |                  | "$in":["protected"]}}         |
                +---------------------------+------------------+-------------------------------+
                | backup_status             | $in              | The backup status of this     |
                |                           |                  | resource. Possible values     |
                |                           |                  | include success,              |
                |                           |                  | partial_success, failure and  |
                |                           |                  | no_backup.                    |
                +---------------------------+------------------+-------------------------------+
                | deactivated               | $eq              | Filter assets protected by a  |
                |                           |                  | deactivated policy.           |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | The Clumio-assigned ID of the |
                |                           |                  | policy protecting this        |
                |                           |                  | resource.                     |
                |                           |                  | filter={"protection_info.poli |
                |                           |                  | cy_id":{"$eq":"c764abb6-5819- |
                |                           |                  | 16ea-bb9f-b2e1c9a040ad"}}     |
                +---------------------------+------------------+-------------------------------+
                | tags.id                   | $all             | The ID of the AWS tag applied |
                |                           |                  | to the EC2 instance. For      |
                |                           |                  | example,                      |
                |                           |                  | filter={"tags.id":{"$all":["c |
                |                           |                  | 764b152-5819-11ea-bb9f-       |
                |                           |                  | b2e1c9a040ad","c764abb6-5819- |
                |                           |                  | 11ea-bb9f-b2e1c9a040ad"]}}.   |
                |                           |                  | If multiple tags are          |
                |                           |                  | specified, all of them must   |
                |                           |                  | be applied to the same EC2    |
                |                           |                  | instance.                     |
                +---------------------------+------------------+-------------------------------+
                | is_deleted                | $eq, $in         | The deletion status of the    |
                |                           |                  | EC2 instance. Default value   |
                |                           |                  | is "false". Set to "true" to  |
                |                           |                  | retrieve deleted EC2          |
                |                           |                  | instance. For example, filter |
                |                           |                  | ={"is_deleted":{"$eq":true}}  |
                |                           |                  | filter={"is_deleted":{"$in":[ |
                |                           |                  | "true","false"]}}             |
                +---------------------------+------------------+-------------------------------+
                | availability_zone         | $eq              | The AWS availability zone.    |
                |                           |                  | For example,                  |
                |                           |                  | filter={"availability_zone":{ |
                |                           |                  | "$eq":"us-east-1a"}}          |
                +---------------------------+------------------+-------------------------------+

                For more information about filtering, refer to the Filtering section
                of this guide.
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following
                embeddable links to include additional details associated with each resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the associated policy of a protected EC2     |
                |                        | instance into the response. For                     |
                |                        | example, embed=read-policy-definition               |
                +------------------------+-----------------------------------------------------+

                For more information about embedded links, refer to the Embedding
                Referenced Resources section of this guide.
            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_ec2_instances_response.ListEc2InstancesResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/aws/ec2-instances'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
            'embed': embed,
            'lookback_days': lookback_days,
        }

        resp_instance: list_ec2_instances_response.ListEc2InstancesResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'list_aws_ec2_instances for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_aws_ec2_instance(
        self,
        instance_id: str | None = None,
        lookback_days: int | None = None,
        embed: str | None = None,
        **kwargs,
    ) -> read_ec2_instance_response.ReadEc2InstanceResponse:
        """Returns a representation of the specified EC2 instance.

        Args:
            instance_id:
                Performs the operation on the EC2 instance with the specified ID.
            lookback_days:
                Calculate backup status for the last `lookback_days` days.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the associated policy of a protected EC2     |
                |                        | instance into the response. For example,            |
                |                        | embed=read-policy-definition                        |
                +------------------------+-----------------------------------------------------+

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_ec2_instance_response.ReadEc2InstanceResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/aws/ec2-instances/{instance_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'instance_id': instance_id}
        )

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'lookback_days': lookback_days,
            'embed': embed,
        }

        resp_instance: read_ec2_instance_response.ReadEc2InstanceResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'read_aws_ec2_instance for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class AwsEc2InstancesV1ControllerPaginator:
    """A Controller to access Endpoints for aws-ec2-instances resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_aws_ec2_instances(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: aws_ec2_instances_types.ListAwsEc2InstancesV1FilterT | None = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> Iterator[list_ec2_instances_response.ListEc2InstancesResponse]:
        """Returns a list of EC2 instances.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following
                table lists the supported filter fields for this resource and the filter
                conditions that can
                be applied on those fields:

                +---------------------------+------------------+-------------------------------+
                |           Field           | Filter Condition |          Description          |
                +===========================+==================+===============================+
                | environment_id            | $eq              | The Clumio-assigned ID of the |
                |                           |                  | AWS environment.              |
                +---------------------------+------------------+-------------------------------+
                | name                      | $contains, $eq   | The AWS-assigned name of this |
                |                           |                  | resource to conditionalize    |
                |                           |                  | on. For example,              |
                |                           |                  | filter={"name":{"$contains":" |
                |                           |                  | dev"}} retrieves all EC2      |
                |                           |                  | instances with "dev" in       |
                |                           |                  | their name.                   |
                |                           |                  | filter={"name":{"$eq":"dev"}} |
                |                           |                  | retrieves only EC2 instances  |
                |                           |                  | with names that               |
                |                           |                  | exactly match "dev"           |
                +---------------------------+------------------+-------------------------------+
                | instance_native_id        | $eq, $contains   | The AWS-assigned ID of the    |
                |                           |                  | EC2 instance.                 |
                |                           |                  | For example, filter={"instanc |
                |                           |                  | e_native_id":{"$eq":"i-       |
                |                           |                  | 07aa02a849fe376d0"}} or       |
                |                           |                  | filter={"instance_native_id": |
                |                           |                  | {"$contains":"2a849fe37"}}    |
                |                           |                  | Both filter operations cannot |
                |                           |                  | be used simultaneously.       |
                |                           |                  |                               |
                +---------------------------+------------------+-------------------------------+
                | account_native_id         | $eq              | The AWS-assigned ID of the    |
                |                           |                  | AWS account. For example,     |
                |                           |                  | filter={"account_native_id":{ |
                |                           |                  | "$eq":"789901323485"}}        |
                +---------------------------+------------------+-------------------------------+
                | aws_region                | $eq              | The AWS region of a given     |
                |                           |                  | account to which this         |
                |                           |                  | resource belongs. For         |
                |                           |                  | example,                      |
                |                           |                  | filter={"aws_region":{"$eq":" |
                |                           |                  | us-east-1"}}                  |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $in              | The protection status of the  |
                |                           |                  | EC2 instance. Possible values |
                |                           |                  | include "protected",          |
                |                           |                  | "unprotected", and            |
                |                           |                  | "unsupported". For example,   |
                |                           |                  | filter={"protection_status":{ |
                |                           |                  | "$in":["protected"]}}         |
                +---------------------------+------------------+-------------------------------+
                | backup_status             | $in              | The backup status of this     |
                |                           |                  | resource. Possible values     |
                |                           |                  | include success,              |
                |                           |                  | partial_success, failure and  |
                |                           |                  | no_backup.                    |
                +---------------------------+------------------+-------------------------------+
                | deactivated               | $eq              | Filter assets protected by a  |
                |                           |                  | deactivated policy.           |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | The Clumio-assigned ID of the |
                |                           |                  | policy protecting this        |
                |                           |                  | resource.                     |
                |                           |                  | filter={"protection_info.poli |
                |                           |                  | cy_id":{"$eq":"c764abb6-5819- |
                |                           |                  | 16ea-bb9f-b2e1c9a040ad"}}     |
                +---------------------------+------------------+-------------------------------+
                | tags.id                   | $all             | The ID of the AWS tag applied |
                |                           |                  | to the EC2 instance. For      |
                |                           |                  | example,                      |
                |                           |                  | filter={"tags.id":{"$all":["c |
                |                           |                  | 764b152-5819-11ea-bb9f-       |
                |                           |                  | b2e1c9a040ad","c764abb6-5819- |
                |                           |                  | 11ea-bb9f-b2e1c9a040ad"]}}.   |
                |                           |                  | If multiple tags are          |
                |                           |                  | specified, all of them must   |
                |                           |                  | be applied to the same EC2    |
                |                           |                  | instance.                     |
                +---------------------------+------------------+-------------------------------+
                | is_deleted                | $eq, $in         | The deletion status of the    |
                |                           |                  | EC2 instance. Default value   |
                |                           |                  | is "false". Set to "true" to  |
                |                           |                  | retrieve deleted EC2          |
                |                           |                  | instance. For example, filter |
                |                           |                  | ={"is_deleted":{"$eq":true}}  |
                |                           |                  | filter={"is_deleted":{"$in":[ |
                |                           |                  | "true","false"]}}             |
                +---------------------------+------------------+-------------------------------+
                | availability_zone         | $eq              | The AWS availability zone.    |
                |                           |                  | For example,                  |
                |                           |                  | filter={"availability_zone":{ |
                |                           |                  | "$eq":"us-east-1a"}}          |
                +---------------------------+------------------+-------------------------------+

                For more information about filtering, refer to the Filtering section
                of this guide.
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following
                embeddable links to include additional details associated with each resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the associated policy of a protected EC2     |
                |                        | instance into the response. For                     |
                |                        | example, embed=read-policy-definition               |
                +------------------------+-----------------------------------------------------+

                For more information about embedded links, refer to the Embedding
                Referenced Resources section of this guide.
            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        """
        controller = AwsEc2InstancesV1Controller(self.controller)
        while True:
            response = controller.list_aws_ec2_instances(
                limit=limit,
                start=start,
                filter=filter,
                embed=embed,
                lookback_days=lookback_days,
                **kwargs,
            )
            yield response
            next_link = response.Links.Next  # type: ignore
            if not next_link:
                break
            next_link = next_link.Href
            if match := re.search(r'start=([^&]+)', next_link):  # type: ignore
                start = match.group(1)
            else:
                raise clumio_exception.ClumioException(
                    'Next link is malformed. Please contact clumio support.'
                )
