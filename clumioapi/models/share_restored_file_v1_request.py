#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ShareRestoredFileV1Request')


class ShareRestoredFileV1Request:
    """Implementation of the 'ShareRestoredFileV1Request' model.

    Attributes:
        email_address:
            The email address of the user who will receive the download link to the restored
            file.
        message:
            The optional message sent as part of the email.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'email_address': 'email_address', 'message': 'message'}

    def __init__(self, email_address: str | None = None, message: str | None = None) -> None:
        """Constructor for the ShareRestoredFileV1Request class."""

        # Initialize members of the class
        self.email_address: str | None = email_address
        self.message: str | None = message

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
        val = dictionary.get('email_address', None)
        val_email_address = val

        val = dictionary.get('message', None)
        val_message = val

        # Return an object of this model
        return cls(
            val_email_address,
            val_message,
        )
