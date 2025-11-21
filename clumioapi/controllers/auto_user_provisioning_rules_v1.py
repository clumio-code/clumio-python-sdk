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
from clumioapi.controllers.types import auto_user_provisioning_rules_types
from clumioapi.controllers.types import aws_s3_buckets_v1_bucket_matcher_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_auto_user_provisioning_rule_response
from clumioapi.models import create_auto_user_provisioning_rule_v1_request
from clumioapi.models import list_auto_user_provisioning_rules_response
from clumioapi.models import read_auto_user_provisioning_rule_response
from clumioapi.models import update_auto_user_provisioning_rule_response
from clumioapi.models import update_auto_user_provisioning_rule_v1_request
import requests
import retrying


class AutoUserProvisioningRulesV1Controller:
    """A Controller to access Endpoints for auto-user-provisioning-rules resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.auto-user-provisioning-rules=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_auto_user_provisioning_rules(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            auto_user_provisioning_rules_types.ListAutoUserProvisioningRulesV1FilterT | None
        ) = None,
        **kwargs,
    ) -> list_auto_user_provisioning_rules_response.ListAutoUserProvisioningRulesResponse:
        """Returns a list of auto user provisioning rules.

        Args:
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

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_auto_user_provisioning_rules_response.ListAutoUserProvisioningRulesResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/settings/auto-user-provisioning/rules'

        if start:
            _url_path = f'{_url_path}?start={start}'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: (
            list_auto_user_provisioning_rules_response.ListAutoUserProvisioningRulesResponse
        )
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
            error_str = f'list_auto_user_provisioning_rules for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def create_auto_user_provisioning_rule(
        self,
        body: (
            create_auto_user_provisioning_rule_v1_request.CreateAutoUserProvisioningRuleV1Request
            | None
        ) = None,
        **kwargs,
    ) -> create_auto_user_provisioning_rule_response.CreateAutoUserProvisioningRuleResponse:
        """Creates a new auto user provisioning rule. Auto user provisioning rules
        determine the role and
        organizational units to be assigned to a user subject to the condition.

        Args:
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return create_auto_user_provisioning_rule_response.CreateAutoUserProvisioningRuleResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/settings/auto-user-provisioning/rules'

        _query_parameters: dict[str, Any] = {}

        resp_instance: (
            create_auto_user_provisioning_rule_response.CreateAutoUserProvisioningRuleResponse
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
            error_str = f'create_auto_user_provisioning_rule for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_auto_user_provisioning_rule(
        self, rule_id: str | None = None, **kwargs
    ) -> read_auto_user_provisioning_rule_response.ReadAutoUserProvisioningRuleResponse:
        """Returns a representation of the specified auto user provisioning rule.

        Args:
            rule_id:
                Retrieves the rule with the specified ID.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_auto_user_provisioning_rule_response.ReadAutoUserProvisioningRuleResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/settings/auto-user-provisioning/rules/{rule_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'rule_id': rule_id})

        _query_parameters: dict[str, Any] = {}

        resp_instance: (
            read_auto_user_provisioning_rule_response.ReadAutoUserProvisioningRuleResponse
        )
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
                f'read_auto_user_provisioning_rule for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def update_auto_user_provisioning_rule(
        self,
        rule_id: str | None = None,
        body: (
            update_auto_user_provisioning_rule_v1_request.UpdateAutoUserProvisioningRuleV1Request
            | None
        ) = None,
        **kwargs,
    ) -> update_auto_user_provisioning_rule_response.UpdateAutoUserProvisioningRuleResponse:
        """Update an existing auto user provisioning rule.

        Args:
            rule_id:
                Updates the rule with the specified ID.
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return update_auto_user_provisioning_rule_response.UpdateAutoUserProvisioningRuleResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/settings/auto-user-provisioning/rules/{rule_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'rule_id': rule_id})

        _query_parameters: dict[str, Any] = {}

        resp_instance: (
            update_auto_user_provisioning_rule_response.UpdateAutoUserProvisioningRuleResponse
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
            error_str = f'update_auto_user_provisioning_rule for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def delete_auto_user_provisioning_rule(self, rule_id: str | None = None, **kwargs) -> object:
        """Delete the specified auto user provisioning rule.

        Args:
            rule_id:
                Deletes the rule with the specified ID.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return resp

        # Prepare query URL
        _url_path = '/settings/auto-user-provisioning/rules/{rule_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'rule_id': rule_id})

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
            error_str = f'delete_auto_user_provisioning_rule for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class AutoUserProvisioningRulesV1ControllerPaginator:
    """A Controller to access Endpoints for auto-user-provisioning-rules resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_auto_user_provisioning_rules(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            auto_user_provisioning_rules_types.ListAutoUserProvisioningRulesV1FilterT | None
        ) = None,
        **kwargs,
    ) -> Iterator[list_auto_user_provisioning_rules_response.ListAutoUserProvisioningRulesResponse]:
        """Returns a list of auto user provisioning rules.

        Args:
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

        """
        controller = AutoUserProvisioningRulesV1Controller(self.controller)
        while True:
            response = controller.list_auto_user_provisioning_rules(
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
