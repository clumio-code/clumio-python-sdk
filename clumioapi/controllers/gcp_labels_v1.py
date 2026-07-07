#
# Copyright 2023. Clumio, A Commvault Company.
#

import re
from typing import Any, Iterator
import urllib.parse

from clumioapi import api_helper
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import gcp_labels_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_gcp_label_keys_response
from clumioapi.models import list_gcp_label_values_response
import requests
import retrying


class GcpLabelsV1Controller:
    """A Controller to access Endpoints for gcp-labels resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.gcp-labels=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_gcp_label_keys(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            gcp_labels_types.ListGcpLabelKeysV1FilterT
            | gcp_labels_types.ListGcpLabelKeysV1FilterTypeDef
            | None
        ) = None,
        **kwargs,
    ) -> list_gcp_label_keys_response.ListGCPLabelKeysResponse:
        """Returns a list of GCP label keys.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                TODO: Add comment
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_gcp_label_keys_response.ListGCPLabelKeysResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/gcp/label-keys'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': api_helper.to_filter_query_str(
                filter, gcp_labels_types.ListGcpLabelKeysV1FilterT
            ),
        }

        resp_instance: list_gcp_label_keys_response.ListGCPLabelKeysResponse
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
            error_str = f'list_gcp_label_keys for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def list_gcp_label_values(
        self,
        label_key_id: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            gcp_labels_types.ListGcpLabelValuesV1FilterT
            | gcp_labels_types.ListGcpLabelValuesV1FilterTypeDef
            | None
        ) = None,
        **kwargs,
    ) -> list_gcp_label_values_response.ListGCPLabelValuesResponse:
        """Returns a list of GCP label values for the specified label key.

        Args:
            label_key_id:

            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                TODO: Add comment
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_gcp_label_values_response.ListGCPLabelValuesResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/gcp/label-keys/{label_key_id}/label-values'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'label_key_id': label_key_id}
        )

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': api_helper.to_filter_query_str(
                filter, gcp_labels_types.ListGcpLabelValuesV1FilterT
            ),
        }

        resp_instance: list_gcp_label_values_response.ListGCPLabelValuesResponse
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
            error_str = f'list_gcp_label_values for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class GcpLabelsV1ControllerPaginator:
    """A Controller to access Endpoints for gcp-labels resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_gcp_label_keys(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            gcp_labels_types.ListGcpLabelKeysV1FilterT
            | gcp_labels_types.ListGcpLabelKeysV1FilterTypeDef
            | None
        ) = None,
        **kwargs,
    ) -> Iterator[list_gcp_label_keys_response.ListGCPLabelKeysResponse]:
        """Returns a list of GCP label keys.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                TODO: Add comment
        """
        controller = GcpLabelsV1Controller(self.controller)
        while True:
            response = controller.list_gcp_label_keys(
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

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_gcp_label_values(
        self,
        label_key_id: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            gcp_labels_types.ListGcpLabelValuesV1FilterT
            | gcp_labels_types.ListGcpLabelValuesV1FilterTypeDef
            | None
        ) = None,
        **kwargs,
    ) -> Iterator[list_gcp_label_values_response.ListGCPLabelValuesResponse]:
        """Returns a list of GCP label values for the specified label key.

        Args:
            label_key_id:

            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                TODO: Add comment
        """
        controller = GcpLabelsV1Controller(self.controller)
        while True:
            response = controller.list_gcp_label_values(
                label_key_id=label_key_id, limit=limit, start=start, filter=filter, **kwargs
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
