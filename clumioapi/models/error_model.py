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
    _names = {'error_code': 'error_code', 'error_message': 'error_message'}

    def __init__(self, error_code: str = None, error_message: str = None) -> None:
        """Constructor for the ErrorModel class."""

        # Initialize members of the class
        self.error_code: str = error_code
        self.error_message: str = error_message

    @classmethod
    def from_dictionary(cls: Type, dictionary: Mapping[str, Any]) -> Optional[T]:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """
        if not dictionary:
            return None

        # Extract variables from the dictionary
        error_code = dictionary.get('error_code')
        error_message = dictionary.get('error_message')
        # Return an object of this model
        return cls(error_code, error_message)
