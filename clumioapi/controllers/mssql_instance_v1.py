#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_mssql_instances_response
from clumioapi.models import read_mssql_instance_response
import requests


class MssqlInstanceV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for mssql-instance resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config

    def list_mssql_instance(
        self, limit: int = None, start: str = None, filter: str = None
    ) -> list_mssql_instances_response.ListMssqlInstancesResponse:
        """Returns a list of Instances

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
                | name                      | $contains        | Filter Instance where given   |
                |                           |                  | string is a substring of the  |
                |                           |                  | name.                         |
                +---------------------------+------------------+-------------------------------+
                | group_id                  | $eq              | Filter Instance where given   |
                |                           |                  | string is equal to the        |
                |                           |                  | group_id.                     |
                +---------------------------+------------------+-------------------------------+
                | subgroup_id               | $eq              | Filter Instance where given   |
                |                           |                  | string is equal to the        |
                |                           |                  | subgroup_id.                  |
                +---------------------------+------------------+-------------------------------+
                | host_id                   | $eq              | Filter Instance where given   |
                |                           |                  | string is equal to the        |
                |                           |                  | host_id.                      |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | Filter Instance whose         |
                |                           |                  | policy_id is equal to the     |
                |                           |                  | given string.                 |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $eq              | Filter Instance whose         |
                |                           |                  | protection_status is equal to |
                |                           |                  | the given string.             |
                +---------------------------+------------------+-------------------------------+
                | status                    | $eq              | Filter Database whose status  |
                |                           |                  | is equal to the given string. |
                +---------------------------+------------------+-------------------------------+

        Returns:
            ListMssqlInstancesResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/mssql/instances'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Prepare headers
        _headers = {
            'accept': 'application/api.clumio.mssql-instance=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_mssql_instance.', errors
            )
        return list_mssql_instances_response.ListMssqlInstancesResponse.from_dictionary(resp)

    def read_mssql_instance(
        self, instance_id: str
    ) -> read_mssql_instance_response.ReadMssqlInstanceResponse:
        """Returns a representation of the specified instance.

        Args:
            instance_id:
                Performs the operation on the instance with the specified ID.
        Returns:
            ReadMssqlInstanceResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/mssql/instances/{instance_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'instance_id': instance_id}
        )
        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/api.clumio.mssql-instance=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_mssql_instance.', errors
            )
        return read_mssql_instance_response.ReadMssqlInstanceResponse.from_dictionary(resp)
