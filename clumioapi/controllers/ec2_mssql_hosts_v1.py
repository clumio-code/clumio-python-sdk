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
from clumioapi.models import list_ec2_mssql_inv_hosts_response
from clumioapi.models import read_ec2_mssql_inv_host_response
import requests


class Ec2MssqlHostsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for ec2-mssql-hosts resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.ec2-mssql-hosts=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_ec2_mssql_hosts(
        self, limit: int = None, start: str = None, filter: str = None, embed: str = None, **kwargs
    ) -> Union[
        list_ec2_mssql_inv_hosts_response.ListEC2MSSQLInvHostsResponse,
        tuple[
            requests.Response,
            Optional[list_ec2_mssql_inv_hosts_response.ListEC2MSSQLInvHostsResponse],
        ],
    ]:
        """Returns a list of EC2 MSSQL hosts

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
                | environment_id            | $eq              | The Clumio-assigned ID of the |
                |                           |                  | AWS environment.              |
                +---------------------------+------------------+-------------------------------+
                | id                        | $eq              | Filter Host whose id is equal |
                |                           |                  | to the given string.          |
                +---------------------------+------------------+-------------------------------+
                | name                      | $contains        | Filter Host where given       |
                |                           |                  | string is a substring of the  |
                |                           |                  | name.                         |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | Filter Host whose policy_id   |
                |                           |                  | is equal to the given string. |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $eq              | Filter Host whose             |
                |                           |                  | protection_status is equal to |
                |                           |                  | the given string.             |
                +---------------------------+------------------+-------------------------------+
                | status                    | $eq              | Filter Hosts whose status is  |
                |                           |                  | equal to the given string.    |
                +---------------------------+------------------+-------------------------------+

            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +-----------------+-------------+
                | Embeddable Link | Description |
                +=================+=============+
                +-----------------+-------------+

                For more information about embedded links, refer to the
                Embedding Referenced Resources section of this guide.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_ec2_mssql_inv_hosts_response.ListEC2MSSQLInvHostsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/aws/ec2-mssql/hosts'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter, 'embed': embed}

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
                'Error occurred while executing list_ec2_mssql_hosts.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                list_ec2_mssql_inv_hosts_response.ListEC2MSSQLInvHostsResponse.from_dictionary(
                    resp.json()
                ),
            )
        return list_ec2_mssql_inv_hosts_response.ListEC2MSSQLInvHostsResponse.from_dictionary(resp)

    def read_ec2_mssql_host(self, host_id: str, **kwargs) -> Union[
        read_ec2_mssql_inv_host_response.ReadEC2MSSQLInvHostResponse,
        tuple[
            requests.Response,
            Optional[read_ec2_mssql_inv_host_response.ReadEC2MSSQLInvHostResponse],
        ],
    ]:
        """Returns a representation of the specified host.

        Args:
            host_id:
                Performs the operation on a host within the specified host id.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_ec2_mssql_inv_host_response.ReadEC2MSSQLInvHostResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/aws/ec2-mssql/hosts/{host_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'host_id': host_id})
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
                'Error occurred while executing read_ec2_mssql_host.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                read_ec2_mssql_inv_host_response.ReadEC2MSSQLInvHostResponse.from_dictionary(
                    resp.json()
                ),
            )
        return read_ec2_mssql_inv_host_response.ReadEC2MSSQLInvHostResponse.from_dictionary(resp)
