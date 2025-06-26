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
    _names = {'message': 'message', 'recipient_emails': 'recipient_emails'}

    def __init__(self, message: str = None, recipient_emails: Sequence[str] = None) -> None:
        """Constructor for the EmailRecipientsDataAccessOption class."""

        # Initialize members of the class
        self.message: str = message
        self.recipient_emails: Sequence[str] = recipient_emails

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
        message = dictionary.get('message')
        recipient_emails = dictionary.get('recipient_emails')
        # Return an object of this model
        return cls(message, recipient_emails)
