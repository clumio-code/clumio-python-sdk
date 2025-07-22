#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    protection_group_bucket_continuous_backup_stats as \
    protection_group_bucket_continuous_backup_stats_
from clumioapi.models import \
    protection_group_bucket_continuous_backup_stats_links as \
    protection_group_bucket_continuous_backup_stats_links_

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
    _names: dict[str, str] = {'links': '_links', 'bins': 'bins', 'total_stats': 'total_stats'}

    def __init__(
        self,
        links: protection_group_bucket_continuous_backup_stats_links_.ProtectionGroupBucketContinuousBackupStatsLinks,
        bins: Sequence[
            protection_group_bucket_continuous_backup_stats_.ProtectionGroupBucketContinuousBackupStats
        ],
        total_stats: protection_group_bucket_continuous_backup_stats_.ProtectionGroupBucketContinuousBackupStats,
    ) -> None:
        """Constructor for the ReadProtectionGroupS3AssetContinuousBackupStatsResponse class."""

        # Initialize members of the class
        self.links: (
            protection_group_bucket_continuous_backup_stats_links_.ProtectionGroupBucketContinuousBackupStatsLinks
        ) = links
        self.bins: Sequence[
            protection_group_bucket_continuous_backup_stats_.ProtectionGroupBucketContinuousBackupStats
        ] = bins
        self.total_stats: (
            protection_group_bucket_continuous_backup_stats_.ProtectionGroupBucketContinuousBackupStats
        ) = total_stats

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
        val = dictionary['_links']
        val_links = protection_group_bucket_continuous_backup_stats_links_.ProtectionGroupBucketContinuousBackupStatsLinks.from_dictionary(
            val
        )

        val = dictionary['bins']

        val_bins = None
        if val:
            val_bins = list()
            for value in val:
                val_bins.append(
                    protection_group_bucket_continuous_backup_stats_.ProtectionGroupBucketContinuousBackupStats.from_dictionary(
                        value
                    )
                )

        val = dictionary['total_stats']
        val_total_stats = protection_group_bucket_continuous_backup_stats_.ProtectionGroupBucketContinuousBackupStats.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_links,  # type: ignore
            val_bins,  # type: ignore
            val_total_stats,  # type: ignore
        )
