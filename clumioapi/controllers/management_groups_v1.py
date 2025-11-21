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
from clumioapi.models import list_management_groups_response
from clumioapi.models import read_management_group_response
from clumioapi.models import update_management_group_response
from clumioapi.models import update_management_group_v1_request
import requests
import retrying


class ManagementGroupsV1Controller:
    """A Controller to access Endpoints for management-groups resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.management-groups=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

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

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_management_groups_response.ListManagementGroupsResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/management-groups'

        if start:
            _url_path = f'{_url_path}?start={start}'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
        }

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

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_management_group_response.ReadManagementGroupResponse.from_response(resp)

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

        def get_instance_from_response(resp: requests.Response) -> Any:
            return update_management_group_response.UpdateManagementGroupResponse.from_response(
                resp
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


class ManagementGroupsV1ControllerPaginator:
    """A Controller to access Endpoints for management-groups resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
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
        controller = ManagementGroupsV1Controller(self.controller)
        while True:
            response = controller.list_management_groups(limit=limit, start=start, **kwargs)
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
