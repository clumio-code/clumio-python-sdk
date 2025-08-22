#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='UpdateUserProfileV1Request')


class UpdateUserProfileV1Request:
    """Implementation of the 'UpdateUserProfileV1Request' model.

    Attributes:
        full_name:
            The full name of the user that is to replace the existing full name.
            For example, enter the user's first name and last name.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'full_name': 'full_name'}

    def __init__(self, full_name: str | None = None) -> None:
        """Constructor for the UpdateUserProfileV1Request class."""

        # Initialize members of the class
        self.full_name: str | None = full_name

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
        val = dictionary.get('full_name', None)
        val_full_name = val

        # Return an object of this model
        return cls(
            val_full_name,
        )
