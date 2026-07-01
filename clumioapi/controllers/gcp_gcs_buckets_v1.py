#
# Copyright 2023. Clumio, A Commvault Company.
#

import re
from typing import Any, Iterator
import urllib.parse

from clumioapi import api_helper
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import gcp_gcs_buckets_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_gcs_buckets_response
from clumioapi.models import read_gcs_bucket_response
import requests
import retrying


class GcpGcsBucketsV1Controller:
    """A Controller to access Endpoints for gcp-gcs-buckets resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.gcp-gcs-buckets=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_gcp_gcs_buckets(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            gcp_gcs_buckets_types.ListGcpGcsBucketsV1FilterT
            | gcp_gcs_buckets_types.ListGcpGcsBucketsV1FilterTypeDef
            | None
        ) = None,
        bucket_matcher: str | None = None,
        **kwargs,
    ) -> list_gcs_buckets_response.ListGCSBucketsResponse:
        """Returns a list of GCS buckets.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria.
                Supported filter fields:

                +--------------+-------------------+-------------------------------------------+
                |    Field     |     Condition     |                Description                |
                +==============+===================+===========================================+
                | id           | $eq,$in           | The Clumio-assigned ID of the GCS bucket. |
                +--------------+-------------------+-------------------------------------------+
                | native_id    | $eq,$in           | The native GCP identifier of the bucket.  |
                +--------------+-------------------+-------------------------------------------+
                | project_id   | $eq,$in           | The native GCP project ID that owns the   |
                |              |                   | bucket.                                   |
                +--------------+-------------------+-------------------------------------------+
                | project_uuid | $eq,$in           | The Clumio-assigned UUID of the GCP       |
                |              |                   | project that owns the bucket.             |
                +--------------+-------------------+-------------------------------------------+
                | region_uuid  | $eq,$in           | The Clumio-assigned UUID of the GCP       |
                |              |                   | region associated with the bucket.        |
                +--------------+-------------------+-------------------------------------------+
                | is_deleted   | $eq               | Boolean flag indicating whether to return |
                |              |                   | deleted (true) or active (false) buckets. |
                +--------------+-------------------+-------------------------------------------+
                | name         | $eq,$contains,$in | The display name of the GCS bucket.       |
                +--------------+-------------------+-------------------------------------------+
            bucket_matcher:
                The bucket_matcher query parameter filters buckets using the same expression
                format as
                protection group bucket rules. Matches buckets by GCP labels, project ID, and
                location.
                For example, bucket_matcher={"gcp_label":{"$eq":{"key":"env","value":"prod"}},
                "gcp_project_id":{"$eq":"my-project"},"gcp_location":{"$in":["us-central1","us-
                west1"]}}
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_gcs_buckets_response.ListGCSBucketsResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/gcp/gcs-buckets'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': api_helper.to_filter_query_str(
                filter, gcp_gcs_buckets_types.ListGcpGcsBucketsV1FilterT
            ),
            'bucket_matcher': bucket_matcher,
        }

        resp_instance: list_gcs_buckets_response.ListGCSBucketsResponse
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
            error_str = f'list_gcp_gcs_buckets for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_gcp_gcs_bucket(
        self, bucket_id: str | None = None, **kwargs
    ) -> read_gcs_bucket_response.ReadGCSBucketResponse:
        """Returns a representation of the specified GCS bucket.

        Args:
            bucket_id:
                Performs the operation on the Bucket with the specified ID.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_gcs_bucket_response.ReadGCSBucketResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/gcp/gcs-buckets/{bucket_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'bucket_id': bucket_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: read_gcs_bucket_response.ReadGCSBucketResponse
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
            error_str = f'read_gcp_gcs_bucket for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class GcpGcsBucketsV1ControllerPaginator:
    """A Controller to access Endpoints for gcp-gcs-buckets resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_gcp_gcs_buckets(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            gcp_gcs_buckets_types.ListGcpGcsBucketsV1FilterT
            | gcp_gcs_buckets_types.ListGcpGcsBucketsV1FilterTypeDef
            | None
        ) = None,
        bucket_matcher: str | None = None,
        **kwargs,
    ) -> Iterator[list_gcs_buckets_response.ListGCSBucketsResponse]:
        """Returns a list of GCS buckets.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria.
                Supported filter fields:

                +--------------+-------------------+-------------------------------------------+
                |    Field     |     Condition     |                Description                |
                +==============+===================+===========================================+
                | id           | $eq,$in           | The Clumio-assigned ID of the GCS bucket. |
                +--------------+-------------------+-------------------------------------------+
                | native_id    | $eq,$in           | The native GCP identifier of the bucket.  |
                +--------------+-------------------+-------------------------------------------+
                | project_id   | $eq,$in           | The native GCP project ID that owns the   |
                |              |                   | bucket.                                   |
                +--------------+-------------------+-------------------------------------------+
                | project_uuid | $eq,$in           | The Clumio-assigned UUID of the GCP       |
                |              |                   | project that owns the bucket.             |
                +--------------+-------------------+-------------------------------------------+
                | region_uuid  | $eq,$in           | The Clumio-assigned UUID of the GCP       |
                |              |                   | region associated with the bucket.        |
                +--------------+-------------------+-------------------------------------------+
                | is_deleted   | $eq               | Boolean flag indicating whether to return |
                |              |                   | deleted (true) or active (false) buckets. |
                +--------------+-------------------+-------------------------------------------+
                | name         | $eq,$contains,$in | The display name of the GCS bucket.       |
                +--------------+-------------------+-------------------------------------------+
            bucket_matcher:
                The bucket_matcher query parameter filters buckets using the same expression
                format as
                protection group bucket rules. Matches buckets by GCP labels, project ID, and
                location.
                For example, bucket_matcher={"gcp_label":{"$eq":{"key":"env","value":"prod"}},
                "gcp_project_id":{"$eq":"my-project"},"gcp_location":{"$in":["us-central1","us-
                west1"]}}
        """
        controller = GcpGcsBucketsV1Controller(self.controller)
        while True:
            response = controller.list_gcp_gcs_buckets(
                limit=limit, start=start, filter=filter, bucket_matcher=bucket_matcher, **kwargs
            )
            yield response
            next_link = response.Links.Next  # type: ignore
            if not next_link:
                break
            next_link = next_link.Href
            if match := re.search(r'start=([^&]+)', next_link):  # type: ignore
                start = match.group(1)
            else:
                raise clumio_exception.ClumioException(
                    'Next link is malformed. Please contact clumio support.'
                )
