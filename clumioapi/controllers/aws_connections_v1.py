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
from clumioapi.controllers.types import aws_connections_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_aws_connection_response
from clumioapi.models import create_aws_connection_v1_request
from clumioapi.models import list_aws_connections_response
from clumioapi.models import read_aws_connection_response
from clumioapi.models import update_aws_connection_response
from clumioapi.models import update_aws_connection_v1_request
import requests


class AwsConnectionsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for aws-connections resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.aws-connections=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_aws_connections(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: aws_connections_types.ListAwsConnectionsV1FilterT | None = None,
        **kwargs,
    ) -> list_aws_connections_response.ListAWSConnectionsResponse:
        """Returns a list of AWS Connections

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria.
                The following table lists the supported filter fields for this resource and the
                operations
                that can be performed on the field:

                +------------------------+-------------------+---------------------------------+
                |         Field          | Filter Condition  |           Description           |
                +========================+===================+=================================+
                | account_native_id      | $begins_with, $in | A prefix of the account ID to   |
                |                        |                   | search for or the list of       |
                |                        |                   | account IDs to return.          |
                |                        |                   |                                 |
                |                        |                   | {"account_native_id":{"$begins_ |
                |                        |                   | with":"23345"}}                 |
                |                        |                   |                                 |
                |                        |                   |                                 |
                |                        |                   | {"account_native_id":{"$in":["1 |
                |                        |                   | 11111111111", "222222222222"]}} |
                |                        |                   |                                 |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+
                | aws_region             | $in               | Lists the connections in the    |
                |                        |                   | given regions.                  |
                |                        |                   |                                 |
                |                        |                   | {"aws_region":{"$in":"["us-     |
                |                        |                   | west-2"]"}}                     |
                |                        |                   |                                 |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+
                | account_alias          | $contains         | A substring within the account  |
                |                        |                   | alias (if available) to search  |
                |                        |                   | for.                            |
                |                        |                   |                                 |
                |                        |                   | {"account_alias":{"$contains":" |
                |                        |                   | foo"}}                          |
                |                        |                   |                                 |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+
                | connection_type        | $eq               | A connection type to search     |
                |                        |                   | for. Supported types are:       |
                |                        |                   | ['discover', 'protect'].        |
                |                        |                   |                                 |
                |                        |                   | {"connection_type":{"$eq":"prot |
                |                        |                   | ect"}}                          |
                |                        |                   |                                 |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+
                | connection_status      | $eq, $in          | The status of the connection to |
                |                        |                   | the environment. Possible       |
                |                        |                   | values include "connecting",    |
                |                        |                   | "connected", "unlinked". For    |
                |                        |                   | example,                        |
                |                        |                   | filter={"connection_status":{"$ |
                |                        |                   | eq":"connected"}}               |
                |                        |                   | filter={"connection_status":{"$ |
                |                        |                   | in":["unlinked","connected"]}}  |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+
                | organizational_unit_id | $in               | Lists the connections in the    |
                |                        |                   | specified organizational units. |
                |                        |                   |                                 |
                |                        |                   | {"organizational_unit_id":{"$in |
                |                        |                   | ":["ca849d10-7ea1-4869-b2d0-    |
                |                        |                   | 46c42b5f2bea", "27b9ee09-c59c-  |
                |                        |                   | 466f-b2c4-223e9h8df7c8"]}}      |
                |                        |                   |                                 |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+
                | services_enabled       | $contains         | Lists the connections that have |
                |                        |                   | the given asset_types enabled.  |
                |                        |                   | Supported types are: ['rds',    |
                |                        |                   | 's3', 'ebs', 'ec2mssql',        |
                |                        |                   | 'iceberg_on_glue'].             |
                |                        |                   |                                 |
                |                        |                   | {"services_enabled":{"$contains |
                |                        |                   | ":"rds"}}                       |
                |                        |                   |                                 |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_aws_connections_response.ListAWSConnectionsResponse.from_response(response)

        # Prepare query URL
        _url_path = '/connections/aws'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_aws_connections_response.ListAWSConnectionsResponse
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
            error_str = f'list_aws_connections for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def create_aws_connection(
        self,
        body: create_aws_connection_v1_request.CreateAwsConnectionV1Request | None = None,
        **kwargs,
    ) -> create_aws_connection_response.CreateAWSConnectionResponse:
        """Initiate a new AWS connection.

        Args:
            body:

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return create_aws_connection_response.CreateAWSConnectionResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/connections/aws'

        _query_parameters: dict[str, Any] = {}

        resp_instance: create_aws_connection_response.CreateAWSConnectionResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=body.dict() if body else None,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'create_aws_connection for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_aws_connection(
        self, connection_id: str | None = None, return_external_id: str | None = None, **kwargs
    ) -> read_aws_connection_response.ReadAWSConnectionResponse:
        """Returns a representation of the specified AWS connection.

        Args:
            connection_id:
                Performs the operation on the AWS connection with the specified ID.
            return_external_id:
                Returns external id along with the connection details
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return read_aws_connection_response.ReadAWSConnectionResponse.from_response(response)

        # Prepare query URL
        _url_path = '/connections/aws/{connection_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'connection_id': connection_id}
        )
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'return_external_id': return_external_id}

        resp_instance: read_aws_connection_response.ReadAWSConnectionResponse
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
            error_str = f'read_aws_connection for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def delete_aws_connection(self, connection_id: str | None = None, **kwargs) -> object:
        """Delete the specified AWS connection.

        Args:
            connection_id:
                Performs the operation on the AWS connection with the specified ID.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return resp

        # Prepare query URL
        _url_path = '/connections/aws/{connection_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'connection_id': connection_id}
        )
        _query_parameters: dict[str, Any] = {}

        resp_instance: object
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.delete(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'delete_aws_connection for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def update_aws_connection(
        self,
        connection_id: str | None = None,
        body: update_aws_connection_v1_request.UpdateAwsConnectionV1Request | None = None,
        **kwargs,
    ) -> update_aws_connection_response.UpdateAWSConnectionResponse:
        """Returns a new template url for the specified configuration.

        Args:
            connection_id:
                Updates the connection with the specified connection ID
            body:

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return update_aws_connection_response.UpdateAWSConnectionResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/connections/aws/{connection_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'connection_id': connection_id}
        )
        _query_parameters: dict[str, Any] = {}

        resp_instance: update_aws_connection_response.UpdateAWSConnectionResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.patch(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=body.dict() if body else None,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'update_aws_connection for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class AwsConnectionsV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for aws-connections resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = AwsConnectionsV1Controller(config)

    def list_aws_connections(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: aws_connections_types.ListAwsConnectionsV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[list_aws_connections_response.ListAWSConnectionsResponse]:
        """Returns a list of AWS Connections

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria.
                The following table lists the supported filter fields for this resource and the
                operations
                that can be performed on the field:

                +------------------------+-------------------+---------------------------------+
                |         Field          | Filter Condition  |           Description           |
                +========================+===================+=================================+
                | account_native_id      | $begins_with, $in | A prefix of the account ID to   |
                |                        |                   | search for or the list of       |
                |                        |                   | account IDs to return.          |
                |                        |                   |                                 |
                |                        |                   | {"account_native_id":{"$begins_ |
                |                        |                   | with":"23345"}}                 |
                |                        |                   |                                 |
                |                        |                   |                                 |
                |                        |                   | {"account_native_id":{"$in":["1 |
                |                        |                   | 11111111111", "222222222222"]}} |
                |                        |                   |                                 |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+
                | aws_region             | $in               | Lists the connections in the    |
                |                        |                   | given regions.                  |
                |                        |                   |                                 |
                |                        |                   | {"aws_region":{"$in":"["us-     |
                |                        |                   | west-2"]"}}                     |
                |                        |                   |                                 |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+
                | account_alias          | $contains         | A substring within the account  |
                |                        |                   | alias (if available) to search  |
                |                        |                   | for.                            |
                |                        |                   |                                 |
                |                        |                   | {"account_alias":{"$contains":" |
                |                        |                   | foo"}}                          |
                |                        |                   |                                 |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+
                | connection_type        | $eq               | A connection type to search     |
                |                        |                   | for. Supported types are:       |
                |                        |                   | ['discover', 'protect'].        |
                |                        |                   |                                 |
                |                        |                   | {"connection_type":{"$eq":"prot |
                |                        |                   | ect"}}                          |
                |                        |                   |                                 |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+
                | connection_status      | $eq, $in          | The status of the connection to |
                |                        |                   | the environment. Possible       |
                |                        |                   | values include "connecting",    |
                |                        |                   | "connected", "unlinked". For    |
                |                        |                   | example,                        |
                |                        |                   | filter={"connection_status":{"$ |
                |                        |                   | eq":"connected"}}               |
                |                        |                   | filter={"connection_status":{"$ |
                |                        |                   | in":["unlinked","connected"]}}  |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+
                | organizational_unit_id | $in               | Lists the connections in the    |
                |                        |                   | specified organizational units. |
                |                        |                   |                                 |
                |                        |                   | {"organizational_unit_id":{"$in |
                |                        |                   | ":["ca849d10-7ea1-4869-b2d0-    |
                |                        |                   | 46c42b5f2bea", "27b9ee09-c59c-  |
                |                        |                   | 466f-b2c4-223e9h8df7c8"]}}      |
                |                        |                   |                                 |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+
                | services_enabled       | $contains         | Lists the connections that have |
                |                        |                   | the given asset_types enabled.  |
                |                        |                   | Supported types are: ['rds',    |
                |                        |                   | 's3', 'ebs', 'ec2mssql',        |
                |                        |                   | 'iceberg_on_glue'].             |
                |                        |                   |                                 |
                |                        |                   | {"services_enabled":{"$contains |
                |                        |                   | ":"rds"}}                       |
                |                        |                   |                                 |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+

        """
        start = start or '1'
        while True:
            response = self.controller.list_aws_connections(
                limit=limit, start=start, filter=filter, **kwargs
            )
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
