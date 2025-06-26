#
# Copyright 2023. Clumio, Inc.
#

import json
from typing import Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
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
        self, limit: int = None, start: str = None, filter: str = None, **kwargs
    ) -> Union[
        list_compliance_configurations_response.ListComplianceConfigurationsResponse,
        tuple[
            requests.Response,
            Optional[list_compliance_configurations_response.ListComplianceConfigurationsResponse],
        ],
    ]:
        """Get a list of all the compliance report configurations.

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
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
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_compliance_configurations_response.ListComplianceConfigurationsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/reports/compliance/configurations'

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
                'Error occurred while executing list_compliance_report_configurations.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                list_compliance_configurations_response.ListComplianceConfigurationsResponse.from_dictionary(
                    resp.json()
                ),
            )
        return list_compliance_configurations_response.ListComplianceConfigurationsResponse.from_dictionary(
            resp
        )

    def create_compliance_report_configuration(
        self,
        body: create_compliance_report_configuration_v1_request.CreateComplianceReportConfigurationV1Request = None,
        **kwargs,
    ) -> Union[
        create_compliance_configuration_response.CreateComplianceConfigurationResponse,
        tuple[
            requests.Response,
            Optional[
                create_compliance_configuration_response.CreateComplianceConfigurationResponse
            ],
        ],
    ]:
        """Create a compliance report configuration.

        Args:
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            create_compliance_configuration_response.CreateComplianceConfigurationResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/reports/compliance/configurations'

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
                'Error occurred while executing create_compliance_report_configuration.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                create_compliance_configuration_response.CreateComplianceConfigurationResponse.from_dictionary(
                    resp.json()
                ),
            )
        return create_compliance_configuration_response.CreateComplianceConfigurationResponse.from_dictionary(
            resp
        )

    def read_compliance_report_configuration(self, configuration_id: str, **kwargs) -> Union[
        read_compliance_configuration_response.ReadComplianceConfigurationResponse,
        tuple[
            requests.Response,
            Optional[read_compliance_configuration_response.ReadComplianceConfigurationResponse],
        ],
    ]:
        """Returns a representation of the specified compliance report configuration.

        Args:
            configuration_id:
                Performs the operation on the report configuration with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_compliance_configuration_response.ReadComplianceConfigurationResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/reports/compliance/configurations/{configuration_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'configuration_id': configuration_id}
        )
        _query_parameters = {}

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
                'Error occurred while executing read_compliance_report_configuration.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                read_compliance_configuration_response.ReadComplianceConfigurationResponse.from_dictionary(
                    resp.json()
                ),
            )
        return read_compliance_configuration_response.ReadComplianceConfigurationResponse.from_dictionary(
            resp
        )

    def update_compliance_report_configuration(
        self,
        configuration_id: str,
        body: update_compliance_report_configuration_v1_request.UpdateComplianceReportConfigurationV1Request = None,
        **kwargs,
    ) -> Union[
        update_compliance_configuration_response.UpdateComplianceConfigurationResponse,
        tuple[
            requests.Response,
            Optional[
                update_compliance_configuration_response.UpdateComplianceConfigurationResponse
            ],
        ],
    ]:
        """Update a compliance report configuration with the id {configuration_id}.

        Args:
            configuration_id:
                Performs the operation on the report configuration with the specified ID.
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            update_compliance_configuration_response.UpdateComplianceConfigurationResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/reports/compliance/configurations/{configuration_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'configuration_id': configuration_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.put(
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
                'Error occurred while executing update_compliance_report_configuration.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                update_compliance_configuration_response.UpdateComplianceConfigurationResponse.from_dictionary(
                    resp.json()
                ),
            )
        return update_compliance_configuration_response.UpdateComplianceConfigurationResponse.from_dictionary(
            resp
        )

    def delete_compliance_report_configuration(
        self, configuration_id: str, **kwargs
    ) -> Union[object, tuple[requests.Response, Optional[object]]]:
        """Delete a compliance report configuration with the id {configuration_id}.

        Args:
            configuration_id:
                Performs the operation on the compliance report configuration with the specified
                ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            object: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/reports/compliance/configurations/{configuration_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'configuration_id': configuration_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.delete(
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
                'Error occurred while executing delete_compliance_report_configuration.', errors
            )

        if self.config.raw_response:
            return resp, resp.json()
        return resp
