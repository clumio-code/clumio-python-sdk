#
# Copyright 2023. Clumio, A Commvault Company.
#

import json

import requests


class ClumioException(Exception):
    """ClumioException is raised by all SDK APIs."""

    def __init__(
        self,
        reason: str,
        resp: requests.Response | None = None,
        error: requests.exceptions.HTTPError | None = None,
    ) -> None:
        """Constructor for the ClumioException class.

        Args:
            reason: The reason (or error message) for the Exception
                to be raised.
            resp: The response object from the API call that caused the exception.
        """

        if resp:
            resp_str = (
                f'HTTP Status Code: {resp.status_code}.\n'
                f'Reason: {resp.reason}.\n'
                f'Body: {json.dumps(json.loads(resp.text), indent=2, default=str)}'
            )

        if error:
            resp_str = (
                f'HTTP Status Code: {error.response.status_code}.\n'
                f'Reason: {error.response.reason}.\n'
                f'Body: {json.dumps(json.loads(error.response.text), indent=2, default=str)}'
            )
        super().__init__(f'{reason} {resp_str if resp or error else ''}')
