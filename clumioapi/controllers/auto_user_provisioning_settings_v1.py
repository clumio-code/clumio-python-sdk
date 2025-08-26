#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Any, Iterator, Optional, Union
import urllib.parse

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import read_auto_user_provisioning_setting_response
from clumioapi.models import update_auto_user_provisioning_setting_response
from clumioapi.models import update_auto_user_provisioning_setting_v1_request
import requests


class AutoUserProvisioningSettingsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for auto-user-provisioning-settings resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.auto-user-provisioning-settings=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def read_auto_user_provisioning_setting(self, **kwargs):
        """Returns a representation of the auto user provisioning settings."""

        def get_instance_from_response(response: requests.Response) -> Any:
            return read_auto_user_provisioning_setting_response.ReadAutoUserProvisioningSettingResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/settings/auto-user-provisioning'

        _query_parameters: dict[str, Any] = {}

        resp_instance: (
            read_auto_user_provisioning_setting_response.ReadAutoUserProvisioningSettingResponse
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
            error_str = f'read_auto_user_provisioning_setting for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def update_auto_user_provisioning_setting(
        self,
        body: (
            update_auto_user_provisioning_setting_v1_request.UpdateAutoUserProvisioningSettingV1Request
            | None
        ) = None,
        **kwargs,
    ) -> update_auto_user_provisioning_setting_response.UpdateAutoUserProvisioningSettingResponse:
        """Update the auto user provisioning settings.

        Args:
            body:

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return update_auto_user_provisioning_setting_response.UpdateAutoUserProvisioningSettingResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/settings/auto-user-provisioning'

        _query_parameters: dict[str, Any] = {}

        resp_instance: (
            update_auto_user_provisioning_setting_response.UpdateAutoUserProvisioningSettingResponse
        )
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.put(
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
            error_str = f'update_auto_user_provisioning_setting for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class AutoUserProvisioningSettingsV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for auto-user-provisioning-settings resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = AutoUserProvisioningSettingsV1Controller(config)
