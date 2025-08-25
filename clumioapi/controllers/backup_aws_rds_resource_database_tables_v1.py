#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Any, Iterator, Optional, Union
import urllib.parse

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import backup_aws_rds_resource_database_tables_types
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
        filter: (
            backup_aws_rds_resource_database_tables_types.ListBackupAwsRdsResourceDatabaseTablesV1FilterT
            | None
        ) = None,
        **kwargs,
    ) -> list_rds_database_tables_response.ListRDSDatabaseTablesResponse:
        """Returns a list of RDS tables from the specified RDS backup.

        Args:
            backup_id:
                Performs the operation on tables within the specified backup.
            database_name:
                Performs the operation on the database with the specified name.
            current_count:
                The number of items listed on the current page.
            limit:
                Limits the size of the items returned in the response.
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

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_rds_database_tables_response.ListRDSDatabaseTablesResponse.from_response(
                response
            )

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
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_rds_database_tables_response.ListRDSDatabaseTablesResponse
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
            error_str = f'list_backup_aws_rds_resource_database_tables for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_backup_aws_rds_resource_database_table(
        self,
        backup_id: str | None = None,
        database_name: str | None = None,
        table_id: str | None = None,
        embed: str | None = None,
        **kwargs,
    ) -> read_rds_database_table_response.ReadRDSDatabaseTableResponse:
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

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return read_rds_database_table_response.ReadRDSDatabaseTableResponse.from_response(
                response
            )

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

        resp_instance: read_rds_database_table_response.ReadRDSDatabaseTableResponse
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
            error_str = f'read_backup_aws_rds_resource_database_table for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_backup_aws_rds_resource_database_table_columns(
        self,
        backup_id: str | None = None,
        database_name: str | None = None,
        table_id: str | None = None,
        **kwargs,
    ) -> read_rds_database_table_columns_response.ReadRDSDatabaseTableColumnsResponse:
        """Returns a list of columns within the specified table.

        Args:
            backup_id:
                Performs the operation on tables within the specified backup.
            database_name:
                Performs the operation on the database with the specified name.
            table_id:
                Performs the operation on the RDS database table with the specified ID.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return read_rds_database_table_columns_response.ReadRDSDatabaseTableColumnsResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/backups/aws/rds-resources/{backup_id}/databases/{database_name}/tables/{table_id}/columns'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path,
            {'backup_id': backup_id, 'database_name': database_name, 'table_id': table_id},
        )
        _query_parameters: dict[str, Any] = {}

        resp_instance: read_rds_database_table_columns_response.ReadRDSDatabaseTableColumnsResponse
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
            error_str = f'read_backup_aws_rds_resource_database_table_columns for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class BackupAwsRdsResourceDatabaseTablesV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for backup-aws-rds-resource-database-tables resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = BackupAwsRdsResourceDatabaseTablesV1Controller(config)

    def list_backup_aws_rds_resource_database_tables(
        self,
        current_count: int | None = None,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            backup_aws_rds_resource_database_tables_types.ListBackupAwsRdsResourceDatabaseTablesV1FilterT
            | None
        ) = None,
        **kwargs,
    ) -> Iterator[list_rds_database_tables_response.ListRDSDatabaseTablesResponse]:
        """Returns a list of RDS tables from the specified RDS backup.

        Args:
            backup_id:
                Performs the operation on tables within the specified backup.
            database_name:
                Performs the operation on the database with the specified name.
            current_count:
                The number of items listed on the current page.
            limit:
                Limits the size of the items returned in the response.
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

        """
        start = start or '1'
        while True:
            response = self.controller.list_backup_aws_rds_resource_database_tables(
                current_count=current_count, limit=limit, start=start, filter=filter, **kwargs
            )
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
