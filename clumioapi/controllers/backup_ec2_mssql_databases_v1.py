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
from clumioapi.controllers.types import backup_ec2_mssql_databases_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_backup_ec2_mssql_database_v1_request
from clumioapi.models import list_ec2_mssql_database_backups_response
from clumioapi.models import on_demand_ec2_mssql_database_backup_response
from clumioapi.models import read_ec2_mssql_database_backup_response
import requests


class BackupEc2MssqlDatabasesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for backup-ec2-mssql-databases resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.backup-ec2-mssql-databases=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_backup_ec2_mssql_databases(
        self,
        limit: int | None = None,
        start: str | None = None,
        sort: str | None = None,
        filter: backup_ec2_mssql_databases_types.ListBackupEc2MssqlDatabasesV1FilterT | None = None,
        embed: str | None = None,
        **kwargs,
    ) -> list_ec2_mssql_database_backups_response.ListEC2MSSQLDatabaseBackupsResponse:
        """Retrieve a list of EC2 MSSQL database backups.

        Args:
            limit:
                Limits the size of the items returned in the response.
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
                |                 |                  | `ec2_mssql_database_backup`, `ec2_mssql |
                |                 |                  | _log_backup_full_recovery_model` and    |
                |                 |                  | `ec2_mssql_log_backup_bulk_logged_model |
                |                 |                  | `.                                      |
                +-----------------+------------------+-----------------------------------------+

            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +----------------------+-------------------------------------------------------+
                |   Embeddable Link    |                      Description                      |
                +======================+=======================================================+
                | read-aws-environment | Embeds the associated AWS Environment details in the  |
                |                      | response. For example, embed=read-aws-environment     |
                +----------------------+-------------------------------------------------------+

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_ec2_mssql_database_backups_response.ListEC2MSSQLDatabaseBackupsResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/backups/aws/ec2-mssql/databases'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'sort': sort,
            'filter': filter.query_str if filter else None,
            'embed': embed,
        }

        resp_instance: list_ec2_mssql_database_backups_response.ListEC2MSSQLDatabaseBackupsResponse
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
            error_str = (
                f'list_backup_ec2_mssql_databases for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def create_backup_ec2_mssql_database(
        self,
        embed: str | None = None,
        body: (
            create_backup_ec2_mssql_database_v1_request.CreateBackupEc2MssqlDatabaseV1Request | None
        ) = None,
        **kwargs,
    ) -> on_demand_ec2_mssql_database_backup_response.OnDemandEC2MSSQLDatabaseBackupResponse:
        """Performs an on-demand backup for the specified EC2 MSSQL asset.

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

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return on_demand_ec2_mssql_database_backup_response.OnDemandEC2MSSQLDatabaseBackupResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/backups/aws/ec2-mssql/databases'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed}

        resp_instance: (
            on_demand_ec2_mssql_database_backup_response.OnDemandEC2MSSQLDatabaseBackupResponse
        )
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=body.dict() if body else None,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = (
                f'create_backup_ec2_mssql_database for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_backup_ec2_mssql_database(
        self, backup_id: str | None = None, **kwargs
    ) -> read_ec2_mssql_database_backup_response.ReadEC2MSSQLDatabaseBackupResponse:
        """Returns a representation of the specified EC2 MSSQL database backup.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID. Use the
                [GET /backups/aws/ec2-mssql/databases](#operation/list-backup-ec2-mssql-
                databases)
                endpoint to fetch valid values.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return read_ec2_mssql_database_backup_response.ReadEC2MSSQLDatabaseBackupResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/backups/aws/ec2-mssql/databases/{backup_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'backup_id': backup_id}
        )
        _query_parameters: dict[str, Any] = {}

        resp_instance: read_ec2_mssql_database_backup_response.ReadEC2MSSQLDatabaseBackupResponse
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
            error_str = (
                f'read_backup_ec2_mssql_database for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class BackupEc2MssqlDatabasesV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for backup-ec2-mssql-databases resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = BackupEc2MssqlDatabasesV1Controller(config)

    def list_backup_ec2_mssql_databases(
        self,
        limit: int | None = None,
        start: str | None = None,
        sort: str | None = None,
        filter: backup_ec2_mssql_databases_types.ListBackupEc2MssqlDatabasesV1FilterT | None = None,
        embed: str | None = None,
        **kwargs,
    ) -> Iterator[list_ec2_mssql_database_backups_response.ListEC2MSSQLDatabaseBackupsResponse]:
        """Retrieve a list of EC2 MSSQL database backups.

        Args:
            limit:
                Limits the size of the items returned in the response.
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
                |                 |                  | `ec2_mssql_database_backup`, `ec2_mssql |
                |                 |                  | _log_backup_full_recovery_model` and    |
                |                 |                  | `ec2_mssql_log_backup_bulk_logged_model |
                |                 |                  | `.                                      |
                +-----------------+------------------+-----------------------------------------+

            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +----------------------+-------------------------------------------------------+
                |   Embeddable Link    |                      Description                      |
                +======================+=======================================================+
                | read-aws-environment | Embeds the associated AWS Environment details in the  |
                |                      | response. For example, embed=read-aws-environment     |
                +----------------------+-------------------------------------------------------+

        """
        start = start or '1'
        while True:
            response = self.controller.list_backup_ec2_mssql_databases(
                limit=limit, start=start, sort=sort, filter=filter, embed=embed, **kwargs
            )
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
