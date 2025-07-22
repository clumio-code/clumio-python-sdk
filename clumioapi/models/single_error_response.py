#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='SingleErrorResponse')


class SingleErrorResponse:
    """Implementation of the 'SingleErrorResponse' model.

    Attributes:
        error_code:

        error_message:
            The reason for the error.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'error_code': 'error_code', 'error_message': 'error_message'}

    def __init__(self, error_code: int, error_message: str) -> None:
        """Constructor for the SingleErrorResponse class."""

        # Initialize members of the class
        self.error_code: int = error_code
        self.error_message: str = error_message

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

        # Extract variables from the dictionary
        val = dictionary['error_code']
        val_error_code = val

        val = dictionary['error_message']
        val_error_message = val

        # Return an object of this model
        return cls(
            val_error_code,  # type: ignore
            val_error_message,  # type: ignore
        )
