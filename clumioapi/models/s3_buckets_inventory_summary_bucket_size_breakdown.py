#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='S3BucketsInventorySummaryBucketSizeBreakdown')


@dataclasses.dataclass
class S3BucketsInventorySummaryBucketSizeBreakdown:
    """Implementation of the 'S3BucketsInventorySummaryBucketSizeBreakdown' model.

    The total size breakdown of S3 buckets in bytes per storage class. This
    parameter aggregates relevant fields from cloudwatch_metrics >
    size_bytes_per_storage_class

    Attributes:
        GlacierDeepArchiveStorageBytes:
            Size of glacier deep archive storage in bytes.

        GlacierFlexibleRetrievalStorageBytes:
            Size of glacier flexible retrieval storage in bytes.

        GlacierInstantRetrievalStorageBytes:
            Size of glacier instant retrieval storage in bytes.

        IntelligentTieringStorageBytes:
            Size of intelligent-tiering storage objects in bytes.

        OneZoneIaStorageBytes:
            Size of onezone-ia storage in bytes.

        ReducedRedundancyStorageBytes:
            Size of reduced redundancy storage in bytes.

        StandardIaStorageBytes:
            Size of standard-ia storage in bytes.

        StandardStorageBytes:
            Size of standard storage in bytes.

    """

    GlacierDeepArchiveStorageBytes: int | None = None
    GlacierFlexibleRetrievalStorageBytes: int | None = None
    GlacierInstantRetrievalStorageBytes: int | None = None
    IntelligentTieringStorageBytes: int | None = None
    OneZoneIaStorageBytes: int | None = None
    ReducedRedundancyStorageBytes: int | None = None
    StandardIaStorageBytes: int | None = None
    StandardStorageBytes: int | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('glacier_deep_archive_storage_bytes', None)
        val_glacier_deep_archive_storage_bytes = val

        val = dictionary.get('glacier_flexible_retrieval_storage_bytes', None)
        val_glacier_flexible_retrieval_storage_bytes = val

        val = dictionary.get('glacier_instant_retrieval_storage_bytes', None)
        val_glacier_instant_retrieval_storage_bytes = val

        val = dictionary.get('intelligent_tiering_storage_bytes', None)
        val_intelligent_tiering_storage_bytes = val

        val = dictionary.get('one_zone_ia_storage_bytes', None)
        val_one_zone_ia_storage_bytes = val

        val = dictionary.get('reduced_redundancy_storage_bytes', None)
        val_reduced_redundancy_storage_bytes = val

        val = dictionary.get('standard_ia_storage_bytes', None)
        val_standard_ia_storage_bytes = val

        val = dictionary.get('standard_storage_bytes', None)
        val_standard_storage_bytes = val

        # Return an object of this model
        return cls(
            val_glacier_deep_archive_storage_bytes,
            val_glacier_flexible_retrieval_storage_bytes,
            val_glacier_instant_retrieval_storage_bytes,
            val_intelligent_tiering_storage_bytes,
            val_one_zone_ia_storage_bytes,
            val_reduced_redundancy_storage_bytes,
            val_standard_ia_storage_bytes,
            val_standard_storage_bytes,
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
        return model_instance
