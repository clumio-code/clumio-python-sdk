#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='EmailDownloadDataAccessObject')


@dataclasses.dataclass
class EmailDownloadDataAccessObject:
    """Implementation of the 'EmailDownloadDataAccessObject' model.

    The details used to access the restored file, if it was shared by email. If
    therestored file was shared by direct download (and not email), then this field
    has avalue of `null`.

    Attributes:
        EmailMessage:
            The optional message that was sent as part of the email.

        RetrievedBy:
            The email address of the user who initiated the file level restore.

        RetrievedFor:
            The email address of the user who the file was retrieved for.

    """

    EmailMessage: str | None = None
    RetrievedBy: str | None = None
    RetrievedFor: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
