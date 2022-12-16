#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import download_shared_file_links

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
    _names = {'links': '_links', 'download_url': 'download_url'}

    def __init__(
        self,
        links: download_shared_file_links.DownloadSharedFileLinks = None,
        download_url: str = None,
    ) -> None:
        """Constructor for the DownloadSharedFileResponse class."""

        # Initialize members of the class
        self.links: download_shared_file_links.DownloadSharedFileLinks = links
        self.download_url: str = download_url

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
        key = '_links'
        links = (
            download_shared_file_links.DownloadSharedFileLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        download_url = dictionary.get('download_url')
        # Return an object of this model
        return cls(links, download_url)
