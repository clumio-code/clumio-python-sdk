#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import read_aws_templates_response
import requests


class AwsCloudformationTemplatesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for aws-cloudformation-templates resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config

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

        # Prepare headers
        _headers = {
            'accept': 'application/aws-cloudformation-templates=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_aws_connection_templates.', errors
            )
        return read_aws_templates_response.ReadAWSTemplatesResponse.from_dictionary(resp)