#
# Copyright 2021. Clumio, Inc.
#

import json

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_backup_mssql_database_v1_request
from clumioapi.models import list_mssql_database_backups_response
from clumioapi.models import on_demand_mssql_backup_response
from clumioapi.models import read_mssql_database_backup_response
import requests


class BackupMssqlDatabasesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for backup-mssql-databases resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.backup-mssql-databases=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_backup_mssql_databases(
        self,
        limit: int = None,
        start: str = None,
        sort: str = None,
        filter: str = None,
        embed: str = None,
    ) -> list_mssql_database_backups_response.ListMssqlDatabaseBackupsResponse:
        """Retrieve a list of MSSQL database backups.

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
                | database_id     | $eq              | Filter database backups whose database  |
                |                 |                  | ID equal the specified string.          |
                +-----------------+------------------+-----------------------------------------+
                | start_timestamp | $lte, $gt        | Filter database backups whose start     |
                |                 |                  | timestamp is "less than or equal to" or |
                |                 |                  | "greater than" a given timestamp.       |
                +-----------------+------------------+-----------------------------------------+
                | type            | $in              | Filter a particular type of database    |
                |                 |                  | backups. Possible values include        |
                |                 |                  | `mssql_database_backup`,                |
                |                 |                  | `mssql_log_backup_full_recovery_model`  |
                |                 |                  | and                                     |
                |                 |                  | `mssql_log_backup_bulk_logged_model`.   |
                +-----------------+------------------+-----------------------------------------+

            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +--------------------------+---------------------------------------------------+
                |     Embeddable Link      |                    Description                    |
                +==========================+===================================================+
                | read-management-group    | Embeds the associated management group details in |
                |                          | the response. For example, embed=read-management- |
                |                          | group                                             |
                +--------------------------+---------------------------------------------------+
                | read-management-subgroup | Embeds the associated management subgroup details |
                |                          | in the response. For example, embed=read-         |
                |                          | management-subgroup                               |
                +--------------------------+---------------------------------------------------+

        Returns:
            list_mssql_database_backups_response.ListMssqlDatabaseBackupsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/mssql/databases'

        _query_parameters = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'sort': sort,
            'filter': filter,
            'embed': embed,
        }

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_backup_mssql_databases.', errors
            )

        return (
            list_mssql_database_backups_response.ListMssqlDatabaseBackupsResponse.from_dictionary(
                resp
            )
        )

    def create_backup_mssql_database(
        self,
        embed: str = None,
        body: create_backup_mssql_database_v1_request.CreateBackupMssqlDatabaseV1Request = None,
    ) -> on_demand_mssql_backup_response.OnDemandMssqlBackupResponse:
        """Performs an on-demand backup for the specified MSSQL asset.

        Args:
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +-----------------+------------------------------------------------------------+
                | Embeddable Link |                        Description                         |
                +=================+============================================================+
                | read-task       | Embeds the associated task in the response. For example,   |
                |                 | embed=read-task                                            |
                +-----------------+------------------------------------------------------------+

            body:

        Returns:
            on_demand_mssql_backup_response.OnDemandMssqlBackupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/mssql/databases'

        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_backup_mssql_database.', errors
            )

        return on_demand_mssql_backup_response.OnDemandMssqlBackupResponse.from_dictionary(resp)

    def read_backup_mssql_database(
        self, backup_id: str
    ) -> read_mssql_database_backup_response.ReadMssqlDatabaseBackupResponse:
        """Returns a representation of the specified MSSQL database backup.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID.
        Returns:
            read_mssql_database_backup_response.ReadMssqlDatabaseBackupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/mssql/databases/{backup_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'backup_id': backup_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_backup_mssql_database.', errors
            )

        return read_mssql_database_backup_response.ReadMssqlDatabaseBackupResponse.from_dictionary(
            resp
        )
