#
# Copyright 2021. Clumio, Inc.
#

import json

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import preview_protection_group_s3_asset_async_response
from clumioapi.models import preview_protection_group_s3_asset_details_response
from clumioapi.models import preview_protection_group_s3_asset_sync_response
from clumioapi.models import preview_protection_group_s3_asset_v1_request
from clumioapi.models import restore_protection_group_s3_asset_response
from clumioapi.models import restore_protection_group_s3_asset_v1_request
import requests


class RestoredProtectionGroupS3AssetsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for restored-protection-group-s3-assets resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.restored-protection-group-s3-assets=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def restore_protection_group_s3_asset(
        self,
        embed: str = None,
        body: restore_protection_group_s3_asset_v1_request.RestoreProtectionGroupS3AssetV1Request = None,
    ) -> restore_protection_group_s3_asset_response.RestoreProtectionGroupS3AssetResponse:
        """Restores the specified protection group S3 asset backup to the specified target
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
            restore_protection_group_s3_asset_response.RestoreProtectionGroupS3AssetResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/restores/protection-groups/s3-assets'

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
                'Error occurred while executing restore_protection_group_s3_asset.', errors
            )

        return restore_protection_group_s3_asset_response.RestoreProtectionGroupS3AssetResponse.from_dictionary(
            resp
        )

    def preview_protection_group_s3_asset(
        self,
        protection_group_s3_asset_id: str,
        body: preview_protection_group_s3_asset_v1_request.PreviewProtectionGroupS3AssetV1Request = None,
    ) -> preview_protection_group_s3_asset_sync_response.PreviewProtectionGroupS3AssetSyncResponse | preview_protection_group_s3_asset_async_response.PreviewProtectionGroupS3AssetAsyncResponse:
        """Preview a protection group S3 asset restore

        Args:
            protection_group_s3_asset_id:
                Performs the operation on the ProtectionGroup with the specified ID.
            body:

        Returns:
            preview_protection_group_s3_asset_sync_response.PreviewProtectionGroupS3AssetSyncResponse | preview_protection_group_s3_asset_async_response.PreviewProtectionGroupS3AssetAsyncResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/restores/protection-groups/s3-assets/{protection_group_s3_asset_id}/previews'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'protection_group_s3_asset_id': protection_group_s3_asset_id}
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
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing preview_protection_group_s3_asset.', errors
            )
        unmarshalled_dict = json.loads(resp.text)
        if resp.status_code == 200:
            return preview_protection_group_s3_asset_sync_response.PreviewProtectionGroupS3AssetSyncResponse.from_dictionary(
                unmarshalled_dict
            )
        if resp.status_code == 202:
            return preview_protection_group_s3_asset_async_response.PreviewProtectionGroupS3AssetAsyncResponse.from_dictionary(
                unmarshalled_dict
            )

    def preview_details_protection_group_s3_asset(
        self, protection_group_s3_asset_id: str, preview_id: str
    ) -> preview_protection_group_s3_asset_details_response.PreviewProtectionGroupS3AssetDetailsResponse:
        """Details for protection group S3 asset restore preview

        Args:
            protection_group_s3_asset_id:
                Performs the operation on the ProtectionGroup with the specified ID.
            preview_id:
                Performs the operation on the Preview with the specified ID.
        Returns:
            preview_protection_group_s3_asset_details_response.PreviewProtectionGroupS3AssetDetailsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/restores/protection-groups/s3-assets/{protection_group_s3_asset_id}/previews/{preview_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path,
            {
                'protection_group_s3_asset_id': protection_group_s3_asset_id,
                'preview_id': preview_id,
            },
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing preview_details_protection_group_s3_asset.', errors
            )

        return preview_protection_group_s3_asset_details_response.PreviewProtectionGroupS3AssetDetailsResponse.from_dictionary(
            resp
        )
