#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Any, Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import preview_aws_s3_bucket_v1_request
from clumioapi.models import preview_details_s3_bucket_response
from clumioapi.models import preview_s3_bucket_response
from clumioapi.models import restore_aws_s3_bucket_v1_request
from clumioapi.models import restore_s3_bucket_response
import requests


class RestoredAwsS3BucketsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for restored-aws-s3-buckets resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.restored-aws-s3-buckets=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def restore_aws_s3_bucket(
        self,
        body: restore_aws_s3_bucket_v1_request.RestoreAwsS3BucketV1Request | None = None,
        **kwargs,
    ) -> Union[
        restore_s3_bucket_response.RestoreS3BucketResponse,
        tuple[requests.Response, Optional[restore_s3_bucket_response.RestoreS3BucketResponse]],
    ]:
        """Restores the specified S3 bucket to the specified target destination using
        Clumio Backtrack.

        Args:
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            restore_s3_bucket_response.RestoreS3BucketResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/aws/s3-buckets'

        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing restore_aws_s3_bucket.', errors
            )

        obj = restore_s3_bucket_response.RestoreS3BucketResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def preview_aws_s3_bucket(
        self,
        bucket_id: str | None = None,
        body: preview_aws_s3_bucket_v1_request.PreviewAwsS3BucketV1Request | None = None,
        **kwargs,
    ) -> Union[
        preview_s3_bucket_response.PreviewS3BucketResponse,
        tuple[requests.Response, Optional[preview_s3_bucket_response.PreviewS3BucketResponse]],
    ]:
        """Previews the objects that will be restored by S3 bucket restore.

        Args:
            bucket_id:
                Preview bucket ID
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            preview_s3_bucket_response.PreviewS3BucketResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/aws/s3-buckets/{bucket_id}/previews'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'bucket_id': bucket_id}
        )
        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing preview_aws_s3_bucket.', errors
            )

        obj = preview_s3_bucket_response.PreviewS3BucketResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def preview_details_aws_s3_bucket(
        self, bucket_id: str | None = None, preview_id: str | None = None, **kwargs
    ) -> Union[
        preview_details_s3_bucket_response.PreviewDetailsS3BucketResponse,
        tuple[
            requests.Response,
            Optional[preview_details_s3_bucket_response.PreviewDetailsS3BucketResponse],
        ],
    ]:
        """Details of an S3 bucket restore preview task, started by PreviewS3Bucket API.

        Args:
            bucket_id:
                Preview bucket ID
            preview_id:
                Preview ID
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            preview_details_s3_bucket_response.PreviewDetailsS3BucketResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/aws/s3-buckets/{bucket_id}/previews/{preview_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'bucket_id': bucket_id, 'preview_id': preview_id}
        )
        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing preview_details_aws_s3_bucket.', errors
            )

        obj = preview_details_s3_bucket_response.PreviewDetailsS3BucketResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj
