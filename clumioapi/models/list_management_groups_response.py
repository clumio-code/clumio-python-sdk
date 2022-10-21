#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import management_group_list_embedded, management_group_list_links

T = TypeVar('T', bound='ListManagementGroupsResponse')


class ListManagementGroupsResponse:
    """Implementation of the 'ListManagementGroupsResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        current_count:
            The number of items listed on the current page.
        limit:
            The maximum number of items displayed per page in the response.
        min_count:
            The total count of groups upto 10. Any number of groups beyond 10 will
            still be returned as 10.
        start:
            The page token used to get this response.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'current_count': 'current_count',
        'limit': 'limit',
        'min_count': 'min_count',
        'start': 'start',
    }

    def __init__(
        self,
        embedded: management_group_list_embedded.ManagementGroupListEmbedded = None,
        links: management_group_list_links.ManagementGroupListLinks = None,
        current_count: int = None,
        limit: int = None,
        min_count: int = None,
        start: str = None,
    ) -> None:
        """Constructor for the ListManagementGroupsResponse class."""

        # Initialize members of the class
        self.embedded: management_group_list_embedded.ManagementGroupListEmbedded = embedded
        self.links: management_group_list_links.ManagementGroupListLinks = links
        self.current_count: int = current_count
        self.limit: int = limit
        self.min_count: int = min_count
        self.start: str = start

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
        key = '_embedded'
        embedded = (
            management_group_list_embedded.ManagementGroupListEmbedded.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            management_group_list_links.ManagementGroupListLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        current_count = dictionary.get('current_count')
        limit = dictionary.get('limit')
        min_count = dictionary.get('min_count')
        start = dictionary.get('start')
        # Return an object of this model
        return cls(embedded, links, current_count, limit, min_count, start)
