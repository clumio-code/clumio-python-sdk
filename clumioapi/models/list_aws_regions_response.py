#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import connection_region_list_embedded
from clumioapi.models import connection_region_list_links

T = TypeVar('T', bound='ListAWSRegionsResponse')


class ListAWSRegionsResponse:
    """Implementation of the 'ListAWSRegionsResponse' model.

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
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'current_count': 'current_count',
        'limit': 'limit',
        'start': 'start',
    }

    def __init__(
        self,
        embedded: connection_region_list_embedded.ConnectionRegionListEmbedded = None,
        links: connection_region_list_links.ConnectionRegionListLinks = None,
        current_count: int = None,
        limit: int = None,
        start: str = None,
    ) -> None:
        """Constructor for the ListAWSRegionsResponse class."""

        # Initialize members of the class
        self.embedded: connection_region_list_embedded.ConnectionRegionListEmbedded = embedded
        self.links: connection_region_list_links.ConnectionRegionListLinks = links
        self.current_count: int = current_count
        self.limit: int = limit
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
            connection_region_list_embedded.ConnectionRegionListEmbedded.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            connection_region_list_links.ConnectionRegionListLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        current_count = dictionary.get('current_count')
        limit = dictionary.get('limit')
        start = dictionary.get('start')
        # Return an object of this model
        return cls(embedded, links, current_count, limit, start)
