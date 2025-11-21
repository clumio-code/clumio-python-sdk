#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='EmailDownloadDataAccessOption')


@dataclasses.dataclass
class EmailDownloadDataAccessOption:
    """Implementation of the 'EmailDownloadDataAccessOption' model.

    Specifies a download link (accessible via email) as the restore target. If
    notspecified, `target` defaults to `direct_download`. If you specify `email`,
    alsosend the user the passcode that gets generated from this request (see
    `passcode` inthe response). After the user clicks the download link, they must
    enter thepasscode to access the files.

    Attributes:
        EmailAddress:
            The email address of the user who will receive the download link to the restored
            file.

        Message:
            The optional message sent as part of the email.

    """

    EmailAddress: str | None = None
    Message: str | None = None

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
        val = dictionary.get('email_address', None)
        val_email_address = val

        val = dictionary.get('message', None)
        val_message = val

        # Return an object of this model
        return cls(
            val_email_address,
            val_message,
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
