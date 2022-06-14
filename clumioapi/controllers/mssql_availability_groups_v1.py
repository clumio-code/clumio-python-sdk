#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_mssql_a_gs_response
from clumioapi.models import read_mssql_ag_response
import requests


class MssqlAvailabilityGroupsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for mssql-availability-groups resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.mssql-availability-groups=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }

    def list_mssql_availability_groups(
        self, limit: int = None, start: str = None, filter: str = None
    ) -> list_mssql_a_gs_response.ListMssqlAGsResponse:
        """Returns a list of Availability Groups.

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +---------------------------+------------------+-------------------------------+
                |           Field           | Filter Condition |          Description          |
                +===========================+==================+===============================+
                | name                      | $contains        | Filter availability groups    |
                |                           |                  | where given string is a       |
                |                           |                  | substring of the name.        |
                +---------------------------+------------------+-------------------------------+
                | group_id                  | $eq              | Filter availability groups    |
                |                           |                  | where given string is a equal |
                |                           |                  | to the group_id.              |
                +---------------------------+------------------+-------------------------------+
                | subgroup_id               | $eq              | Filter availability groups    |
                |                           |                  | where given string is a equal |
                |                           |                  | to the subgroup_id.           |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | Filter availability groups    |
                |                           |                  | whose policy_id is equal to   |
                |                           |                  | the given string.             |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $eq              | Filter availability groups    |
                |                           |                  | whose protection_status is    |
                |                           |                  | equal to the given string.    |
                +---------------------------+------------------+-------------------------------+
                | status                    | $eq              | Filter Database whose status  |
                |                           |                  | is equal to the given string. |
                +---------------------------+------------------+-------------------------------+

        Returns:
            ListMssqlAGsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/mssql/availability-groups'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_mssql_availability_groups.', errors
            )
        return list_mssql_a_gs_response.ListMssqlAGsResponse.from_dictionary(resp)

    def read_mssql_availability_group(
        self, availability_group_id: str
    ) -> read_mssql_ag_response.ReadMssqlAGResponse:
        """Returns a representation of the specified availability group.

        Args:
            availability_group_id:
                Performs the operation on the ag with the specified ID.
        Returns:
            ReadMssqlAGResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = (
            f'{self.config.base_path}/datasources/mssql/availability-groups/{availability_group_id}'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'availability_group_id': availability_group_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_mssql_availability_group.', errors
            )
        return read_mssql_ag_response.ReadMssqlAGResponse.from_dictionary(resp)
