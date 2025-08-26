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
from clumioapi.controllers.types import backup_aws_rds_resource_databases_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_rds_backup_databases_response
import requests


class BackupAwsRdsResourceDatabasesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for backup-aws-rds-resource-databases resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.backup-aws-rds-resource-databases=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_backup_aws_rds_resource_databases(
        self,
        backup_id: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            backup_aws_rds_resource_databases_types.ListBackupAwsRdsResourceDatabasesV1FilterT
            | None
        ) = None,
        **kwargs,
    ) -> list_rds_backup_databases_response.ListRDSBackupDatabasesResponse:
        """Retrieves a list of RDS databases from an RDS backup.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID.
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +-------+------------------+---------------------------------+
                | Field | Filter Condition |           Description           |
                +=======+==================+=================================+
                | name  | $begins_with     | Prefix of the RDS database name |
                +-------+------------------+---------------------------------+

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_rds_backup_databases_response.ListRDSBackupDatabasesResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/backups/aws/rds-resources/{backup_id}/databases'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'backup_id': backup_id}
        )
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_rds_backup_databases_response.ListRDSBackupDatabasesResponse
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
            error_str = f'list_backup_aws_rds_resource_databases for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class BackupAwsRdsResourceDatabasesV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for backup-aws-rds-resource-databases resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = BackupAwsRdsResourceDatabasesV1Controller(config)

    def list_backup_aws_rds_resource_databases(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            backup_aws_rds_resource_databases_types.ListBackupAwsRdsResourceDatabasesV1FilterT
            | None
        ) = None,
        **kwargs,
    ) -> Iterator[list_rds_backup_databases_response.ListRDSBackupDatabasesResponse]:
        """Retrieves a list of RDS databases from an RDS backup.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID.
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +-------+------------------+---------------------------------+
                | Field | Filter Condition |           Description           |
                +=======+==================+=================================+
                | name  | $begins_with     | Prefix of the RDS database name |
                +-------+------------------+---------------------------------+

        """
        start = start or '1'
        while True:
            response = self.controller.list_backup_aws_rds_resource_databases(
                limit=limit, start=start, filter=filter, **kwargs
            )
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
