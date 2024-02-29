#
# Copyright 2023. Clumio, Inc.
#

import json
from typing import Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_ec2_mssql_instances_response
from clumioapi.models import read_ec2_mssql_instance_response
import requests


class Ec2MssqlInstanceV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for ec2-mssql-instance resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.ec2-mssql-instance=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_ec2_mssql_instances(
        self, limit: int = None, start: str = None, filter: str = None, **kwargs
    ) -> Union[
        list_ec2_mssql_instances_response.ListEC2MSSQLInstancesResponse,
        tuple[
            requests.Response,
            Optional[list_ec2_mssql_instances_response.ListEC2MSSQLInstancesResponse],
        ],
    ]:
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
                | environment_id            | $eq              | The Clumio-assigned ID of the |
                |                           |                  | AWS environment.              |
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
                | status                    | $eq              | Filter Instances whose status |
                |                           |                  | is equal to the given string. |
                +---------------------------+------------------+-------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_ec2_mssql_instances_response.ListEC2MSSQLInstancesResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/aws/ec2-mssql/instances'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

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
                'Error occurred while executing list_ec2_mssql_instances.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                list_ec2_mssql_instances_response.ListEC2MSSQLInstancesResponse.from_dictionary(
                    resp.json()
                ),
            )
        return list_ec2_mssql_instances_response.ListEC2MSSQLInstancesResponse.from_dictionary(resp)

    def read_ec2_mssql_instance(self, instance_id: str, **kwargs) -> Union[
        read_ec2_mssql_instance_response.ReadEC2MSSQLInstanceResponse,
        tuple[
            requests.Response,
            Optional[read_ec2_mssql_instance_response.ReadEC2MSSQLInstanceResponse],
        ],
    ]:
        """Returns a representation of the specified instance.

        Args:
            instance_id:
                Performs the operation on the instance with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_ec2_mssql_instance_response.ReadEC2MSSQLInstanceResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/aws/ec2-mssql/instances/{instance_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'instance_id': instance_id}
        )
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
                'Error occurred while executing read_ec2_mssql_instance.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                read_ec2_mssql_instance_response.ReadEC2MSSQLInstanceResponse.from_dictionary(
                    resp.json()
                ),
            )
        return read_ec2_mssql_instance_response.ReadEC2MSSQLInstanceResponse.from_dictionary(resp)
