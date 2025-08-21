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
    ) -> Union[
        list_management_groups_response.ListManagementGroupsResponse,
        tuple[
            requests.Response,
            Optional[list_management_groups_response.ListManagementGroupsResponse],
        ],
    ]:
        """Returns a list of management groups.

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_management_groups_response.ListManagementGroupsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/management-groups'

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
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_management_groups', error=http_error
            )

        obj = list_management_groups_response.ListManagementGroupsResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj

    def read_management_group(self, group_id: str | None = None, **kwargs) -> Union[
        read_management_group_response.ReadManagementGroupResponse,
        tuple[
            requests.Response, Optional[read_management_group_response.ReadManagementGroupResponse]
        ],
    ]:
        """Returns a representation of the specified management group. Management groups
        are used to
        manage the SQL hosts and cloud connectors deployed in vCenter servers.

        Returns a representation of the specified management-groups.

        Args:
            group_id:
                Performs the operation on the management group with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_management_group_response.ReadManagementGroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/management-groups/{group_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'group_id': group_id}
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
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_management_group', error=http_error
            )

        obj = read_management_group_response.ReadManagementGroupResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj

    def update_management_group(
        self,
        group_id: str | None = None,
        body: update_management_group_v1_request.UpdateManagementGroupV1Request | None = None,
        **kwargs,
    ) -> Union[
        update_management_group_response.UpdateManagementGroupResponse,
        tuple[
            requests.Response,
            Optional[update_management_group_response.UpdateManagementGroupResponse],
        ],
    ]:
        """Update the specified management group.

        Args:
            group_id:
                Performs the operation on the management group with the specified ID.
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            update_management_group_response.UpdateManagementGroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/management-groups/{group_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'group_id': group_id}
        )
        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.put(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            raise clumio_exception.ClumioException(
                'Error occurred while executing update_management_group', error=http_error
            )

        obj = update_management_group_response.UpdateManagementGroupResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj
