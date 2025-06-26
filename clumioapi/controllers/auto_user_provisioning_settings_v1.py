#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Optional, Union

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
        """Returns a representation of the auto user provisioning settings.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_auto_user_provisioning_setting_response.ReadAutoUserProvisioningSettingResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/settings/auto-user-provisioning'

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
                'Error occurred while executing read_auto_user_provisioning_setting.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                read_auto_user_provisioning_setting_response.ReadAutoUserProvisioningSettingResponse.from_dictionary(
                    resp.json()
                ),
            )
        return read_auto_user_provisioning_setting_response.ReadAutoUserProvisioningSettingResponse.from_dictionary(
            resp
        )

    def update_auto_user_provisioning_setting(
        self,
        body: update_auto_user_provisioning_setting_v1_request.UpdateAutoUserProvisioningSettingV1Request = None,
        **kwargs,
    ) -> Union[
        update_auto_user_provisioning_setting_response.UpdateAutoUserProvisioningSettingResponse,
        tuple[
            requests.Response,
            Optional[
                update_auto_user_provisioning_setting_response.UpdateAutoUserProvisioningSettingResponse
            ],
        ],
    ]:
        """Update the auto user provisioning settings.

        Args:
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            update_auto_user_provisioning_setting_response.UpdateAutoUserProvisioningSettingResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/settings/auto-user-provisioning'

        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.put(
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
                'Error occurred while executing update_auto_user_provisioning_setting.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                update_auto_user_provisioning_setting_response.UpdateAutoUserProvisioningSettingResponse.from_dictionary(
                    resp.json()
                ),
            )
        return update_auto_user_provisioning_setting_response.UpdateAutoUserProvisioningSettingResponse.from_dictionary(
            resp
        )
