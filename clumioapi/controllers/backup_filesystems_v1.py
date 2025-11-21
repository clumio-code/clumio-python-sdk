#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
import re
from typing import Any, Iterator, Optional, Union
import urllib.parse

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import aws_s3_buckets_v1_bucket_matcher_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_file_systems_response
from clumioapi.models import read_file_system_response
import requests
import retrying


class BackupFilesystemsV1Controller:
    """A Controller to access Endpoints for backup-filesystems resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.backup-filesystems=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_backup_filesystems(
        self,
        backup_id: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        **kwargs,
    ) -> list_file_systems_response.ListFileSystemsResponse:
        """Returns a list of filesystems.

        Args:
            backup_id:
                The Clumio assigned ID of the backup to retrieve.
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_file_systems_response.ListFileSystemsResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/backups/{backup_id}/filesystems'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'backup_id': backup_id}
        )

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
        }

        resp_instance: list_file_systems_response.ListFileSystemsResponse
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
            error_str = f'list_backup_filesystems for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_filesystem(
        self, filesystem_id: str | None = None, backup_id: str | None = None, **kwargs
    ) -> read_file_system_response.ReadFileSystemResponse:
        """Returns a representation of the specified filesystem.

        Args:
            filesystem_id:
                Performs the operation on the filesystem with the specified ID.
            backup_id:
                Performs the operation on a filesystem within the specified backup.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_file_system_response.ReadFileSystemResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/backups/{backup_id}/filesystems/{filesystem_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'filesystem_id': filesystem_id, 'backup_id': backup_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: read_file_system_response.ReadFileSystemResponse
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
            error_str = f'read_filesystem for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class BackupFilesystemsV1ControllerPaginator:
    """A Controller to access Endpoints for backup-filesystems resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_backup_filesystems(
        self,
        backup_id: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        **kwargs,
    ) -> Iterator[list_file_systems_response.ListFileSystemsResponse]:
        """Returns a list of filesystems.

        Args:
            backup_id:
                The Clumio assigned ID of the backup to retrieve.
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
        """
        controller = BackupFilesystemsV1Controller(self.controller)
        while True:
            response = controller.list_backup_filesystems(
                backup_id=backup_id, limit=limit, start=start, **kwargs
            )
            yield response
            next_link = response.Links.Next  # type: ignore
            if not next_link:
                break
            next_link = next_link.Href
            if match := re.search(r'start=([^&]+)', next_link):  # type: ignore
                start = match.group(1)
            else:
                raise clumio_exception.ClumioException(
                    'Next link is malformed. Please contact clumio support.'
                )
