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
from clumioapi.models import preview_details_protection_group_response
from clumioapi.models import preview_protection_group_async_response
from clumioapi.models import preview_protection_group_sync_response
from clumioapi.models import preview_protection_group_v1_request
from clumioapi.models import restore_objects_response
from clumioapi.models import restore_protection_group_response
from clumioapi.models import restore_protection_group_s3_objects_v1_request
from clumioapi.models import restore_protection_group_v1_request
import requests
import retrying


class RestoredProtectionGroupsV1Controller:
    """A Controller to access Endpoints for restored-protection-groups resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.restored-protection-groups=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def restore_protection_group(
        self,
        embed: str | None = None,
        body: restore_protection_group_v1_request.RestoreProtectionGroupV1Request | None = None,
        **kwargs,
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

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return restore_protection_group_response.RestoreProtectionGroupResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/restores/protection-groups'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'embed': embed,
        }

        resp_instance: restore_protection_group_response.RestoreProtectionGroupResponse
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
            error_str = f'restore_protection_group for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def preview_protection_group(
        self,
        protection_group_id: str | None = None,
        body: preview_protection_group_v1_request.PreviewProtectionGroupV1Request | None = None,
        **kwargs,
    ) -> Union[
        preview_protection_group_sync_response.PreviewProtectionGroupSyncResponse,
        preview_protection_group_async_response.PreviewProtectionGroupAsyncResponse,
    ]:
        """Preview a protection group restore.

        Args:
            protection_group_id:
                Performs the operation on the ProtectionGroup with the specified ID.
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:

            obj: Any

            if resp.status_code == 200:
                obj = preview_protection_group_sync_response.PreviewProtectionGroupSyncResponse.from_response(
                    resp
                )
                return obj

            if resp.status_code == 202:
                obj = preview_protection_group_async_response.PreviewProtectionGroupAsyncResponse.from_response(
                    resp
                )
                return obj

            raise clumio_exception.ClumioException(
                f'Unexpected response code for preview_protection_group.', resp=resp
            )

        # Prepare query URL
        _url_path = '/restores/protection-groups/{protection_group_id}/previews'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'protection_group_id': protection_group_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: Union[
            preview_protection_group_sync_response.PreviewProtectionGroupSyncResponse,
            preview_protection_group_async_response.PreviewProtectionGroupAsyncResponse,
        ]
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
            error_str = f'preview_protection_group for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def preview_details_protection_group(
        self, protection_group_id: str | None = None, preview_id: str | None = None, **kwargs
    ) -> preview_details_protection_group_response.PreviewDetailsProtectionGroupResponse:
        """Details for protection group bucket restore preview

        Args:
            protection_group_id:
                Performs the operation on the ProtectionGroup with the specified ID.
            preview_id:
                Performs the operation on the Preview with the specified ID.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return preview_details_protection_group_response.PreviewDetailsProtectionGroupResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/restores/protection-groups/{protection_group_id}/previews/{preview_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'protection_group_id': protection_group_id, 'preview_id': preview_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: (
            preview_details_protection_group_response.PreviewDetailsProtectionGroupResponse
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
            error_str = (
                f'preview_details_protection_group for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def restore_protection_group_s3_objects(
        self,
        protection_group_id: str | None = None,
        embed: str | None = None,
        body: (
            restore_protection_group_s3_objects_v1_request.RestoreProtectionGroupS3ObjectsV1Request
            | None
        ) = None,
        **kwargs,
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

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return restore_objects_response.RestoreObjectsResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/restores/protection-groups/{protection_group_id}/s3-objects'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'protection_group_id': protection_group_id}
        )

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'embed': embed,
        }

        resp_instance: restore_objects_response.RestoreObjectsResponse
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
            error_str = f'restore_protection_group_s3_objects for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class RestoredProtectionGroupsV1ControllerPaginator:
    """A Controller to access Endpoints for restored-protection-groups resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
