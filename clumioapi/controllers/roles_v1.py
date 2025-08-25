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
from clumioapi.models import list_permissions_response
from clumioapi.models import list_roles_response
from clumioapi.models import read_role_response
import requests


class RolesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for roles resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.roles=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_roles(self, **kwargs):
        """Returns a list of roles that can be assigned to users, either while inviting
        users using the
        [POST /users](#operation/create-user) API, or by updating the user using the
        [PATCH /users/{user_id}](#operation/update-user) API.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_roles_response.ListRolesResponse.from_response(response)

        # Prepare query URL
        _url_path = '/roles'

        _query_parameters: dict[str, Any] = {}

        resp_instance: list_roles_response.ListRolesResponse
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
            error_str = f'list_roles for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def list_permissions(self, **kwargs):
        """Returns the list of supported permissions."""

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_permissions_response.ListPermissionsResponse.from_response(response)

        # Prepare query URL
        _url_path = '/roles/permissions'

        _query_parameters: dict[str, Any] = {}

        resp_instance: list_permissions_response.ListPermissionsResponse
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
            error_str = f'list_permissions for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_role(
        self, role_id: str | None = None, **kwargs
    ) -> read_role_response.ReadRoleResponse:
        """Returns a representation of the specified role.

        Args:
            role_id:
                Retrieves the role with the specified ID.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return read_role_response.ReadRoleResponse.from_response(response)

        # Prepare query URL
        _url_path = '/roles/{role_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'role_id': role_id})
        _query_parameters: dict[str, Any] = {}

        resp_instance: read_role_response.ReadRoleResponse
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
            error_str = f'read_role for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class RolesV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for roles resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = RolesV1Controller(config)
