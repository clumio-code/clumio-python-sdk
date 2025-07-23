#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Any, Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_aws_environments_response
from clumioapi.models import read_aws_environment_response
import requests


class AwsEnvironmentsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for aws-environments resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.aws-environments=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_aws_environments(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: str | None = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> Union[
        list_aws_environments_response.ListAWSEnvironmentsResponse,
        tuple[
            requests.Response, Optional[list_aws_environments_response.ListAWSEnvironmentsResponse]
        ],
    ]:
        """Returns a list of AWS environments.

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
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
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_aws_environments_response.ListAWSEnvironmentsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/aws/environments'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter,
            'embed': embed,
            'lookback_days': lookback_days,
        }

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_aws_environments.', errors
            )

        obj = list_aws_environments_response.ListAWSEnvironmentsResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj

    def read_aws_environment(
        self,
        environment_id: str | None = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> Union[
        read_aws_environment_response.ReadAWSEnvironmentResponse,
        tuple[
            requests.Response, Optional[read_aws_environment_response.ReadAWSEnvironmentResponse]
        ],
    ]:
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
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_aws_environment_response.ReadAWSEnvironmentResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/aws/environments/{environment_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'environment_id': environment_id}
        )
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed, 'lookback_days': lookback_days}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_aws_environment.', errors
            )

        obj = read_aws_environment_response.ReadAWSEnvironmentResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj
