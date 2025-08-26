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
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_management_groups_response
from clumioapi.models import read_management_group_response
from clumioapi.models import update_management_group_response
from clumioapi.models import update_management_group_v1_request
import requests


class ManagementGroupsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for management-groups resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.management-groups=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_management_groups(
        self, limit: int | None = None, start: str | None = None, **kwargs
    ) -> list_management_groups_response.ListManagementGroupsResponse:
        """Returns a list of management groups.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_management_groups_response.ListManagementGroupsResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/management-groups'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'limit': limit, 'start': start}

        resp_instance: list_management_groups_response.ListManagementGroupsResponse
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
            error_str = f'list_management_groups for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_management_group(
        self, group_id: str | None = None, **kwargs
    ) -> read_management_group_response.ReadManagementGroupResponse:
        """Returns a representation of the specified management group. Management groups
        are used to
        manage the SQL hosts and cloud connectors deployed in vCenter servers.

        Returns a representation of the specified management-groups.

        Args:
            group_id:
                Performs the operation on the management group with the specified ID.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return read_management_group_response.ReadManagementGroupResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/management-groups/{group_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'group_id': group_id}
        )
        _query_parameters: dict[str, Any] = {}

        resp_instance: read_management_group_response.ReadManagementGroupResponse
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
            error_str = f'read_management_group for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def update_management_group(
        self,
        group_id: str | None = None,
        body: update_management_group_v1_request.UpdateManagementGroupV1Request | None = None,
        **kwargs,
    ) -> update_management_group_response.UpdateManagementGroupResponse:
        """Update the specified management group.

        Args:
            group_id:
                Performs the operation on the management group with the specified ID.
            body:

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return update_management_group_response.UpdateManagementGroupResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/management-groups/{group_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'group_id': group_id}
        )
        _query_parameters: dict[str, Any] = {}

        resp_instance: update_management_group_response.UpdateManagementGroupResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.put(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=body.dict() if body else None,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'update_management_group for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class ManagementGroupsV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for management-groups resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = ManagementGroupsV1Controller(config)

    def list_management_groups(
        self, limit: int | None = None, start: str | None = None, **kwargs
    ) -> Iterator[list_management_groups_response.ListManagementGroupsResponse]:
        """Returns a list of management groups.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        """
        start = start or '1'
        while True:
            response = self.controller.list_management_groups(limit=limit, start=start, **kwargs)
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
