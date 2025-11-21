#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='S3BucketSizeRes')


@dataclasses.dataclass
class S3BucketSizeRes:
    """Implementation of the 'S3BucketSizeRes' model.

    The size breakdown in bytes with timestamps of a bucket per storage class.

    Attributes:
        DeepArchiveObjectOverhead:
            Size of deep archive object overhead in bytes.

        DeepArchiveObjectOverheadRetrievedTime:
            Timestamp when cloudwatch reported the deep archive object overhead size.

        DeepArchiveS3ObjectOverhead:
            Size of deep archive s3 object overhead in bytes.

        DeepArchiveS3ObjectOverheadRetrievedTime:
            Timestamp when cloudwatch reported the deep archive s3 object overhead size.

        DeepArchiveStagingStorage:
            Size of deep archive staging storage objects in bytes.

        DeepArchiveStagingStorageRetrievedTime:
            Timestamp when cloudwatch reported the deep archive staging storage objects
            size.

        DeepArchiveStorage:
            Size of deep archive storage objects in bytes.

        DeepArchiveStorageRetrievedTime:
            Timestamp when cloudwatch reported the deep archive storage objects size.

        GlacierInstantRetrievalStorage:
            Size of glacier instant retrieval storage objects in bytes.

        GlacierInstantRetrievalStorageRetrievedTime:
            Timestamp when cloudwatch reported the glacier instant retrieval storage objects
            size.

        GlacierObjectOverhead:
            Size of glacier object overhead in bytes.

        GlacierObjectOverheadRetrievedTime:
            Timestamp when cloudwatch reported the glacier object overhead size.

        GlacierS3ObjectOverhead:
            Size of glacier s3 object overhead in bytes.

        GlacierS3ObjectOverheadRetrievedTime:
            Timestamp when cloudwatch reported the glacier s3 object overhead size.

        GlacierStagingStorage:
            Size of glacier staging storage objects in bytes.

        GlacierStagingStorageRetrievedTime:
            Timestamp when cloudwatch reported the glacier staging storage objects size.

        GlacierStorage:
            Size of glacier storage objects in bytes.

        GlacierStorageRetrievedTime:
            Timestamp when cloudwatch reported the glacier storage objects size.

        IntelligentTieringAaStorage:
            Size of intelligent-tiering aa storage objects in bytes.

        IntelligentTieringAaStorageRetrievedTime:
            Timestamp when cloudwatch reported the intelligent-tiering aa storage objects
            size.

        IntelligentTieringAiaStorage:
            Size of intelligent-tiering aia storage objects in bytes.

        IntelligentTieringAiaStorageRetrievedTime:
            Timestamp when cloudwatch reported the intelligent-tiering aia storage objects
            size.

        IntelligentTieringDaaStorage:
            Size of intelligent-tiering daa storage objects in bytes.

        IntelligentTieringDaaStorageRetrievedTime:
            Timestamp when cloudwatch reported the intelligent-tiering daa storage objects
            size.

        IntelligentTieringFaStorage:
            Size of intelligent-tiering fa storage objects in bytes.

        IntelligentTieringFaStorageRetrievedTime:
            Timestamp when cloudwatch reported the intelligent-tiering fa storage objects
            size.

        IntelligentTieringIaStorage:
            Size of intelligent-tiering ia storage objects in bytes.

        IntelligentTieringIaStorageRetrievedTime:
            Timestamp when cloudwatch reported the intelligent-tiering ia storage objects
            size.

        OneZoneIaSizeOverhead:
            Size of onezone ia overhead in bytes.

        OneZoneIaSizeOverheadRetrievedTime:
            Timestamp when cloudwatch reported the onezone ia overhead size.

        OneZoneIaStorage:
            Size of onezone ia storage objects in bytes.

        OneZoneIaStorageRetrievedTime:
            Timestamp when cloudwatch reported the onezone ia storage objects size.

        ReducedRedundancyStorage:
            Size of reduced redundancy storage objects in bytes.

        ReducedRedundancyStorageRetrievedTime:
            Timestamp when cloudwatch reported the reduced redundancy storage objects size.

        StandardIaObjectOverhead:
            Size of standard ia object overhead in bytes.

        StandardIaObjectOverheadRetrievedTime:
            Timestamp when cloudwatch reported the standard ia object overhead size.

        StandardIaSizeOverhead:
            Size of standard ia overhead in bytes.

        StandardIaSizeOverheadRetrievedTime:
            Timestamp when cloudwatch reported the standard ia overhead size.

        StandardIaStorage:
            Size of standard ia storage objects in bytes.

        StandardIaStorageRetrievedTime:
            Timestamp when cloudwatch reported the standard ia storage objects size.

        StandardStorage:
            Size of standard storage objects in bytes.

        StandardStorageRetrievedTime:
            Timestamp when cloudwatch reported the standard storage objects size.

    """

    DeepArchiveObjectOverhead: int | None = None
    DeepArchiveObjectOverheadRetrievedTime: str | None = None
    DeepArchiveS3ObjectOverhead: int | None = None
    DeepArchiveS3ObjectOverheadRetrievedTime: str | None = None
    DeepArchiveStagingStorage: int | None = None
    DeepArchiveStagingStorageRetrievedTime: str | None = None
    DeepArchiveStorage: int | None = None
    DeepArchiveStorageRetrievedTime: str | None = None
    GlacierInstantRetrievalStorage: int | None = None
    GlacierInstantRetrievalStorageRetrievedTime: str | None = None
    GlacierObjectOverhead: int | None = None
    GlacierObjectOverheadRetrievedTime: str | None = None
    GlacierS3ObjectOverhead: int | None = None
    GlacierS3ObjectOverheadRetrievedTime: str | None = None
    GlacierStagingStorage: int | None = None
    GlacierStagingStorageRetrievedTime: str | None = None
    GlacierStorage: int | None = None
    GlacierStorageRetrievedTime: str | None = None
    IntelligentTieringAaStorage: int | None = None
    IntelligentTieringAaStorageRetrievedTime: str | None = None
    IntelligentTieringAiaStorage: int | None = None
    IntelligentTieringAiaStorageRetrievedTime: str | None = None
    IntelligentTieringDaaStorage: int | None = None
    IntelligentTieringDaaStorageRetrievedTime: str | None = None
    IntelligentTieringFaStorage: int | None = None
    IntelligentTieringFaStorageRetrievedTime: str | None = None
    IntelligentTieringIaStorage: int | None = None
    IntelligentTieringIaStorageRetrievedTime: str | None = None
    OneZoneIaSizeOverhead: int | None = None
    OneZoneIaSizeOverheadRetrievedTime: str | None = None
    OneZoneIaStorage: int | None = None
    OneZoneIaStorageRetrievedTime: str | None = None
    ReducedRedundancyStorage: int | None = None
    ReducedRedundancyStorageRetrievedTime: str | None = None
    StandardIaObjectOverhead: int | None = None
    StandardIaObjectOverheadRetrievedTime: str | None = None
    StandardIaSizeOverhead: int | None = None
    StandardIaSizeOverheadRetrievedTime: str | None = None
    StandardIaStorage: int | None = None
    StandardIaStorageRetrievedTime: str | None = None
    StandardStorage: int | None = None
    StandardStorageRetrievedTime: str | None = None

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
        val = dictionary.get('deep_archive_object_overhead', None)
        val_deep_archive_object_overhead = val

        val = dictionary.get('deep_archive_object_overhead_retrieved_time', None)
        val_deep_archive_object_overhead_retrieved_time = val

        val = dictionary.get('deep_archive_s3_object_overhead', None)
        val_deep_archive_s3_object_overhead = val

        val = dictionary.get('deep_archive_s3_object_overhead_retrieved_time', None)
        val_deep_archive_s3_object_overhead_retrieved_time = val

        val = dictionary.get('deep_archive_staging_storage', None)
        val_deep_archive_staging_storage = val

        val = dictionary.get('deep_archive_staging_storage_retrieved_time', None)
        val_deep_archive_staging_storage_retrieved_time = val

        val = dictionary.get('deep_archive_storage', None)
        val_deep_archive_storage = val

        val = dictionary.get('deep_archive_storage_retrieved_time', None)
        val_deep_archive_storage_retrieved_time = val

        val = dictionary.get('glacier_instant_retrieval_storage', None)
        val_glacier_instant_retrieval_storage = val

        val = dictionary.get('glacier_instant_retrieval_storage_retrieved_time', None)
        val_glacier_instant_retrieval_storage_retrieved_time = val

        val = dictionary.get('glacier_object_overhead', None)
        val_glacier_object_overhead = val

        val = dictionary.get('glacier_object_overhead_retrieved_time', None)
        val_glacier_object_overhead_retrieved_time = val

        val = dictionary.get('glacier_s3_object_overhead', None)
        val_glacier_s3_object_overhead = val

        val = dictionary.get('glacier_s3_object_overhead_retrieved_time', None)
        val_glacier_s3_object_overhead_retrieved_time = val

        val = dictionary.get('glacier_staging_storage', None)
        val_glacier_staging_storage = val

        val = dictionary.get('glacier_staging_storage_retrieved_time', None)
        val_glacier_staging_storage_retrieved_time = val

        val = dictionary.get('glacier_storage', None)
        val_glacier_storage = val

        val = dictionary.get('glacier_storage_retrieved_time', None)
        val_glacier_storage_retrieved_time = val

        val = dictionary.get('intelligent_tiering_aa_storage', None)
        val_intelligent_tiering_aa_storage = val

        val = dictionary.get('intelligent_tiering_aa_storage_retrieved_time', None)
        val_intelligent_tiering_aa_storage_retrieved_time = val

        val = dictionary.get('intelligent_tiering_aia_storage', None)
        val_intelligent_tiering_aia_storage = val

        val = dictionary.get('intelligent_tiering_aia_storage_retrieved_time', None)
        val_intelligent_tiering_aia_storage_retrieved_time = val

        val = dictionary.get('intelligent_tiering_daa_storage', None)
        val_intelligent_tiering_daa_storage = val

        val = dictionary.get('intelligent_tiering_daa_storage_retrieved_time', None)
        val_intelligent_tiering_daa_storage_retrieved_time = val

        val = dictionary.get('intelligent_tiering_fa_storage', None)
        val_intelligent_tiering_fa_storage = val

        val = dictionary.get('intelligent_tiering_fa_storage_retrieved_time', None)
        val_intelligent_tiering_fa_storage_retrieved_time = val

        val = dictionary.get('intelligent_tiering_ia_storage', None)
        val_intelligent_tiering_ia_storage = val

        val = dictionary.get('intelligent_tiering_ia_storage_retrieved_time', None)
        val_intelligent_tiering_ia_storage_retrieved_time = val

        val = dictionary.get('one_zone_ia_size_overhead', None)
        val_one_zone_ia_size_overhead = val

        val = dictionary.get('one_zone_ia_size_overhead_retrieved_time', None)
        val_one_zone_ia_size_overhead_retrieved_time = val

        val = dictionary.get('one_zone_ia_storage', None)
        val_one_zone_ia_storage = val

        val = dictionary.get('one_zone_ia_storage_retrieved_time', None)
        val_one_zone_ia_storage_retrieved_time = val

        val = dictionary.get('reduced_redundancy_storage', None)
        val_reduced_redundancy_storage = val

        val = dictionary.get('reduced_redundancy_storage_retrieved_time', None)
        val_reduced_redundancy_storage_retrieved_time = val

        val = dictionary.get('standard_ia_object_overhead', None)
        val_standard_ia_object_overhead = val

        val = dictionary.get('standard_ia_object_overhead_retrieved_time', None)
        val_standard_ia_object_overhead_retrieved_time = val

        val = dictionary.get('standard_ia_size_overhead', None)
        val_standard_ia_size_overhead = val

        val = dictionary.get('standard_ia_size_overhead_retrieved_time', None)
        val_standard_ia_size_overhead_retrieved_time = val

        val = dictionary.get('standard_ia_storage', None)
        val_standard_ia_storage = val

        val = dictionary.get('standard_ia_storage_retrieved_time', None)
        val_standard_ia_storage_retrieved_time = val

        val = dictionary.get('standard_storage', None)
        val_standard_storage = val

        val = dictionary.get('standard_storage_retrieved_time', None)
        val_standard_storage_retrieved_time = val

        # Return an object of this model
        return cls(
            val_deep_archive_object_overhead,
            val_deep_archive_object_overhead_retrieved_time,
            val_deep_archive_s3_object_overhead,
            val_deep_archive_s3_object_overhead_retrieved_time,
            val_deep_archive_staging_storage,
            val_deep_archive_staging_storage_retrieved_time,
            val_deep_archive_storage,
            val_deep_archive_storage_retrieved_time,
            val_glacier_instant_retrieval_storage,
            val_glacier_instant_retrieval_storage_retrieved_time,
            val_glacier_object_overhead,
            val_glacier_object_overhead_retrieved_time,
            val_glacier_s3_object_overhead,
            val_glacier_s3_object_overhead_retrieved_time,
            val_glacier_staging_storage,
            val_glacier_staging_storage_retrieved_time,
            val_glacier_storage,
            val_glacier_storage_retrieved_time,
            val_intelligent_tiering_aa_storage,
            val_intelligent_tiering_aa_storage_retrieved_time,
            val_intelligent_tiering_aia_storage,
            val_intelligent_tiering_aia_storage_retrieved_time,
            val_intelligent_tiering_daa_storage,
            val_intelligent_tiering_daa_storage_retrieved_time,
            val_intelligent_tiering_fa_storage,
            val_intelligent_tiering_fa_storage_retrieved_time,
            val_intelligent_tiering_ia_storage,
            val_intelligent_tiering_ia_storage_retrieved_time,
            val_one_zone_ia_size_overhead,
            val_one_zone_ia_size_overhead_retrieved_time,
            val_one_zone_ia_storage,
            val_one_zone_ia_storage_retrieved_time,
            val_reduced_redundancy_storage,
            val_reduced_redundancy_storage_retrieved_time,
            val_standard_ia_object_overhead,
            val_standard_ia_object_overhead_retrieved_time,
            val_standard_ia_size_overhead,
            val_standard_ia_size_overhead_retrieved_time,
            val_standard_ia_storage,
            val_standard_ia_storage_retrieved_time,
            val_standard_storage,
            val_standard_storage_retrieved_time,
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
