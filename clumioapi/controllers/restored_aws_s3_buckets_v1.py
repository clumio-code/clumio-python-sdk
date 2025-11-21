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
from clumioapi.models import preview_aws_s3_bucket_v1_request
from clumioapi.models import preview_details_s3_bucket_response
from clumioapi.models import preview_s3_bucket_response
from clumioapi.models import restore_aws_s3_bucket_v1_request
from clumioapi.models import restore_s3_bucket_response
import requests
import retrying


class RestoredAwsS3BucketsV1Controller:
    """A Controller to access Endpoints for restored-aws-s3-buckets resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.restored-aws-s3-buckets=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def restore_aws_s3_bucket(
        self,
        body: restore_aws_s3_bucket_v1_request.RestoreAwsS3BucketV1Request | None = None,
        **kwargs,
    ) -> restore_s3_bucket_response.RestoreS3BucketResponse:
        """Restores the specified S3 bucket to the specified target destination using
        Clumio Backtrack.

        Args:
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return restore_s3_bucket_response.RestoreS3BucketResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/restores/aws/s3-buckets'

        _query_parameters: dict[str, Any] = {}

        resp_instance: restore_s3_bucket_response.RestoreS3BucketResponse
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
            error_str = f'restore_aws_s3_bucket for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def preview_aws_s3_bucket(
        self,
        bucket_id: str | None = None,
        body: preview_aws_s3_bucket_v1_request.PreviewAwsS3BucketV1Request | None = None,
        **kwargs,
    ) -> preview_s3_bucket_response.PreviewS3BucketResponse:
        """Previews the objects that will be restored by S3 bucket restore.

        Args:
            bucket_id:
                Preview bucket ID
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return preview_s3_bucket_response.PreviewS3BucketResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/restores/aws/s3-buckets/{bucket_id}/previews'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'bucket_id': bucket_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: preview_s3_bucket_response.PreviewS3BucketResponse
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
            error_str = f'preview_aws_s3_bucket for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def preview_details_aws_s3_bucket(
        self, bucket_id: str | None = None, preview_id: str | None = None, **kwargs
    ) -> preview_details_s3_bucket_response.PreviewDetailsS3BucketResponse:
        """Details of an S3 bucket restore preview task, started by PreviewS3Bucket API.

        Args:
            bucket_id:
                Preview bucket ID
            preview_id:
                Preview ID
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return preview_details_s3_bucket_response.PreviewDetailsS3BucketResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/restores/aws/s3-buckets/{bucket_id}/previews/{preview_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'bucket_id': bucket_id, 'preview_id': preview_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: preview_details_s3_bucket_response.PreviewDetailsS3BucketResponse
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
                f'preview_details_aws_s3_bucket for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class RestoredAwsS3BucketsV1ControllerPaginator:
    """A Controller to access Endpoints for restored-aws-s3-buckets resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
