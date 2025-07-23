#
# Copyright 2023. Clumio, A Commvault Company.
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
    _names: dict[str, str] = {
        'email_message': 'email_message',
        'retrieved_by': 'retrieved_by',
        'retrieved_for': 'retrieved_for',
    }

    def __init__(
        self,
        email_message: str | None = None,
        retrieved_by: str | None = None,
        retrieved_for: str | None = None,
    ) -> None:
        """Constructor for the EmailDownloadDataAccessObject class."""

        # Initialize members of the class
        self.email_message: str | None = email_message
        self.retrieved_by: str | None = retrieved_by
        self.retrieved_for: str | None = retrieved_for

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
        val = dictionary.get('email_message', None)
        val_email_message = val

        val = dictionary.get('retrieved_by', None)
        val_retrieved_by = val

        val = dictionary.get('retrieved_for', None)
        val_retrieved_for = val

        # Return an object of this model
        return cls(
            val_email_message,
            val_retrieved_by,
            val_retrieved_for,
        )
