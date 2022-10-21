#
# Copyright 2021. Clumio, Inc.
#

import requests

from clumioapi import api_helper, configuration, sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import (
    create_aws_connection_template_v1_request,
    create_aws_template_response,
    read_aws_templates_response,
)


class AwsCloudformationTemplatesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for aws-cloudformation-templates resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.aws-cloudformation-templates=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def read_aws_connection_templates(self):
        """Returns the AWS CloudFormation templates available to install to connect
        to Clumio. The provided URL will be pasted into the Amazon S3 URL field when
        creating the CloudFormation stack.
        Returns:
            ReadAWSTemplatesResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/connections/aws/cloudformation-templates'

        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                "Error occurred while executing read_aws_connection_templates.", errors
            )
        return read_aws_templates_response.ReadAWSTemplatesResponse.from_dictionary(resp)

    def create_aws_connection_template(
        self,
        body: create_aws_connection_template_v1_request.CreateAwsConnectionTemplateV1Request = None,
    ) -> create_aws_template_response.CreateAWSTemplateResponse:
        """Returns the AWS CloudFormation template URL corresponding to a given
        configuration of asset types.

        Args:
            body:
                The body of the request.
        Returns:
            CreateAWSTemplateResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/connections/aws/cloudformation-templates'

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
                "Error occurred while executing create_aws_connection_template.", errors
            )
        return create_aws_template_response.CreateAWSTemplateResponse.from_dictionary(resp)
