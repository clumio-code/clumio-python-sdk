#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import download_shared_file_links as download_shared_file_links_

T = TypeVar('T', bound='DownloadSharedFileResponse')


class DownloadSharedFileResponse:
    """Implementation of the 'DownloadSharedFileResponse' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        download_url:
            A download link that lets you directly download the file. The link expires
            24 hours after file restore.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'links': '_links', 'download_url': 'download_url'}

    def __init__(
        self,
        links: download_shared_file_links_.DownloadSharedFileLinks | None = None,
        download_url: str | None = None,
    ) -> None:
        """Constructor for the DownloadSharedFileResponse class."""

        # Initialize members of the class
        self.links: download_shared_file_links_.DownloadSharedFileLinks | None = links
        self.download_url: str | None = download_url

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
        val = dictionary.get('_links', None)
        val_links = download_shared_file_links_.DownloadSharedFileLinks.from_dictionary(val)

        val = dictionary.get('download_url', None)
        val_download_url = val

        # Return an object of this model
        return cls(
            val_links,
            val_download_url,
        )
