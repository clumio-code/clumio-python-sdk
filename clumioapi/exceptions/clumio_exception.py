#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, List, Mapping, Optional

from clumioapi import api_helper
from clumioapi.models import single_error_response


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
            context:  The HttpContext of the API call.
        """
        self.errors: List[single_error_response.SingleErrorResponse] = list()
        dictionary = api_helper.json_deserialize(errors)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)
        if len(self.errors) > 0:
            error_msgs: List[str] = [
                f'{str(i+1)}. {self.errors[i].error_message}\n' for i in range(len(self.errors))
            ]
            errors_string = ''.join(error_msgs)
            reason = f'{reason}\n{errors_string}'
        super().__init__(reason)

    def unbox(self, dictionary: Optional[Mapping[str, Any]]) -> None:
        """Populates the object properties by extracting them from dictionary.

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys MUST
                match property names in the API description.
        """
        if dictionary.get('errors'):
            for structure in dictionary.get('errors', {}):
                self.errors.append(
                    single_error_response.SingleErrorResponse.from_dictionary(structure)
                )
