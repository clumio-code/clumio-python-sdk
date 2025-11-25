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
from clumioapi.controllers.types import aws_environments_types
from clumioapi.controllers.types import aws_s3_buckets_v1_bucket_matcher_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_aws_environments_response
from clumioapi.models import read_aws_environment_response
import requests
import retrying


class AwsEnvironmentsV1Controller:
    """A Controller to access Endpoints for aws-environments resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.aws-environments=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_aws_environments(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: aws_environments_types.ListAwsEnvironmentsV1FilterT | None = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> list_aws_environments_response.ListAWSEnvironmentsResponse:
        """Returns a list of AWS environments.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +-------------------+-------------------+--------------------------------------+
                |       Field       | Filter Condition  |             Description              |
                +===================+===================+======================================+
                | account_native_id | $eq, $begins_with | The AWS-assigned ID of the account   |
                |                   |                   | associated with the environment. For |
                |                   |                   | example, filter={"account_native_id" |
                |                   |                   | :{"$eq":"891106098885"}}             |
                +-------------------+-------------------+--------------------------------------+
                | aws_region        | $eq               | The AWS region associated with the   |
                |                   |                   | environment. For example,            |
                |                   |                   | filter={"aws_region":{"$eq":"us-     |
                |                   |                   | west-2"}}.                           |
                +-------------------+-------------------+--------------------------------------+
                | connection_status | $eq               | The status of the connection to the  |
                |                   |                   | environment, which is mediated by a  |
                |                   |                   | CloudFormation stack. Possible       |
                |                   |                   | values include "installed". For      |
                |                   |                   | example, filter={"connection_status" |
                |                   |                   | :{"$eq":"installed"}}                |
                +-------------------+-------------------+--------------------------------------+
                | services_enabled  | $contains         | The AWS services enabled for this    |
                |                   |                   | environment. This is case            |
                |                   |                   | insensitive. Possible values include |
                |                   |                   | "EBS", "RDS" and "DynamoDB". For     |
                |                   |                   | example, filter={"services_enabled": |
                |                   |                   | {"$contains":"RDS"}}.                |
                +-------------------+-------------------+--------------------------------------+


            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-aws-environment-ebs-volumes-     | Embeds protection stats about EBS    |
                | protection-stats                      | Volumes for each AWS environment     |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-ebs-      |
                |                                       | volumes-protection-stats             |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-ec2-instances-   | Embeds protection stats about EC2    |
                | protection-stats                      | Instance for each AWS environment    |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-          |
                |                                       | ec2-instances-protection-stats       |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-ec2-mssql-       | Embeds protection stats about EC2    |
                | protection-stats                      | MSSQL for each AWS environment into  |
                |                                       | the response. For example,           |
                |                                       | embed=read-aws-environment-          |
                |                                       | ec2-mssql-protection-stats           |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-rds-resources-   | Embeds protection stats about RDS    |
                | protection-stats                      | Instance for each AWS environment    |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-rds-      |
                |                                       | resources-protection-stats           |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-dynamodb-tables- | Embeds protection stats about        |
                | protection-stats                      | DynamoDB tables for each AWS         |
                |                                       | environment into the response. For   |
                |                                       | example, embed=read-aws-environment- |
                |                                       | dynamodb-tables-protection-stats     |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-protection-      | Embeds protection stats about        |
                | groups-protection-stats               | Protection Group for each AWS        |
                |                                       | environment into the response. For   |
                |                                       | example, embed=read-aws-environment- |
                |                                       | protection-groups-protection-stats   |
                +---------------------------------------+--------------------------------------+
                | read-aws-environments-backup-status-  | Embeds backup statistics for each    |
                | stats                                 | AWS environment into the response.   |
                |                                       | For example, embed=read-aws-         |
                |                                       | environments-backup-status-stats     |
                +---------------------------------------+--------------------------------------+

            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_aws_environments_response.ListAWSEnvironmentsResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/aws/environments'

        if start:
            _url_path = f'{_url_path}?start={start}'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'filter': filter.query_str if filter else None,
            'embed': embed,
            'lookback_days': lookback_days,
        }

        resp_instance: list_aws_environments_response.ListAWSEnvironmentsResponse
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
            error_str = f'list_aws_environments for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_aws_environment(
        self,
        environment_id: str | None = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> read_aws_environment_response.ReadAWSEnvironmentResponse:
        """Returns a representation of the specified AWS environment.

        Args:
            environment_id:
                Performs the operation on the environment with the specified ID.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-aws-environment-ebs-volumes-     | Embeds protection stats about EBS    |
                | protection-stats                      | Volumes for each AWS environment     |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-ebs-      |
                |                                       | volumes-protection-stats             |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-ec2-instances-   | Embeds protection stats about EC2    |
                | protection-stats                      | Instance for each AWS environment    |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-          |
                |                                       | ec2-instances-protection-stats       |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-ec2-mssql-       | Embeds protection stats about EC2    |
                | protection-stats                      | MSSQL for each AWS environment into  |
                |                                       | the response. For example,           |
                |                                       | embed=read-aws-environment-          |
                |                                       | ec2-mssql-protection-stats           |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-rds-resources-   | Embeds protection stats about RDS    |
                | protection-stats                      | Instance for each AWS environment    |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-rds-      |
                |                                       | resources-protection-stats           |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-dynamodb-tables- | Embeds protection stats about        |
                | protection-stats                      | DynamoDB tables for each AWS         |
                |                                       | environment into the response. For   |
                |                                       | example, embed=read-aws-environment- |
                |                                       | dynamodb-tables-protection-stats     |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-protection-      | Embeds protection stats about        |
                | groups-protection-stats               | Protection Group for each AWS        |
                |                                       | environment into the response. For   |
                |                                       | example, embed=read-aws-environment- |
                |                                       | protection-groups-protection-stats   |
                +---------------------------------------+--------------------------------------+
                | read-aws-environments-backup-status-  | Embeds backup statistics for each    |
                | stats                                 | AWS environment into the response.   |
                |                                       | For example, embed=read-aws-         |
                |                                       | environments-backup-status-stats     |
                +---------------------------------------+--------------------------------------+

            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_aws_environment_response.ReadAWSEnvironmentResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/aws/environments/{environment_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'environment_id': environment_id}
        )

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'embed': embed,
            'lookback_days': lookback_days,
        }

        resp_instance: read_aws_environment_response.ReadAWSEnvironmentResponse
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
            error_str = f'read_aws_environment for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class AwsEnvironmentsV1ControllerPaginator:
    """A Controller to access Endpoints for aws-environments resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_aws_environments(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: aws_environments_types.ListAwsEnvironmentsV1FilterT | None = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> Iterator[list_aws_environments_response.ListAWSEnvironmentsResponse]:
        """Returns a list of AWS environments.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +-------------------+-------------------+--------------------------------------+
                |       Field       | Filter Condition  |             Description              |
                +===================+===================+======================================+
                | account_native_id | $eq, $begins_with | The AWS-assigned ID of the account   |
                |                   |                   | associated with the environment. For |
                |                   |                   | example, filter={"account_native_id" |
                |                   |                   | :{"$eq":"891106098885"}}             |
                +-------------------+-------------------+--------------------------------------+
                | aws_region        | $eq               | The AWS region associated with the   |
                |                   |                   | environment. For example,            |
                |                   |                   | filter={"aws_region":{"$eq":"us-     |
                |                   |                   | west-2"}}.                           |
                +-------------------+-------------------+--------------------------------------+
                | connection_status | $eq               | The status of the connection to the  |
                |                   |                   | environment, which is mediated by a  |
                |                   |                   | CloudFormation stack. Possible       |
                |                   |                   | values include "installed". For      |
                |                   |                   | example, filter={"connection_status" |
                |                   |                   | :{"$eq":"installed"}}                |
                +-------------------+-------------------+--------------------------------------+
                | services_enabled  | $contains         | The AWS services enabled for this    |
                |                   |                   | environment. This is case            |
                |                   |                   | insensitive. Possible values include |
                |                   |                   | "EBS", "RDS" and "DynamoDB". For     |
                |                   |                   | example, filter={"services_enabled": |
                |                   |                   | {"$contains":"RDS"}}.                |
                +-------------------+-------------------+--------------------------------------+


            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-aws-environment-ebs-volumes-     | Embeds protection stats about EBS    |
                | protection-stats                      | Volumes for each AWS environment     |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-ebs-      |
                |                                       | volumes-protection-stats             |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-ec2-instances-   | Embeds protection stats about EC2    |
                | protection-stats                      | Instance for each AWS environment    |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-          |
                |                                       | ec2-instances-protection-stats       |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-ec2-mssql-       | Embeds protection stats about EC2    |
                | protection-stats                      | MSSQL for each AWS environment into  |
                |                                       | the response. For example,           |
                |                                       | embed=read-aws-environment-          |
                |                                       | ec2-mssql-protection-stats           |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-rds-resources-   | Embeds protection stats about RDS    |
                | protection-stats                      | Instance for each AWS environment    |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-rds-      |
                |                                       | resources-protection-stats           |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-dynamodb-tables- | Embeds protection stats about        |
                | protection-stats                      | DynamoDB tables for each AWS         |
                |                                       | environment into the response. For   |
                |                                       | example, embed=read-aws-environment- |
                |                                       | dynamodb-tables-protection-stats     |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-protection-      | Embeds protection stats about        |
                | groups-protection-stats               | Protection Group for each AWS        |
                |                                       | environment into the response. For   |
                |                                       | example, embed=read-aws-environment- |
                |                                       | protection-groups-protection-stats   |
                +---------------------------------------+--------------------------------------+
                | read-aws-environments-backup-status-  | Embeds backup statistics for each    |
                | stats                                 | AWS environment into the response.   |
                |                                       | For example, embed=read-aws-         |
                |                                       | environments-backup-status-stats     |
                +---------------------------------------+--------------------------------------+

            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        """
        controller = AwsEnvironmentsV1Controller(self.controller)
        while True:
            response = controller.list_aws_environments(
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
