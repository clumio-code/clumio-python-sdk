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
from clumioapi.controllers.types import policy_rules_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_policy_rule_v1_request
from clumioapi.models import create_rule_response
from clumioapi.models import delete_rule_response
from clumioapi.models import list_rules_response
from clumioapi.models import read_rule_response
from clumioapi.models import update_policy_rule_v1_request
from clumioapi.models import update_rule_response
import requests
import retrying


class PolicyRulesV1Controller:
    """A Controller to access Endpoints for policy-rules resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.policy-rules=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_policy_rules(
        self,
        limit: int | None = None,
        start: str | None = None,
        organizational_unit_id: str | None = None,
        sort: str | None = None,
        filter: policy_rules_types.ListPolicyRulesV1FilterT | None = None,
        **kwargs,
    ) -> list_rules_response.ListRulesResponse:
        """Returns a list of policy rules.

        Args:
            limit:
                Limits the size of the items returned in the response.
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

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_rules_response.ListRulesResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/policies/rules'

        if start:
            _url_path = f'{_url_path}?start={start}'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'organizational_unit_id': organizational_unit_id,
            'sort': sort,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_rules_response.ListRulesResponse
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
            error_str = f'list_policy_rules for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def create_policy_rule(
        self, body: create_policy_rule_v1_request.CreatePolicyRuleV1Request | None = None, **kwargs
    ) -> create_rule_response.CreateRuleResponse:
        """Creates a new policy rule. Policy rules determine how a policy should be
        assigned to assets.
        Additionally, to create a rule in the context of another Organizational Unit,
        refer to the
        Getting Started documentation.

        Args:
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return create_rule_response.CreateRuleResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/policies/rules'

        _query_parameters: dict[str, Any] = {}

        resp_instance: create_rule_response.CreateRuleResponse
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
            error_str = f'create_policy_rule for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_policy_rule(
        self, rule_id: str | None = None, **kwargs
    ) -> read_rule_response.ReadRuleResponse:
        """Returns a representation of the specified policy rule.

        Args:
            rule_id:
                Performs the operation on the rule with the specified ID.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_rule_response.ReadRuleResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/policies/rules/{rule_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'rule_id': rule_id})

        _query_parameters: dict[str, Any] = {}

        resp_instance: read_rule_response.ReadRuleResponse
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
            error_str = f'read_policy_rule for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def update_policy_rule(
        self,
        rule_id: str | None = None,
        body: update_policy_rule_v1_request.UpdatePolicyRuleV1Request | None = None,
        **kwargs,
    ) -> update_rule_response.UpdateRuleResponse:
        """Updates an existing policy rule.

        Args:
            rule_id:
                Performs the operation on the rule with the specified ID.
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return update_rule_response.UpdateRuleResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/policies/rules/{rule_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'rule_id': rule_id})

        _query_parameters: dict[str, Any] = {}

        resp_instance: update_rule_response.UpdateRuleResponse
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
            error_str = f'update_policy_rule for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def delete_policy_rule(
        self, rule_id: str | None = None, body: object | None = None, **kwargs
    ) -> delete_rule_response.DeleteRuleResponse:
        """Deletes the specified policy rule.

        Args:
            rule_id:
                Performs the operation on the rule with the specified ID.
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return delete_rule_response.DeleteRuleResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/policies/rules/{rule_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'rule_id': rule_id})

        _query_parameters: dict[str, Any] = {}

        resp_instance: delete_rule_response.DeleteRuleResponse
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
            error_str = f'delete_policy_rule for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class PolicyRulesV1ControllerPaginator:
    """A Controller to access Endpoints for policy-rules resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_policy_rules(
        self,
        limit: int | None = None,
        start: str | None = None,
        organizational_unit_id: str | None = None,
        sort: str | None = None,
        filter: policy_rules_types.ListPolicyRulesV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[list_rules_response.ListRulesResponse]:
        """Returns a list of policy rules.

        Args:
            limit:
                Limits the size of the items returned in the response.
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

        """
        controller = PolicyRulesV1Controller(self.controller)
        while True:
            response = controller.list_policy_rules(
                limit=limit,
                start=start,
                organizational_unit_id=organizational_unit_id,
                sort=sort,
                filter=filter,
                **kwargs,
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
