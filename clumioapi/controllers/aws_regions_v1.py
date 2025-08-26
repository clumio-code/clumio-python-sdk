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
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_aws_regions_response
import requests


class AwsRegionsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for aws-regions resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.aws-regions=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_connection_aws_regions(
        self, limit: int | None = None, start: str | None = None, **kwargs
    ) -> list_aws_regions_response.ListAWSRegionsResponse:
        """Returns a list of valid regions for creating AWS connections

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_aws_regions_response.ListAWSRegionsResponse.from_response(response)

        # Prepare query URL
        _url_path = '/connections/aws/regions'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'limit': limit, 'start': start}

        resp_instance: list_aws_regions_response.ListAWSRegionsResponse
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
            error_str = (
                f'list_connection_aws_regions for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class AwsRegionsV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for aws-regions resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = AwsRegionsV1Controller(config)

    def list_connection_aws_regions(
        self, limit: int | None = None, start: str | None = None, **kwargs
    ) -> Iterator[list_aws_regions_response.ListAWSRegionsResponse]:
        """Returns a list of valid regions for creating AWS connections

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        """
        start = start or '1'
        while True:
            response = self.controller.list_connection_aws_regions(
                limit=limit, start=start, **kwargs
            )
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
