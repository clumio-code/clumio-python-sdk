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
from clumioapi.models import preview_details_protection_group_response
from clumioapi.models import preview_protection_group_async_response
from clumioapi.models import preview_protection_group_sync_response
from clumioapi.models import preview_protection_group_v1_request
from clumioapi.models import restore_objects_response
from clumioapi.models import restore_protection_group_response
from clumioapi.models import restore_protection_group_s3_objects_v1_request
from clumioapi.models import restore_protection_group_v1_request
import requests


class RestoredProtectionGroupsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for restored-protection-groups resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.restored-protection-groups=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def restore_protection_group(
        self,
        embed: str = None,
        body: restore_protection_group_v1_request.RestoreProtectionGroupV1Request = None,
        **kwargs,
    ) -> Union[
        restore_protection_group_response.RestoreProtectionGroupResponse,
        tuple[
            requests.Response,
            Optional[restore_protection_group_response.RestoreProtectionGroupResponse],
        ],
    ]:
        """Restores the specified protection group backup to the specified target
        destination.

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
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            restore_protection_group_response.RestoreProtectionGroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/protection-groups'

        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing restore_protection_group.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                restore_protection_group_response.RestoreProtectionGroupResponse.from_dictionary(
                    resp.json()
                ),
            )
        return restore_protection_group_response.RestoreProtectionGroupResponse.from_dictionary(
            resp
        )

    def preview_protection_group(
        self,
        protection_group_id: str,
        body: preview_protection_group_v1_request.PreviewProtectionGroupV1Request = None,
        **kwargs,
    ) -> Union[
        Union[
            preview_protection_group_sync_response.PreviewProtectionGroupSyncResponse,
            preview_protection_group_async_response.PreviewProtectionGroupAsyncResponse,
        ],
        tuple[
            requests.Response,
            Optional[
                Union[
                    preview_protection_group_sync_response.PreviewProtectionGroupSyncResponse,
                    preview_protection_group_async_response.PreviewProtectionGroupAsyncResponse,
                ]
            ],
        ],
    ]:
        """Preview a protection group restore.

        Args:
            protection_group_id:
                Performs the operation on the ProtectionGroup with the specified ID.
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            Union[preview_protection_group_sync_response.PreviewProtectionGroupSyncResponse, preview_protection_group_async_response.PreviewProtectionGroupAsyncResponse]: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = (
            '/restores/protection-groups/{protection_group_id}/previews'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'protection_group_id': protection_group_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing preview_protection_group.', errors
            )
        unmarshalled_dict = json.loads(resp.text)
        if resp.status_code == 200:
            if self.config.raw_response:
                return (
                    resp,
                    preview_protection_group_sync_response.PreviewProtectionGroupSyncResponse.from_dictionary(
                        unmarshalled_dict
                    ),
                )
            return preview_protection_group_sync_response.PreviewProtectionGroupSyncResponse.from_dictionary(
                unmarshalled_dict
            )
        if resp.status_code == 202:
            if self.config.raw_response:
                return (
                    resp,
                    preview_protection_group_async_response.PreviewProtectionGroupAsyncResponse.from_dictionary(
                        unmarshalled_dict
                    ),
                )
            return preview_protection_group_async_response.PreviewProtectionGroupAsyncResponse.from_dictionary(
                unmarshalled_dict
            )

    def preview_details_protection_group(
        self, protection_group_id: str, preview_id: str, **kwargs
    ) -> Union[
        preview_details_protection_group_response.PreviewDetailsProtectionGroupResponse,
        tuple[
            requests.Response,
            Optional[
                preview_details_protection_group_response.PreviewDetailsProtectionGroupResponse
            ],
        ],
    ]:
        """Details for protection group bucket restore preview

        Args:
            protection_group_id:
                Performs the operation on the ProtectionGroup with the specified ID.
            preview_id:
                Performs the operation on the Preview with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            preview_details_protection_group_response.PreviewDetailsProtectionGroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/protection-groups/{protection_group_id}/previews/{preview_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'protection_group_id': protection_group_id, 'preview_id': preview_id}
        )
        _query_parameters = {}

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
                'Error occurred while executing preview_details_protection_group.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                preview_details_protection_group_response.PreviewDetailsProtectionGroupResponse.from_dictionary(
                    resp.json()
                ),
            )
        return preview_details_protection_group_response.PreviewDetailsProtectionGroupResponse.from_dictionary(
            resp
        )

    def restore_protection_group_s3_objects(
        self,
        protection_group_id: str,
        embed: str = None,
        body: restore_protection_group_s3_objects_v1_request.RestoreProtectionGroupS3ObjectsV1Request = None,
        **kwargs,
    ) -> Union[
        restore_objects_response.RestoreObjectsResponse,
        tuple[requests.Response, Optional[restore_objects_response.RestoreObjectsResponse]],
    ]:
        """Restores the specified list of S3 objects to the specified target destination.

        Args:
            protection_group_id:
                Performs the operation on the ProtectionGroup with the specified ID.
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
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            restore_objects_response.RestoreObjectsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = (
            '/restores/protection-groups/{protection_group_id}/s3-objects'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'protection_group_id': protection_group_id}
        )
        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing restore_protection_group_s3_objects.', errors
            )

        if self.config.raw_response:
            return resp, restore_objects_response.RestoreObjectsResponse.from_dictionary(
                resp.json()
            )
        return restore_objects_response.RestoreObjectsResponse.from_dictionary(resp)
