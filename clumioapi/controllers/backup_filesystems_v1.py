#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Any, Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
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
        self.headers = {
            'accept': 'application/api.clumio.backup-filesystems=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_backup_filesystems(
        self,
        backup_id: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        **kwargs,
    ) -> Union[
        list_file_systems_response.ListFileSystemsResponse,
        tuple[requests.Response, Optional[list_file_systems_response.ListFileSystemsResponse]],
    ]:
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
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_file_systems_response.ListFileSystemsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/backups/{backup_id}/filesystems'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'backup_id': backup_id}
        )
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'limit': limit, 'start': start}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_backup_filesystems.', errors
            )

        obj = list_file_systems_response.ListFileSystemsResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def read_filesystem(
        self, filesystem_id: str | None = None, backup_id: str | None = None, **kwargs
    ) -> Union[
        read_file_system_response.ReadFileSystemResponse,
        tuple[requests.Response, Optional[read_file_system_response.ReadFileSystemResponse]],
    ]:
        """Returns a representation of the specified filesystem.

        Args:
            filesystem_id:
                Performs the operation on the filesystem with the specified ID.
            backup_id:
                Performs the operation on a filesystem within the specified backup.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_file_system_response.ReadFileSystemResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/backups/{backup_id}/filesystems/{filesystem_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'filesystem_id': filesystem_id, 'backup_id': backup_id}
        )
        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_filesystem.', errors
            )

        obj = read_file_system_response.ReadFileSystemResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj
