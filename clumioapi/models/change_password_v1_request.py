#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ChangePasswordV1Request')


class ChangePasswordV1Request:
    """Implementation of the 'ChangePasswordV1Request' model.

    Attributes:
        current_password:
            The user's current password.
        new_password:
            The new password that is to replace the user's current password. Passwords must
            be between 14 and 64 characters
            and include the following: one uppercase character, one lowercase character, one
            number, and one special character.
            Spaces are not allowed.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'current_password': 'current_password',
        'new_password': 'new_password',
    }

    def __init__(
        self, current_password: str | None = None, new_password: str | None = None
    ) -> None:
        """Constructor for the ChangePasswordV1Request class."""

        # Initialize members of the class
        self.current_password: str | None = current_password
        self.new_password: str | None = new_password

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
        val = dictionary.get('current_password', None)
        val_current_password = val

        val = dictionary.get('new_password', None)
        val_new_password = val

        # Return an object of this model
        return cls(
            val_current_password,
            val_new_password,
        )
