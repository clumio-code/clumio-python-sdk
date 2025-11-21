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
from clumioapi.controllers.types import report_compliance_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_compliance_configuration_response
from clumioapi.models import create_compliance_report_configuration_v1_request
from clumioapi.models import list_compliance_configurations_response
from clumioapi.models import read_compliance_configuration_response
from clumioapi.models import update_compliance_configuration_response
from clumioapi.models import update_compliance_report_configuration_v1_request
import requests
import retrying


class ReportComplianceV1Controller:
    """A Controller to access Endpoints for report-compliance resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.report-compliance=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_compliance_report_configurations(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: report_compliance_types.ListComplianceReportConfigurationsV1FilterT | None = None,
        **kwargs,
    ) -> list_compliance_configurations_response.ListComplianceConfigurationsResponse:
        """Get a list of all the compliance report configurations.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria.
                The following table lists the supported filter fields for this resource and the
                filter conditions that can be applied on those fields:

                +-------------------+------------------+---------------------------------------+
                |       Field       | Filter Condition |              Description              |
                +===================+==================+=======================================+
                | report_name       | $contains        | The substring in the name of the      |
                |                   |                  | report to filter with.                |
                |                   |                  | For example, "filter": "{"report_name |
                |                   |                  | ":{"$contains":"name"}}"              |
                |                   |                  |                                       |
                +-------------------+------------------+---------------------------------------+
                | compliance_status | $eq              | The compliance status of the report   |
                |                   |                  | configuration to filter with.         |
                |                   |                  | The possible values are "compliant"   |
                |                   |                  | and "non_compliant".                  |
                |                   |                  | For example, "filter": "{"compliance_ |
                |                   |                  | status":{"$eq":"compliant"}}"         |
                |                   |                  |                                       |
                +-------------------+------------------+---------------------------------------+

                For more information about filtering, refer to the
                Filtering section of this guide.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_compliance_configurations_response.ListComplianceConfigurationsResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/reports/compliance/configurations'

        if start:
            _url_path = f'{_url_path}?start={start}'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_compliance_configurations_response.ListComplianceConfigurationsResponse
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
            error_str = f'list_compliance_report_configurations for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def create_compliance_report_configuration(
        self,
        body: (
            create_compliance_report_configuration_v1_request.CreateComplianceReportConfigurationV1Request
            | None
        ) = None,
        **kwargs,
    ) -> create_compliance_configuration_response.CreateComplianceConfigurationResponse:
        """Create a compliance report configuration.

        Args:
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return create_compliance_configuration_response.CreateComplianceConfigurationResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/reports/compliance/configurations'

        _query_parameters: dict[str, Any] = {}

        resp_instance: (
            create_compliance_configuration_response.CreateComplianceConfigurationResponse
        )
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
            error_str = f'create_compliance_report_configuration for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_compliance_report_configuration(
        self, configuration_id: str | None = None, **kwargs
    ) -> read_compliance_configuration_response.ReadComplianceConfigurationResponse:
        """Returns a representation of the specified compliance report configuration.

        Args:
            configuration_id:
                Performs the operation on the report configuration with the specified ID.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_compliance_configuration_response.ReadComplianceConfigurationResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/reports/compliance/configurations/{configuration_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'configuration_id': configuration_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: read_compliance_configuration_response.ReadComplianceConfigurationResponse
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
            error_str = f'read_compliance_report_configuration for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def update_compliance_report_configuration(
        self,
        configuration_id: str | None = None,
        body: (
            update_compliance_report_configuration_v1_request.UpdateComplianceReportConfigurationV1Request
            | None
        ) = None,
        **kwargs,
    ) -> update_compliance_configuration_response.UpdateComplianceConfigurationResponse:
        """Update a compliance report configuration with the id {configuration_id}.

        Args:
            configuration_id:
                Performs the operation on the report configuration with the specified ID.
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return update_compliance_configuration_response.UpdateComplianceConfigurationResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/reports/compliance/configurations/{configuration_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'configuration_id': configuration_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: (
            update_compliance_configuration_response.UpdateComplianceConfigurationResponse
        )
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.put(
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
            error_str = f'update_compliance_report_configuration for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def delete_compliance_report_configuration(
        self, configuration_id: str | None = None, **kwargs
    ) -> object:
        """Delete a compliance report configuration with the id {configuration_id}.

        Args:
            configuration_id:
                Performs the operation on the compliance report configuration with the specified
                ID.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return resp

        # Prepare query URL
        _url_path = '/reports/compliance/configurations/{configuration_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'configuration_id': configuration_id}
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
            error_str = f'delete_compliance_report_configuration for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class ReportComplianceV1ControllerPaginator:
    """A Controller to access Endpoints for report-compliance resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_compliance_report_configurations(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: report_compliance_types.ListComplianceReportConfigurationsV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[list_compliance_configurations_response.ListComplianceConfigurationsResponse]:
        """Get a list of all the compliance report configurations.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria.
                The following table lists the supported filter fields for this resource and the
                filter conditions that can be applied on those fields:

                +-------------------+------------------+---------------------------------------+
                |       Field       | Filter Condition |              Description              |
                +===================+==================+=======================================+
                | report_name       | $contains        | The substring in the name of the      |
                |                   |                  | report to filter with.                |
                |                   |                  | For example, "filter": "{"report_name |
                |                   |                  | ":{"$contains":"name"}}"              |
                |                   |                  |                                       |
                +-------------------+------------------+---------------------------------------+
                | compliance_status | $eq              | The compliance status of the report   |
                |                   |                  | configuration to filter with.         |
                |                   |                  | The possible values are "compliant"   |
                |                   |                  | and "non_compliant".                  |
                |                   |                  | For example, "filter": "{"compliance_ |
                |                   |                  | status":{"$eq":"compliant"}}"         |
                |                   |                  |                                       |
                +-------------------+------------------+---------------------------------------+

                For more information about filtering, refer to the
                Filtering section of this guide.
        """
        controller = ReportComplianceV1Controller(self.controller)
        while True:
            response = controller.list_compliance_report_configurations(
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
