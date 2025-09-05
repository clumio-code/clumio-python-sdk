#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='EmailRecipientsDataAccessOption')


@dataclasses.dataclass
class EmailRecipientsDataAccessOption:
    """Implementation of the 'EmailRecipientsDataAccessOption' model.

        Specifies a download link (accessible via emails) as the restore target. If
        notspecified, `target` defaults to `direct_download`.

        Attributes:
            Message:
    The optional message sent as part of the email.

            RecipientEmails:
    The recipient email addresses who will receive the download link to the restored records.

    """

    Message: str | None = None
    RecipientEmails: Sequence[str] | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self,
            dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v not in [None, {}]},
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
