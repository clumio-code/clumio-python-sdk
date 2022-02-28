#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import file_list_response
from clumioapi.models import file_search_response
import requests


class BackupsFilesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for backups-files resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config

    def list_files(
        self, limit: int = None, start: str = None, filter: str = None
    ) -> file_search_response.FileSearchResponse:
        """Retrieve the list of files whose name matches a given regex pattern.

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists the supported filter fields for this resource and the
                filter
                conditions that can be applied on those fields:

                +------------+------------------+----------------------------------------------+
                |   Field    | Filter Condition |                 Description                  |
                +============+==================+==============================================+
                | asset_type | $eq              | Required. The type of the asset within which |
                |            |                  | to search for files. Possible values include |
                |            |                  | aws_ebs_volume,                              |
                |            |                  | aws_ec2_instance, and vmware_vm.             |
                +------------+------------------+----------------------------------------------+
                | asset_id   | $eq              | Required. The Clumio-assigned ID of the      |
                |            |                  | asset                                        |
                |            |                  | within which to search for files.            |
                +------------+------------------+----------------------------------------------+
                | name       | $regex           | A regex pattern to match against file names. |
                |            |                  | For example,                                 |
                |            |                  | filter={"name":{"$regex":"a(\\w){2,5}"}      |
                +------------+------------------+----------------------------------------------+

        Returns:
            FileSearchResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/files/search'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Prepare headers
        _headers = {
            'accept': 'application/backups-files=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_files.', errors
            )
        return file_search_response.FileSearchResponse.from_dictionary(resp)

    def list_file_versions(
        self, search_result_id: str, limit: int = None, start: str = None
    ) -> file_list_response.FileListResponse:
        """Retrieve the list of versions of the file.

        Args:
            search_result_id:
                Performs the operation on the file with the specified ID.
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
        Returns:
            FileListResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/files/search/{search_result_id}/versions'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'search_result_id': search_result_id}
        )
        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start}

        # Prepare headers
        _headers = {
            'accept': 'application/backups-files=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_file_versions.', errors
            )
        return file_list_response.FileListResponse.from_dictionary(resp)
