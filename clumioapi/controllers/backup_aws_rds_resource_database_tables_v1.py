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
from clumioapi.models import list_rds_database_tables_response
from clumioapi.models import read_rds_database_table_columns_response
from clumioapi.models import read_rds_database_table_response
import requests


class BackupAwsRdsResourceDatabaseTablesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for backup-aws-rds-resource-database-tables resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.backup-aws-rds-resource-database-tables=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_backup_aws_rds_resource_database_tables(
        self,
        backup_id: str | None = None,
        database_name: str | None = None,
        current_count: int | None = None,
        limit: int | None = None,
        start: str | None = None,
        filter: str | None = None,
        **kwargs,
    ) -> Union[
        list_rds_database_tables_response.ListRDSDatabaseTablesResponse,
        tuple[
            requests.Response,
            Optional[list_rds_database_tables_response.ListRDSDatabaseTablesResponse],
        ],
    ]:
        """Returns a list of RDS tables from the specified RDS backup.

        Args:
            backup_id:
                Performs the operation on tables within the specified backup.
            database_name:
                Performs the operation on the database with the specified name.
            current_count:
                The number of items listed on the current page.
            limit:
                The maximum number of items displayed per page in the response.
            start:
                The page token used to get this response.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +-------+------------------+---------------------------+
                | Field | Filter Condition |        Description        |
                +=======+==================+===========================+
                | name  | $begins_with     | Prefix of the table name. |
                +-------+------------------+---------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_rds_database_tables_response.ListRDSDatabaseTablesResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/backups/aws/rds-resources/{backup_id}/databases/{database_name}/tables'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'backup_id': backup_id, 'database_name': database_name}
        )
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'current_count': current_count,
            'limit': limit,
            'start': start,
            'filter': filter,
        }

        # Execute request
        try:
            resp: requests.Response = self.client.get(
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
                'Error occurred while executing list_backup_aws_rds_resource_database_tables.',
                errors,
            )

        if self.config.raw_response:
            return (
                resp,
                list_rds_database_tables_response.ListRDSDatabaseTablesResponse.from_dictionary(
                    resp.json()
                ),
            )
        return list_rds_database_tables_response.ListRDSDatabaseTablesResponse.from_dictionary(
            resp.json()
        )

    def read_backup_aws_rds_resource_database_table(
        self,
        backup_id: str | None = None,
        database_name: str | None = None,
        table_id: str | None = None,
        embed: str | None = None,
        **kwargs,
    ) -> Union[
        read_rds_database_table_response.ReadRDSDatabaseTableResponse,
        tuple[
            requests.Response,
            Optional[read_rds_database_table_response.ReadRDSDatabaseTableResponse],
        ],
    ]:
        """Returns a representation of the specified table from an RDS backup.

        Args:
            backup_id:
                Performs the operation on tables within the specified backup.
            database_name:
                Performs the operation on the database with the specified name.
            table_id:
                Performs the operation on the RDS database table with the specified ID.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-backup-aws-rds-resource-         | Embeds the columns of the table into |
                | database-table-columns                | the _embedded field of the response. |
                |                                       | For example, embed=read-backup-aws-  |
                |                                       | rds-resource-database-table-columns  |
                +---------------------------------------+--------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_rds_database_table_response.ReadRDSDatabaseTableResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = (
            '/backups/aws/rds-resources/{backup_id}/databases/{database_name}/tables/{table_id}'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path,
            {'backup_id': backup_id, 'database_name': database_name, 'table_id': table_id},
        )
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp: requests.Response = self.client.get(
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
                'Error occurred while executing read_backup_aws_rds_resource_database_table.',
                errors,
            )

        if self.config.raw_response:
            return (
                resp,
                read_rds_database_table_response.ReadRDSDatabaseTableResponse.from_dictionary(
                    resp.json()
                ),
            )
        return read_rds_database_table_response.ReadRDSDatabaseTableResponse.from_dictionary(
            resp.json()
        )

    def read_backup_aws_rds_resource_database_table_columns(
        self,
        backup_id: str | None = None,
        database_name: str | None = None,
        table_id: str | None = None,
        **kwargs,
    ) -> Union[
        read_rds_database_table_columns_response.ReadRDSDatabaseTableColumnsResponse,
        tuple[
            requests.Response,
            Optional[read_rds_database_table_columns_response.ReadRDSDatabaseTableColumnsResponse],
        ],
    ]:
        """Returns a list of columns within the specified table.

        Args:
            backup_id:
                Performs the operation on tables within the specified backup.
            database_name:
                Performs the operation on the database with the specified name.
            table_id:
                Performs the operation on the RDS database table with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_rds_database_table_columns_response.ReadRDSDatabaseTableColumnsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/backups/aws/rds-resources/{backup_id}/databases/{database_name}/tables/{table_id}/columns'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path,
            {'backup_id': backup_id, 'database_name': database_name, 'table_id': table_id},
        )
        _query_parameters: dict[str, Any] = {}

        # Execute request
        try:
            resp: requests.Response = self.client.get(
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
                'Error occurred while executing read_backup_aws_rds_resource_database_table_columns.',
                errors,
            )

        if self.config.raw_response:
            return (
                resp,
                read_rds_database_table_columns_response.ReadRDSDatabaseTableColumnsResponse.from_dictionary(
                    resp.json()
                ),
            )
        return read_rds_database_table_columns_response.ReadRDSDatabaseTableColumnsResponse.from_dictionary(
            resp.json()
        )
