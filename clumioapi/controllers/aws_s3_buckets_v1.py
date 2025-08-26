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
from clumioapi.controllers.types import aws_s3_buckets_types
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
        filter: aws_s3_buckets_types.ListAwsS3BucketsV1FilterT | None = None,
        **kwargs,
    ) -> list_buckets_response.ListBucketsResponse:
        """Returns a list of S3 buckets.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
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
                |                             |                  | example, filter={"name":{"$ |
                |                             |                  | contains":"dev"}} retrieves |
                |                             |                  | all S3 buckets with "dev"   |
                |                             |                  | in their name. filter={"nam |
                |                             |                  | e":{"$in":["prod", "dev"]}} |
                |                             |                  | retrieves only S3 buckets   |
                |                             |                  | with names that exactly     |
                |                             |                  | match "dev" or "prod"       |
                +-----------------------------+------------------+-----------------------------+
                | account_native_id           | $eq              |                             |
                | Deprecated                  |                  | This field will be          |
                |                             |                  | deprecated. Use             |
                |                             |                  | bucket_matcher filter       |
                |                             |                  | instead.                    |
                |                             |                  | The AWS-assigned ID of the  |
                |                             |                  | AWS account. For example, f |
                |                             |                  | ilter={"account_native_id": |
                |                             |                  | {"$eq":"789901323485"}}     |
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
                |                             |                  | example, filter={"aws_regio |
                |                             |                  | n":{"$eq":"us-east-1"}}     |
                |                             |                  |                             |
                +-----------------------------+------------------+-----------------------------+
                | is_deleted                  | $eq,$in          | The deletion status of the  |
                |                             |                  | bucket. Set to "true" to    |
                |                             |                  | retrieve deleted buckets.   |
                |                             |                  | For example, filter={"is_de |
                |                             |                  | leted":{"$eq":true}} filter |
                |                             |                  | ={"is_deleted":{"$in":["tru |
                |                             |                  | e","false"]}}               |
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
                |                             |                  | by these IDs. If multiple   |
                |                             |                  | tags are specified, all of  |
                |                             |                  | them must be applied to the |
                |                             |                  | same S3 bucket.             |
                +-----------------------------+------------------+-----------------------------+
                | aws_tag Deprecated          | $in, $all        |                             |
                |                             |                  | This field will be          |
                |                             |                  | deprecated. Use             |
                |                             |                  | bucket_matcher filter       |
                |                             |                  | instead.                    |
                |                             |                  | Denotes the AWS tags to     |
                |                             |                  | conditionalize on. For      |
                |                             |                  | example, filter={"aws_tag": |
                |                             |                  | {"$in":[{"key":"Environment |
                |                             |                  | ", "value":"Prod"},         |
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
                |                             |                  | For example, filter={"exclu |
                |                             |                  | ded_aws_tag":{"$all":[{"key |
                |                             |                  | ":"Environment",            |
                |                             |                  | "value":"Prod"},            |
                |                             |                  | {"key":"Hello",             |
                |                             |                  | "value":"World"}]}}         |
                |                             |                  |                             |
                +-----------------------------+------------------+-----------------------------+
                | organizational_unit_id      | $in              | Denotes the organizational  |
                |                             |                  | unit IDs that can own the   |
                |                             |                  | assets that are returned.   |
                |                             |                  | For example, filter={"organ |
                |                             |                  | izational_unit_id":{"$in":[ |
                |                             |                  | "c764b152-5819-11ea-bb9f-   |
                |                             |                  | b2e1c9a040ad","c764abb6-    |
                |                             |                  | 5819-11ea-                  |
                |                             |                  | bb9f-b2e1c9a040ad"]}}       |
                +-----------------------------+------------------+-----------------------------+
                | asset_id                    | $in              | Denotes the asset IDs that  |
                |                             |                  | the results will be         |
                |                             |                  | constrained to, with other  |
                |                             |                  | filters still applied. For  |
                |                             |                  | example, filter={"asset_id" |
                |                             |                  | :{"$in":["c764b152-5819-    |
                |                             |                  | 11ea-bb9f-                  |
                |                             |                  | b2e1c9a040ad","c764abb6-    |
                |                             |                  | 5819-11ea-                  |
                |                             |                  | bb9f-b2e1c9a040ad"]}}       |
                +-----------------------------+------------------+-----------------------------+
                | event_bridge_enabled        | $eq              | The AWS EventBridge status  |
                |                             |                  | for the S3 bucket required  |
                |                             |                  | for S3 continuous backup.   |
                |                             |                  | For example, filter={"event |
                |                             |                  | _bridge_enabled":{"$eq":tru |
                |                             |                  | e}}                         |
                +-----------------------------+------------------+-----------------------------+
                | is_versioning_enabled       | $eq              | The AWS Version status for  |
                |                             |                  | the S3 bucket. For example, |
                |                             |                  | filter={"is_versioning_enab |
                |                             |                  | led":{"$eq":true}}          |
                +-----------------------------+------------------+-----------------------------+
                | is_encryption_enabled       | $eq              | The AWS Encryption status   |
                |                             |                  | for the S3 bucket. For      |
                |                             |                  | example, filter={"is_encryp |
                |                             |                  | tion_enabled":{"$eq":true}} |
                +-----------------------------+------------------+-----------------------------+
                | is_replication_enabled      | $eq              | The AWS Replication status  |
                |                             |                  | for the S3 bucket. For      |
                |                             |                  | example, filter={"is_replic |
                |                             |                  | ation_enabled":{"$eq":true} |
                |                             |                  | }                           |
                +-----------------------------+------------------+-----------------------------+
                | is_supported                | $eq              | The Clumio supported status |
                |                             |                  | for the S3 bucket. For      |
                |                             |                  | example, filter={"is_suppor |
                |                             |                  | ted":{"$eq":true}}          |
                +-----------------------------+------------------+-----------------------------+
                | is_active                   | $eq              | The Clumio status for the   |
                |                             |                  | S3 bucket - whether its     |
                |                             |                  | information has been        |
                |                             |                  | updated within the last 5   |
                |                             |                  | days. For example, filter={ |
                |                             |                  | "is_active":{"$eq":true}}   |
                +-----------------------------+------------------+-----------------------------+
                | protection_method           | $eq, $in         | The applied protection      |
                |                             |                  | method for the S3 bucket.   |
                |                             |                  | Returns if any protection   |
                |                             |                  | group is protected by the   |
                |                             |                  | specified protection        |
                |                             |                  | method. For example, filter |
                |                             |                  | ={"protection_method":{"$eq |
                |                             |                  | ":"securevault"}}           |
                |                             |                  | Possible values include:    |
                |                             |                  | 'securevault', 'backtrack', |
                |                             |                  | 'none'                      |
                +-----------------------------+------------------+-----------------------------+


                in: query

                The Bucket matcher query parameter receives an expression to query the bucket.
                This field is an expression to match s3 buckets. Search for buckets that match
                the conditions in the expression.
                For example, bucket_matcher={"aws_tag":{"$eq":{"key":"key1", "value":"val1"}},"a
                ws_account_native_id":{"$eq":"account"},"aws_region":{"$eq":"us-west-2"}}
                The following formulas are supported.
                Denotes the properties to conditionalize on. For `$eq`, `$not_eq`, `$contains`
                and `$not_contains` a single element is provided: `{'$eq':{'key':'Environment',
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
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_buckets_response.ListBucketsResponse.from_response(response)

        # Prepare query URL
        _url_path = '/datasources/aws/s3-buckets'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_buckets_response.ListBucketsResponse
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
            error_str = f'list_aws_s3_buckets for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_aws_s3_bucket(
        self, bucket_id: str | None = None, **kwargs
    ) -> read_bucket_response.ReadBucketResponse:
        """Returns a representation of the specified S3 bucket.

        Args:
            bucket_id:
                Performs the operation on the Bucket with the specified ID.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return read_bucket_response.ReadBucketResponse.from_response(response)

        # Prepare query URL
        _url_path = '/datasources/aws/s3-buckets/{bucket_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'bucket_id': bucket_id}
        )
        _query_parameters: dict[str, Any] = {}

        resp_instance: read_bucket_response.ReadBucketResponse
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
            error_str = f'read_aws_s3_bucket for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def set_bucket_properties(
        self,
        bucket_id: str | None = None,
        body: set_bucket_properties_v1_request.SetBucketPropertiesV1Request | None = None,
        **kwargs,
    ) -> set_bucket_properties_response.SetBucketPropertiesResponse:
        """Idempotent call to set properties on an S3 bucket to enable S3 continuous
        backup.

        Args:
            bucket_id:
                Set the properties for the bucket with the specified ID.
            body:
                The set of properties that are being updated for the given bucket.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return set_bucket_properties_response.SetBucketPropertiesResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/datasources/aws/s3-buckets/{bucket_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'bucket_id': bucket_id}
        )
        _query_parameters: dict[str, Any] = {}

        resp_instance: set_bucket_properties_response.SetBucketPropertiesResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.patch(
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
            error_str = f'set_bucket_properties for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class AwsS3BucketsV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for aws-s3-buckets resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = AwsS3BucketsV1Controller(config)

    def list_aws_s3_buckets(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: aws_s3_buckets_types.ListAwsS3BucketsV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[list_buckets_response.ListBucketsResponse]:
        """Returns a list of S3 buckets.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
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
                |                             |                  | example, filter={"name":{"$ |
                |                             |                  | contains":"dev"}} retrieves |
                |                             |                  | all S3 buckets with "dev"   |
                |                             |                  | in their name. filter={"nam |
                |                             |                  | e":{"$in":["prod", "dev"]}} |
                |                             |                  | retrieves only S3 buckets   |
                |                             |                  | with names that exactly     |
                |                             |                  | match "dev" or "prod"       |
                +-----------------------------+------------------+-----------------------------+
                | account_native_id           | $eq              |                             |
                | Deprecated                  |                  | This field will be          |
                |                             |                  | deprecated. Use             |
                |                             |                  | bucket_matcher filter       |
                |                             |                  | instead.                    |
                |                             |                  | The AWS-assigned ID of the  |
                |                             |                  | AWS account. For example, f |
                |                             |                  | ilter={"account_native_id": |
                |                             |                  | {"$eq":"789901323485"}}     |
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
                |                             |                  | example, filter={"aws_regio |
                |                             |                  | n":{"$eq":"us-east-1"}}     |
                |                             |                  |                             |
                +-----------------------------+------------------+-----------------------------+
                | is_deleted                  | $eq,$in          | The deletion status of the  |
                |                             |                  | bucket. Set to "true" to    |
                |                             |                  | retrieve deleted buckets.   |
                |                             |                  | For example, filter={"is_de |
                |                             |                  | leted":{"$eq":true}} filter |
                |                             |                  | ={"is_deleted":{"$in":["tru |
                |                             |                  | e","false"]}}               |
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
                |                             |                  | by these IDs. If multiple   |
                |                             |                  | tags are specified, all of  |
                |                             |                  | them must be applied to the |
                |                             |                  | same S3 bucket.             |
                +-----------------------------+------------------+-----------------------------+
                | aws_tag Deprecated          | $in, $all        |                             |
                |                             |                  | This field will be          |
                |                             |                  | deprecated. Use             |
                |                             |                  | bucket_matcher filter       |
                |                             |                  | instead.                    |
                |                             |                  | Denotes the AWS tags to     |
                |                             |                  | conditionalize on. For      |
                |                             |                  | example, filter={"aws_tag": |
                |                             |                  | {"$in":[{"key":"Environment |
                |                             |                  | ", "value":"Prod"},         |
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
                |                             |                  | For example, filter={"exclu |
                |                             |                  | ded_aws_tag":{"$all":[{"key |
                |                             |                  | ":"Environment",            |
                |                             |                  | "value":"Prod"},            |
                |                             |                  | {"key":"Hello",             |
                |                             |                  | "value":"World"}]}}         |
                |                             |                  |                             |
                +-----------------------------+------------------+-----------------------------+
                | organizational_unit_id      | $in              | Denotes the organizational  |
                |                             |                  | unit IDs that can own the   |
                |                             |                  | assets that are returned.   |
                |                             |                  | For example, filter={"organ |
                |                             |                  | izational_unit_id":{"$in":[ |
                |                             |                  | "c764b152-5819-11ea-bb9f-   |
                |                             |                  | b2e1c9a040ad","c764abb6-    |
                |                             |                  | 5819-11ea-                  |
                |                             |                  | bb9f-b2e1c9a040ad"]}}       |
                +-----------------------------+------------------+-----------------------------+
                | asset_id                    | $in              | Denotes the asset IDs that  |
                |                             |                  | the results will be         |
                |                             |                  | constrained to, with other  |
                |                             |                  | filters still applied. For  |
                |                             |                  | example, filter={"asset_id" |
                |                             |                  | :{"$in":["c764b152-5819-    |
                |                             |                  | 11ea-bb9f-                  |
                |                             |                  | b2e1c9a040ad","c764abb6-    |
                |                             |                  | 5819-11ea-                  |
                |                             |                  | bb9f-b2e1c9a040ad"]}}       |
                +-----------------------------+------------------+-----------------------------+
                | event_bridge_enabled        | $eq              | The AWS EventBridge status  |
                |                             |                  | for the S3 bucket required  |
                |                             |                  | for S3 continuous backup.   |
                |                             |                  | For example, filter={"event |
                |                             |                  | _bridge_enabled":{"$eq":tru |
                |                             |                  | e}}                         |
                +-----------------------------+------------------+-----------------------------+
                | is_versioning_enabled       | $eq              | The AWS Version status for  |
                |                             |                  | the S3 bucket. For example, |
                |                             |                  | filter={"is_versioning_enab |
                |                             |                  | led":{"$eq":true}}          |
                +-----------------------------+------------------+-----------------------------+
                | is_encryption_enabled       | $eq              | The AWS Encryption status   |
                |                             |                  | for the S3 bucket. For      |
                |                             |                  | example, filter={"is_encryp |
                |                             |                  | tion_enabled":{"$eq":true}} |
                +-----------------------------+------------------+-----------------------------+
                | is_replication_enabled      | $eq              | The AWS Replication status  |
                |                             |                  | for the S3 bucket. For      |
                |                             |                  | example, filter={"is_replic |
                |                             |                  | ation_enabled":{"$eq":true} |
                |                             |                  | }                           |
                +-----------------------------+------------------+-----------------------------+
                | is_supported                | $eq              | The Clumio supported status |
                |                             |                  | for the S3 bucket. For      |
                |                             |                  | example, filter={"is_suppor |
                |                             |                  | ted":{"$eq":true}}          |
                +-----------------------------+------------------+-----------------------------+
                | is_active                   | $eq              | The Clumio status for the   |
                |                             |                  | S3 bucket - whether its     |
                |                             |                  | information has been        |
                |                             |                  | updated within the last 5   |
                |                             |                  | days. For example, filter={ |
                |                             |                  | "is_active":{"$eq":true}}   |
                +-----------------------------+------------------+-----------------------------+
                | protection_method           | $eq, $in         | The applied protection      |
                |                             |                  | method for the S3 bucket.   |
                |                             |                  | Returns if any protection   |
                |                             |                  | group is protected by the   |
                |                             |                  | specified protection        |
                |                             |                  | method. For example, filter |
                |                             |                  | ={"protection_method":{"$eq |
                |                             |                  | ":"securevault"}}           |
                |                             |                  | Possible values include:    |
                |                             |                  | 'securevault', 'backtrack', |
                |                             |                  | 'none'                      |
                +-----------------------------+------------------+-----------------------------+


                in: query

                The Bucket matcher query parameter receives an expression to query the bucket.
                This field is an expression to match s3 buckets. Search for buckets that match
                the conditions in the expression.
                For example, bucket_matcher={"aws_tag":{"$eq":{"key":"key1", "value":"val1"}},"a
                ws_account_native_id":{"$eq":"account"},"aws_region":{"$eq":"us-west-2"}}
                The following formulas are supported.
                Denotes the properties to conditionalize on. For `$eq`, `$not_eq`, `$contains`
                and `$not_contains` a single element is provided: `{'$eq':{'key':'Environment',
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
        """
        start = start or '1'
        while True:
            response = self.controller.list_aws_s3_buckets(
                limit=limit, start=start, filter=filter, **kwargs
            )
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
