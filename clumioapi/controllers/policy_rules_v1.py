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
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_policy_rules(
        self,
        limit: int | None = None,
        start: str | None = None,
        organizational_unit_id: str | None = None,
        sort: str | None = None,
        filter: str | None = None,
        **kwargs,
    ) -> Union[
        list_rules_response.ListRulesResponse,
        tuple[requests.Response, Optional[list_rules_response.ListRulesResponse]],
    ]:
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
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_rules_response.ListRulesResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/policies/rules'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'organizational_unit_id': organizational_unit_id,
            'sort': sort,
            'filter': filter,
        }

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
                'Error occurred while executing list_policy_rules.', errors
            )

        obj = list_rules_response.ListRulesResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def create_policy_rule(
        self, body: create_policy_rule_v1_request.CreatePolicyRuleV1Request | None = None, **kwargs
    ) -> Union[
        create_rule_response.CreateRuleResponse,
        tuple[requests.Response, Optional[create_rule_response.CreateRuleResponse]],
    ]:
        """Creates a new policy rule. Policy rules determine how a policy should be
        assigned to assets.
        Additionally, to create a rule in the context of another Organizational Unit,
        refer to the
        Getting Started documentation.

        Args:
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            create_rule_response.CreateRuleResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/policies/rules'

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
                'Error occurred while executing create_policy_rule.', errors
            )

        obj = create_rule_response.CreateRuleResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def read_policy_rule(self, rule_id: str | None = None, **kwargs) -> Union[
        read_rule_response.ReadRuleResponse,
        tuple[requests.Response, Optional[read_rule_response.ReadRuleResponse]],
    ]:
        """Returns a representation of the specified policy rule.

        Args:
            rule_id:
                Performs the operation on the rule with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_rule_response.ReadRuleResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/policies/rules/{rule_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'rule_id': rule_id})
        _query_parameters: dict[str, Any] = {}

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
                'Error occurred while executing read_policy_rule.', errors
            )

        obj = read_rule_response.ReadRuleResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def update_policy_rule(
        self,
        rule_id: str | None = None,
        body: update_policy_rule_v1_request.UpdatePolicyRuleV1Request | None = None,
        **kwargs,
    ) -> Union[
        update_rule_response.UpdateRuleResponse,
        tuple[requests.Response, Optional[update_rule_response.UpdateRuleResponse]],
    ]:
        """Updates an existing policy rule.

        Args:
            rule_id:
                Performs the operation on the rule with the specified ID.
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            update_rule_response.UpdateRuleResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/policies/rules/{rule_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'rule_id': rule_id})
        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.put(
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
                'Error occurred while executing update_policy_rule.', errors
            )

        obj = update_rule_response.UpdateRuleResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def delete_policy_rule(
        self, rule_id: str | None = None, body: object | None = None, **kwargs
    ) -> Union[
        delete_rule_response.DeleteRuleResponse,
        tuple[requests.Response, Optional[delete_rule_response.DeleteRuleResponse]],
    ]:
        """Deletes the specified policy rule.

        Args:
            rule_id:
                Performs the operation on the rule with the specified ID.
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            delete_rule_response.DeleteRuleResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/policies/rules/{rule_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'rule_id': rule_id})
        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.delete(
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
                'Error occurred while executing delete_policy_rule.', errors
            )

        obj = delete_rule_response.DeleteRuleResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj
