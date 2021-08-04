#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
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

    def list_aws_environments(
        self, limit: int = None, start: str = None, filter: str = None, embed: str = None
    ) -> list_aws_environments_response.ListAWSEnvironmentsResponse:
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
                |                   |                   | environment. This field must be set  |
                |                   |                   | with account_native_id. For example, |
                |                   |                   | filter={"aws_region":{"$eq":"us-west |
                |                   |                   | -2"},"account_native_id":{"$eq":"891 |
                |                   |                   | 106098888"}}.                        |
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
                |                   |                   | "EBS" and "RDS". For example, filter |
                |                   |                   | ={"services_enabled":{"$eq":"RDS"}}. |
                +-------------------+-------------------+--------------------------------------+


            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-aws-environment-ebs-volumes-     | Embeds compliance statistics about   |
                | compliance-stats                      | EBS volumes for each AWS environment |
                |                                       | into the response. For example,      |
                |                                       | embed=read-aws-environment-ebs-      |
                |                                       | volumes-compliance-stats             |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-rds-resources-   | Embeds compliance statistics about   |
                | compliance-stats                      | RDS resources for each AWS           |
                |                                       | environment into the response. For   |
                |                                       | example, embed=read-aws-environment- |
                |                                       | rds-resources-compliance-stats       |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-dynamodb-tables- | Embeds compliance statistics about   |
                | compliance-stats                      | DynamoDB tables for each AWS         |
                |                                       | environment into the response. For   |
                |                                       | example, embed=read-aws-environment- |
                |                                       | dynamodb-tables-compliance-stats     |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-ec2-mssql-       | Embeds compliance statistics about   |
                | compliance-stats                      | EC2 MSSQL databases for each AWS     |
                |                                       | environment into the response. For   |
                |                                       | example, embed=read-aws-environment- |
                |                                       | ec2-mssql-compliance-stats           |
                +---------------------------------------+--------------------------------------+

        Returns:
            ListAWSEnvironmentsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/aws/environments'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter, 'embed': embed}

        # Prepare headers
        _headers = {
            'accept': 'application/aws-environments=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_aws_environments.', errors
            )
        return list_aws_environments_response.ListAWSEnvironmentsResponse.from_dictionary(resp)

    def read_aws_environment(
        self, environment_id: str, embed: str = None
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
                | read-aws-environment-ebs-volumes-     | Embeds compliance stats about EBS    |
                | compliance-stats                      | Volumes into the _embedded field of  |
                |                                       | the response. For example,           |
                |                                       | embed=read-aws-environment-ebs-      |
                |                                       | volumes-compliance-stats             |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-rds-resources-   | Embeds compliance stats about RDS    |
                | compliance-stats                      | resources into the _embedded field   |
                |                                       | of the response. For example,        |
                |                                       | embed=read-aws-environment-rds-      |
                |                                       | resources-compliance-stats           |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-dynamodb-tables- | Embeds compliance stats about        |
                | compliance-stats                      | DynamoDB tables into the _embedded   |
                |                                       | field of the response. For example,  |
                |                                       | embed=read-aws-environment-dynamodb- |
                |                                       | tables-compliance-stats              |
                +---------------------------------------+--------------------------------------+
                | read-aws-environment-ec2-mssql-       | Embeds compliance statistics about   |
                | compliance-stats                      | EC2 MSSQL databases for each AWS     |
                |                                       | environment into the response. For   |
                |                                       | example, embed=read-aws-environment- |
                |                                       | ec2-mssql-compliance-stats           |
                +---------------------------------------+--------------------------------------+

        Returns:
            ReadAWSEnvironmentResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/aws/environments/{environment_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'environment_id': environment_id}
        )
        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Prepare headers
        _headers = {
            'accept': 'application/aws-environments=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_aws_environment.', errors
            )
        return read_aws_environment_response.ReadAWSEnvironmentResponse.from_dictionary(resp)
