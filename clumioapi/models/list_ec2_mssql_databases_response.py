#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_mssql_database_list_embedded as ec2_mssql_database_list_embedded_
from clumioapi.models import ec2_mssql_database_list_links as ec2_mssql_database_list_links_

T = TypeVar('T', bound='ListEC2MSSQLDatabasesResponse')


class ListEC2MSSQLDatabasesResponse:
    """Implementation of the 'ListEC2MSSQLDatabasesResponse' model.

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
    _names: dict[str, str] = {
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
        embedded: ec2_mssql_database_list_embedded_.EC2MSSQLDatabaseListEmbedded,
        links: ec2_mssql_database_list_links_.EC2MSSQLDatabaseListLinks,
        current_count: int,
        filter_applied: str,
        limit: int,
        start: str,
        total_count: int,
        total_pages_count: int,
    ) -> None:
        """Constructor for the ListEC2MSSQLDatabasesResponse class."""

        # Initialize members of the class
        self.embedded: ec2_mssql_database_list_embedded_.EC2MSSQLDatabaseListEmbedded = embedded
        self.links: ec2_mssql_database_list_links_.EC2MSSQLDatabaseListLinks = links
        self.current_count: int = current_count
        self.filter_applied: str = filter_applied
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
        val_embedded = (
            ec2_mssql_database_list_embedded_.EC2MSSQLDatabaseListEmbedded.from_dictionary(val)
        )

        val = dictionary['_links']
        val_links = ec2_mssql_database_list_links_.EC2MSSQLDatabaseListLinks.from_dictionary(val)

        val = dictionary['current_count']
        val_current_count = val

        val = dictionary['filter_applied']
        val_filter_applied = val

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
            val_filter_applied,  # type: ignore
            val_limit,  # type: ignore
            val_start,  # type: ignore
            val_total_count,  # type: ignore
            val_total_pages_count,  # type: ignore
        )
