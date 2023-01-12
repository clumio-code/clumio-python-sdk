#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import preview_details_protection_group_response
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
    ) -> restore_protection_group_response.RestoreProtectionGroupResponse:
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
            RestoreProtectionGroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/restores/protection-groups'

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
                'Error occurred while executing restore_protection_group.', errors
            )
        return restore_protection_group_response.RestoreProtectionGroupResponse.from_dictionary(
            resp
        )

    def preview_protection_group(
        self,
        protection_group_id: str,
        body: preview_protection_group_v1_request.PreviewProtectionGroupV1Request = None,
    ) -> preview_protection_group_sync_response.PreviewProtectionGroupSyncResponse:
        """Preview a protection group restore.

        Args:
            protection_group_id:
                Performs the operation on the ProtectionGroup with the specified ID.
            body:

        Returns:
            PreviewProtectionGroupSyncResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = (
            f'{self.config.base_path}/restores/protection-groups/{protection_group_id}/previews'
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
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing preview_protection_group.', errors
            )
        return preview_protection_group_sync_response.PreviewProtectionGroupSyncResponse.from_dictionary(
            resp
        )

    def preview_details_protection_group(
        self, protection_group_id: str, preview_id: str
    ) -> preview_details_protection_group_response.PreviewDetailsProtectionGroupResponse:
        """Details for protection group bucket restore preview

        Args:
            protection_group_id:
                Performs the operation on the ProtectionGroup with the specified ID.
            preview_id:
                Performs the operation on the Preview with the specified ID.
        Returns:
            PreviewDetailsProtectionGroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/restores/protection-groups/{protection_group_id}/previews/{preview_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'protection_group_id': protection_group_id, 'preview_id': preview_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing preview_details_protection_group.', errors
            )
        return preview_details_protection_group_response.PreviewDetailsProtectionGroupResponse.from_dictionary(
            resp
        )

    def restore_protection_group_s3_objects(
        self,
        protection_group_id: str,
        embed: str = None,
        body: restore_protection_group_s3_objects_v1_request.RestoreProtectionGroupS3ObjectsV1Request = None,
    ) -> restore_objects_response.RestoreObjectsResponse:
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
            RestoreObjectsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = (
            f'{self.config.base_path}/restores/protection-groups/{protection_group_id}/s3-objects'
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
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing restore_protection_group_s3_objects.', errors
            )
        return restore_objects_response.RestoreObjectsResponse.from_dictionary(resp)
