#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_file_systems_response
from clumioapi.models import read_file_system_response
import requests


class BackupFilesystemsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for backup-filesystems resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config

    def list_backup_filesystems(
        self, backup_id: str, limit: int = None, start: str = None
    ) -> list_file_systems_response.ListFileSystemsResponse:
        """Returns a list of filesystems.

        Args:
            backup_id:
                The Clumio assigned ID of the backup to retrieve.
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
        Returns:
            ListFileSystemsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/{backup_id}/filesystems'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'backup_id': backup_id}
        )
        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start}

        # Prepare headers
        _headers = {
            'accept': 'application/backup-filesystems=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_backup_filesystems.', errors
            )
        return list_file_systems_response.ListFileSystemsResponse.from_dictionary(resp)

    def read_filesystem(
        self, filesystem_id: str, backup_id: str
    ) -> read_file_system_response.ReadFileSystemResponse:
        """Returns a representation of the specified filesystem.

        Args:
            filesystem_id:
                Performs the operation on the filesystem with the specified ID.
            backup_id:
                Performs the operation on a filesystem within the specified backup.
        Returns:
            ReadFileSystemResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/{backup_id}/filesystems/{filesystem_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'filesystem_id': filesystem_id, 'backup_id': backup_id}
        )
        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/backup-filesystems=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_filesystem.', errors
            )
        return read_file_system_response.ReadFileSystemResponse.from_dictionary(resp)
