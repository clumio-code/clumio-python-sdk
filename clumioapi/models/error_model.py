#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ErrorModel')


class ErrorModel:
    """Implementation of the 'ErrorModel' model.

    Attributes:
        error_code:
            ErrorCode is a short string describing the error, if any.
        error_message:
            ErrorMessage is a longer description explaining the error, if any, and how to
            fix it.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'error_code': 'error_code', 'error_message': 'error_message'}

    def __init__(self, error_code: str | None = None, error_message: str | None = None) -> None:
        """Constructor for the ErrorModel class."""

        # Initialize members of the class
        self.error_code: str | None = error_code
        self.error_message: str | None = error_message

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
        val = dictionary.get('error_code', None)
        val_error_code = val

        val = dictionary.get('error_message', None)
        val_error_message = val

        # Return an object of this model
        return cls(
            val_error_code,
            val_error_message,
        )
