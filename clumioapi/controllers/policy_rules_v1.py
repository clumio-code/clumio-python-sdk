#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_policy_rule_v1_request
from clumioapi.models import create_rule_response
from clumioapi.models import delete_rule_response
from clumioapi.models import list_rules_response
from clumioapi.models import read_rule_response
from clumioapi.models import update_policy_rule_v1_request
from clumioapi.models import update_rule_response
import requests


class PolicyRulesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for policy-rules resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.policy-rules=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }

    def list_policy_rules(
        self,
        limit: int = None,
        start: str = None,
        organizational_unit_id: str = None,
        sort: str = None,
        filter: str = None,
    ) -> list_rules_response.ListRulesResponse:
        """Returns a list of policy rules.

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
            organizational_unit_id:
                The Clumio-assigned ID of the organizational unit (OU) for which to retrieve
                rules.
                Only ancestor OU IDs or OU IDs accessible to the current OU or the current OU ID
                itself are allowed.
            sort:
                Returns the list of rules in the order specified. Set `sort` to the name of the
                sort field by
                which to sort in ascending order. To sort the list in reverse order, prefix the
                field name
                with a minus sign (`-`). Only one field may be sorted at a time.

                The following table lists the supported sort fields for this resource:

                +------------+-----------------------------------------------------------------+
                | Sort Field |                           Description                           |
                +============+=================================================================+
                | priority   | Sorts the rules in ascending priority (lowest first) order. For |
                |            | example, sort=priority                                          |
                +------------+-----------------------------------------------------------------+

                If a sort order is not specified, the individual rules are sorted by "priority"
                in descending priority (highest first) order.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +-------+------------------+---------------------------------------------------+
                | Field | Filter Condition |                    Description                    |
                +=======+==================+===================================================+
                | id    | $in              | Denotes the specific Rule IDs to retrieve, up to  |
                |       |                  | 100 ids                                           |
                |       |                  |                                                   |
                |       |                  | {"rule_id":{"$in":["1", "2"]}}                    |
                |       |                  |                                                   |
                |       |                  |                                                   |
                +-------+------------------+---------------------------------------------------+

        Returns:
            ListRulesResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/policies/rules'

        _query_parameters = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'organizational_unit_id': organizational_unit_id,
            'sort': sort,
            'filter': filter,
        }

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_policy_rules.', errors
            )
        return list_rules_response.ListRulesResponse.from_dictionary(resp)

    def create_policy_rule(
        self, body: create_policy_rule_v1_request.CreatePolicyRuleV1Request = None
    ) -> create_rule_response.CreateRuleResponse:
        """Creates a new policy rule. Policy rules determine how a policy should be
        assigned to assets.
        Additionally, to create a rule in the context of another Organizational Unit,
        refer to the
        Getting Started documentation.

        Args:
            body:

        Returns:
            CreateRuleResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/policies/rules'

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
                'Error occurred while executing create_policy_rule.', errors
            )
        return create_rule_response.CreateRuleResponse.from_dictionary(resp)

    def read_policy_rule(self, rule_id: str) -> read_rule_response.ReadRuleResponse:
        """Returns a representation of the specified policy rule.

        Args:
            rule_id:
                Performs the operation on the rule with the specified ID.
        Returns:
            ReadRuleResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/policies/rules/{rule_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'rule_id': rule_id})
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_policy_rule.', errors
            )
        return read_rule_response.ReadRuleResponse.from_dictionary(resp)

    def update_policy_rule(
        self, rule_id: str, body: update_policy_rule_v1_request.UpdatePolicyRuleV1Request = None
    ) -> update_rule_response.UpdateRuleResponse:
        """Updates an existing policy rule.

        Args:
            rule_id:
                Performs the operation on the rule with the specified ID.
            body:

        Returns:
            UpdateRuleResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/policies/rules/{rule_id}'
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
                'Error occurred while executing update_policy_rule.', errors
            )
        return update_rule_response.UpdateRuleResponse.from_dictionary(resp)

    def delete_policy_rule(
        self, rule_id: str, body: object = None
    ) -> delete_rule_response.DeleteRuleResponse:
        """Deletes the specified policy rule.

        Args:
            rule_id:
                Performs the operation on the rule with the specified ID.
            body:

        Returns:
            DeleteRuleResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/policies/rules/{rule_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'rule_id': rule_id})
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.delete(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing delete_policy_rule.', errors
            )
        return delete_rule_response.DeleteRuleResponse.from_dictionary(resp)
