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
from clumioapi.models import create_compliance_report_run_v1_request
from clumioapi.models import create_compliance_run_response
from clumioapi.models import list_compliance_runs_response
from clumioapi.models import send_compliance_report_run_email_v1_request
from clumioapi.models import send_compliance_run_email_response
import requests


class ReportComplianceRunsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for report-compliance-runs resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.report-compliance-runs=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_compliance_report_runs(
        self,
        configuration_id: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        filter: str | None = None,
        **kwargs,
    ) -> Union[
        list_compliance_runs_response.ListComplianceRunsResponse,
        tuple[
            requests.Response, Optional[list_compliance_runs_response.ListComplianceRunsResponse]
        ],
    ]:
        """Get a list of all the compliance report runs belonging to the configuration.

        Args:
            configuration_id:
                Performs the operation on the compliance report configuration with the specified
                ID.
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +-------------------+------------------+---------------------------------------+
                |       Field       | Filter Condition |              Description              |
                +===================+==================+=======================================+
                | status            | $in              | The generation status of the report   |
                |                   |                  | configuration to filter with.         |
                |                   |                  | The possible values are "completed",  |
                |                   |                  | "failed" and "generating".            |
                |                   |                  | For example, "filter":                |
                |                   |                  | "{"status":{"$in":["completed"]}}".   |
                |                   |                  |                                       |
                +-------------------+------------------+---------------------------------------+
                | compliance_status | $in              | The compliance status of the report   |
                |                   |                  | run to filter with.                   |
                |                   |                  | The possible values are "compliant"   |
                |                   |                  | and "non_compliant".                  |
                |                   |                  | For example, "filter": "{"compliance_ |
                |                   |                  | status":{"$in":["compliant"]}}".      |
                |                   |                  |                                       |
                +-------------------+------------------+---------------------------------------+

                For more information about filtering, refer to the
                Filtering section of this guide.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_compliance_runs_response.ListComplianceRunsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/reports/compliance/configurations/{configuration_id}/runs'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'configuration_id': configuration_id}
        )
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
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_compliance_report_runs.', errors
            )

        obj = list_compliance_runs_response.ListComplianceRunsResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def create_compliance_report_run(
        self,
        configuration_id: str | None = None,
        body: (
            create_compliance_report_run_v1_request.CreateComplianceReportRunV1Request | None
        ) = None,
        **kwargs,
    ) -> Union[
        create_compliance_run_response.CreateComplianceRunResponse,
        tuple[
            requests.Response, Optional[create_compliance_run_response.CreateComplianceRunResponse]
        ],
    ]:
        """Create a new compliance report run.

        Args:
            configuration_id:
                Performs the operation on the compliance report configuration with the specified
                ID.
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            create_compliance_run_response.CreateComplianceRunResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/reports/compliance/configurations/{configuration_id}/runs'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'configuration_id': configuration_id}
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
                'Error occurred while executing create_compliance_report_run.', errors
            )

        obj = create_compliance_run_response.CreateComplianceRunResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj

    def delete_compliance_report_run(
        self, configuration_id: str | None = None, run_id: str | None = None, **kwargs
    ) -> Union[object, tuple[requests.Response, Optional[object]]]:
        """Delete a compliance report run.

        Args:
            configuration_id:
                Performs the operation on the compliance report configuration with the specified
                ID.
            run_id:
                Performs the operation on the compliance report run with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            object: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/reports/compliance/configurations/{configuration_id}/runs/{run_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'configuration_id': configuration_id, 'run_id': run_id}
        )
        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.delete(
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
                'Error occurred while executing delete_compliance_report_run.', errors
            )

        if raw_response:
            return resp, resp.json()
        return resp

    def send_compliance_report_run_email(
        self,
        configuration_id: str | None = None,
        run_id: str | None = None,
        body: (
            send_compliance_report_run_email_v1_request.SendComplianceReportRunEmailV1Request | None
        ) = None,
        **kwargs,
    ) -> Union[
        send_compliance_run_email_response.SendComplianceRunEmailResponse,
        tuple[
            requests.Response,
            Optional[send_compliance_run_email_response.SendComplianceRunEmailResponse],
        ],
    ]:
        """Send a compliance report run to the given emails.

        Args:
            configuration_id:
                Performs the operation on the compliance report configuration with the specified
                ID.
            run_id:
                Performs the operation on the compliance report run with the specified ID.
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            send_compliance_run_email_response.SendComplianceRunEmailResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/reports/compliance/configurations/{configuration_id}/runs/{run_id}/_notify'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'configuration_id': configuration_id, 'run_id': run_id}
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
                'Error occurred while executing send_compliance_report_run_email.', errors
            )

        obj = send_compliance_run_email_response.SendComplianceRunEmailResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj
