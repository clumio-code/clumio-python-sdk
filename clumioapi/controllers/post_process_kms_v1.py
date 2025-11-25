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
from clumioapi.models import post_process_kms_v1_request
import requests
import retrying


class PostProcessKmsV1Controller:
    """A Controller to access Endpoints for post-process-kms resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.post-process-kms=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def post_process_kms(
        self, body: post_process_kms_v1_request.PostProcessKmsV1Request | None = None, **kwargs
    ) -> object:
        """This API runs automatically and performs post-processing after a KMS template
        Create, Update, or Delete operation. It must be invoked by the Clumio Terraform
        provider and must not be invoked manually.

        Args:
            body:
                The body of the request.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return resp

        # Prepare query URL
        _url_path = '/wallets/_post-process'

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
            error_str = f'post_process_kms for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class PostProcessKmsV1ControllerPaginator:
    """A Controller to access Endpoints for post-process-kms resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
