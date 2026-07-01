#
# Copyright 2023. Clumio, A Commvault Company.
#

import re
from typing import Any, Iterator
import urllib.parse

from clumioapi import api_helper
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import gcp_projects_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_gcp_projects_response
import requests
import retrying


class GcpProjectsV1Controller:
    """A Controller to access Endpoints for gcp-projects resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.gcp-projects=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_gcp_projects(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            gcp_projects_types.ListGcpProjectsV1FilterT
            | gcp_projects_types.ListGcpProjectsV1FilterTypeDef
            | None
        ) = None,
        **kwargs,
    ) -> list_gcp_projects_response.ListGCPProjectsResponse:
        """Returns a list of GCP projects. By default only active projects are
        returned; use the is_deleted filter to return deleted projects.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria.
                Supported filter fields:

                +------------+-----------+-----------------------------------------------------+
                |   Field    | Condition |                     Description                     |
                +============+===========+=====================================================+
                | project_id | $eq,$in   | The GCP project ID.                                 |
                +------------+-----------+-----------------------------------------------------+
                | is_deleted | $eq       | Boolean flag indicating whether to return deleted   |
                |            |           | (true) or active (false) projects.                  |
                +------------+-----------+-----------------------------------------------------+
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_gcp_projects_response.ListGCPProjectsResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/gcp/projects'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': api_helper.to_filter_query_str(
                filter, gcp_projects_types.ListGcpProjectsV1FilterT
            ),
        }

        resp_instance: list_gcp_projects_response.ListGCPProjectsResponse
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
            error_str = f'list_gcp_projects for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class GcpProjectsV1ControllerPaginator:
    """A Controller to access Endpoints for gcp-projects resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_gcp_projects(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            gcp_projects_types.ListGcpProjectsV1FilterT
            | gcp_projects_types.ListGcpProjectsV1FilterTypeDef
            | None
        ) = None,
        **kwargs,
    ) -> Iterator[list_gcp_projects_response.ListGCPProjectsResponse]:
        """Returns a list of GCP projects. By default only active projects are
        returned; use the is_deleted filter to return deleted projects.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria.
                Supported filter fields:

                +------------+-----------+-----------------------------------------------------+
                |   Field    | Condition |                     Description                     |
                +============+===========+=====================================================+
                | project_id | $eq,$in   | The GCP project ID.                                 |
                +------------+-----------+-----------------------------------------------------+
                | is_deleted | $eq       | Boolean flag indicating whether to return deleted   |
                |            |           | (true) or active (false) projects.                  |
                +------------+-----------+-----------------------------------------------------+
        """
        controller = GcpProjectsV1Controller(self.controller)
        while True:
            response = controller.list_gcp_projects(
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
