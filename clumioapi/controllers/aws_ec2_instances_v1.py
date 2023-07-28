#
# Copyright 2021. Clumio, Inc.
#

import json
from typing import Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_ec2_instances_response
from clumioapi.models import read_ec2_instance_response
import requests


class AwsEc2InstancesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for aws-ec2-instances resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.aws-ec2-instances=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_aws_ec2_instances(
        self, limit: int = None, start: str = None, filter: str = None, embed: str = None, **kwargs
    ) -> Union[
        list_ec2_instances_response.ListEc2InstancesResponse,
        tuple[requests.Response, Optional[list_ec2_instances_response.ListEc2InstancesResponse]],
    ]:
        """Returns a list of EC2 instances.

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +---------------------------+------------------+-------------------------------+
                |           Field           | Filter Condition |          Description          |
                +===========================+==================+===============================+
                | environment_id            | $eq              | The Clumio-assigned ID of the |
                |                           |                  | AWS environment.              |
                +---------------------------+------------------+-------------------------------+
                | instance_native_id        | $eq              | The AWS-assigned ID of the    |
                |                           |                  | EC2 instance. For example, fi |
                |                           |                  | lter={"instance_native_id":{" |
                |                           |                  | $eq":"i-07aa02a849fe376d0"}}  |
                +---------------------------+------------------+-------------------------------+
                | account_native_id         | $eq              | The AWS-assigned ID of the    |
                |                           |                  | AWS account. For example, fil |
                |                           |                  | ter={"account_native_id":{"$e |
                |                           |                  | q":"789901323485"}}           |
                +---------------------------+------------------+-------------------------------+
                | compliance_status         | $eq, in          | The compliance status of the  |
                |                           |                  | EC2 instance. Possible values |
                |                           |                  | include "compliant" and       |
                |                           |                  | "non_compliant". filter={"com |
                |                           |                  | pliance_status":{"$eq":"non_c |
                |                           |                  | ompliant"}}                   |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $eq              | The protection status of the  |
                |                           |                  | EC2 instance. Possible values |
                |                           |                  | include "protected",          |
                |                           |                  | "unprotected", and            |
                |                           |                  | "unsupported". For example, f |
                |                           |                  | ilter={"protection_status":{" |
                |                           |                  | $eq":"protected"}}            |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | The Clumio-assigned ID of the |
                |                           |                  | policy protecting this        |
                |                           |                  | resource. filter={"protection |
                |                           |                  | _info.policy_id":{"$eq":"c764 |
                |                           |                  | abb6-5819-16ea-               |
                |                           |                  | bb9f-b2e1c9a040ad"}}          |
                +---------------------------+------------------+-------------------------------+
                | tags.id                   | $all             | The ID of the AWS tag applied |
                |                           |                  | to the EC2 instance. For      |
                |                           |                  | example, filter={"tags.id":{" |
                |                           |                  | $all":["c764b152-5819-11ea-bb |
                |                           |                  | 9f-b2e1c9a040ad","c764abb6-   |
                |                           |                  | 5819-11ea-                    |
                |                           |                  | bb9f-b2e1c9a040ad"]}}. If     |
                |                           |                  | multiple tags are specified,  |
                |                           |                  | all of them must be applied   |
                |                           |                  | to the same EC2 instance.     |
                +---------------------------+------------------+-------------------------------+
                | is_deleted                | $eq              | The deletion status of the    |
                |                           |                  | EC2 instance. Default value   |
                |                           |                  | is "false". Set to "true" to  |
                |                           |                  | retrieve deleted EC2          |
                |                           |                  | instance. For example, filter |
                |                           |                  | ={"is_deleted":{"$eq":true}}  |
                +---------------------------+------------------+-------------------------------+
                | availability_zone         | $eq              | The AWS availability zone.    |
                |                           |                  | For example, filter={"availab |
                |                           |                  | ility_zone":{"$eq":"us-       |
                |                           |                  | east-1a"}}                    |
                +---------------------------+------------------+-------------------------------+

            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with each
                resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the associated policy of a protected EC2     |
                |                        | instance into the response. For example,            |
                |                        | embed=read-policy-definition                        |
                +------------------------+-----------------------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_ec2_instances_response.ListEc2InstancesResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/aws/ec2-instances'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter, 'embed': embed}

        # Execute request
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_aws_ec2_instances.', errors
            )

        if self.config.raw_response:
            return resp, list_ec2_instances_response.ListEc2InstancesResponse.from_dictionary(
                resp.json()
            )
        return list_ec2_instances_response.ListEc2InstancesResponse.from_dictionary(resp)

    def read_aws_ec2_instance(
        self, instance_id: str, embed: str = None, **kwargs
    ) -> Union[
        read_ec2_instance_response.ReadEc2InstanceResponse,
        tuple[requests.Response, Optional[read_ec2_instance_response.ReadEc2InstanceResponse]],
    ]:
        """Returns a representation of the specified EC2 instance.

        Args:
            instance_id:
                Performs the operation on the EC2 instance with the specified ID.
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

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_ec2_instance_response.ReadEc2InstanceResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/aws/ec2-instances/{instance_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'instance_id': instance_id}
        )
        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_aws_ec2_instance.', errors
            )

        if self.config.raw_response:
            return resp, read_ec2_instance_response.ReadEc2InstanceResponse.from_dictionary(
                resp.json()
            )
        return read_ec2_instance_response.ReadEc2InstanceResponse.from_dictionary(resp)
