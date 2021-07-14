#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_aws_regions_response
import requests


class AwsRegionsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for aws-regions resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config

    def list_connection_aws_regions(
        self, limit: int = None, start: str = None
    ) -> list_aws_regions_response.ListAWSRegionsResponse:
        """Returns a list of valid regions for creating AWS connections

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        Returns:
            ListAWSRegionsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/connections/aws/regions'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start}

        # Prepare headers
        _headers = {
            'accept': 'application/aws-regions=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_connection_aws_regions.', errors
            )
        return list_aws_regions_response.ListAWSRegionsResponse.from_dictionary(resp)
