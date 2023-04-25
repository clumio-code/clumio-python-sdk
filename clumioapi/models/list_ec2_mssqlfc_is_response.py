#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_mssqlfci_list_embedded
from clumioapi.models import ec2_mssqlfci_list_links

T = TypeVar('T', bound='ListEC2MSSQLFCIsResponse')


class ListEC2MSSQLFCIsResponse:
    """Implementation of the 'ListEC2MSSQLFCIsResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        current_count:
            The number of items listed on the current page.
        filter_applied:
            The filter used in the request. The filter includes both manually-specified and
            system-generated filters.
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
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'current_count': 'current_count',
        'filter_applied': 'filter_applied',
        'limit': 'limit',
        'start': 'start',
        'total_count': 'total_count',
        'total_pages_count': 'total_pages_count',
    }

    def __init__(
        self,
        embedded: ec2_mssqlfci_list_embedded.EC2MSSQLFCIListEmbedded = None,
        links: ec2_mssqlfci_list_links.EC2MSSQLFCIListLinks = None,
        current_count: int = None,
        filter_applied: str = None,
        limit: int = None,
        start: str = None,
        total_count: int = None,
        total_pages_count: int = None,
    ) -> None:
        """Constructor for the ListEC2MSSQLFCIsResponse class."""

        # Initialize members of the class
        self.embedded: ec2_mssqlfci_list_embedded.EC2MSSQLFCIListEmbedded = embedded
        self.links: ec2_mssqlfci_list_links.EC2MSSQLFCIListLinks = links
        self.current_count: int = current_count
        self.filter_applied: str = filter_applied
        self.limit: int = limit
        self.start: str = start
        self.total_count: int = total_count
        self.total_pages_count: int = total_pages_count

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
            ec2_mssqlfci_list_embedded.EC2MSSQLFCIListEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            ec2_mssqlfci_list_links.EC2MSSQLFCIListLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        current_count = dictionary.get('current_count')
        filter_applied = dictionary.get('filter_applied')
        limit = dictionary.get('limit')
        start = dictionary.get('start')
        total_count = dictionary.get('total_count')
        total_pages_count = dictionary.get('total_pages_count')
        # Return an object of this model
        return cls(
            embedded,
            links,
            current_count,
            filter_applied,
            limit,
            start,
            total_count,
            total_pages_count,
        )