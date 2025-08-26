#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import download_shared_file_links as download_shared_file_links_
import requests

T = TypeVar('T', bound='DownloadSharedFileResponse')


@dataclasses.dataclass
class DownloadSharedFileResponse:
    """Implementation of the 'DownloadSharedFileResponse' model.

        Attributes:
            Links:
                Urls to pages related to the resource.

            DownloadUrl:
                A download link that lets you directly download the file. the link expires
    24 hours after file restore.

    """

    Links: download_shared_file_links_.DownloadSharedFileLinks | None = None
    DownloadUrl: str | None = None
    raw_response: Optional[requests.Response] = None

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
        val = dictionary.get('_links', None)
        val_links = download_shared_file_links_.DownloadSharedFileLinks.from_dictionary(val)

        val = dictionary.get('download_url', None)
        val_download_url = val

        # Return an object of this model
        return cls(
            val_links,
            val_download_url,
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
        model_instance.raw_response = response
        return model_instance
