#
# Copyright 2023. Clumio, Inc.
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
    _names = {'email_address': 'email_address', 'message': 'message'}

    def __init__(self, email_address: str = None, message: str = None) -> None:
        """Constructor for the ShareRestoredFileV1Request class."""

        # Initialize members of the class
        self.email_address: str = email_address
        self.message: str = message

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
        email_address = dictionary.get('email_address')
        message = dictionary.get('message')
        # Return an object of this model
        return cls(email_address, message)
