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
from clumioapi.controllers.types import report_compliance_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_compliance_configuration_response
from clumioapi.models import create_compliance_report_configuration_v1_request
from clumioapi.models import list_compliance_configurations_response
from clumioapi.models import read_compliance_configuration_response
from clumioapi.models import update_compliance_configuration_response
from clumioapi.models import update_compliance_report_configuration_v1_request
import requests


class ReportComplianceV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for report-compliance resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.report-compliance=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

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

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_compliance_configurations_response.ListComplianceConfigurationsResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/reports/compliance/configurations'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
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

        def get_instance_from_response(response: requests.Response) -> Any:
            return create_compliance_configuration_response.CreateComplianceConfigurationResponse.from_response(
                response
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

        def get_instance_from_response(response: requests.Response) -> Any:
            return read_compliance_configuration_response.ReadComplianceConfigurationResponse.from_response(
                response
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

        def get_instance_from_response(response: requests.Response) -> Any:
            return update_compliance_configuration_response.UpdateComplianceConfigurationResponse.from_response(
                response
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

        def get_instance_from_response(response: requests.Response) -> Any:
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


class ReportComplianceV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for report-compliance resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = ReportComplianceV1Controller(config)

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
        start = start or '1'
        while True:
            response = self.controller.list_compliance_report_configurations(
                limit=limit, start=start, filter=filter, **kwargs
            )
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
