#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_buckets_response
from clumioapi.models import read_bucket_response
import requests


class AwsS3BucketsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for aws-s3-buckets resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.aws-s3-buckets=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }

    def list_aws_s3_buckets(
        self, limit: int = None, start: str = None, filter: str = None
    ) -> list_buckets_response.ListBucketsResponse:
        """Returns a list of S3 buckets.

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +------------------------+------------------+----------------------------------+
                |         Field          | Filter Condition |           Description            |
                +========================+==================+==================================+
                | environment_id         | $eq              | The Clumio-assigned ID of the    |
                |                        |                  | AWS environment.                 |
                +------------------------+------------------+----------------------------------+
                | name                   | $contains, $in   | The AWS-assigned name of this    |
                |                        |                  | resource to conditionalize on.   |
                |                        |                  | For example, filter={"name":{"$c |
                |                        |                  | ontains":"dev"}} retrieves all   |
                |                        |                  | S3 buckets with "dev" in their   |
                |                        |                  | name.                            |
                |                        |                  | filter={"name":{"$in":["prod",   |
                |                        |                  | "dev"]}} retrieves only S3       |
                |                        |                  | buckets with names that exactly  |
                |                        |                  | match "dev" or "prod"            |
                +------------------------+------------------+----------------------------------+
                | account_native_id      | $eq              | The AWS-assigned ID of the AWS   |
                |                        |                  | account. For example, filter={"a |
                |                        |                  | ccount_native_id":{"$eq":"789901 |
                |                        |                  | 323485"}}                        |
                +------------------------+------------------+----------------------------------+
                | aws_region             | $eq, $in         | The AWS region of a given        |
                |                        |                  | account to which this resource   |
                |                        |                  | belongs. For example,            |
                |                        |                  | filter={"aws_region":{"$eq":"us- |
                |                        |                  | east-1"}}                        |
                +------------------------+------------------+----------------------------------+
                | is_deleted             | $eq              | The deletion status of the       |
                |                        |                  | bucket. Set to "true" to         |
                |                        |                  | retrieve deleted buckets. For    |
                |                        |                  | example, filter={"is_deleted":{" |
                |                        |                  | $eq":true}}                      |
                +------------------------+------------------+----------------------------------+
                | tags.id                | $all             | The Clumio-assigned ID(s) of AWS |
                |                        |                  | tag(s) applied to this resource. |
                |                        |                  | For example, filter={"tags.id":{ |
                |                        |                  | "$all":["c764b152-5819-11ea-bb9f |
                |                        |                  | -b2e1c9a040ad","c764abb6-5819-   |
                |                        |                  | 11ea-bb9f-b2e1c9a040ad"]}}       |
                |                        |                  | retrieves all S3 buckets that    |
                |                        |                  | are associated with the 2 AWS    |
                |                        |                  | tags identified by these IDs. If |
                |                        |                  | multiple tags are specified, all |
                |                        |                  | of them must be applied to the   |
                |                        |                  | same S3 bucket.                  |
                +------------------------+------------------+----------------------------------+
                | aws_tag                | $in, $all        | Denotes the AWS tags to          |
                |                        |                  | conditionalize on. For example,  |
                |                        |                  | filter={"aws_tag":{"$in":[{"key" |
                |                        |                  | :"Environment", "value":"Prod"}, |
                |                        |                  | {"key":"Hello",                  |
                |                        |                  | "value":"World"}]}}              |
                +------------------------+------------------+----------------------------------+
                | excluded_aws_tag       | $all             | Denotes the AWS tags to          |
                |                        |                  | conditionalize against, that     |
                |                        |                  | assets cannot have. For example, |
                |                        |                  | filter={"excluded_aws_tag":{"$al |
                |                        |                  | l":[{"key":"Environment",        |
                |                        |                  | "value":"Prod"}, {"key":"Hello", |
                |                        |                  | "value":"World"}]}}              |
                +------------------------+------------------+----------------------------------+
                | organizational_unit_id | $in              | Denotes the organizational unit  |
                |                        |                  | IDs that can own the assets that |
                |                        |                  | are returned. For example, filte |
                |                        |                  | r={"organizational_unit_id":{"$i |
                |                        |                  | n":["c764b152-5819-11ea-bb9f-    |
                |                        |                  | b2e1c9a040ad","c764abb6-5819-    |
                |                        |                  | 11ea-bb9f-b2e1c9a040ad"]}}       |
                +------------------------+------------------+----------------------------------+
                | asset_id               | $in              | Denotes the asset IDs that the   |
                |                        |                  | results will be constrained to,  |
                |                        |                  | with other filters still         |
                |                        |                  | applied. For example, filter={"a |
                |                        |                  | sset_id":{"$in":["c764b152-5819- |
                |                        |                  | 11ea-bb9f-                       |
                |                        |                  | b2e1c9a040ad","c764abb6-5819-    |
                |                        |                  | 11ea-bb9f-b2e1c9a040ad"]}}       |
                +------------------------+------------------+----------------------------------+

        Returns:
            ListBucketsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/aws/s3-buckets'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_aws_s3_buckets.', errors
            )
        return list_buckets_response.ListBucketsResponse.from_dictionary(resp)

    def read_aws_s3_bucket(self, bucket_id: str) -> read_bucket_response.ReadBucketResponse:
        """Returns a representation of the specified S3 bucket.

        Args:
            bucket_id:
                Performs the operation on the Bucket with the specified ID.
        Returns:
            ReadBucketResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/aws/s3-buckets/{bucket_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'bucket_id': bucket_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_aws_s3_bucket.', errors
            )
        return read_bucket_response.ReadBucketResponse.from_dictionary(resp)
