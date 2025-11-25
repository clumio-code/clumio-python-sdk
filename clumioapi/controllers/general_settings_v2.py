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
from clumioapi.models import patch_general_settings_response_v2
from clumioapi.models import read_general_settings_response_v2
from clumioapi.models import update_general_settings_v2_request
import requests
import retrying


class GeneralSettingsV2Controller:
    """A Controller to access Endpoints for general-settings resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.general-settings=v2+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def read_general_settings(self, **kwargs):
        """Retrieves organization-wide setting details, including password and security
        settings.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_general_settings_response_v2.ReadGeneralSettingsResponseV2.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/settings/general'

        _query_parameters: dict[str, Any] = {}

        resp_instance: read_general_settings_response_v2.ReadGeneralSettingsResponseV2
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
            error_str = f'read_general_settings for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def update_general_settings(
        self,
        body: update_general_settings_v2_request.UpdateGeneralSettingsV2Request | None = None,
        **kwargs,
    ) -> patch_general_settings_response_v2.PatchGeneralSettingsResponseV2:
        """Updates organization-wide settings, including password and security settings.

        Args:
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return patch_general_settings_response_v2.PatchGeneralSettingsResponseV2.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/settings/general'

        _query_parameters: dict[str, Any] = {}

        resp_instance: patch_general_settings_response_v2.PatchGeneralSettingsResponseV2
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.patch(
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
            error_str = f'update_general_settings for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class GeneralSettingsV2ControllerPaginator:
    """A Controller to access Endpoints for general-settings resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
