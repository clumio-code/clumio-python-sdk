#
# Copyright 2023. Clumio, Inc.
#

import json
from typing import Any


class ClumioException(Exception):
    """ClumioException is raised by all SDK APIs.

    Attributes:
        response_code: The status code of the response.
        context: The HttpContext of the API call.
    """

    def __init__(self, reason: str, errors: Any) -> None:
        """Constructor for the ClumioException class.

        Args:
            reason: The reason (or error message) for the Exception
                to be raised.
            errors:  Errors.
        """
        
        if errors is not None:
            errors_str = json.dumps(errors, indent=2, default=str)
        else:
            errors_str = "None"
        super().__init__(f'ClumioException: {reason}, errors: {errors_str}')
