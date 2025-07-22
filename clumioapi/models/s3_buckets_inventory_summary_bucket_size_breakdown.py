#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3BucketsInventorySummaryBucketSizeBreakdown')


class S3BucketsInventorySummaryBucketSizeBreakdown:
    """Implementation of the 'S3BucketsInventorySummaryBucketSizeBreakdown' model.

    The total size breakdown of S3 buckets in bytes per storage class. This
    parameter aggregates relevant fields from cloudwatch_metrics >
    size_bytes_per_storage_class

    Attributes:
        glacier_deep_archive_storage_bytes:
            Size of Glacier Deep Archive Storage in bytes.
        glacier_flexible_retrieval_storage_bytes:
            Size of Glacier Flexible Retrieval Storage in bytes.
        glacier_instant_retrieval_storage_bytes:
            Size of Glacier Instant Retrieval Storage in bytes.
        intelligent_tiering_storage_bytes:
            Size of Intelligent-Tiering Storage objects in bytes.
        one_zone_ia_storage_bytes:
            Size of OneZone-IA Storage in bytes.
        reduced_redundancy_storage_bytes:
            Size of Reduced Redundancy Storage in bytes.
        standard_ia_storage_bytes:
            Size of Standard-IA Storage in bytes.
        standard_storage_bytes:
            Size of Standard Storage in bytes.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'glacier_deep_archive_storage_bytes': 'glacier_deep_archive_storage_bytes',
        'glacier_flexible_retrieval_storage_bytes': 'glacier_flexible_retrieval_storage_bytes',
        'glacier_instant_retrieval_storage_bytes': 'glacier_instant_retrieval_storage_bytes',
        'intelligent_tiering_storage_bytes': 'intelligent_tiering_storage_bytes',
        'one_zone_ia_storage_bytes': 'one_zone_ia_storage_bytes',
        'reduced_redundancy_storage_bytes': 'reduced_redundancy_storage_bytes',
        'standard_ia_storage_bytes': 'standard_ia_storage_bytes',
        'standard_storage_bytes': 'standard_storage_bytes',
    }

    def __init__(
        self,
        glacier_deep_archive_storage_bytes: int,
        glacier_flexible_retrieval_storage_bytes: int,
        glacier_instant_retrieval_storage_bytes: int,
        intelligent_tiering_storage_bytes: int,
        one_zone_ia_storage_bytes: int,
        reduced_redundancy_storage_bytes: int,
        standard_ia_storage_bytes: int,
        standard_storage_bytes: int,
    ) -> None:
        """Constructor for the S3BucketsInventorySummaryBucketSizeBreakdown class."""

        # Initialize members of the class
        self.glacier_deep_archive_storage_bytes: int = glacier_deep_archive_storage_bytes
        self.glacier_flexible_retrieval_storage_bytes: int = (
            glacier_flexible_retrieval_storage_bytes
        )
        self.glacier_instant_retrieval_storage_bytes: int = glacier_instant_retrieval_storage_bytes
        self.intelligent_tiering_storage_bytes: int = intelligent_tiering_storage_bytes
        self.one_zone_ia_storage_bytes: int = one_zone_ia_storage_bytes
        self.reduced_redundancy_storage_bytes: int = reduced_redundancy_storage_bytes
        self.standard_ia_storage_bytes: int = standard_ia_storage_bytes
        self.standard_storage_bytes: int = standard_storage_bytes

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
        val = dictionary['glacier_deep_archive_storage_bytes']
        val_glacier_deep_archive_storage_bytes = val

        val = dictionary['glacier_flexible_retrieval_storage_bytes']
        val_glacier_flexible_retrieval_storage_bytes = val

        val = dictionary['glacier_instant_retrieval_storage_bytes']
        val_glacier_instant_retrieval_storage_bytes = val

        val = dictionary['intelligent_tiering_storage_bytes']
        val_intelligent_tiering_storage_bytes = val

        val = dictionary['one_zone_ia_storage_bytes']
        val_one_zone_ia_storage_bytes = val

        val = dictionary['reduced_redundancy_storage_bytes']
        val_reduced_redundancy_storage_bytes = val

        val = dictionary['standard_ia_storage_bytes']
        val_standard_ia_storage_bytes = val

        val = dictionary['standard_storage_bytes']
        val_standard_storage_bytes = val

        # Return an object of this model
        return cls(
            val_glacier_deep_archive_storage_bytes,  # type: ignore
            val_glacier_flexible_retrieval_storage_bytes,  # type: ignore
            val_glacier_instant_retrieval_storage_bytes,  # type: ignore
            val_intelligent_tiering_storage_bytes,  # type: ignore
            val_one_zone_ia_storage_bytes,  # type: ignore
            val_reduced_redundancy_storage_bytes,  # type: ignore
            val_standard_ia_storage_bytes,  # type: ignore
            val_standard_storage_bytes,  # type: ignore
        )
