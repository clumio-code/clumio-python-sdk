#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import download_shared_file_response
from clumioapi.models import download_shared_file_v1_request
from clumioapi.models import generate_restored_file_passcode_response
from clumioapi.models import restore_file_response
from clumioapi.models import restore_files_v1_request
from clumioapi.models import restored_files_response
from clumioapi.models import share_file_restore_email_response
from clumioapi.models import share_restored_file_v1_request
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
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

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
        self, embed: str = None, body: restore_files_v1_request.RestoreFilesV1Request = None
    ) -> restore_file_response.RestoreFileResponse:
        """Restores one or more files from the specified backup.

        Args:
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +-----------------+------------------------------------------------------------+
                | Embeddable Link |                        Description                         |
                +=================+============================================================+
                | read-task       | Embeds the associated task in the response. For example,   |
                |                 | embed=read-task                                            |
                +-----------------+------------------------------------------------------------+

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
        _query_parameters = {'embed': embed}

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

    def download_shared_file(
        self, body: download_shared_file_v1_request.DownloadSharedFileV1Request = None
    ) -> download_shared_file_response.DownloadSharedFileResponse:
        """Downloads one or more restored files, bundled into a ZIP file, that another user
        shared with you by email.

        Args:
            body:

        Returns:
            DownloadSharedFileResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/restores/files/_download'

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
                'Error occurred while executing download_shared_file.', errors
            )
        return download_shared_file_response.DownloadSharedFileResponse.from_dictionary(resp)

    def generate_restored_file_passcode(
        self, restored_file_id: str
    ) -> generate_restored_file_passcode_response.GenerateRestoredFilePasscodeResponse:
        """Generates a new passcode to access restored files shared by email. A passcode is
        automatically generated when you share restored files by email. Only regenerate
        a
        passcode if you (or the recipient) have lost the original passcode. When you
        regenerate a new passcode, the old one becomes invalid.

        Args:
            restored_file_id:
                Performs the operation on the restored file with the specified ID. Use
                [GET /restores/files](#operation/list-restored-files) to fetch the `id` value.
        Returns:
            GenerateRestoredFilePasscodeResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/restores/files/{restored_file_id}/_generate_passcode'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'restored_file_id': restored_file_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.post(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing generate_restored_file_passcode.', errors
            )
        return generate_restored_file_passcode_response.GenerateRestoredFilePasscodeResponse.from_dictionary(
            resp
        )

    def share_restored_file(
        self,
        restored_file_id: str,
        body: share_restored_file_v1_request.ShareRestoredFileV1Request = None,
    ) -> share_file_restore_email_response.ShareFileRestoreEmailResponse:
        """Sends a downloadable link to the specified email recipient to access restored
        files
        shared by email. Restored files are initially sent by email using
        [POST /restores/files](#operation/restore-files). After you send the initial
        email to one user, you can run
        this endpoint to share the email with additional users or to resend the email to
        the initial user. Also send the passcode generated from
        [POST /restores/files](#operation/restore-files) to these users so they can
        access
        the restored files.

        Args:
            restored_file_id:
                Performs the operation on the restored files with the specified ID. Use
                [GET/restores/files](#operation/list-restored-files) to fetch the `id` value.
            body:

        Returns:
            ShareFileRestoreEmailResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/restores/files/{restored_file_id}/_share'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'restored_file_id': restored_file_id}
        )
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
                'Error occurred while executing share_restored_file.', errors
            )
        return share_file_restore_email_response.ShareFileRestoreEmailResponse.from_dictionary(resp)
