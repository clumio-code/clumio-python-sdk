#
# Copyright 2021. Clumio, Inc.
#

import json
from typing import Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
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
        self, limit: int = None, start: str = None, filter: str = None, **kwargs
    ) -> Union[
        list_report_downloads_response.ListReportDownloadsResponse,
        tuple[
            requests.Response, Optional[list_report_downloads_response.ListReportDownloadsResponse]
        ],
    ]:
        """Returns a list of unexpired, generated reports.

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:

                +-----------------+------------------+-----------------------------------------+
                |      Field      | Filter Condition |               Description               |
                +=================+==================+=========================================+
                | start_timestamp | $gte, $lt        | Start timestamp denotes the time filter |
                |                 |                  | for listing CSV report downloads.       |
                |                 |                  | $gte and $lt accept RFC-3999            |
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
                |                 |                  | "compliance", "audit", and              |
                |                 |                  | "consumption".                          |
                |                 |                  |                                         |
                |                 |                  | filter={"report_type":{"$in":["complian |
                |                 |                  | ce"]}}                                  |
                |                 |                  |                                         |
                |                 |                  |                                         |
                +-----------------+------------------+-----------------------------------------+

                For more information about filtering, refer to the
                Filtering section of this guide.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_report_downloads_response.ListReportDownloadsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/reports/downloads'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Execute request
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_report_downloads.', errors
            )

        if self.config.raw_response:
            return resp, list_report_downloads_response.ListReportDownloadsResponse.from_dictionary(
                resp.json()
            )
        return list_report_downloads_response.ListReportDownloadsResponse.from_dictionary(resp)

    def create_report_download(
        self, body: create_report_download_v1_request.CreateReportDownloadV1Request = None, **kwargs
    ) -> Union[
        create_report_download_response.CreateReportDownloadResponse,
        tuple[
            requests.Response,
            Optional[create_report_download_response.CreateReportDownloadResponse],
        ],
    ]:
        """Generates a report of a specified type given certain general conditions such as
        time range and other type-specific filters.

        Args:
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            create_report_download_response.CreateReportDownloadResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/reports/downloads'

        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_report_download.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                create_report_download_response.CreateReportDownloadResponse.from_dictionary(
                    resp.json()
                ),
            )
        return create_report_download_response.CreateReportDownloadResponse.from_dictionary(resp)
