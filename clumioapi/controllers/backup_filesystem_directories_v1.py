#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import read_directory_response
import requests


class BackupFilesystemDirectoriesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for backup-filesystem-directories resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config

    def read_backup_filesystem_directory(
        self,
        backup_id: str,
        filesystem_id: str,
        directory_id: str,
        limit: int = None,
        start: str = None,
    ) -> read_directory_response.ReadDirectoryResponse:
        """Browse files in the directory with the specified ID.

        Args:
            backup_id:
                Performs the operation on a directory within the specified backup.
            filesystem_id:
                Performs the operation on a directory within the specified filesystem.
            directory_id:
                Performs the operation on the directory with the specified ID.
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        Returns:
            ReadDirectoryResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/{backup_id}/filesystems/{filesystem_id}/directories/{directory_id}/browse'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path,
            {'backup_id': backup_id, 'filesystem_id': filesystem_id, 'directory_id': directory_id},
        )
        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start}

        # Prepare headers
        _headers = {
            'accept': 'application/backup-filesystem-directories=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_backup_filesystem_directory.', errors
            )
        return read_directory_response.ReadDirectoryResponse.from_dictionary(resp)