#
# Copyright 2021. Clumio, Inc.
#

import requests

from clumioapi import api_helper, configuration, sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import (
    list_subgroups_response,
    read_subgroup_response,
    update_management_subgroup_v1_request,
    update_subgroup_response,
)


class ManagementSubgroupsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for management-subgroups resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.management-subgroups=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_management_subgroups(
        self, group_id: str, limit: int = None, start: str = None
    ) -> list_subgroups_response.ListSubgroupsResponse:
        """Returns a list of subgroups.

        Args:
            group_id:
                Performs the operation on the subgroup with the specified parent group ID.
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        Returns:
            ListSubgroupsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/management-groups/{group_id}/subgroups'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'group_id': group_id}
        )
        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                "Error occurred while executing list_management_subgroups.", errors
            )
        return list_subgroups_response.ListSubgroupsResponse.from_dictionary(resp)

    def read_management_subgroup(
        self, subgroup_id: str, group_id: str
    ) -> read_subgroup_response.ReadSubgroupResponse:
        """Subgroups are used to manage cloud connectors and SQL hosts residing in the same
        vCenter server.

        Returns a representation of the specified subgroups.

        Args:
            subgroup_id:
                Performs the operation on the subgroup with the specified ID.
            group_id:
                Performs the operation on the subgroup with the specified parent group ID.
        Returns:
            ReadSubgroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/management-groups/{group_id}/subgroups/{subgroup_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'subgroup_id': subgroup_id, 'group_id': group_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                "Error occurred while executing read_management_subgroup.", errors
            )
        return read_subgroup_response.ReadSubgroupResponse.from_dictionary(resp)

    def update_management_subgroup(
        self,
        subgroup_id: str,
        group_id: str,
        body: update_management_subgroup_v1_request.UpdateManagementSubgroupV1Request = None,
    ) -> update_subgroup_response.UpdateSubgroupResponse:
        """Update the specified subgroup.

        Args:
            subgroup_id:
                Performs the operation on the subgroup with the specified ID.
            group_id:
                Performs the operation on the subgroup with the specified parent group ID.
            body:

        Returns:
            UpdateSubgroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/management-groups/{group_id}/subgroups/{subgroup_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'subgroup_id': subgroup_id, 'group_id': group_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.put(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                "Error occurred while executing update_management_subgroup.", errors
            )
        return update_subgroup_response.UpdateSubgroupResponse.from_dictionary(resp)
