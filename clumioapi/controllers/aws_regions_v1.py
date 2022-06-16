#
# Copyright 2021. Clumio, Inc.
#

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

    def list_connection_aws_regions(
        self, limit: int = None, start: str = None, filter: str = None
    ) -> list_aws_regions_response.ListAWSRegionsResponse:
        """Returns a list of valid regions for creating AWS connections

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +----------------------+------------------+------------------------------------+
                |        Field         | Filter Condition |            Description             |
                +======================+==================+====================================+
                | is_data_plane_region | $eq              | The target regions which can be    |
                |                      |                  | chosen for out-of-region backups.  |
                |                      |                  | These are the regions for which    |
                |                      |                  | Clumio has a data plane. Set to    |
                |                      |                  | "true" to retrieve the AWS data    |
                |                      |                  | plane regions. For example, filter |
                |                      |                  | ={"is_data_plane_region":{"$eq":tr |
                |                      |                  | ue}}                               |
                +----------------------+------------------+------------------------------------+

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
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_connection_aws_regions.', errors
            )
        return list_aws_regions_response.ListAWSRegionsResponse.from_dictionary(resp)
