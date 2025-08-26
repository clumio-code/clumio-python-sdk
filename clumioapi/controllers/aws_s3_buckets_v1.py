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
from clumioapi.models import list_buckets_response
from clumioapi.models import read_bucket_response
from clumioapi.models import set_bucket_properties_response
from clumioapi.models import set_bucket_properties_v1_request
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
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_aws_s3_buckets(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: str | None = None,
        **kwargs,
    ) -> Union[
        list_buckets_response.ListBucketsResponse,
        tuple[requests.Response, Optional[list_buckets_response.ListBucketsResponse]],
    ]:
        """Returns a list of S3 buckets.

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following
                table lists the supported filter fields for this resource and the filter
                conditions that can
                be applied on those fields:

                +-----------------------------+------------------+-----------------------------+
                |            Field            | Filter Condition |         Description         |
                +=============================+==================+=============================+
                | environment_id              | $eq              | The Clumio-assigned ID of   |
                |                             |                  | the AWS environment.        |
                +-----------------------------+------------------+-----------------------------+
                | name                        | $contains, $in   | The AWS-assigned name of    |
                |                             |                  | this resource to            |
                |                             |                  | conditionalize on. For      |
                |                             |                  | example,                    |
                |                             |                  | filter={"name":{"$contains" |
                |                             |                  | :"dev"}} retrieves all S3   |
                |                             |                  | buckets with "dev" in       |
                |                             |                  | their name. filter={"name": |
                |                             |                  | {"$in":["prod", "dev"]}}    |
                |                             |                  | retrieves only S3 buckets   |
                |                             |                  | with                        |
                |                             |                  | names that exactly match    |
                |                             |                  | "dev" or "prod"             |
                +-----------------------------+------------------+-----------------------------+
                | account_native_id           | $eq              |                             |
                | Deprecated                  |                  | This field will be          |
                |                             |                  | deprecated. Use             |
                |                             |                  | bucket_matcher filter       |
                |                             |                  | instead.                    |
                |                             |                  | The AWS-assigned ID of the  |
                |                             |                  | AWS account. For example,   |
                |                             |                  | filter={"account_native_id" |
                |                             |                  | :{"$eq":"789901323485"}}    |
                |                             |                  |                             |
                +-----------------------------+------------------+-----------------------------+
                | aws_region Deprecated       | $eq, $in         |                             |
                |                             |                  | This field will be          |
                |                             |                  | deprecated. Use             |
                |                             |                  | bucket_matcher filter       |
                |                             |                  | instead.                    |
                |                             |                  | The AWS region of a given   |
                |                             |                  | account to which this       |
                |                             |                  | resource belongs. For       |
                |                             |                  | example,                    |
                |                             |                  | filter={"aws_region":{"$eq" |
                |                             |                  | :"us-east-1"}}              |
                |                             |                  |                             |
                +-----------------------------+------------------+-----------------------------+
                | is_deleted                  | $eq,$in          | The deletion status of the  |
                |                             |                  | bucket. Set to "true" to    |
                |                             |                  | retrieve deleted buckets.   |
                |                             |                  | For                         |
                |                             |                  | example, filter={"is_delete |
                |                             |                  | d":{"$eq":true}}            |
                |                             |                  | filter={"is_deleted":{"$in" |
                |                             |                  | :["true","false"]}}         |
                +-----------------------------+------------------+-----------------------------+
                | tags.id                     | $all             | The Clumio-assigned ID(s)   |
                |                             |                  | of AWS tag(s) applied to    |
                |                             |                  | this resource. For example, |
                |                             |                  | filter={"tags.id":{"$all":[ |
                |                             |                  | "c764b152-5819-11ea-bb9f-   |
                |                             |                  | b2e1c9a040ad","c764abb6-    |
                |                             |                  | 5819-11ea-                  |
                |                             |                  | bb9f-b2e1c9a040ad"]}}       |
                |                             |                  | retrieves all S3 buckets    |
                |                             |                  | that are associated with    |
                |                             |                  | the 2 AWS tags identified   |
                |                             |                  | by these IDs. If            |
                |                             |                  | multiple tags are           |
                |                             |                  | specified, all of them must |
                |                             |                  | be applied to the same S3   |
                |                             |                  | bucket.                     |
                +-----------------------------+------------------+-----------------------------+
                | aws_tag Deprecated          | $in, $all        |                             |
                |                             |                  | This field will be          |
                |                             |                  | deprecated. Use             |
                |                             |                  | bucket_matcher filter       |
                |                             |                  | instead.                    |
                |                             |                  | Denotes the AWS tags to     |
                |                             |                  | conditionalize on. For      |
                |                             |                  | example,                    |
                |                             |                  | filter={"aws_tag":{"$in":[{ |
                |                             |                  | "key":"Environment",        |
                |                             |                  | "value":"Prod"},            |
                |                             |                  | {"key":"Hello",             |
                |                             |                  | "value":"World"}]}}         |
                |                             |                  |                             |
                +-----------------------------+------------------+-----------------------------+
                | excluded_aws_tag Deprecated | $all             |                             |
                |                             |                  | This field will be          |
                |                             |                  | deprecated. Use             |
                |                             |                  | bucket_matcher filter       |
                |                             |                  | instead.                    |
                |                             |                  | Denotes the AWS tags to     |
                |                             |                  | conditionalize against,     |
                |                             |                  | that assets cannot have.    |
                |                             |                  | For example,                |
                |                             |                  | filter={"excluded_aws_tag": |
                |                             |                  | {"$all":[{"key":"Environmen |
                |                             |                  | t", "value":"Prod"},        |
                |                             |                  | {"key":"Hello",             |
                |                             |                  | "value":"World"}]}}         |
                |                             |                  |                             |
                +-----------------------------+------------------+-----------------------------+
                | organizational_unit_id      | $in              | Denotes the organizational  |
                |                             |                  | unit IDs that can own the   |
                |                             |                  | assets that are returned.   |
                |                             |                  | For                         |
                |                             |                  | example,                    |
                |                             |                  | filter={"organizational_uni |
                |                             |                  | t_id":{"$in":["c764b152-    |
                |                             |                  | 5819-11ea-bb9f-             |
                |                             |                  | b2e1c9a040ad","c764abb6-    |
                |                             |                  | 5819-11ea-                  |
                |                             |                  | bb9f-b2e1c9a040ad"]}}       |
                +-----------------------------+------------------+-----------------------------+
                | asset_id                    | $in              | Denotes the asset IDs that  |
                |                             |                  | the results will be         |
                |                             |                  | constrained to, with other  |
                |                             |                  | filters still               |
                |                             |                  | applied. For example,       |
                |                             |                  | filter={"asset_id":{"$in":[ |
                |                             |                  | "c764b152-5819-11ea-bb9f-   |
                |                             |                  | b2e1c9a040ad","c764abb6-    |
                |                             |                  | 5819-11ea-                  |
                |                             |                  | bb9f-b2e1c9a040ad"]}}       |
                +-----------------------------+------------------+-----------------------------+
                | event_bridge_enabled        | $eq              | The AWS EventBridge status  |
                |                             |                  | for the S3 bucket required  |
                |                             |                  | for S3 continuous backup.   |
                |                             |                  | For                         |
                |                             |                  | example, filter={"event_bri |
                |                             |                  | dge_enabled":{"$eq":true}}  |
                +-----------------------------+------------------+-----------------------------+
                | is_versioning_enabled       | $eq              | The AWS Version status for  |
                |                             |                  | the S3 bucket. For example, |
                |                             |                  | filter={"is_versioning_enab |
                |                             |                  | led":{"$eq":true}}          |
                +-----------------------------+------------------+-----------------------------+
                | is_encryption_enabled       | $eq              | The AWS Encryption status   |
                |                             |                  | for the S3 bucket. For      |
                |                             |                  | example,                    |
                |                             |                  | filter={"is_encryption_enab |
                |                             |                  | led":{"$eq":true}}          |
                +-----------------------------+------------------+-----------------------------+
                | is_replication_enabled      | $eq              | The AWS Replication status  |
                |                             |                  | for the S3 bucket. For      |
                |                             |                  | example,                    |
                |                             |                  | filter={"is_replication_ena |
                |                             |                  | bled":{"$eq":true}}         |
                +-----------------------------+------------------+-----------------------------+
                | is_supported                | $eq              | The Clumio supported status |
                |                             |                  | for the S3 bucket. For      |
                |                             |                  | example,                    |
                |                             |                  | filter={"is_supported":{"$e |
                |                             |                  | q":true}}                   |
                +-----------------------------+------------------+-----------------------------+
                | is_active                   | $eq              | The Clumio status for the   |
                |                             |                  | S3 bucket - whether its     |
                |                             |                  | information has been        |
                |                             |                  | updated within              |
                |                             |                  | the last 5 days. For        |
                |                             |                  | example, filter={"is_active |
                |                             |                  | ":{"$eq":true}}             |
                +-----------------------------+------------------+-----------------------------+
                | protection_method           | $eq, $in         | The applied protection      |
                |                             |                  | method for the S3 bucket.   |
                |                             |                  | Returns if any protection   |
                |                             |                  | group is                    |
                |                             |                  | protected by the specified  |
                |                             |                  | protection method. For      |
                |                             |                  | example,                    |
                |                             |                  | filter={"protection_method" |
                |                             |                  | :{"$eq":"securevault"}}     |
                |                             |                  | Possible values include:    |
                |                             |                  | 'securevault', 'backtrack', |
                |                             |                  | 'none'                      |
                +-----------------------------+------------------+-----------------------------+

                For more information about filtering, refer to the Filtering section
                of this guide.
                in: query

                The Bucket matcher query parameter receives an expression to query the bucket.
                This field is an expression to match s3 buckets. Search for buckets that match
                the conditions
                in the expression. For example, bucket_matcher={"aws_tag":{"$eq":{"key":"key1",
                "value":"val1"}},"aws_account_native_id":{"$eq":"account"},"aws_region":{"$eq":"
                us-west-2"}}
                The following formulas are supported.
                Denotes the properties to conditionalize on. For `$eq`, `$not_eq`, `$contains`
                and
                `$not_contains` a single element is provided: `{'$eq':{'key':'Environment',
                'value':'Prod'}}`. For all other operations, a list is provided:
                `{'$in':[{'key':'Environment','value':'Prod'}, {'key':'Hello',
                'value':'World'}]}`.

                +--------------------------+-------------------------+-------------------------+
                |          Field           |     Rule Condition      |       Description       |
                +==========================+=========================+=========================+
                | aws_tag                  | $eq, $not_eq,           | Supports filtering by   |
                |                          | $contains,              | AWS tag(s) using the    |
                |                          | $not_contains, $all,    | following operators.    |
                |                          | $not_all, $in, $not_in  | For example,            |
                |                          |                         |                         |
                |                          |                         | {"aws_tag":{"$eq":{"key |
                |                          |                         | ":"Environment",        |
                |                          |                         | "value":"Prod"}}}       |
                |                          |                         |                         |
                |                          |                         |                         |
                +--------------------------+-------------------------+-------------------------+
                | aws_account_native_id    | $eq, $in                | Supports filtering by   |
                |                          |                         | AWS account(s) using    |
                |                          |                         | the following           |
                |                          |                         | operators. For example, |
                |                          |                         |                         |
                |                          |                         | {"aws_account_native_id |
                |                          |                         | ":{"$eq":"111111111111" |
                |                          |                         | }}                      |
                |                          |                         |                         |
                |                          |                         |                         |
                +--------------------------+-------------------------+-------------------------+
                | account_native_idDepreca | $eq, $in                |                         |
                | ted                      |                         | This will be deprecated |
                |                          |                         | and use                 |
                |                          |                         | aws_account_native_id   |
                |                          |                         | instead.                |
                |                          |                         | Supports filtering by   |
                |                          |                         | AWS account(s) using    |
                |                          |                         | the following           |
                |                          |                         | operators. For example, |
                |                          |                         |                         |
                |                          |                         | {"account_native_id":{" |
                |                          |                         | $in":["111111111111"]}} |
                |                          |                         |                         |
                |                          |                         |                         |
                +--------------------------+-------------------------+-------------------------+
                | aws_region               | $eq, $in                | Supports filtering by   |
                |                          |                         | AWS region(s) using the |
                |                          |                         | following operators.    |
                |                          |                         | For example,            |
                |                          |                         |                         |
                |                          |                         | {"aws_region":{"$eq":"u |
                |                          |                         | s-west-2"}}             |
                |                          |                         |                         |
                |                          |                         |                         |
                +--------------------------+-------------------------+-------------------------+
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_buckets_response.ListBucketsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/aws/s3-buckets'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

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
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_aws_s3_buckets', error=http_error
            )

        obj = list_buckets_response.ListBucketsResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def read_aws_s3_bucket(self, bucket_id: str | None = None, **kwargs) -> Union[
        read_bucket_response.ReadBucketResponse,
        tuple[requests.Response, Optional[read_bucket_response.ReadBucketResponse]],
    ]:
        """Returns a representation of the specified S3 bucket.

        Args:
            bucket_id:
                Performs the operation on the Bucket with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_bucket_response.ReadBucketResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/aws/s3-buckets/{bucket_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'bucket_id': bucket_id}
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
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_aws_s3_bucket', error=http_error
            )

        obj = read_bucket_response.ReadBucketResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def set_bucket_properties(
        self,
        bucket_id: str | None = None,
        body: set_bucket_properties_v1_request.SetBucketPropertiesV1Request | None = None,
        **kwargs,
    ) -> Union[
        set_bucket_properties_response.SetBucketPropertiesResponse,
        tuple[
            requests.Response, Optional[set_bucket_properties_response.SetBucketPropertiesResponse]
        ],
    ]:
        """Idempotent call to set properties on an S3 bucket to enable S3 continuous
        backup.

        Args:
            bucket_id:
                Set the properties for the bucket with the specified ID.
            body:
                The set of properties that are being updated for the given bucket.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            set_bucket_properties_response.SetBucketPropertiesResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/aws/s3-buckets/{bucket_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'bucket_id': bucket_id}
        )
        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.patch(
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
            raise clumio_exception.ClumioException(
                'Error occurred while executing set_bucket_properties', error=http_error
            )

        obj = set_bucket_properties_response.SetBucketPropertiesResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj
