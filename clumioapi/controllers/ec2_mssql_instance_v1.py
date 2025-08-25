#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Any, Iterator, Optional, Union
import urllib.parse

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import ec2_mssql_instance_types
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
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: ec2_mssql_instance_types.ListEc2MssqlInstancesV1FilterT | None = None,
        **kwargs,
    ) -> list_ec2_mssql_instances_response.ListEC2MSSQLInstancesResponse:
        """Returns a list of Instances

        Args:
            limit:
                Limits the size of the items returned in the response.
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

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_ec2_mssql_instances_response.ListEC2MSSQLInstancesResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/datasources/aws/ec2-mssql/instances'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_ec2_mssql_instances_response.ListEC2MSSQLInstancesResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'list_ec2_mssql_instances for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_ec2_mssql_instance(
        self, instance_id: str | None = None, **kwargs
    ) -> read_ec2_mssql_instance_response.ReadEC2MSSQLInstanceResponse:
        """Returns a representation of the specified instance.

        Args:
            instance_id:
                Performs the operation on the instance with the specified ID.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return read_ec2_mssql_instance_response.ReadEC2MSSQLInstanceResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/datasources/aws/ec2-mssql/instances/{instance_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'instance_id': instance_id}
        )
        _query_parameters: dict[str, Any] = {}

        resp_instance: read_ec2_mssql_instance_response.ReadEC2MSSQLInstanceResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'read_ec2_mssql_instance for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class Ec2MssqlInstanceV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for ec2-mssql-instance resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = Ec2MssqlInstanceV1Controller(config)

    def list_ec2_mssql_instances(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: ec2_mssql_instance_types.ListEc2MssqlInstancesV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[list_ec2_mssql_instances_response.ListEC2MSSQLInstancesResponse]:
        """Returns a list of Instances

        Args:
            limit:
                Limits the size of the items returned in the response.
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

        """
        start = start or '1'
        while True:
            response = self.controller.list_ec2_mssql_instances(
                limit=limit, start=start, filter=filter, **kwargs
            )
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
