#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Any, Iterator, Optional, Union
import urllib.parse

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
        body: (
            post_process_aws_connection_v1_request.PostProcessAwsConnectionV1Request | None
        ) = None,
        **kwargs,
    ) -> object:
        """Performs post-processing after AWS Connection Create, Update or Delete. This API
        should only be invoked by the Clumio Terraform provider and should not be
        invoked manually.

        Args:
            body:
                The body of the request.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return resp

        # Prepare query URL
        _url_path = '/connections/aws/post-process'

        _query_parameters: dict[str, Any] = {}

        resp_instance: object
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
                f'post_process_aws_connection for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class PostProcessAwsConnectionV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for post-process-aws-connection resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = PostProcessAwsConnectionV1Controller(config)
