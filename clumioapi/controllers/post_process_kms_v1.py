#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import post_process_kms_v1_request
import requests


class PostProcessKmsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for post-process-kms resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.post-process-kms=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }

    def post_process_kms(
        self, body: post_process_kms_v1_request.PostProcessKmsV1Request = None
    ) -> object:
        """This API runs automatically and performs post-processing after a KMS template
        Create, Update, or Delete operation. It must be invoked by the Clumio Terraform
        provider and must not be invoked manually.

        Args:
            body:
                The body of the request.
        Returns:
            object: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/wallets/_post-process'

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
                'Error occurred while executing post_process_kms.', errors
            )
        return resp
