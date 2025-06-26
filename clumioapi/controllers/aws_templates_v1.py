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
from clumioapi.models import create_aws_template_v2_response
from clumioapi.models import create_connection_template_v1_request
from clumioapi.models import read_aws_templates_v2_response
import requests


class AwsTemplatesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for aws-templates resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.aws-templates=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def read_connection_templates(self, **kwargs):
        """Returns the AWS CloudFormation and Terraform templates available to install to
        connect
        to Clumio.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_aws_templates_v2_response.ReadAWSTemplatesV2Response: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/connections/aws/templates'

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
                'Error occurred while executing read_connection_templates.', errors
            )

        if self.config.raw_response:
            return resp, read_aws_templates_v2_response.ReadAWSTemplatesV2Response.from_dictionary(
                resp.json()
            )
        return read_aws_templates_v2_response.ReadAWSTemplatesV2Response.from_dictionary(resp)

    def create_connection_template(
        self,
        return_group_token: bool = None,
        body: create_connection_template_v1_request.CreateConnectionTemplateV1Request = None,
        **kwargs,
    ) -> Union[
        create_aws_template_v2_response.CreateAWSTemplateV2Response,
        tuple[
            requests.Response, Optional[create_aws_template_v2_response.CreateAWSTemplateV2Response]
        ],
    ]:
        """Returns the URLs for AWS CloudFormation and terraform templates  corresponding
        to a given configuration of asset types.

        Args:
            return_group_token:
                If passed as true, then the API will return grouping token for the template.
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            create_aws_template_v2_response.CreateAWSTemplateV2Response: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/connections/aws/templates'

        _query_parameters = {}
        _query_parameters = {'return_group_token': return_group_token}

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
                'Error occurred while executing create_connection_template.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                create_aws_template_v2_response.CreateAWSTemplateV2Response.from_dictionary(
                    resp.json()
                ),
            )
        return create_aws_template_v2_response.CreateAWSTemplateV2Response.from_dictionary(resp)
