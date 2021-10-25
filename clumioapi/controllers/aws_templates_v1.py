#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_aws_template_v2_response
from clumioapi.models import create_connection_template_v1_request
from clumioapi.models import read_aws_templates_v2_response
import requests


class AwsTemplatesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for aws-templates resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config

    def read_connection_templates(self):
        """Returns the AWS CloudFormation and Terraform templates available to install to
        connect
        to Clumio.
        Returns:
            ReadAWSTemplatesV2Response: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/connections/aws/templates'

        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/aws-templates=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_connection_templates.', errors
            )
        return read_aws_templates_v2_response.ReadAWSTemplatesV2Response.from_dictionary(resp)

    def create_connection_template(
        self, body: create_connection_template_v1_request.CreateConnectionTemplateV1Request = None
    ) -> create_aws_template_v2_response.CreateAWSTemplateV2Response:
        """Returns the URLs for AWS CloudFormation and terraform templates  corresponding
        to a given configuration of asset types.

        Args:
            body:
                The body of the request.
        Returns:
            CreateAWSTemplateV2Response: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/connections/aws/templates'

        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/aws-templates=v1+json',
        }
        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=_headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_connection_template.', errors
            )
        return create_aws_template_v2_response.CreateAWSTemplateV2Response.from_dictionary(resp)
