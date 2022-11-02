#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_protection_group_backups_response
from clumioapi.models import list_protection_group_s3_asset_backups_response
from clumioapi.models import read_protection_group_backup_response
from clumioapi.models import read_protection_group_s3_asset_backup_response
import requests


class BackupProtectionGroupsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for backup-protection-groups resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.backup-protection-groups=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_backup_protection_groups(
        self, limit: int = None, start: str = None, filter: str = None
    ) -> list_protection_group_backups_response.ListProtectionGroupBackupsResponse:
        """Retrieves a list of protection group backups.

        Args:
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

                +---------------------+-----------+--------------------------------------------+
                | protection_group_id |    $eq    |    The ID of the protection group. For     |
                |                     |           |                  example,                  |
                |                     |           | filter={"protection_group_id":{"$eq":"d0ba |
                |                     |           |    78cc-582b-11ea-9bdc-82f798bd42fe"}}     |
                +=====================+===========+============================================+
                | start_timestamp     | $lte, $gt | The timestamp value of when the backup     |
                |                     |           | started. Represented in RFC-3339 format.   |
                |                     |           | For example,                               |
                |                     |           | filter={"start_timestamp":{"$lte":"1985-   |
                |                     |           | 04-12T23:20:50Z"}}                         |
                +---------------------+-----------+--------------------------------------------+

        Returns:
            ListProtectionGroupBackupsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/protection-groups'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_backup_protection_groups.', errors
            )
        return list_protection_group_backups_response.ListProtectionGroupBackupsResponse.from_dictionary(
            resp
        )

    def list_backup_protection_group_s3_assets(
        self, limit: int = None, start: str = None, filter: str = None
    ) -> list_protection_group_s3_asset_backups_response.ListProtectionGroupS3AssetBackupsResponse:
        """Retrieves a list of protection group S3 asset backups.

        Args:
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

                +---------------------------------+-----------+--------------------------------+
                |  protection_group_s3_asset_id   |    $eq    | The ID of the protection group |
                |                                 |           |     S3 asset. For example,     |
                |                                 |           | filter={"protection_group_s3_a |
                |                                 |           |   sset_id":{"$eq":"d0ba78cc-   |
                |                                 |           | 582b-11ea-9bdc-82f798bd42fe"}} |
                +=================================+===========+================================+
                | parent_protection_group_backup_ | $eq       | The ID of the parent           |
                | id                              |           | protection group backup. For   |
                |                                 |           | example,                       |
                |                                 |           | filter={"parent_protection_gro |
                |                                 |           | up_backup_id":{"$eq":"d0ba78cc |
                |                                 |           | -582b-11ea-9bdc-               |
                |                                 |           | 82f798bd42fe_2022-01-          |
                |                                 |           | 01T00:02:00Z.13753"}}          |
                +---------------------------------+-----------+--------------------------------+
                | start_timestamp                 | $lte, $gt | The timestamp value of when    |
                |                                 |           | the backup started.            |
                |                                 |           | Represented in RFC-3339        |
                |                                 |           | format. For example,           |
                |                                 |           | filter={"start_timestamp":{"$l |
                |                                 |           | te":"1985-04-12T23:20:50Z"}}   |
                +---------------------------------+-----------+--------------------------------+
                | bucket_region                   | $eq       | The bucket region. For         |
                |                                 |           | example, filter={"bucket_regio |
                |                                 |           | n":{"$eq":"us-west-2"}}        |
                +---------------------------------+-----------+--------------------------------+

        Returns:
            ListProtectionGroupS3AssetBackupsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/protection-groups/s3-assets'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_backup_protection_group_s3_assets.', errors
            )
        return list_protection_group_s3_asset_backups_response.ListProtectionGroupS3AssetBackupsResponse.from_dictionary(
            resp
        )

    def read_backup_protection_group_s3_asset(
        self, backup_id: str
    ) -> read_protection_group_s3_asset_backup_response.ReadProtectionGroupS3AssetBackupResponse:
        """Returns a representation of the specified protection group S3 asset backup.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID.
        Returns:
            ReadProtectionGroupS3AssetBackupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/protection-groups/s3-assets/{backup_id}'
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
                'Error occurred while executing read_backup_protection_group_s3_asset.', errors
            )
        return read_protection_group_s3_asset_backup_response.ReadProtectionGroupS3AssetBackupResponse.from_dictionary(
            resp
        )

    def read_backup_protection_group(
        self, backup_id: str
    ) -> read_protection_group_backup_response.ReadProtectionGroupBackupResponse:
        """Returns a representation of the specified protection group backup.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID.
        Returns:
            ReadProtectionGroupBackupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/protection-groups/{backup_id}'
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
                'Error occurred while executing read_backup_protection_group.', errors
            )
        return (
            read_protection_group_backup_response.ReadProtectionGroupBackupResponse.from_dictionary(
                resp
            )
        )
