#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
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

    def read_general_settings(self):
        """Retrieves organization-wide setting details, including password and security
        settings.
        Returns:
            ReadGeneralSettingsResponseV2: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/settings/general'

        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/general-settings=v2+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
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
            PatchGeneralSettingsResponseV2: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/settings/general'

        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/general-settings=v2+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.patch(
                _url_path,
                headers=_headers,
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
