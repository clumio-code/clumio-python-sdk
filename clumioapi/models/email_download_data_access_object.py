#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='EmailDownloadDataAccessObject')


class EmailDownloadDataAccessObject:
    """Implementation of the 'EmailDownloadDataAccessObject' model.

    The details used to access the restored file, if it was shared by email. If
    therestored file was shared by direct download (and not email), then this field
    has avalue of `null`.

    Attributes:
        email_message:
            The optional message that was sent as part of the email.
        retrieved_by:
            The email address of the user who initiated the file level restore.
        retrieved_for:
            The email address of the user who the file was retrieved for.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'email_message': 'email_message',
        'retrieved_by': 'retrieved_by',
        'retrieved_for': 'retrieved_for',
    }

    def __init__(
        self, email_message: str = None, retrieved_by: str = None, retrieved_for: str = None
    ) -> None:
        """Constructor for the EmailDownloadDataAccessObject class."""

        # Initialize members of the class
        self.email_message: str = email_message
        self.retrieved_by: str = retrieved_by
        self.retrieved_for: str = retrieved_for

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
        email_message = dictionary.get('email_message')
        retrieved_by = dictionary.get('retrieved_by')
        retrieved_for = dictionary.get('retrieved_for')
        # Return an object of this model
        return cls(email_message, retrieved_by, retrieved_for)
