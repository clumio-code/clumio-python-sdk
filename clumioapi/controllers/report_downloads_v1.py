#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_report_download_response
from clumioapi.models import create_report_download_v1_request
from clumioapi.models import list_report_downloads_response
from clumioapi.models import list_report_downloads_v1_request
import requests


class ReportDownloadsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for report-downloads resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config

    def list_report_downloads(
        self, body: list_report_downloads_v1_request.ListReportDownloadsV1Request = None
    ) -> list_report_downloads_response.ListReportDownloadsResponse:
        """List unexpired report downloads.

        Args:
            body:

        Returns:
            ListReportDownloadsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/reports/downloads'

        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/report-downloads=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(
                _url_path,
                headers=_headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_report_downloads.', errors
            )
        return list_report_downloads_response.ListReportDownloadsResponse.from_dictionary(resp)

    def create_report_download(
        self, body: create_report_download_v1_request.CreateReportDownloadV1Request = None
    ) -> create_report_download_response.CreateReportDownloadResponse:
        """Create a new Report download.

        Args:
            body:

        Returns:
            CreateReportDownloadResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/reports/downloads'

        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/report-downloads=v1+json',
        }
        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=_headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_report_download.', errors
            )
        return create_report_download_response.CreateReportDownloadResponse.from_dictionary(resp)
