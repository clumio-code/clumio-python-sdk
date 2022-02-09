#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
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

    def list_management_groups(
        self, limit: int = None, start: str = None
    ) -> list_management_groups_response.ListManagementGroupsResponse:
        """Returns a list of management groups.

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        Returns:
            ListManagementGroupsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/management-groups'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start}

        # Prepare headers
        _headers = {
            'accept': 'application/management-groups=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_management_groups.', errors
            )
        return list_management_groups_response.ListManagementGroupsResponse.from_dictionary(resp)

    def read_management_group(
        self, group_id: str
    ) -> read_management_group_response.ReadManagementGroupResponse:
        """Returns a representation of the specified management group. Management groups
        are used to
        manage the SQL hosts and cloud connectors deployed in vCenter servers.

        Returns a representation of the specified management-groups.

        Args:
            group_id:
                Performs the operation on the management group with the specified ID.
        Returns:
            ReadManagementGroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/management-groups/{group_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'group_id': group_id}
        )
        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/management-groups=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_management_group.', errors
            )
        return read_management_group_response.ReadManagementGroupResponse.from_dictionary(resp)

    def update_management_group(
        self,
        group_id: str,
        body: update_management_group_v1_request.UpdateManagementGroupV1Request = None,
    ) -> update_management_group_response.UpdateManagementGroupResponse:
        """Update the specified management group.

        Args:
            group_id:
                Performs the operation on the management group with the specified ID.
            body:

        Returns:
            UpdateManagementGroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/management-groups/{group_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'group_id': group_id}
        )
        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/management-groups=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.put(
                _url_path,
                headers=_headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing update_management_group.', errors
            )
        return update_management_group_response.UpdateManagementGroupResponse.from_dictionary(resp)
