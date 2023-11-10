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
        self, limit: int = None, start: str = None, **kwargs
    ) -> Union[
        list_aws_regions_response.ListAWSRegionsResponse,
        tuple[requests.Response, Optional[list_aws_regions_response.ListAWSRegionsResponse]],
    ]:
        """Returns a list of valid regions for creating AWS connections

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_aws_regions_response.ListAWSRegionsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/connections/aws/regions'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start}

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
                'Error occurred while executing list_connection_aws_regions.', errors
            )

        if self.config.raw_response:
            return resp, list_aws_regions_response.ListAWSRegionsResponse.from_dictionary(
                resp.json()
            )
        return list_aws_regions_response.ListAWSRegionsResponse.from_dictionary(resp)
