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
from clumioapi.controllers.types import report_downloads_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_report_download_response
from clumioapi.models import create_report_download_v1_request
from clumioapi.models import list_report_downloads_response
import requests
import retrying


class ReportDownloadsV1Controller:
    """A Controller to access Endpoints for report-downloads resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.report-downloads=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_report_downloads(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: report_downloads_types.ListReportDownloadsV1FilterT | None = None,
        **kwargs,
    ) -> list_report_downloads_response.ListReportDownloadsResponse:
        """Returns a list of unexpired, generated reports.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:

                +-----------------+------------------+-----------------------------------------+
                |      Field      | Filter Condition |               Description               |
                +=================+==================+=========================================+
                | start_timestamp | $gte, $lt        | Start timestamp denotes the time filter |
                |                 |                  | for listing CSV report downloads.       |
                |                 |                  | $gte and $lt accept RFC-3339            |
                |                 |                  | timestamps. For example,                |
                |                 |                  |                                         |
                |                 |                  | "filter":"{"start_timestamp":{"$gt":"20 |
                |                 |                  | 19-10-12T07:20:50.52Z"}}"               |
                |                 |                  |                                         |
                |                 |                  |                                         |
                +-----------------+------------------+-----------------------------------------+
                | report_type     | $in              |                                         |
                |                 |                  | Filter report downloaded records whose  |
                |                 |                  | type is one of the given values. The    |
                |                 |                  | possible values are: "activity",        |
                |                 |                  | "audit", and "consumption".             |
                |                 |                  |                                         |
                |                 |                  | filter={"report_type":{"$in":["activity |
                |                 |                  | "]}}                                    |
                |                 |                  |                                         |
                |                 |                  |                                         |
                +-----------------+------------------+-----------------------------------------+

                For more information about filtering, refer to the
                Filtering section of this guide.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_report_downloads_response.ListReportDownloadsResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/reports/downloads'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_report_downloads_response.ListReportDownloadsResponse
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
            error_str = f'list_report_downloads for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def create_report_download(
        self,
        body: create_report_download_v1_request.CreateReportDownloadV1Request | None = None,
        **kwargs,
    ) -> create_report_download_response.CreateReportDownloadResponse:
        """Generates a report of a specified type given certain general conditions such as
        time range and other type-specific filters.

        Args:
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return create_report_download_response.CreateReportDownloadResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/reports/downloads'

        _query_parameters: dict[str, Any] = {}

        resp_instance: create_report_download_response.CreateReportDownloadResponse
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
            error_str = f'create_report_download for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class ReportDownloadsV1ControllerPaginator:
    """A Controller to access Endpoints for report-downloads resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_report_downloads(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: report_downloads_types.ListReportDownloadsV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[list_report_downloads_response.ListReportDownloadsResponse]:
        """Returns a list of unexpired, generated reports.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:

                +-----------------+------------------+-----------------------------------------+
                |      Field      | Filter Condition |               Description               |
                +=================+==================+=========================================+
                | start_timestamp | $gte, $lt        | Start timestamp denotes the time filter |
                |                 |                  | for listing CSV report downloads.       |
                |                 |                  | $gte and $lt accept RFC-3339            |
                |                 |                  | timestamps. For example,                |
                |                 |                  |                                         |
                |                 |                  | "filter":"{"start_timestamp":{"$gt":"20 |
                |                 |                  | 19-10-12T07:20:50.52Z"}}"               |
                |                 |                  |                                         |
                |                 |                  |                                         |
                +-----------------+------------------+-----------------------------------------+
                | report_type     | $in              |                                         |
                |                 |                  | Filter report downloaded records whose  |
                |                 |                  | type is one of the given values. The    |
                |                 |                  | possible values are: "activity",        |
                |                 |                  | "audit", and "consumption".             |
                |                 |                  |                                         |
                |                 |                  | filter={"report_type":{"$in":["activity |
                |                 |                  | "]}}                                    |
                |                 |                  |                                         |
                |                 |                  |                                         |
                +-----------------+------------------+-----------------------------------------+

                For more information about filtering, refer to the
                Filtering section of this guide.
        """
        controller = ReportDownloadsV1Controller(self.controller)
        while True:
            response = controller.list_report_downloads(
                limit=limit, start=start, filter=filter, **kwargs
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
