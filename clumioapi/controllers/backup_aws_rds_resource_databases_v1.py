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
        self, backup_id: str, limit: int = None, start: str = None, filter: str = None, **kwargs
    ) -> Union[
        list_rds_backup_databases_response.ListRDSBackupDatabasesResponse,
        tuple[
            requests.Response,
            Optional[list_rds_backup_databases_response.ListRDSBackupDatabasesResponse],
        ],
    ]:
        """Retrieves a list of RDS databases from an RDS backup.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID.
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

                +-------+------------------+---------------------------------+
                | Field | Filter Condition |           Description           |
                +=======+==================+=================================+
                | name  | $begins_with     | Prefix of the RDS database name |
                +-------+------------------+---------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_rds_backup_databases_response.ListRDSBackupDatabasesResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/backups/aws/rds-resources/{backup_id}/databases'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'backup_id': backup_id}
        )
        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

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
                'Error occurred while executing list_backup_aws_rds_resource_databases.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                list_rds_backup_databases_response.ListRDSBackupDatabasesResponse.from_dictionary(
                    resp.json()
                ),
            )
        return list_rds_backup_databases_response.ListRDSBackupDatabasesResponse.from_dictionary(
            resp
        )
