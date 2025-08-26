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
from clumioapi.controllers.types import report_compliance_runs_types
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
        filter: report_compliance_runs_types.ListComplianceReportRunsV1FilterT | None = None,
        **kwargs,
    ) -> list_compliance_runs_response.ListComplianceRunsResponse:
        """Get a list of all the compliance report runs belonging to the configuration.

        Args:
            configuration_id:
                Performs the operation on the compliance report configuration with the specified
                ID.
            limit:
                Limits the size of the items returned in the response.
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
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_compliance_runs_response.ListComplianceRunsResponse.from_response(response)

        # Prepare query URL
        _url_path = '/reports/compliance/configurations/{configuration_id}/runs'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'configuration_id': configuration_id}
        )
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_compliance_runs_response.ListComplianceRunsResponse
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
            error_str = (
                f'list_compliance_report_runs for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def create_compliance_report_run(
        self,
        configuration_id: str | None = None,
        body: (
            create_compliance_report_run_v1_request.CreateComplianceReportRunV1Request | None
        ) = None,
        **kwargs,
    ) -> create_compliance_run_response.CreateComplianceRunResponse:
        """Create a new compliance report run.

        Args:
            configuration_id:
                Performs the operation on the compliance report configuration with the specified
                ID.
            body:

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return create_compliance_run_response.CreateComplianceRunResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/reports/compliance/configurations/{configuration_id}/runs'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'configuration_id': configuration_id}
        )
        _query_parameters: dict[str, Any] = {}

        resp_instance: create_compliance_run_response.CreateComplianceRunResponse
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
            error_str = (
                f'create_compliance_report_run for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def delete_compliance_report_run(
        self, configuration_id: str | None = None, run_id: str | None = None, **kwargs
    ) -> object:
        """Delete a compliance report run.

        Args:
            configuration_id:
                Performs the operation on the compliance report configuration with the specified
                ID.
            run_id:
                Performs the operation on the compliance report run with the specified ID.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return resp

        # Prepare query URL
        _url_path = '/reports/compliance/configurations/{configuration_id}/runs/{run_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'configuration_id': configuration_id, 'run_id': run_id}
        )
        _query_parameters: dict[str, Any] = {}

        resp_instance: object
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.delete(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = (
                f'delete_compliance_report_run for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def send_compliance_report_run_email(
        self,
        configuration_id: str | None = None,
        run_id: str | None = None,
        body: (
            send_compliance_report_run_email_v1_request.SendComplianceReportRunEmailV1Request | None
        ) = None,
        **kwargs,
    ) -> send_compliance_run_email_response.SendComplianceRunEmailResponse:
        """Send a compliance report run to the given emails.

        Args:
            configuration_id:
                Performs the operation on the compliance report configuration with the specified
                ID.
            run_id:
                Performs the operation on the compliance report run with the specified ID.
            body:

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return send_compliance_run_email_response.SendComplianceRunEmailResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/reports/compliance/configurations/{configuration_id}/runs/{run_id}/_notify'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'configuration_id': configuration_id, 'run_id': run_id}
        )
        _query_parameters: dict[str, Any] = {}

        resp_instance: send_compliance_run_email_response.SendComplianceRunEmailResponse
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
            error_str = (
                f'send_compliance_report_run_email for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class ReportComplianceRunsV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for report-compliance-runs resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = ReportComplianceRunsV1Controller(config)

    def list_compliance_report_runs(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: report_compliance_runs_types.ListComplianceReportRunsV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[list_compliance_runs_response.ListComplianceRunsResponse]:
        """Get a list of all the compliance report runs belonging to the configuration.

        Args:
            configuration_id:
                Performs the operation on the compliance report configuration with the specified
                ID.
            limit:
                Limits the size of the items returned in the response.
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
        """
        start = start or '1'
        while True:
            response = self.controller.list_compliance_report_runs(
                limit=limit, start=start, filter=filter, **kwargs
            )
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
