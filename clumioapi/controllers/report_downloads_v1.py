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
from clumioapi.controllers.types import report_downloads_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_report_download_response
from clumioapi.models import create_report_download_v1_request
from clumioapi.models import list_report_downloads_response
import requests


class ReportDownloadsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for report-downloads resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.report-downloads=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

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

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_report_downloads_response.ListReportDownloadsResponse.from_response(
                response
            )

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

        def get_instance_from_response(response: requests.Response) -> Any:
            return create_report_download_response.CreateReportDownloadResponse.from_response(
                response
            )

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


class ReportDownloadsV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for report-downloads resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = ReportDownloadsV1Controller(config)

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
        start = start or '1'
        while True:
            response = self.controller.list_report_downloads(
                limit=limit, start=start, filter=filter, **kwargs
            )
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
