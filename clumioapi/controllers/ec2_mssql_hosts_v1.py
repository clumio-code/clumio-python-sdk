#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
import re
from typing import Any, Iterator, Optional, Union
import urllib.parse

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import aws_s3_buckets_v1_bucket_matcher_types
from clumioapi.controllers.types import ec2_mssql_hosts_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_ec2_mssql_inv_hosts_response
from clumioapi.models import read_ec2_mssql_inv_host_response
import requests
import retrying


class Ec2MssqlHostsV1Controller:
    """A Controller to access Endpoints for ec2-mssql-hosts resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.ec2-mssql-hosts=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_ec2_mssql_hosts(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: ec2_mssql_hosts_types.ListEc2MssqlHostsV1FilterT | None = None,
        embed: str | None = None,
        **kwargs,
    ) -> list_ec2_mssql_inv_hosts_response.ListEC2MSSQLInvHostsResponse:
        """Returns a list of EC2 MSSQL hosts

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
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_ec2_mssql_inv_hosts_response.ListEC2MSSQLInvHostsResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/datasources/aws/ec2-mssql/hosts'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
            'embed': embed,
        }

        resp_instance: list_ec2_mssql_inv_hosts_response.ListEC2MSSQLInvHostsResponse
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
            error_str = f'list_ec2_mssql_hosts for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_ec2_mssql_host(
        self, host_id: str | None = None, **kwargs
    ) -> read_ec2_mssql_inv_host_response.ReadEC2MSSQLInvHostResponse:
        """Returns a representation of the specified host.

        Args:
            host_id:
                Performs the operation on a host within the specified host id.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_ec2_mssql_inv_host_response.ReadEC2MSSQLInvHostResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/aws/ec2-mssql/hosts/{host_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'host_id': host_id})

        _query_parameters: dict[str, Any] = {}

        resp_instance: read_ec2_mssql_inv_host_response.ReadEC2MSSQLInvHostResponse
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
            error_str = f'read_ec2_mssql_host for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class Ec2MssqlHostsV1ControllerPaginator:
    """A Controller to access Endpoints for ec2-mssql-hosts resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_ec2_mssql_hosts(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: ec2_mssql_hosts_types.ListEc2MssqlHostsV1FilterT | None = None,
        embed: str | None = None,
        **kwargs,
    ) -> Iterator[list_ec2_mssql_inv_hosts_response.ListEC2MSSQLInvHostsResponse]:
        """Returns a list of EC2 MSSQL hosts

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
        """
        controller = Ec2MssqlHostsV1Controller(self.controller)
        while True:
            response = controller.list_ec2_mssql_hosts(
                limit=limit, start=start, filter=filter, embed=embed, **kwargs
            )
            yield response
            next_link = response.Links.Next  # type: ignore
            if not next_link:
                break
            next_link = next_link.Href
            if match := re.search(r'start=([^&]+)', next_link):  # type: ignore
                start = match.group(1)
            else:
                raise clumio_exception.ClumioException(
                    'Next link is malformed. Please contact clumio support.'
                )
