#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
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
            RestoreProtectionGroupS3AssetResponse: Response from the API.
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
