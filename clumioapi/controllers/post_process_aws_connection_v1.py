#
# Copyright 2021. Clumio, Inc.
#

import json
from typing import Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import post_process_aws_connection_v1_request
import requests


class PostProcessAwsConnectionV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for post-process-aws-connection resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.post-process-aws-connection=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def post_process_aws_connection(
        self,
        body: post_process_aws_connection_v1_request.PostProcessAwsConnectionV1Request = None,
        **kwargs,
    ) -> Union[object, tuple[requests.Response, Optional[object]]]:
        """Performs post-processing after AWS Connection Create, Update or Delete. This API
        should only be invoked by the Clumio Terraform provider and should not be
        invoked manually.

        Args:
            body:
                The body of the request.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            object: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/connections/aws/post-process'

        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.post(
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
                'Error occurred while executing post_process_aws_connection.', errors
            )

        if self.config.raw_response:
            return resp, resp.json()
        return resp
