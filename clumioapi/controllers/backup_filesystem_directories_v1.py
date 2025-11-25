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
from clumioapi.models import read_directory_response
import requests
import retrying


class BackupFilesystemDirectoriesV1Controller:
    """A Controller to access Endpoints for backup-filesystem-directories resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.backup-filesystem-directories=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def read_backup_filesystem_directory(
        self,
        backup_id: str | None = None,
        filesystem_id: str | None = None,
        directory_id: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        **kwargs,
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
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_directory_response.ReadDirectoryResponse.from_response(resp)

        # Prepare query URL
        _url_path = (
            '/backups/{backup_id}/filesystems/{filesystem_id}/directories/{directory_id}/browse'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path,
            {'backup_id': backup_id, 'filesystem_id': filesystem_id, 'directory_id': directory_id},
        )

        if start:
            _url_path = f'{_url_path}?start={start}'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
        }

        resp_instance: read_directory_response.ReadDirectoryResponse
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
                f'read_backup_filesystem_directory for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class BackupFilesystemDirectoriesV1ControllerPaginator:
    """A Controller to access Endpoints for backup-filesystem-directories resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def read_backup_filesystem_directory(
        self,
        backup_id: str | None = None,
        filesystem_id: str | None = None,
        directory_id: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        **kwargs,
    ) -> Iterator[read_directory_response.ReadDirectoryResponse]:
        """Browse files in the directory with the specified ID.

        Args:
            backup_id:
                Performs the operation on a directory within the specified backup.
            filesystem_id:
                Performs the operation on a directory within the specified filesystem.
            directory_id:
                Performs the operation on the directory with the specified ID.
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        """
        controller = BackupFilesystemDirectoriesV1Controller(self.controller)
        while True:
            response = controller.read_backup_filesystem_directory(
                backup_id=backup_id,
                filesystem_id=filesystem_id,
                directory_id=directory_id,
                limit=limit,
                start=start,
                **kwargs,
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
