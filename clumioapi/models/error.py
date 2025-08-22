#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import single_error_response as single_error_response_

T = TypeVar('T', bound='Error')


class Error:
    """Implementation of the 'Error' model.

    Error

    Attributes:
        errors:
            A list of errors encountered during runtime.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'errors': 'errors'}

    def __init__(
        self, errors: Sequence[single_error_response_.SingleErrorResponse] | None = None
    ) -> None:
        """Constructor for the Error class."""

        # Initialize members of the class
        self.errors: Sequence[single_error_response_.SingleErrorResponse] | None = errors

    @classmethod
    def from_dictionary(cls: Type[T], dictionary: Mapping[str, Any]) -> T:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('errors', None)

        val_errors = None
        if val:
            val_errors = list()
            for value in val:
                val_errors.append(single_error_response_.SingleErrorResponse.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_errors,
        )
