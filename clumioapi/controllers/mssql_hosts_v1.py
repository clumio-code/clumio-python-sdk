#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_hcm_host_response
from clumioapi.models import create_host_ec_credentials_response
from clumioapi.models import create_mssql_host_connection_credentials_v1_request
from clumioapi.models import create_mssql_host_connections_v1_request
from clumioapi.models import delete_hcm_host_response
from clumioapi.models import delete_mssql_host_connections_v1_request
from clumioapi.models import list_hcm_hosts_response
from clumioapi.models import list_mssql_hosts_response
from clumioapi.models import move_hcm_hosts_response
from clumioapi.models import move_mssql_host_connections_v1_request
from clumioapi.models import read_hcm_host_response
from clumioapi.models import read_mssql_host_response
import requests


class MssqlHostsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for mssql-hosts resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config

    def list_mssql_host_connections(
        self, current_count: int = None, filter: str = None, limit: int = None, start: str = None
    ) -> list_hcm_hosts_response.ListHcmHostsResponse:
        """Returns a list of hosts

        Args:
            current_count:
                The number of items listed on the current page.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +-------------+------------------+---------------------------------------------+
                |    Field    | Filter Condition |                 Description                 |
                +=============+==================+=============================================+
                | uuid        | $in              | Filter hosts which are in the given list of |
                |             |                  | uuids.                                      |
                +-------------+------------------+---------------------------------------------+
                | group_id    | $eq              | Filter hosts which belong to the given      |
                |             |                  | group.                                      |
                +-------------+------------------+---------------------------------------------+
                | subgroup_id | $eq              | Filter hosts which belong to the given sub- |
                |             |                  | group.                                      |
                +-------------+------------------+---------------------------------------------+

            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        Returns:
            ListHcmHostsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/connections/mssql/hosts'

        _query_parameters = {}
        _query_parameters = {
            'current_count': current_count,
            'filter': filter,
            'limit': limit,
            'start': start,
        }

        # Prepare headers
        _headers = {
            'accept': 'application/mssql-hosts=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_mssql_host_connections.', errors
            )
        return list_hcm_hosts_response.ListHcmHostsResponse.from_dictionary(resp)

    def create_mssql_host_connections(
        self,
        body: create_mssql_host_connections_v1_request.CreateMssqlHostConnectionsV1Request = None,
    ) -> create_hcm_host_response.CreateHcmHostResponse:
        """Create a MSSQL Connection.

        Args:
            body:

        Returns:
            CreateHcmHostResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/connections/mssql/hosts'

        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/mssql-hosts=v1+json',
        }
        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=_headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_mssql_host_connections.', errors
            )
        return create_hcm_host_response.CreateHcmHostResponse.from_dictionary(resp)

    def delete_mssql_host_connections(
        self,
        embed: str = None,
        body: delete_mssql_host_connections_v1_request.DeleteMssqlHostConnectionsV1Request = None,
    ) -> delete_hcm_host_response.DeleteHcmHostResponse:
        """Delete the specified MSSQL host.

        Args:
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +-----------------+------------------------------------------------------------+
                | Embeddable Link |                        Description                         |
                +=================+============================================================+
                | read-task       | Embeds the associated task in the response. For example,   |
                |                 | embed=read-task                                            |
                +-----------------+------------------------------------------------------------+

            body:

        Returns:
            DeleteHcmHostResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/connections/mssql/hosts'

        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Prepare headers
        _headers = {
            'accept': 'application/mssql-hosts=v1+json',
        }
        # Execute request
        try:
            resp = self.client.delete(
                _url_path,
                headers=_headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing delete_mssql_host_connections.', errors
            )
        return delete_hcm_host_response.DeleteHcmHostResponse.from_dictionary(resp)

    def move_mssql_host_connections(
        self,
        embed: str = None,
        body: move_mssql_host_connections_v1_request.MoveMssqlHostConnectionsV1Request = None,
    ) -> move_hcm_hosts_response.MoveHcmHostsResponse:
        """Move the specified MSSQL hosts from a source Sub-Group to a destination Sub-
        Group.

        Args:
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +-----------------+------------------------------------------------------------+
                | Embeddable Link |                        Description                         |
                +=================+============================================================+
                | read-task       | Embeds the associated task in the response. For example,   |
                |                 | embed=read-task                                            |
                +-----------------+------------------------------------------------------------+

            body:

        Returns:
            MoveHcmHostsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/connections/mssql/hosts'

        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Prepare headers
        _headers = {
            'accept': 'application/mssql-hosts=v1+json',
        }
        # Execute request
        try:
            resp = self.client.patch(
                _url_path,
                headers=_headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing move_mssql_host_connections.', errors
            )
        return move_hcm_hosts_response.MoveHcmHostsResponse.from_dictionary(resp)

    def create_mssql_host_connection_credentials(
        self,
        body: create_mssql_host_connection_credentials_v1_request.CreateMssqlHostConnectionCredentialsV1Request = None,
    ) -> create_host_ec_credentials_response.CreateHostECCredentialsResponse:
        """Create Edge Connector Credentials for the specified MSSQL host.

        Args:
            body:

        Returns:
            CreateHostECCredentialsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/connections/mssql/hosts/eccredentials'

        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/mssql-hosts=v1+json',
        }
        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=_headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_mssql_host_connection_credentials.', errors
            )
        return create_host_ec_credentials_response.CreateHostECCredentialsResponse.from_dictionary(
            resp
        )

    def read_mssql_host_connections(
        self, host_id: str
    ) -> read_hcm_host_response.ReadHcmHostResponse:
        """Returns a representation of the specified host.

        Args:
            host_id:
                Performs the operation on a host within the specified host id.
        Returns:
            ReadHcmHostResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/connections/mssql/hosts/{host_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'host_id': host_id})
        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/mssql-hosts=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_mssql_host_connections.', errors
            )
        return read_hcm_host_response.ReadHcmHostResponse.from_dictionary(resp)

    def list_mssql_hosts(
        self, limit: int = None, start: str = None, filter: str = None, embed: str = None
    ) -> list_mssql_hosts_response.ListMssqlHostsResponse:
        """Returns a list of hosts

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
                | endpoint                  | $contains        | Filter Host where given       |
                |                           |                  | string is a substring of the  |
                |                           |                  | endpoint.                     |
                +---------------------------+------------------+-------------------------------+
                | group_id                  | $eq              | Filter Host where given       |
                |                           |                  | string is equal to the        |
                |                           |                  | group_id.                     |
                +---------------------------+------------------+-------------------------------+
                | subgroup_id               | $eq              | Filter Host where given       |
                |                           |                  | string is equal to the        |
                |                           |                  | subgroup_id.                  |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | Filter Host whose policy_id   |
                |                           |                  | is equal to the given string. |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $eq              | Filter Host whose             |
                |                           |                  | protection_status is equal to |
                |                           |                  | the given string.             |
                +---------------------------+------------------+-------------------------------+
                | id                        | $eq              | Filter Host whose id is equal |
                |                           |                  | to the given string.          |
                +---------------------------+------------------+-------------------------------+
                | status                    | $eq              | Filter Database whose status  |
                |                           |                  | is equal to the given string. |
                +---------------------------+------------------+-------------------------------+

            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +--------------------------+---------------------------------------------------+
                |     Embeddable Link      |                    Description                    |
                +==========================+===================================================+
                | read-management-group    | Embeds the associated management group details    |
                |                          | in the response. For example, embed=read-         |
                |                          | management-group                                  |
                +--------------------------+---------------------------------------------------+
                | read-management-subgroup | Embeds the associated management subgroup         |
                |                          | details in the response. For example, embed=read- |
                |                          | management-subgroup                               |
                +--------------------------+---------------------------------------------------+

                For more information about embedded links, refer to the
                Embedding Referenced Resources section of this guide.
        Returns:
            ListMssqlHostsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/mssql/hosts'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter, 'embed': embed}

        # Prepare headers
        _headers = {
            'accept': 'application/mssql-hosts=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_mssql_hosts.', errors
            )
        return list_mssql_hosts_response.ListMssqlHostsResponse.from_dictionary(resp)

    def read_mssql_hosts(self, host_id: str) -> read_mssql_host_response.ReadMssqlHostResponse:
        """Returns a representation of the specified host.

        Args:
            host_id:
                Performs the operation on a host within the specified host id.
        Returns:
            ReadMssqlHostResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/mssql/hosts/{host_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'host_id': host_id})
        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/mssql-hosts=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_mssql_hosts.', errors
            )
        return read_mssql_host_response.ReadMssqlHostResponse.from_dictionary(resp)
