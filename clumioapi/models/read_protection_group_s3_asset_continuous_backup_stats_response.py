#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    protection_group_bucket_continuous_backup_stats as \
    protection_group_bucket_continuous_backup_stats_
from clumioapi.models import \
    protection_group_bucket_continuous_backup_stats_links as \
    protection_group_bucket_continuous_backup_stats_links_
import requests

T = TypeVar('T', bound='ReadProtectionGroupS3AssetContinuousBackupStatsResponse')


@dataclasses.dataclass
class ReadProtectionGroupS3AssetContinuousBackupStatsResponse:
    """Implementation of the 'ReadProtectionGroupS3AssetContinuousBackupStatsResponse' model.

        Attributes:
            Links:
                Protectiongroupbucketcontinuousbackupstatslinks
    urls to pages related to the resources.

            Bins:
                The list of continuous backup statistics grouped by the given time interval.

            TotalStats:
                Protectiongroupbucketcontinuousbackupstats.

    """

    Links: (
        protection_group_bucket_continuous_backup_stats_links_.ProtectionGroupBucketContinuousBackupStatsLinks
        | None
    ) = None
    Bins: (
        Sequence[
            protection_group_bucket_continuous_backup_stats_.ProtectionGroupBucketContinuousBackupStats
        ]
        | None
    ) = None
    TotalStats: (
        protection_group_bucket_continuous_backup_stats_.ProtectionGroupBucketContinuousBackupStats
        | None
    ) = None
    raw_response: Optional[requests.Response] = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
        val = dictionary.get('_links', None)
        val_links = protection_group_bucket_continuous_backup_stats_links_.ProtectionGroupBucketContinuousBackupStatsLinks.from_dictionary(
            val
        )

        val = dictionary.get('bins', None)

        val_bins = []
        if val:
            for value in val:
                val_bins.append(
                    protection_group_bucket_continuous_backup_stats_.ProtectionGroupBucketContinuousBackupStats.from_dictionary(
                        value
                    )
                )

        val = dictionary.get('total_stats', None)
        val_total_stats = protection_group_bucket_continuous_backup_stats_.ProtectionGroupBucketContinuousBackupStats.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_links,
            val_bins,
            val_total_stats,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        model_instance.raw_response = response
        return model_instance
