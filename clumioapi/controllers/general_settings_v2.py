#
# Copyright 2021. Clumio, Inc.
#

import json

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import patch_general_settings_response_v2
from clumioapi.models import read_general_settings_response_v2
from clumioapi.models import update_general_settings_v2_request
import requests


class GeneralSettingsV2Controller(base_controller.BaseController):
    """A Controller to access Endpoints for general-settings resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.general-settings=v2+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def read_general_settings(self):
        """Retrieves organization-wide setting details, including password and security
        settings.
        Returns:
            read_general_settings_response_v2.ReadGeneralSettingsResponseV2: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/settings/general'

        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_general_settings.', errors
            )

        return read_general_settings_response_v2.ReadGeneralSettingsResponseV2.from_dictionary(resp)

    def update_general_settings(
        self, body: update_general_settings_v2_request.UpdateGeneralSettingsV2Request = None
    ) -> patch_general_settings_response_v2.PatchGeneralSettingsResponseV2:
        """Updates organization-wide settings, including password and security settings.

        Args:
            body:

        Returns:
            patch_general_settings_response_v2.PatchGeneralSettingsResponseV2: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/settings/general'

        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.patch(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing update_general_settings.', errors
            )

        return patch_general_settings_response_v2.PatchGeneralSettingsResponseV2.from_dictionary(
            resp
        )
