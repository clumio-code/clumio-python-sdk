#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
import re
from typing import Any, Iterator, Optional, Union
import urllib.parse

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import aws_s3_buckets_v1_bucket_matcher_types
from clumioapi.controllers.types import restored_files_types
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
import retrying


class RestoredFilesV1Controller:
    """A Controller to access Endpoints for restored-files resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.restored-files=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_restored_files(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: restored_files_types.ListRestoredFilesV1FilterT | None = None,
        **kwargs,
    ) -> restored_files_response.RestoredFilesResponse:
        """Gets the list of active restored files for an asset.

        Args:
            limit:
                Limits the size of the items returned in the response.
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
                |            |                  | aws_ec2_instance, aws_ec2_instance and       |
                |            |                  | aws_dynamodb_table.                          |
                +------------+------------------+----------------------------------------------+
                | asset_id   | $eq              | Required. The Clumio-assigned ID of the      |
                |            |                  | asset                                        |
                |            |                  | within which to search for files.            |
                +------------+------------------+----------------------------------------------+

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return restored_files_response.RestoredFilesResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/restores/files'

        if start:
            _url_path = f'{_url_path}?start={start}'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: restored_files_response.RestoredFilesResponse
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
            error_str = f'list_restored_files for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def restore_files(
        self,
        embed: str | None = None,
        body: restore_files_v1_request.RestoreFilesV1Request | None = None,
        **kwargs,
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

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return restore_file_response.RestoreFileResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/restores/files'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'embed': embed,
        }

        resp_instance: restore_file_response.RestoreFileResponse
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
            error_str = f'restore_files for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def download_shared_file(
        self,
        body: download_shared_file_v1_request.DownloadSharedFileV1Request | None = None,
        **kwargs,
    ) -> download_shared_file_response.DownloadSharedFileResponse:
        """Downloads one or more restored files, bundled into a ZIP file, that another user
        shared with you by email.

        Args:
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return download_shared_file_response.DownloadSharedFileResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/restores/files/_download'

        _query_parameters: dict[str, Any] = {}

        resp_instance: download_shared_file_response.DownloadSharedFileResponse
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
            error_str = f'download_shared_file for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def generate_restored_file_passcode(
        self, restored_file_id: str | None = None, **kwargs
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
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return generate_restored_file_passcode_response.GenerateRestoredFilePasscodeResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/restores/files/{restored_file_id}/_generate_passcode'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'restored_file_id': restored_file_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: generate_restored_file_passcode_response.GenerateRestoredFilePasscodeResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.post(
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
                f'generate_restored_file_passcode for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def share_restored_file(
        self,
        restored_file_id: str | None = None,
        body: share_restored_file_v1_request.ShareRestoredFileV1Request | None = None,
        **kwargs,
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

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return share_file_restore_email_response.ShareFileRestoreEmailResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/restores/files/{restored_file_id}/_share'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'restored_file_id': restored_file_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: share_file_restore_email_response.ShareFileRestoreEmailResponse
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
            error_str = f'share_restored_file for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class RestoredFilesV1ControllerPaginator:
    """A Controller to access Endpoints for restored-files resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_restored_files(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: restored_files_types.ListRestoredFilesV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[restored_files_response.RestoredFilesResponse]:
        """Gets the list of active restored files for an asset.

        Args:
            limit:
                Limits the size of the items returned in the response.
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
                |            |                  | aws_ec2_instance, aws_ec2_instance and       |
                |            |                  | aws_dynamodb_table.                          |
                +------------+------------------+----------------------------------------------+
                | asset_id   | $eq              | Required. The Clumio-assigned ID of the      |
                |            |                  | asset                                        |
                |            |                  | within which to search for files.            |
                +------------+------------------+----------------------------------------------+

        """
        controller = RestoredFilesV1Controller(self.controller)
        while True:
            response = controller.list_restored_files(
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
