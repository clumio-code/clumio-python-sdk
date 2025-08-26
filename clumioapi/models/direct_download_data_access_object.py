#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='DirectDownloadDataAccessObject')


@dataclasses.dataclass
class DirectDownloadDataAccessObject:
    """Implementation of the 'DirectDownloadDataAccessObject' model.

    The details used to access the restored file if it was shared by direct
    download. Ifthe restored file was shared by email (and not by direct download),
    then this fieldhas a value of `null`.

    Attributes:
        DownloadLink:
            The download link used to access the restored file through direct download.

        RetrievedBy:
            The email address of the user who initiated the file level restore.

    """

    DownloadLink: str | None = None
    RetrievedBy: str | None = None

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
        val = dictionary.get('download_link', None)
        val_download_link = val

        val = dictionary.get('retrieved_by', None)
        val_retrieved_by = val

        # Return an object of this model
        return cls(
            val_download_link,
            val_retrieved_by,
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
