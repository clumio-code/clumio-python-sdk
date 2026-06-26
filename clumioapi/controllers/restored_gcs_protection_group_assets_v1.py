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
from clumioapi.exceptions import clumio_exception
from clumioapi.models import preview_gcs_protection_group_asset_async_response
from clumioapi.models import preview_gcs_protection_group_asset_details_response
from clumioapi.models import preview_gcs_protection_group_asset_v1_request
from clumioapi.models import restore_gcs_protection_group_asset_v1_request
from clumioapi.models import restore_gcs_protection_group_bucket_response
import requests
import retrying


class RestoredGcsProtectionGroupAssetsV1Controller:
    """A Controller to access Endpoints for restored-gcs-protection-group-assets resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.restored-gcs-protection-group-assets=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def restore_gcs_protection_group_asset(
        self,
        embed: str | None = None,
        body: (
            restore_gcs_protection_group_asset_v1_request.RestoreGcsProtectionGroupAssetV1Request
            | None
        ) = None,
        **kwargs,
    ) -> restore_gcs_protection_group_bucket_response.RestoreGCSProtectionGroupBucketResponse:
        """Restores the specified asset backup to the specified target destination.

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
            return restore_gcs_protection_group_bucket_response.RestoreGCSProtectionGroupBucketResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/restores/gcp/protection-groups/assets'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'embed': embed,
        }

        resp_instance: (
            restore_gcs_protection_group_bucket_response.RestoreGCSProtectionGroupBucketResponse
        )
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
            error_str = f'restore_gcs_protection_group_asset for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def preview_gcs_protection_group_asset(
        self,
        gcs_asset_id: str | None = None,
        body: (
            preview_gcs_protection_group_asset_v1_request.PreviewGcsProtectionGroupAssetV1Request
            | None
        ) = None,
        **kwargs,
    ) -> (
        preview_gcs_protection_group_asset_async_response.PreviewGCSProtectionGroupAssetAsyncResponse
    ):
        """Preview an asset restore

        Args:
            gcs_asset_id:
                Performs the operation on the GCS Protection Group Asset with the specified ID.
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return preview_gcs_protection_group_asset_async_response.PreviewGCSProtectionGroupAssetAsyncResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/restores/gcp/protection-groups/assets/{gcs_asset_id}/previews'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'gcs_asset_id': gcs_asset_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: (
            preview_gcs_protection_group_asset_async_response.PreviewGCSProtectionGroupAssetAsyncResponse
        )
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
            error_str = f'preview_gcs_protection_group_asset for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def preview_details_gcs_protection_group_asset(
        self, gcs_asset_id: str | None = None, preview_id: str | None = None, **kwargs
    ) -> (
        preview_gcs_protection_group_asset_details_response.PreviewGCSProtectionGroupAssetDetailsResponse
    ):
        """Details for asset restore preview

        Args:
            gcs_asset_id:
                Performs the operation on the GCS Protection Group Asset with the specified ID.
            preview_id:
                Performs the operation on the Preview with the specified ID.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return preview_gcs_protection_group_asset_details_response.PreviewGCSProtectionGroupAssetDetailsResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/restores/gcp/protection-groups/assets/{gcs_asset_id}/previews/{preview_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'gcs_asset_id': gcs_asset_id, 'preview_id': preview_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: (
            preview_gcs_protection_group_asset_details_response.PreviewGCSProtectionGroupAssetDetailsResponse
        )
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
            error_str = f'preview_details_gcs_protection_group_asset for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class RestoredGcsProtectionGroupAssetsV1ControllerPaginator:
    """A Controller to access Endpoints for restored-gcs-protection-group-assets resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
