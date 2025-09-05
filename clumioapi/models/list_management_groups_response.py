#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import management_group_list_embedded as management_group_list_embedded_
from clumioapi.models import management_group_list_links as management_group_list_links_

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
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'current_count': 'current_count',
        'limit': 'limit',
        'min_count': 'min_count',
        'start': 'start',
    }

    def __init__(
        self,
        embedded: management_group_list_embedded_.ManagementGroupListEmbedded | None = None,
        links: management_group_list_links_.ManagementGroupListLinks | None = None,
        current_count: int | None = None,
        limit: int | None = None,
        min_count: int | None = None,
        start: str | None = None,
    ) -> None:
        """Constructor for the ListManagementGroupsResponse class."""

        # Initialize members of the class
        self.embedded: management_group_list_embedded_.ManagementGroupListEmbedded | None = embedded
        self.links: management_group_list_links_.ManagementGroupListLinks | None = links
        self.current_count: int | None = current_count
        self.limit: int | None = limit
        self.min_count: int | None = min_count
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
        val_embedded = management_group_list_embedded_.ManagementGroupListEmbedded.from_dictionary(
            val
        )

        val = dictionary.get('_links', None)
        val_links = management_group_list_links_.ManagementGroupListLinks.from_dictionary(val)

        val = dictionary.get('current_count', None)
        val_current_count = val

        val = dictionary.get('limit', None)
        val_limit = val

        val = dictionary.get('min_count', None)
        val_min_count = val

        val = dictionary.get('start', None)
        val_start = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_current_count,
            val_limit,
            val_min_count,
            val_start,
        )
