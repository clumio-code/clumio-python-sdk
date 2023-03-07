#
# Copyright 2021. Clumio, Inc.
#

import json

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
        self, limit: int = None, start: str = None, filter: str = None
    ) -> list_auto_user_provisioning_rules_response.ListAutoUserProvisioningRulesResponse:
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
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_auto_user_provisioning_rules.', errors
            )

        return list_auto_user_provisioning_rules_response.ListAutoUserProvisioningRulesResponse.from_dictionary(
            resp
        )

    def create_auto_user_provisioning_rule(
        self,
        body: create_auto_user_provisioning_rule_v1_request.CreateAutoUserProvisioningRuleV1Request = None,
    ) -> create_auto_user_provisioning_rule_response.CreateAutoUserProvisioningRuleResponse:
        """Creates a new auto user provisioning rule. Auto user provisioning rules
        determine the role and
        organizational units to be assigned to a user subject to the condition.

        Args:
            body:

        Returns:
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
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_auto_user_provisioning_rule.', errors
            )

        return create_auto_user_provisioning_rule_response.CreateAutoUserProvisioningRuleResponse.from_dictionary(
            resp
        )

    def read_auto_user_provisioning_rule(
        self, rule_id: str
    ) -> read_auto_user_provisioning_rule_response.ReadAutoUserProvisioningRuleResponse:
        """Returns a representation of the specified auto user provisioning rule.

        Args:
            rule_id:
                Retrieves the rule with the specified ID.
        Returns:
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
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_auto_user_provisioning_rule.', errors
            )

        return read_auto_user_provisioning_rule_response.ReadAutoUserProvisioningRuleResponse.from_dictionary(
            resp
        )

    def update_auto_user_provisioning_rule(
        self,
        rule_id: str,
        body: update_auto_user_provisioning_rule_v1_request.UpdateAutoUserProvisioningRuleV1Request = None,
    ) -> update_auto_user_provisioning_rule_response.UpdateAutoUserProvisioningRuleResponse:
        """Update an existing auto user provisioning rule.

        Args:
            rule_id:
                Updates the rule with the specified ID.
            body:

        Returns:
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
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing update_auto_user_provisioning_rule.', errors
            )

        return update_auto_user_provisioning_rule_response.UpdateAutoUserProvisioningRuleResponse.from_dictionary(
            resp
        )

    def delete_auto_user_provisioning_rule(self, rule_id: str) -> object:
        """Delete the specified auto user provisioning rule.

        Args:
            rule_id:
                Deletes the rule with the specified ID.
        Returns:
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
            resp = self.client.delete(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing delete_auto_user_provisioning_rule.', errors
            )

        return resp
