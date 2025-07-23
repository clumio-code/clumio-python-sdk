#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='EmailRecipientsDataAccessOption')


class EmailRecipientsDataAccessOption:
    """Implementation of the 'EmailRecipientsDataAccessOption' model.

    Specifies a download link (accessible via emails) as the restore target. If
    notspecified, `target` defaults to `direct_download`.

    Attributes:
        message:
            The optional message sent as part of the email.
        recipient_emails:
            The recipient email addresses who will receive the download link to the restored
            records.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'message': 'message', 'recipient_emails': 'recipient_emails'}

    def __init__(
        self, message: str | None = None, recipient_emails: Sequence[str] | None = None
    ) -> None:
        """Constructor for the EmailRecipientsDataAccessOption class."""

        # Initialize members of the class
        self.message: str | None = message
        self.recipient_emails: Sequence[str] | None = recipient_emails

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
        val = dictionary.get('message', None)
        val_message = val

        val = dictionary.get('recipient_emails', None)
        val_recipient_emails = val

        # Return an object of this model
        return cls(
            val_message,
            val_recipient_emails,
        )
