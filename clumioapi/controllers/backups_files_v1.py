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
from clumioapi.controllers.types import backups_files_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import file_list_response
from clumioapi.models import file_search_response
import requests


class BackupsFilesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for backups-files resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.backups-files=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_files(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: backups_files_types.ListFilesV1FilterT | None = None,
        **kwargs,
    ) -> file_search_response.FileSearchResponse:
        """Retrieve the list of files whose name matches a given regex pattern.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists the supported filter fields for this resource and the
                filter
                conditions that can be applied on those fields:

                +------------+------------------+----------------------------------------------+
                |   Field    | Filter Condition |                 Description                  |
                +============+==================+==============================================+
                | asset_type | $eq              | Required. The type of the asset within which |
                |            |                  | to search for files. Possible values include |
                |            |                  | aws_ebs_volume and                           |
                |            |                  | aws_ec2_instance.                            |
                +------------+------------------+----------------------------------------------+
                | asset_id   | $eq              | Required. The Clumio-assigned ID of the      |
                |            |                  | asset                                        |
                |            |                  | within which to search for files.            |
                +------------+------------------+----------------------------------------------+
                | name       | $regex           | A regex pattern to match against file names. |
                |            |                  | For example,                                 |
                |            |                  | filter={"name":{"$regex":"a(\\w){2,5}"}      |
                +------------+------------------+----------------------------------------------+

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return file_search_response.FileSearchResponse.from_response(response)

        # Prepare query URL
        _url_path = '/backups/files/search'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: file_search_response.FileSearchResponse
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
            error_str = f'list_files for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def list_file_versions(
        self,
        search_result_id: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        **kwargs,
    ) -> file_list_response.FileListResponse:
        """Retrieve the list of versions of the file.

        Args:
            search_result_id:
                Performs the operation on the file with the specified ID.
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return file_list_response.FileListResponse.from_response(response)

        # Prepare query URL
        _url_path = '/backups/files/search/{search_result_id}/versions'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'search_result_id': search_result_id}
        )
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'limit': limit, 'start': start}

        resp_instance: file_list_response.FileListResponse
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
            error_str = f'list_file_versions for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class BackupsFilesV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for backups-files resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = BackupsFilesV1Controller(config)

    def list_files(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: backups_files_types.ListFilesV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[file_search_response.FileSearchResponse]:
        """Retrieve the list of files whose name matches a given regex pattern.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists the supported filter fields for this resource and the
                filter
                conditions that can be applied on those fields:

                +------------+------------------+----------------------------------------------+
                |   Field    | Filter Condition |                 Description                  |
                +============+==================+==============================================+
                | asset_type | $eq              | Required. The type of the asset within which |
                |            |                  | to search for files. Possible values include |
                |            |                  | aws_ebs_volume and                           |
                |            |                  | aws_ec2_instance.                            |
                +------------+------------------+----------------------------------------------+
                | asset_id   | $eq              | Required. The Clumio-assigned ID of the      |
                |            |                  | asset                                        |
                |            |                  | within which to search for files.            |
                +------------+------------------+----------------------------------------------+
                | name       | $regex           | A regex pattern to match against file names. |
                |            |                  | For example,                                 |
                |            |                  | filter={"name":{"$regex":"a(\\w){2,5}"}      |
                +------------+------------------+----------------------------------------------+

        """
        start = start or '1'
        while True:
            response = self.controller.list_files(limit=limit, start=start, filter=filter, **kwargs)
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)

    def list_file_versions(
        self, limit: int | None = None, start: str | None = None, **kwargs
    ) -> Iterator[file_list_response.FileListResponse]:
        """Retrieve the list of versions of the file.

        Args:
            search_result_id:
                Performs the operation on the file with the specified ID.
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        """
        start = start or '1'
        while True:
            response = self.controller.list_file_versions(limit=limit, start=start, **kwargs)
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
