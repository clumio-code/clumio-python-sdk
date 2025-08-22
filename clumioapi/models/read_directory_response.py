#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import directory_browse_embedded as directory_browse_embedded_
from clumioapi.models import directory_browse_links as directory_browse_links_

T = TypeVar('T', bound='ReadDirectoryResponse')


class ReadDirectoryResponse:
    """Implementation of the 'ReadDirectoryResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        current_count:
            The number of items listed on the current page.
        limit:
            The maximum number of items displayed per page in the response.
        start:
            The page token used to get this response.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'current_count': 'current_count',
        'limit': 'limit',
        'start': 'start',
    }

    def __init__(
        self,
        embedded: directory_browse_embedded_.DirectoryBrowseEmbedded | None = None,
        links: directory_browse_links_.DirectoryBrowseLinks | None = None,
        current_count: int | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> None:
        """Constructor for the ReadDirectoryResponse class."""

        # Initialize members of the class
        self.embedded: directory_browse_embedded_.DirectoryBrowseEmbedded | None = embedded
        self.links: directory_browse_links_.DirectoryBrowseLinks | None = links
        self.current_count: int | None = current_count
        self.limit: int | None = limit
        self.start: str | None = start

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
        val = dictionary.get('_embedded', None)
        val_embedded = directory_browse_embedded_.DirectoryBrowseEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = directory_browse_links_.DirectoryBrowseLinks.from_dictionary(val)

        val = dictionary.get('current_count', None)
        val_current_count = val

        val = dictionary.get('limit', None)
        val_limit = val

        val = dictionary.get('start', None)
        val_start = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_current_count,
            val_limit,
            val_start,
        )
