#
# Copyright 2023. Clumio, A Commvault Company.
#

import json

import requests


class ClumioException(Exception):
    """ClumioException is raised by all SDK APIs."""

    def __init__(self, reason: str, resp: requests.Response | None = None) -> None:
        """Constructor for the ClumioException class.

        Args:
            reason: The reason (or error message) for the Exception
                to be raised.
            resp: The response object from the API call that caused the exception.
        """
        resp_str = ''
        if resp is not None:
            resp_str = (
                f'HTTP Status Code: {resp.status_code}.\n'
                f'Reason: {resp.reason}.\n'
                f'Body: {json.dumps(json.loads(resp.text), indent=2, default=str)}'
            )
        super().__init__(f'{reason}\n{resp_str}')
