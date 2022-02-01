#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
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

    def list_roles(self):
        """Returns a list of roles that can be assigned to users, either while inviting
        users using the
        [POST /users](#operation/create-user) API, or by updating the user using the
        [PATCH /users/{user_id}](#operation/update-user) API.
        Returns:
            ListRolesResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/roles'

        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/roles=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_roles.', errors
            )
        return list_roles_response.ListRolesResponse.from_dictionary(resp)

    def read_role(self, role_id: str) -> read_role_response.ReadRoleResponse:
        """Returns a representation of the specified role.

        Args:
            role_id:
                Retrieves the role with the specified ID.
        Returns:
            ReadRoleResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/roles/{role_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'role_id': role_id})
        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/roles=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_role.', errors
            )
        return read_role_response.ReadRoleResponse.from_dictionary(resp)