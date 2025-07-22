#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import file_system_list_embedded as file_system_list_embedded_
from clumioapi.models import file_system_list_links as file_system_list_links_

T = TypeVar('T', bound='ListFileSystemsResponse')


class ListFileSystemsResponse:
    """Implementation of the 'ListFileSystemsResponse' model.

    Attributes:
        embedded:
            _embedded contains the list of items of a file_system list query
        links:
            _links provides URLs to related navigable pages of a file_system list query
        current_count:
            The number of items listed on the current page.
        limit:
            The maximum number of items displayed per page in the response.
        start:
            The page number used to get this response.
            Pages are indexed starting from 1 (i.e., `"start": "1"`).
        total_count:
            The total number of items, summed across all pages.
        total_pages_count:
            The total number of pages of results.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'current_count': 'current_count',
        'limit': 'limit',
        'start': 'start',
        'total_count': 'total_count',
        'total_pages_count': 'total_pages_count',
    }

    def __init__(
        self,
        embedded: file_system_list_embedded_.FileSystemListEmbedded,
        links: file_system_list_links_.FileSystemListLinks,
        current_count: int,
        limit: int,
        start: str,
        total_count: int,
        total_pages_count: int,
    ) -> None:
        """Constructor for the ListFileSystemsResponse class."""

        # Initialize members of the class
        self.embedded: file_system_list_embedded_.FileSystemListEmbedded = embedded
        self.links: file_system_list_links_.FileSystemListLinks = links
        self.current_count: int = current_count
        self.limit: int = limit
        self.start: str = start
        self.total_count: int = total_count
        self.total_pages_count: int = total_pages_count

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

        # Extract variables from the dictionary
        val = dictionary['_embedded']
        val_embedded = file_system_list_embedded_.FileSystemListEmbedded.from_dictionary(val)

        val = dictionary['_links']
        val_links = file_system_list_links_.FileSystemListLinks.from_dictionary(val)

        val = dictionary['current_count']
        val_current_count = val

        val = dictionary['limit']
        val_limit = val

        val = dictionary['start']
        val_start = val

        val = dictionary['total_count']
        val_total_count = val

        val = dictionary['total_pages_count']
        val_total_pages_count = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_current_count,  # type: ignore
            val_limit,  # type: ignore
            val_start,  # type: ignore
            val_total_count,  # type: ignore
            val_total_pages_count,  # type: ignore
        )
