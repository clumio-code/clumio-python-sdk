#
# Copyright 2023. Clumio, Inc.
#

import json
from typing import Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_backup_aws_dynamodb_table_v1_request
from clumioapi.models import list_dynamo_db_table_backups_response
from clumioapi.models import on_demand_dynamo_db_backup_response
from clumioapi.models import read_dynamo_db_table_backup_response
import requests


class BackupAwsDynamodbTablesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for backup-aws-dynamodb-tables resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.backup-aws-dynamodb-tables=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_backup_aws_dynamodb_tables(
        self, limit: int = None, start: str = None, sort: str = None, filter: str = None, **kwargs
    ) -> Union[
        list_dynamo_db_table_backups_response.ListDynamoDBTableBackupsResponse,
        tuple[
            requests.Response,
            Optional[list_dynamo_db_table_backups_response.ListDynamoDBTableBackupsResponse],
        ],
    ]:
        """Retrieves a list of DynamoDB table backups.

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            sort:
                Returns the list of backups in the order specified. Set `sort` to the name of
                the sort field by
                which to sort in ascending order. To sort the list in reverse order, prefix the
                field name
                with a minus sign (`-`). Only one field may be sorted at a time.

                The following table lists the supported sort fields for this resource:

                +-----------------+------------------------------------------------------------+
                |   Sort Field    |                        Description                         |
                +=================+============================================================+
                | start_timestamp | Sorts the backups in ascending timestamp order (oldest     |
                |                 | first). For example, sort=start_timestamp                  |
                +-----------------+------------------------------------------------------------+

                If a sort order is not specified, the individual rules are sorted by
                "start_timestamp" in descending timestamp order (newest first).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +-----------------+------------------+-----------------------------------------+
                |      Field      | Filter Condition |               Description               |
                +=================+==================+=========================================+
                | table_id        | $eq              | Filter DynamoDB table backups whose     |
                |                 |                  | table ID equal the specified string.    |
                |                 |                  | For example,                            |
                |                 |                  | filter={"table_id":{"$eq":"d0ba78cc-    |
                |                 |                  | 582b-11ea-9bdc-82f798bd42fe"}}          |
                +-----------------+------------------+-----------------------------------------+
                | start_timestamp | $lte, $gt        | Filter DynamoDB table backups whose     |
                |                 |                  | start timestamp is "less than or equal  |
                |                 |                  | to" or                                  |
                |                 |                  | "greater than" a given timestamp. For   |
                |                 |                  | example,                                |
                |                 |                  | filter={"start_timestamp":{"$lte":"1985 |
                |                 |                  | -04-12T23:20:50Z"}}                     |
                +-----------------+------------------+-----------------------------------------+
                | type            | $all             | Filter DynamoDB table backups based on  |
                |                 |                  | backup type (Possible values include    |
                |                 |                  | clumio_backup                           |
                |                 |                  | and aws_snapshot). If empty, fetches    |
                |                 |                  | backups for all DynamoDB backup types.  |
                |                 |                  | For example,                            |
                |                 |                  | filter={"type":{"$all":["clumio_backup" |
                |                 |                  | ]}}                                     |
                +-----------------+------------------+-----------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_dynamo_db_table_backups_response.ListDynamoDBTableBackupsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/aws/dynamodb-tables'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'sort': sort, 'filter': filter}

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
                'Error occurred while executing list_backup_aws_dynamodb_tables.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                list_dynamo_db_table_backups_response.ListDynamoDBTableBackupsResponse.from_dictionary(
                    resp.json()
                ),
            )
        return (
            list_dynamo_db_table_backups_response.ListDynamoDBTableBackupsResponse.from_dictionary(
                resp
            )
        )

    def create_backup_aws_dynamodb_table(
        self,
        embed: str = None,
        body: create_backup_aws_dynamodb_table_v1_request.CreateBackupAwsDynamodbTableV1Request = None,
        **kwargs,
    ) -> Union[
        on_demand_dynamo_db_backup_response.OnDemandDynamoDBBackupResponse,
        tuple[
            requests.Response,
            Optional[on_demand_dynamo_db_backup_response.OnDemandDynamoDBBackupResponse],
        ],
    ]:
        """Performs an on-demand backup for the specified DynamoDB table.

        Args:
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to
                include additional details associated with the resource.

                +-----------------+------------------------------------------------------------+
                | Embeddable Link |                        Description                         |
                +=================+============================================================+
                | read-task       | Embeds the associated task in the response. For example,   |
                |                 | embed=read-task                                            |
                +-----------------+------------------------------------------------------------+

                For more information about embedded links, refer to the
                Embedding Referenced Resources section of this guide.
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            on_demand_dynamo_db_backup_response.OnDemandDynamoDBBackupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/aws/dynamodb-tables'

        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_backup_aws_dynamodb_table.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                on_demand_dynamo_db_backup_response.OnDemandDynamoDBBackupResponse.from_dictionary(
                    resp.json()
                ),
            )
        return on_demand_dynamo_db_backup_response.OnDemandDynamoDBBackupResponse.from_dictionary(
            resp
        )

    def read_backup_aws_dynamodb_table(
        self, backup_id: str, **kwargs
    ) -> Union[
        read_dynamo_db_table_backup_response.ReadDynamoDBTableBackupResponse,
        tuple[
            requests.Response,
            Optional[read_dynamo_db_table_backup_response.ReadDynamoDBTableBackupResponse],
        ],
    ]:
        """Returns a representation of the specified DynamoDB table backup.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_dynamo_db_table_backup_response.ReadDynamoDBTableBackupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/aws/dynamodb-tables/{backup_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'backup_id': backup_id}
        )
        _query_parameters = {}

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
                'Error occurred while executing read_backup_aws_dynamodb_table.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                read_dynamo_db_table_backup_response.ReadDynamoDBTableBackupResponse.from_dictionary(
                    resp.json()
                ),
            )
        return read_dynamo_db_table_backup_response.ReadDynamoDBTableBackupResponse.from_dictionary(
            resp
        )
