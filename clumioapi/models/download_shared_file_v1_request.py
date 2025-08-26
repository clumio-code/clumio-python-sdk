#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='DownloadSharedFileV1Request')


@dataclasses.dataclass
class DownloadSharedFileV1Request:
    """Implementation of the 'DownloadSharedFileV1Request' model.

        Attributes:
            EmailLink:
                The download link that was sent to you by email. to get the download link,
    open the email message, click "download file" to launch the clumio "access
    requested file" page, and copy the url.

            Passcode:
                The passcode used to access the restored file. obtain the passcode from the
    user who generated the restored file.

    """

    EmailLink: str | None = None
    Passcode: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
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
        val = dictionary.get('email_link', None)
        val_email_link = val

        val = dictionary.get('passcode', None)
        val_passcode = val

        # Return an object of this model
        return cls(
            val_email_link,
            val_passcode,
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
