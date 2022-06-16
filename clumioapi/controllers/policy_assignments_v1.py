#
# Copyright 2021. Clumio, Inc.
#

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

    def set_policy_assignments(
        self, body: set_policy_assignments_v1_request.SetPolicyAssignmentsV1Request = None
    ) -> set_assignments_response.SetAssignmentsResponse:
        """Assign (or unassign) policies on up to 100 entities. This endpoint returns a
        task
        ID and queues a task in the background to execute the request. Use the task ID
        to
        monitor task completion.

        Args:
            body:

        Returns:
            SetAssignmentsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/policies/assignments'

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
                'Error occurred while executing set_policy_assignments.', errors
            )
        return set_assignments_response.SetAssignmentsResponse.from_dictionary(resp)
