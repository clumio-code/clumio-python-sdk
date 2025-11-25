#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
import re
from typing import Any, Iterator, Optional, Union
import urllib.parse

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import aws_s3_buckets_v1_bucket_matcher_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_aws_template_v2_response
from clumioapi.models import create_connection_template_v1_request
from clumioapi.models import read_aws_templates_v2_response
import requests
import retrying


class AwsTemplatesV1Controller:
    """A Controller to access Endpoints for aws-templates resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.aws-templates=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def read_connection_templates(self, **kwargs):
        """Returns the AWS CloudFormation and Terraform templates available to install to
        connect
        to Clumio.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_aws_templates_v2_response.ReadAWSTemplatesV2Response.from_response(resp)

        # Prepare query URL
        _url_path = '/connections/aws/templates'

        _query_parameters: dict[str, Any] = {}

        resp_instance: read_aws_templates_v2_response.ReadAWSTemplatesV2Response
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
            error_str = (
                f'read_connection_templates for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def create_connection_template(
        self,
        return_group_token: bool | None = None,
        body: create_connection_template_v1_request.CreateConnectionTemplateV1Request | None = None,
        **kwargs,
    ) -> create_aws_template_v2_response.CreateAWSTemplateV2Response:
        """Returns the URLs for AWS CloudFormation and terraform templates  corresponding
        to a given configuration of asset types.

        Args:
            return_group_token:
                If passed as true, then the API will return grouping token for the template.
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return create_aws_template_v2_response.CreateAWSTemplateV2Response.from_response(resp)

        # Prepare query URL
        _url_path = '/connections/aws/templates'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'return_group_token': return_group_token,
        }

        resp_instance: create_aws_template_v2_response.CreateAWSTemplateV2Response
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.post(
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
            error_str = (
                f'create_connection_template for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class AwsTemplatesV1ControllerPaginator:
    """A Controller to access Endpoints for aws-templates resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
