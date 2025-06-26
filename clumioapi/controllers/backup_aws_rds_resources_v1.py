#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_rds_database_backups_response
from clumioapi.models import list_rds_option_groups_response
from clumioapi.models import read_rds_database_backup_response
import requests


class BackupAwsRdsResourcesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for backup-aws-rds-resources resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.backup-aws-rds-resources=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_backup_aws_rds_resources(
        self, limit: int = None, start: str = None, sort: str = None, filter: str = None, **kwargs
    ) -> Union[
        list_rds_database_backups_response.ListRdsDatabaseBackupsResponse,
        tuple[
            requests.Response,
            Optional[list_rds_database_backups_response.ListRdsDatabaseBackupsResponse],
        ],
    ]:
        """Retrieves a list of RDS database backups.

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
                | resource_id     | $eq              | Filter database backups whose database  |
                |                 |                  | ID equal the specified string. For      |
                |                 |                  | example, filter={"resource_id":{"$eq":" |
                |                 |                  | fdba79ed-502b-11fb-9bdc-83d528bd52dc"}} |
                +-----------------+------------------+-----------------------------------------+
                | start_timestamp | $lte, $gt        | Filter database backups whose start     |
                |                 |                  | timestamp is "less than or equal to" or |
                |                 |                  | "greater than" a given timestamp.       |
                |                 |                  | Represented in RFC-3339 format. For     |
                |                 |                  | example, filter={"start_timestamp":{"$l |
                |                 |                  | te":"1985-04-12T23:20:50Z"}}            |
                +-----------------+------------------+-----------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_rds_database_backups_response.ListRdsDatabaseBackupsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/backups/aws/rds-resources'

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
                'Error occurred while executing list_backup_aws_rds_resources.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                list_rds_database_backups_response.ListRdsDatabaseBackupsResponse.from_dictionary(
                    resp.json()
                ),
            )
        return list_rds_database_backups_response.ListRdsDatabaseBackupsResponse.from_dictionary(
            resp
        )

    def read_backup_aws_rds_resource(self, backup_id: str, **kwargs) -> Union[
        read_rds_database_backup_response.ReadRdsDatabaseBackupResponse,
        tuple[
            requests.Response,
            Optional[read_rds_database_backup_response.ReadRdsDatabaseBackupResponse],
        ],
    ]:
        """Returns a representation of the specified RDS database backup.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_rds_database_backup_response.ReadRdsDatabaseBackupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/backups/aws/rds-resources/{backup_id}'
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
                'Error occurred while executing read_backup_aws_rds_resource.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                read_rds_database_backup_response.ReadRdsDatabaseBackupResponse.from_dictionary(
                    resp.json()
                ),
            )
        return read_rds_database_backup_response.ReadRdsDatabaseBackupResponse.from_dictionary(resp)

    def list_aws_rds_resources_option_groups(
        self, backup_id: str, limit: int = None, start: str = None, filter: str = None, **kwargs
    ) -> Union[
        list_rds_option_groups_response.ListRdsOptionGroupsResponse,
        tuple[
            requests.Response, Optional[list_rds_option_groups_response.ListRdsOptionGroupsResponse]
        ],
    ]:
        """Retrieves a list of RDS option groups which are superset of persistent and
        permanent
        options present in the backup snapshot for a given environment.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID.
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

                +----------------+------------------+------------------------------------------+
                |     Field      | Filter Condition |               Description                |
                +================+==================+==========================================+
                | environment_id | $eq              | The Clumio-assigned ID of the AWS        |
                |                |                  | environment.                             |
                +----------------+------------------+------------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_rds_option_groups_response.ListRdsOptionGroupsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/backups/aws/rds-resources/{backup_id}/option-groups'
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
                'Error occurred while executing list_aws_rds_resources_option_groups.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                list_rds_option_groups_response.ListRdsOptionGroupsResponse.from_dictionary(
                    resp.json()
                ),
            )
        return list_rds_option_groups_response.ListRdsOptionGroupsResponse.from_dictionary(resp)
