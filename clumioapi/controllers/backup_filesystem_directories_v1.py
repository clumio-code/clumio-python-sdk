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
from clumioapi.models import read_directory_response
import requests


class BackupFilesystemDirectoriesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for backup-filesystem-directories resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.backup-filesystem-directories=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def read_backup_filesystem_directory(
        self,
        backup_id: str,
        filesystem_id: str,
        directory_id: str,
        limit: int = None,
        start: str = None,
        **kwargs,
    ) -> Union[
        read_directory_response.ReadDirectoryResponse,
        tuple[requests.Response, Optional[read_directory_response.ReadDirectoryResponse]],
    ]:
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
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_directory_response.ReadDirectoryResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/backups/{backup_id}/filesystems/{filesystem_id}/directories/{directory_id}/browse'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path,
            {'backup_id': backup_id, 'filesystem_id': filesystem_id, 'directory_id': directory_id},
        )
        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start}

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
                'Error occurred while executing read_backup_filesystem_directory.', errors
            )

        if self.config.raw_response:
            return resp, read_directory_response.ReadDirectoryResponse.from_dictionary(resp.json())
        return read_directory_response.ReadDirectoryResponse.from_dictionary(resp)
