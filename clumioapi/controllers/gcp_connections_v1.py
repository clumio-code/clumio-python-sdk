#
# Copyright 2023. Clumio, A Commvault Company.
#

import re
from typing import Any, Iterator
import urllib.parse

from clumioapi import api_helper
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import gcp_connections_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_gcp_connection_response
from clumioapi.models import create_gcp_connection_v1_request
from clumioapi.models import list_gcp_connections_response
from clumioapi.models import post_process_gcp_connection_v1_request
from clumioapi.models import read_gcp_connection_response
from clumioapi.models import update_gcp_connection_response
from clumioapi.models import update_gcp_connection_v1_request
import requests
import retrying


class GcpConnectionsV1Controller:
    """A Controller to access Endpoints for gcp-connections resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.gcp-connections=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_gcp_connections(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            gcp_connections_types.ListGcpConnectionsV1FilterT
            | gcp_connections_types.ListGcpConnectionsV1FilterTypeDef
            | None
        ) = None,
        **kwargs,
    ) -> list_gcp_connections_response.ListGCPConnectionsResponse:
        """Lists GCP Connections for a particular org

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

                +-------------------+------------------+---------------------------------------+
                |       Field       | Filter Condition |              Description              |
                +===================+==================+=======================================+
                | project_id        | $contains        | A substring within the project id to  |
                |                   |                  | search for.                           |
                |                   |                  | {"project_id":{"$contains":"project_i |
                |                   |                  | d1"}}                                 |
                |                   |                  |                                       |
                +-------------------+------------------+---------------------------------------+
                | project_name      | $contains        | A substring within the project name   |
                |                   |                  | to search for.                        |
                |                   |                  | {"project_name":{"$contains":"product |
                |                   |                  | ion"}}                                |
                |                   |                  |                                       |
                +-------------------+------------------+---------------------------------------+
                | connection_status | $in              | The status of the connection.         |
                |                   |                  | Possible values: "pending",           |
                |                   |                  | "connected", "disconnected" and       |
                |                   |                  | "retired".                            |
                |                   |                  | filter={"connection_status":{"$in":[" |
                |                   |                  | installed","new"]}}                   |
                |                   |                  |                                       |
                +-------------------+------------------+---------------------------------------+
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_gcp_connections_response.ListGCPConnectionsResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/connections/gcp'

        if start:
            _url_path = f'{_url_path}?start={start}'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'filter': api_helper.to_filter_query_str(
                filter, gcp_connections_types.ListGcpConnectionsV1FilterT
            ),
        }

        resp_instance: list_gcp_connections_response.ListGCPConnectionsResponse
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
            error_str = f'list_gcp_connections for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def create_gcp_connection(
        self,
        body: create_gcp_connection_v1_request.CreateGcpConnectionV1Request | None = None,
        **kwargs,
    ) -> create_gcp_connection_response.CreateGCPConnectionResponse:
        """Create a new GCP Connection. This API should only be invoked by the Clumio
        Terraform provider and should not be invoked manually.

        Args:
            body:
                The body of the request.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return create_gcp_connection_response.CreateGCPConnectionResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/connections/gcp'

        _query_parameters: dict[str, Any] = {}

        resp_instance: create_gcp_connection_response.CreateGCPConnectionResponse
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
            error_str = f'create_gcp_connection for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def post_process_gcp_connection(
        self,
        body: (
            post_process_gcp_connection_v1_request.PostProcessGcpConnectionV1Request | None
        ) = None,
        **kwargs,
    ) -> object:
        """Performs post-processing after GCP Connection Create, Update or Delete. This API
        should only be invoked by the Clumio Terraform provider and should not be
        invoked manually.

        Args:
            body:
                The body of the request.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return resp

        # Prepare query URL
        _url_path = '/connections/gcp/_post_process'

        _query_parameters: dict[str, Any] = {}

        resp_instance: object
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
            error_str = (
                f'post_process_gcp_connection for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_gcp_connection(
        self, project_id: str | None = None, **kwargs
    ) -> read_gcp_connection_response.ReadGCPConnectionResponse:
        """Reads a GCP Connection from the given project id

        Args:
            project_id:
                Performs the operation on the GCP connection with the specified project ID.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_gcp_connection_response.ReadGCPConnectionResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/connections/gcp/{project_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'project_id': project_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: read_gcp_connection_response.ReadGCPConnectionResponse
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
            error_str = f'read_gcp_connection for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def delete_gcp_connection(self, project_id: str | None = None, **kwargs) -> object:
        """Deletes a GCP Connection

        Args:
            project_id:
                Performs the operation on the GCP connection with the specified project ID.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return resp

        # Prepare query URL
        _url_path = '/connections/gcp/{project_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'project_id': project_id}
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
            error_str = f'delete_gcp_connection for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def update_gcp_connection(
        self,
        project_id: str | None = None,
        body: update_gcp_connection_v1_request.UpdateGcpConnectionV1Request | None = None,
        **kwargs,
    ) -> update_gcp_connection_response.UpdateGCPConnectionResponse:
        """Updates a GCP Connection having the given project id. This API should only be
        invoked by the Clumio Terraform provider and should not be invoked manually.

        Args:
            project_id:
                Performs the operation on the GCP connection with the specified project ID.
            body:
                The body of the request.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return update_gcp_connection_response.UpdateGCPConnectionResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/connections/gcp/{project_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'project_id': project_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: update_gcp_connection_response.UpdateGCPConnectionResponse
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
            error_str = f'update_gcp_connection for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class GcpConnectionsV1ControllerPaginator:
    """A Controller to access Endpoints for gcp-connections resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_gcp_connections(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            gcp_connections_types.ListGcpConnectionsV1FilterT
            | gcp_connections_types.ListGcpConnectionsV1FilterTypeDef
            | None
        ) = None,
        **kwargs,
    ) -> Iterator[list_gcp_connections_response.ListGCPConnectionsResponse]:
        """Lists GCP Connections for a particular org

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

                +-------------------+------------------+---------------------------------------+
                |       Field       | Filter Condition |              Description              |
                +===================+==================+=======================================+
                | project_id        | $contains        | A substring within the project id to  |
                |                   |                  | search for.                           |
                |                   |                  | {"project_id":{"$contains":"project_i |
                |                   |                  | d1"}}                                 |
                |                   |                  |                                       |
                +-------------------+------------------+---------------------------------------+
                | project_name      | $contains        | A substring within the project name   |
                |                   |                  | to search for.                        |
                |                   |                  | {"project_name":{"$contains":"product |
                |                   |                  | ion"}}                                |
                |                   |                  |                                       |
                +-------------------+------------------+---------------------------------------+
                | connection_status | $in              | The status of the connection.         |
                |                   |                  | Possible values: "pending",           |
                |                   |                  | "connected", "disconnected" and       |
                |                   |                  | "retired".                            |
                |                   |                  | filter={"connection_status":{"$in":[" |
                |                   |                  | installed","new"]}}                   |
                |                   |                  |                                       |
                +-------------------+------------------+---------------------------------------+
        """
        controller = GcpConnectionsV1Controller(self.controller)
        while True:
            response = controller.list_gcp_connections(
                limit=limit, start=start, filter=filter, **kwargs
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
