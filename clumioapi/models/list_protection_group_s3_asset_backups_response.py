#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import (
    protection_group_s3_asset_backup_list_embedded,
    protection_group_s3_asset_backup_list_links,
)

T = TypeVar('T', bound='ListProtectionGroupS3AssetBackupsResponse')


class ListProtectionGroupS3AssetBackupsResponse:
    """Implementation of the 'ListProtectionGroupS3AssetBackupsResponse' model.

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
        embedded: protection_group_s3_asset_backup_list_embedded.ProtectionGroupS3AssetBackupListEmbedded = None,
        links: protection_group_s3_asset_backup_list_links.ProtectionGroupS3AssetBackupListLinks = None,
        current_count: int = None,
        filter_applied: str = None,
        limit: int = None,
        start: str = None,
        total_count: int = None,
        total_pages_count: int = None,
    ) -> None:
        """Constructor for the ListProtectionGroupS3AssetBackupsResponse class."""

        # Initialize members of the class
        self.embedded: protection_group_s3_asset_backup_list_embedded.ProtectionGroupS3AssetBackupListEmbedded = (
            embedded
        )
        self.links: protection_group_s3_asset_backup_list_links.ProtectionGroupS3AssetBackupListLinks = (
            links
        )
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
            protection_group_s3_asset_backup_list_embedded.ProtectionGroupS3AssetBackupListEmbedded.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            protection_group_s3_asset_backup_list_links.ProtectionGroupS3AssetBackupListLinks.from_dictionary(
                dictionary.get(key)
            )
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
