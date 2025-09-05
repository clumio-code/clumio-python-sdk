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
from clumioapi.models import list_dynamo_db_table_response
from clumioapi.models import read_dynamo_db_table_response
import requests


class AwsDynamodbTablesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for aws-dynamodb-tables resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.aws-dynamodb-tables=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_aws_dynamodb_tables(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: str | None = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> Union[
        list_dynamo_db_table_response.ListDynamoDBTableResponse,
        tuple[requests.Response, Optional[list_dynamo_db_table_response.ListDynamoDBTableResponse]],
    ]:
        """Retrieve a list of DynamoDB tables.

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
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
                | name                      | $contains        | The AWS-assigned name of this |
                |                           |                  | resource. For example,        |
                |                           |                  | filter={"name":{"$contains":" |
                |                           |                  | dev"}} retrieves all DynamoDB |
                |                           |                  | tables with "dev" in          |
                |                           |                  | their name.                   |
                +---------------------------+------------------+-------------------------------+
                | table_native_id           | $eq              | The AWS-assigned ID of the    |
                |                           |                  | DynamoDB Table. For example,  |
                |                           |                  | filter={"table_native_id":{"$ |
                |                           |                  | eq":"07463bd7-7b66-4748-921c- |
                |                           |                  | 25c9a83c6c3c"}}               |
                +---------------------------+------------------+-------------------------------+
                | aws_region                | $eq              | The AWS region of a given     |
                |                           |                  | account to which this         |
                |                           |                  | resource belongs. For         |
                |                           |                  | example,                      |
                |                           |                  | filter={"account_native_id":{ |
                |                           |                  | "$eq":"789901323485"},        |
                |                           |                  | "aws_region":{"$eq":"us-      |
                |                           |                  | east-1"}} retrieves DynamoDB  |
                |                           |                  | tables in region us-east-1 in |
                |                           |                  | account 789901323485.         |
                +---------------------------+------------------+-------------------------------+
                | account_native_id         | $eq              | The AWS-assigned ID of the    |
                |                           |                  | account to which this         |
                |                           |                  | resource belongs. For         |
                |                           |                  | example,                      |
                |                           |                  | filter={"account_native_id":{ |
                |                           |                  | "$eq":"789901323485"}}        |
                |                           |                  | retrieves DynamoDB tables     |
                |                           |                  | across all regions in account |
                |                           |                  | 789901323485.                 |
                +---------------------------+------------------+-------------------------------+
                | tags.id                   | $all             | The Clumio-assigned ID(s) of  |
                |                           |                  | AWS tag(s) applied to this    |
                |                           |                  | resource. For example,        |
                |                           |                  | filter={"tags.id":{"$all":["c |
                |                           |                  | 764b152-5819-11ea-bb9f-       |
                |                           |                  | b2e1c9a040ad","c764abb6-5819- |
                |                           |                  | 11ea-bb9f-b2e1c9a040ad"]}}    |
                |                           |                  | retrieves all DynamoDB tables |
                |                           |                  | that are associated with the  |
                |                           |                  | 2 AWS tags identified by      |
                |                           |                  | these                         |
                |                           |                  | IDs. If multiple tags are     |
                |                           |                  | specified, all of them must   |
                |                           |                  | be applied to the same        |
                |                           |                  | DynamoDB                      |
                |                           |                  | table.                        |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | The Clumio-assigned ID of the |
                |                           |                  | policy protecting this        |
                |                           |                  | resource.                     |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $in              | The protection status of this |
                |                           |                  | resource. Possible values     |
                |                           |                  | include protected,            |
                |                           |                  | unprotected, and unsupported. |
                +---------------------------+------------------+-------------------------------+
                | deactivated               | $eq              | Filter assets protected by a  |
                |                           |                  | deactivated policy.           |
                +---------------------------+------------------+-------------------------------+
                | backup_status             | $in              | The backup status of this     |
                |                           |                  | resource. Possible values     |
                |                           |                  | include success,              |
                |                           |                  | partial_success, failure and  |
                |                           |                  | no_backup.                    |
                +---------------------------+------------------+-------------------------------+
                | is_deleted                | $eq,$in          | The deletion status of this   |
                |                           |                  | resource. If not specified,   |
                |                           |                  | retrieves only active         |
                |                           |                  | DynamoDB                      |
                |                           |                  | tables. filter={"is_deleted": |
                |                           |                  | {"$in":["true","false"]}}     |
                +---------------------------+------------------+-------------------------------+

                For more information about filtering, refer to the Filtering section
                of this guide.
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following
                embeddable links to include additional details associated with the resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the definition of the policy associated with |
                |                        | this resource. Unprotected resources                |
                |                        | will not have an associated policy. For example,    |
                |                        | embed=read-policy-definition                        |
                +------------------------+-----------------------------------------------------+

                For more information about embedded links, refer to the Embedding
                Referenced Resources section of this guide.
            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_dynamo_db_table_response.ListDynamoDBTableResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/aws/dynamodb-tables'

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
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_aws_dynamodb_tables', error=http_error
            )

        obj = list_dynamo_db_table_response.ListDynamoDBTableResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def read_aws_dynamodb_table(
        self,
        table_id: str | None = None,
        lookback_days: int | None = None,
        embed: str | None = None,
        **kwargs,
    ) -> Union[
        read_dynamo_db_table_response.ReadDynamoDBTableResponse,
        tuple[requests.Response, Optional[read_dynamo_db_table_response.ReadDynamoDBTableResponse]],
    ]:
        """Returns a representation of specified DynamoDB table.

        Args:
            table_id:
                Performs the operation on the DynamoDB table with the specified ID.
            lookback_days:
                Calculate backup status for the last `lookback_days` days.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the associated policy of a protected         |
                |                        | DynamoDB table into the response. For example,      |
                |                        | embed=read-policy-definition                        |
                +------------------------+-----------------------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_dynamo_db_table_response.ReadDynamoDBTableResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/aws/dynamodb-tables/{table_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'table_id': table_id}
        )
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'lookback_days': lookback_days, 'embed': embed}

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
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_aws_dynamodb_table', error=http_error
            )

        obj = read_dynamo_db_table_response.ReadDynamoDBTableResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj
