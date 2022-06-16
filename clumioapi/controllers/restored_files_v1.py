#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import restore_file_response
from clumioapi.models import restore_files_v1_request
from clumioapi.models import restored_files_response
import requests


class RestoredFilesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for restored-files resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.restored-files=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }

    def list_restored_files(
        self, limit: int = None, start: str = None, filter: str = None
    ) -> restored_files_response.RestoredFilesResponse:
        """Gets the list of active restored files for an asset.

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
                |            |                  | aws_ec2_instance, vmware_vm and              |
                |            |                  | aws_dynamodb_table.                          |
                +------------+------------------+----------------------------------------------+
                | asset_id   | $eq              | Required. The Clumio-assigned ID of the      |
                |            |                  | asset                                        |
                |            |                  | within which to search for files.            |
                +------------+------------------+----------------------------------------------+

        Returns:
            RestoredFilesResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/restores/files'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_restored_files.', errors
            )
        return restored_files_response.RestoredFilesResponse.from_dictionary(resp)

    def restore_files(
        self, body: restore_files_v1_request.RestoreFilesV1Request = None
    ) -> restore_file_response.RestoreFileResponse:
        """Restores one or more files from the specified backup.

        Args:
            body:

        Returns:
            RestoreFileResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/restores/files'

        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing restore_files.', errors
            )
        return restore_file_response.RestoreFileResponse.from_dictionary(resp)
