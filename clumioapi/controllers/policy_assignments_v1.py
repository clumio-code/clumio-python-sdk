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
from clumioapi.exceptions import clumio_exception
from clumioapi.models import set_assignments_response
from clumioapi.models import set_policy_assignments_v1_request
import requests


class PolicyAssignmentsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for policy-assignments resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.policy-assignments=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def set_policy_assignments(
        self,
        body: set_policy_assignments_v1_request.SetPolicyAssignmentsV1Request | None = None,
        **kwargs,
    ) -> set_assignments_response.SetAssignmentsResponse:
        """Assign (or unassign) policies on up to 100 entities. This endpoint returns a
        task
        ID and queues a task in the background to execute the request. Use the task ID
        to
        monitor task completion.

        Args:
            body:

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return set_assignments_response.SetAssignmentsResponse.from_response(response)

        # Prepare query URL
        _url_path = '/policies/assignments'

        _query_parameters: dict[str, Any] = {}

        resp_instance: set_assignments_response.SetAssignmentsResponse
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
            error_str = f'set_policy_assignments for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class PolicyAssignmentsV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for policy-assignments resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = PolicyAssignmentsV1Controller(config)
