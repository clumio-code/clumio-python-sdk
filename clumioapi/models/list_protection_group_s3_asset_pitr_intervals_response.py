#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import protection_group_s3_asset_pitr_interval_list_embedded
from clumioapi.models import protection_group_s3_asset_pitr_interval_list_links

T = TypeVar('T', bound='ListProtectionGroupS3AssetPitrIntervalsResponse')


class ListProtectionGroupS3AssetPitrIntervalsResponse:
    """Implementation of the 'ListProtectionGroupS3AssetPitrIntervalsResponse' model.

    ListProtectionGroupS3AssetPitrIntervalsResponse represents the success response

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
            The page token used to get this response.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'current_count': 'current_count',
        'filter_applied': 'filter_applied',
        'limit': 'limit',
        'start': 'start',
    }

    def __init__(
        self,
        embedded: protection_group_s3_asset_pitr_interval_list_embedded.ProtectionGroupS3AssetPitrIntervalListEmbedded = None,
        links: protection_group_s3_asset_pitr_interval_list_links.ProtectionGroupS3AssetPitrIntervalListLinks = None,
        current_count: int = None,
        filter_applied: str = None,
        limit: int = None,
        start: str = None,
    ) -> None:
        """Constructor for the ListProtectionGroupS3AssetPitrIntervalsResponse class."""

        # Initialize members of the class
        self.embedded: (
            protection_group_s3_asset_pitr_interval_list_embedded.ProtectionGroupS3AssetPitrIntervalListEmbedded
        ) = embedded
        self.links: (
            protection_group_s3_asset_pitr_interval_list_links.ProtectionGroupS3AssetPitrIntervalListLinks
        ) = links
        self.current_count: int = current_count
        self.filter_applied: str = filter_applied
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
        val_embedded = (
            protection_group_s3_asset_pitr_interval_list_embedded.ProtectionGroupS3AssetPitrIntervalListEmbedded.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = '_links'
        val_links = (
            protection_group_s3_asset_pitr_interval_list_links.ProtectionGroupS3AssetPitrIntervalListLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        val_current_count = dictionary.get('current_count')
        val_filter_applied = dictionary.get('filter_applied')
        val_limit = dictionary.get('limit')
        val_start = dictionary.get('start')
        # Return an object of this model
        return cls(
            val_embedded, val_links, val_current_count, val_filter_applied, val_limit, val_start
        )
