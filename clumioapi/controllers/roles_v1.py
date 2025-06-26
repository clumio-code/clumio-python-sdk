#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
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
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_roles_response.ListRolesResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/roles'

        _query_parameters = {}

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
                'Error occurred while executing list_roles.', errors
            )

        if self.config.raw_response:
            return resp, list_roles_response.ListRolesResponse.from_dictionary(resp.json())
        return list_roles_response.ListRolesResponse.from_dictionary(resp)

    def read_role(self, role_id: str, **kwargs) -> Union[
        read_role_response.ReadRoleResponse,
        tuple[requests.Response, Optional[read_role_response.ReadRoleResponse]],
    ]:
        """Returns a representation of the specified role.

        Args:
            role_id:
                Retrieves the role with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_role_response.ReadRoleResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/roles/{role_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'role_id': role_id})
        _query_parameters = {}

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
                'Error occurred while executing read_role.', errors
            )

        if self.config.raw_response:
            return resp, read_role_response.ReadRoleResponse.from_dictionary(resp.json())
        return read_role_response.ReadRoleResponse.from_dictionary(resp)
