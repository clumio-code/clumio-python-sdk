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
from clumioapi.models import create_auto_user_provisioning_rule_response
from clumioapi.models import create_auto_user_provisioning_rule_v1_request
from clumioapi.models import list_auto_user_provisioning_rules_response
from clumioapi.models import read_auto_user_provisioning_rule_response
from clumioapi.models import update_auto_user_provisioning_rule_response
from clumioapi.models import update_auto_user_provisioning_rule_v1_request
import requests


class AutoUserProvisioningRulesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for auto-user-provisioning-rules resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.auto-user-provisioning-rules=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_auto_user_provisioning_rules(
        self, limit: int = None, start: str = None, filter: str = None, **kwargs
    ) -> Union[
        list_auto_user_provisioning_rules_response.ListAutoUserProvisioningRulesResponse,
        tuple[
            requests.Response,
            Optional[
                list_auto_user_provisioning_rules_response.ListAutoUserProvisioningRulesResponse
            ],
        ],
    ]:
        """Returns a list of auto user provisioning rules.

        Args:
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

                +------------------------+------------------+----------------------------------+
                |         Field          | Filter Condition |           Description            |
                +========================+==================+==================================+
                | name                   | $contains        | A case sensitive substring of    |
                |                        |                  | the name of the rule.            |
                +------------------------+------------------+----------------------------------+
                | role_id                | $eq              | A Clumio-assigned ID of the      |
                |                        |                  | role.                            |
                +------------------------+------------------+----------------------------------+
                | organizational_unit_id | $eq              | A Clumio-assigned ID of the      |
                |                        |                  | organizational unit.             |
                +------------------------+------------------+----------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_auto_user_provisioning_rules_response.ListAutoUserProvisioningRulesResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/settings/auto-user-provisioning/rules'

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
                'Error occurred while executing list_auto_user_provisioning_rules.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                list_auto_user_provisioning_rules_response.ListAutoUserProvisioningRulesResponse.from_dictionary(
                    resp.json()
                ),
            )
        return list_auto_user_provisioning_rules_response.ListAutoUserProvisioningRulesResponse.from_dictionary(
            resp
        )

    def create_auto_user_provisioning_rule(
        self,
        body: create_auto_user_provisioning_rule_v1_request.CreateAutoUserProvisioningRuleV1Request = None,
        **kwargs,
    ) -> Union[
        create_auto_user_provisioning_rule_response.CreateAutoUserProvisioningRuleResponse,
        tuple[
            requests.Response,
            Optional[
                create_auto_user_provisioning_rule_response.CreateAutoUserProvisioningRuleResponse
            ],
        ],
    ]:
        """Creates a new auto user provisioning rule. Auto user provisioning rules
        determine the role and
        organizational units to be assigned to a user subject to the condition.

        Args:
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            create_auto_user_provisioning_rule_response.CreateAutoUserProvisioningRuleResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/settings/auto-user-provisioning/rules'

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
                'Error occurred while executing create_auto_user_provisioning_rule.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                create_auto_user_provisioning_rule_response.CreateAutoUserProvisioningRuleResponse.from_dictionary(
                    resp.json()
                ),
            )
        return create_auto_user_provisioning_rule_response.CreateAutoUserProvisioningRuleResponse.from_dictionary(
            resp
        )

    def read_auto_user_provisioning_rule(
        self, rule_id: str, **kwargs
    ) -> Union[
        read_auto_user_provisioning_rule_response.ReadAutoUserProvisioningRuleResponse,
        tuple[
            requests.Response,
            Optional[
                read_auto_user_provisioning_rule_response.ReadAutoUserProvisioningRuleResponse
            ],
        ],
    ]:
        """Returns a representation of the specified auto user provisioning rule.

        Args:
            rule_id:
                Retrieves the rule with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_auto_user_provisioning_rule_response.ReadAutoUserProvisioningRuleResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/settings/auto-user-provisioning/rules/{rule_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'rule_id': rule_id})
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
                'Error occurred while executing read_auto_user_provisioning_rule.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                read_auto_user_provisioning_rule_response.ReadAutoUserProvisioningRuleResponse.from_dictionary(
                    resp.json()
                ),
            )
        return read_auto_user_provisioning_rule_response.ReadAutoUserProvisioningRuleResponse.from_dictionary(
            resp
        )

    def update_auto_user_provisioning_rule(
        self,
        rule_id: str,
        body: update_auto_user_provisioning_rule_v1_request.UpdateAutoUserProvisioningRuleV1Request = None,
        **kwargs,
    ) -> Union[
        update_auto_user_provisioning_rule_response.UpdateAutoUserProvisioningRuleResponse,
        tuple[
            requests.Response,
            Optional[
                update_auto_user_provisioning_rule_response.UpdateAutoUserProvisioningRuleResponse
            ],
        ],
    ]:
        """Update an existing auto user provisioning rule.

        Args:
            rule_id:
                Updates the rule with the specified ID.
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            update_auto_user_provisioning_rule_response.UpdateAutoUserProvisioningRuleResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/settings/auto-user-provisioning/rules/{rule_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'rule_id': rule_id})
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
                'Error occurred while executing update_auto_user_provisioning_rule.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                update_auto_user_provisioning_rule_response.UpdateAutoUserProvisioningRuleResponse.from_dictionary(
                    resp.json()
                ),
            )
        return update_auto_user_provisioning_rule_response.UpdateAutoUserProvisioningRuleResponse.from_dictionary(
            resp
        )

    def delete_auto_user_provisioning_rule(
        self, rule_id: str, **kwargs
    ) -> Union[object, tuple[requests.Response, Optional[object]]]:
        """Delete the specified auto user provisioning rule.

        Args:
            rule_id:
                Deletes the rule with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            object: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/settings/auto-user-provisioning/rules/{rule_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'rule_id': rule_id})
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
                'Error occurred while executing delete_auto_user_provisioning_rule.', errors
            )

        if self.config.raw_response:
            return resp, resp.json()
        return resp
