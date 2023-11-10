#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import protection_group_bucket_continuous_backup_stats
from clumioapi.models import protection_group_bucket_continuous_backup_stats_links

T = TypeVar('T', bound='ReadProtectionGroupS3AssetContinuousBackupStatsResponse')


class ReadProtectionGroupS3AssetContinuousBackupStatsResponse:
    """Implementation of the 'ReadProtectionGroupS3AssetContinuousBackupStatsResponse' model.

    Attributes:
        links:
            ProtectionGroupBucketContinuousBackupStatsLinks
            URLs to pages related to the resources.
        bins:
            The list of continuous backup statistics grouped by the given time interval.
        total_stats:
            ProtectionGroupBucketContinuousBackupStats
    """

    # Create a mapping from Model property names to API property names
    _names = {'links': '_links', 'bins': 'bins', 'total_stats': 'total_stats'}

    def __init__(
        self,
        links: protection_group_bucket_continuous_backup_stats_links.ProtectionGroupBucketContinuousBackupStatsLinks = None,
        bins: Sequence[
            protection_group_bucket_continuous_backup_stats.ProtectionGroupBucketContinuousBackupStats
        ] = None,
        total_stats: protection_group_bucket_continuous_backup_stats.ProtectionGroupBucketContinuousBackupStats = None,
    ) -> None:
        """Constructor for the ReadProtectionGroupS3AssetContinuousBackupStatsResponse class."""

        # Initialize members of the class
        self.links: protection_group_bucket_continuous_backup_stats_links.ProtectionGroupBucketContinuousBackupStatsLinks = (
            links
        )
        self.bins: Sequence[
            protection_group_bucket_continuous_backup_stats.ProtectionGroupBucketContinuousBackupStats
        ] = bins
        self.total_stats: protection_group_bucket_continuous_backup_stats.ProtectionGroupBucketContinuousBackupStats = (
            total_stats
        )

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
        key = '_links'
        links = (
            protection_group_bucket_continuous_backup_stats_links.ProtectionGroupBucketContinuousBackupStatsLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        bins = None
        if dictionary.get('bins'):
            bins = list()
            for value in dictionary.get('bins'):
                bins.append(
                    protection_group_bucket_continuous_backup_stats.ProtectionGroupBucketContinuousBackupStats.from_dictionary(
                        value
                    )
                )

        key = 'total_stats'
        total_stats = (
            protection_group_bucket_continuous_backup_stats.ProtectionGroupBucketContinuousBackupStats.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(links, bins, total_stats)
