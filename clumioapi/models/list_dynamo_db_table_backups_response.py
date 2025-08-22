#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    dynamo_db_table_backup_list_embedded as dynamo_db_table_backup_list_embedded_
from clumioapi.models import dynamo_db_table_backup_list_links as dynamo_db_table_backup_list_links_

T = TypeVar('T', bound='ListDynamoDBTableBackupsResponse')


class ListDynamoDBTableBackupsResponse:
    """Implementation of the 'ListDynamoDBTableBackupsResponse' model.

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
        embedded: (
            dynamo_db_table_backup_list_embedded_.DynamoDBTableBackupListEmbedded | None
        ) = None,
        links: dynamo_db_table_backup_list_links_.DynamoDBTableBackupListLinks | None = None,
        current_count: int | None = None,
        filter_applied: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        total_count: int | None = None,
        total_pages_count: int | None = None,
    ) -> None:
        """Constructor for the ListDynamoDBTableBackupsResponse class."""

        # Initialize members of the class
        self.embedded: (
            dynamo_db_table_backup_list_embedded_.DynamoDBTableBackupListEmbedded | None
        ) = embedded
        self.links: dynamo_db_table_backup_list_links_.DynamoDBTableBackupListLinks | None = links
        self.current_count: int | None = current_count
        self.filter_applied: str | None = filter_applied
        self.limit: int | None = limit
        self.start: str | None = start
        self.total_count: int | None = total_count
        self.total_pages_count: int | None = total_pages_count

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
        val_embedded = (
            dynamo_db_table_backup_list_embedded_.DynamoDBTableBackupListEmbedded.from_dictionary(
                val
            )
        )

        val = dictionary.get('_links', None)
        val_links = dynamo_db_table_backup_list_links_.DynamoDBTableBackupListLinks.from_dictionary(
            val
        )

        val = dictionary.get('current_count', None)
        val_current_count = val

        val = dictionary.get('filter_applied', None)
        val_filter_applied = val

        val = dictionary.get('limit', None)
        val_limit = val

        val = dictionary.get('start', None)
        val_start = val

        val = dictionary.get('total_count', None)
        val_total_count = val

        val = dictionary.get('total_pages_count', None)
        val_total_pages_count = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_current_count,
            val_filter_applied,
            val_limit,
            val_start,
            val_total_count,
            val_total_pages_count,
        )
