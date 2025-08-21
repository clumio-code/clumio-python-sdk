#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3BucketSizeRes')


class S3BucketSizeRes:
    """Implementation of the 'S3BucketSizeRes' model.

    The size breakdown in bytes with timestamps of a bucket per storage class.

    Attributes:
        deep_archive_object_overhead:
            Size of Deep Archive Object Overhead in bytes.
        deep_archive_object_overhead_retrieved_time:
            Timestamp when CloudWatch reported the Deep Archive Object Overhead size.
        deep_archive_s3_object_overhead:
            Size of Deep Archive S3 Object Overhead in bytes.
        deep_archive_s3_object_overhead_retrieved_time:
            Timestamp when CloudWatch reported the Deep Archive S3 Object Overhead size.
        deep_archive_staging_storage:
            Size of Deep Archive Staging Storage objects in bytes.
        deep_archive_staging_storage_retrieved_time:
            Timestamp when CloudWatch reported the Deep Archive Staging Storage objects
            size.
        deep_archive_storage:
            Size of Deep Archive Storage objects in bytes.
        deep_archive_storage_retrieved_time:
            Timestamp when CloudWatch reported the Deep Archive Storage objects size.
        glacier_instant_retrieval_storage:
            Size of Glacier Instant Retrieval Storage objects in bytes.
        glacier_instant_retrieval_storage_retrieved_time:
            Timestamp when CloudWatch reported the Glacier Instant Retrieval Storage objects
            size.
        glacier_object_overhead:
            Size of Glacier Object Overhead in bytes.
        glacier_object_overhead_retrieved_time:
            Timestamp when CloudWatch reported the Glacier Object Overhead size.
        glacier_s3_object_overhead:
            Size of Glacier S3 Object Overhead in bytes.
        glacier_s3_object_overhead_retrieved_time:
            Timestamp when CloudWatch reported the Glacier S3 Object Overhead size.
        glacier_staging_storage:
            Size of Glacier Staging Storage objects in bytes.
        glacier_staging_storage_retrieved_time:
            Timestamp when CloudWatch reported the Glacier Staging Storage objects size.
        glacier_storage:
            Size of Glacier Storage objects in bytes.
        glacier_storage_retrieved_time:
            Timestamp when CloudWatch reported the Glacier Storage objects size.
        intelligent_tiering_aa_storage:
            Size of Intelligent-Tiering AA Storage objects in bytes.
        intelligent_tiering_aa_storage_retrieved_time:
            Timestamp when CloudWatch reported the Intelligent-Tiering AA Storage objects
            size.
        intelligent_tiering_aia_storage:
            Size of Intelligent-Tiering AIA Storage objects in bytes.
        intelligent_tiering_aia_storage_retrieved_time:
            Timestamp when CloudWatch reported the Intelligent-Tiering AIA Storage objects
            size.
        intelligent_tiering_daa_storage:
            Size of Intelligent-Tiering DAA Storage objects in bytes.
        intelligent_tiering_daa_storage_retrieved_time:
            Timestamp when CloudWatch reported the Intelligent-Tiering DAA Storage objects
            size.
        intelligent_tiering_fa_storage:
            Size of Intelligent-Tiering FA Storage objects in bytes.
        intelligent_tiering_fa_storage_retrieved_time:
            Timestamp when CloudWatch reported the Intelligent-Tiering FA Storage objects
            size.
        intelligent_tiering_ia_storage:
            Size of Intelligent-Tiering IA Storage objects in bytes.
        intelligent_tiering_ia_storage_retrieved_time:
            Timestamp when CloudWatch reported the Intelligent-Tiering IA Storage objects
            size.
        one_zone_ia_size_overhead:
            Size of OneZone IA Overhead in bytes.
        one_zone_ia_size_overhead_retrieved_time:
            Timestamp when CloudWatch reported the OneZone IA Overhead size.
        one_zone_ia_storage:
            Size of OneZone IA Storage objects in bytes.
        one_zone_ia_storage_retrieved_time:
            Timestamp when CloudWatch reported the OneZone IA Storage objects size.
        reduced_redundancy_storage:
            Size of Reduced Redundancy Storage objects in bytes.
        reduced_redundancy_storage_retrieved_time:
            Timestamp when CloudWatch reported the Reduced Redundancy Storage objects size.
        standard_ia_object_overhead:
            Size of Standard IA Object Overhead in bytes.
        standard_ia_object_overhead_retrieved_time:
            Timestamp when CloudWatch reported the Standard IA Object Overhead size.
        standard_ia_size_overhead:
            Size of Standard IA Overhead in bytes.
        standard_ia_size_overhead_retrieved_time:
            Timestamp when CloudWatch reported the Standard IA Overhead size.
        standard_ia_storage:
            Size of Standard IA Storage objects in bytes.
        standard_ia_storage_retrieved_time:
            Timestamp when CloudWatch reported the Standard IA Storage objects size.
        standard_storage:
            Size of Standard Storage objects in bytes.
        standard_storage_retrieved_time:
            Timestamp when CloudWatch reported the Standard Storage objects size.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'deep_archive_object_overhead': 'deep_archive_object_overhead',
        'deep_archive_object_overhead_retrieved_time': 'deep_archive_object_overhead_retrieved_time',
        'deep_archive_s3_object_overhead': 'deep_archive_s3_object_overhead',
        'deep_archive_s3_object_overhead_retrieved_time': 'deep_archive_s3_object_overhead_retrieved_time',
        'deep_archive_staging_storage': 'deep_archive_staging_storage',
        'deep_archive_staging_storage_retrieved_time': 'deep_archive_staging_storage_retrieved_time',
        'deep_archive_storage': 'deep_archive_storage',
        'deep_archive_storage_retrieved_time': 'deep_archive_storage_retrieved_time',
        'glacier_instant_retrieval_storage': 'glacier_instant_retrieval_storage',
        'glacier_instant_retrieval_storage_retrieved_time': 'glacier_instant_retrieval_storage_retrieved_time',
        'glacier_object_overhead': 'glacier_object_overhead',
        'glacier_object_overhead_retrieved_time': 'glacier_object_overhead_retrieved_time',
        'glacier_s3_object_overhead': 'glacier_s3_object_overhead',
        'glacier_s3_object_overhead_retrieved_time': 'glacier_s3_object_overhead_retrieved_time',
        'glacier_staging_storage': 'glacier_staging_storage',
        'glacier_staging_storage_retrieved_time': 'glacier_staging_storage_retrieved_time',
        'glacier_storage': 'glacier_storage',
        'glacier_storage_retrieved_time': 'glacier_storage_retrieved_time',
        'intelligent_tiering_aa_storage': 'intelligent_tiering_aa_storage',
        'intelligent_tiering_aa_storage_retrieved_time': 'intelligent_tiering_aa_storage_retrieved_time',
        'intelligent_tiering_aia_storage': 'intelligent_tiering_aia_storage',
        'intelligent_tiering_aia_storage_retrieved_time': 'intelligent_tiering_aia_storage_retrieved_time',
        'intelligent_tiering_daa_storage': 'intelligent_tiering_daa_storage',
        'intelligent_tiering_daa_storage_retrieved_time': 'intelligent_tiering_daa_storage_retrieved_time',
        'intelligent_tiering_fa_storage': 'intelligent_tiering_fa_storage',
        'intelligent_tiering_fa_storage_retrieved_time': 'intelligent_tiering_fa_storage_retrieved_time',
        'intelligent_tiering_ia_storage': 'intelligent_tiering_ia_storage',
        'intelligent_tiering_ia_storage_retrieved_time': 'intelligent_tiering_ia_storage_retrieved_time',
        'one_zone_ia_size_overhead': 'one_zone_ia_size_overhead',
        'one_zone_ia_size_overhead_retrieved_time': 'one_zone_ia_size_overhead_retrieved_time',
        'one_zone_ia_storage': 'one_zone_ia_storage',
        'one_zone_ia_storage_retrieved_time': 'one_zone_ia_storage_retrieved_time',
        'reduced_redundancy_storage': 'reduced_redundancy_storage',
        'reduced_redundancy_storage_retrieved_time': 'reduced_redundancy_storage_retrieved_time',
        'standard_ia_object_overhead': 'standard_ia_object_overhead',
        'standard_ia_object_overhead_retrieved_time': 'standard_ia_object_overhead_retrieved_time',
        'standard_ia_size_overhead': 'standard_ia_size_overhead',
        'standard_ia_size_overhead_retrieved_time': 'standard_ia_size_overhead_retrieved_time',
        'standard_ia_storage': 'standard_ia_storage',
        'standard_ia_storage_retrieved_time': 'standard_ia_storage_retrieved_time',
        'standard_storage': 'standard_storage',
        'standard_storage_retrieved_time': 'standard_storage_retrieved_time',
    }

    def __init__(
        self,
        deep_archive_object_overhead: int | None = None,
        deep_archive_object_overhead_retrieved_time: str | None = None,
        deep_archive_s3_object_overhead: int | None = None,
        deep_archive_s3_object_overhead_retrieved_time: str | None = None,
        deep_archive_staging_storage: int | None = None,
        deep_archive_staging_storage_retrieved_time: str | None = None,
        deep_archive_storage: int | None = None,
        deep_archive_storage_retrieved_time: str | None = None,
        glacier_instant_retrieval_storage: int | None = None,
        glacier_instant_retrieval_storage_retrieved_time: str | None = None,
        glacier_object_overhead: int | None = None,
        glacier_object_overhead_retrieved_time: str | None = None,
        glacier_s3_object_overhead: int | None = None,
        glacier_s3_object_overhead_retrieved_time: str | None = None,
        glacier_staging_storage: int | None = None,
        glacier_staging_storage_retrieved_time: str | None = None,
        glacier_storage: int | None = None,
        glacier_storage_retrieved_time: str | None = None,
        intelligent_tiering_aa_storage: int | None = None,
        intelligent_tiering_aa_storage_retrieved_time: str | None = None,
        intelligent_tiering_aia_storage: int | None = None,
        intelligent_tiering_aia_storage_retrieved_time: str | None = None,
        intelligent_tiering_daa_storage: int | None = None,
        intelligent_tiering_daa_storage_retrieved_time: str | None = None,
        intelligent_tiering_fa_storage: int | None = None,
        intelligent_tiering_fa_storage_retrieved_time: str | None = None,
        intelligent_tiering_ia_storage: int | None = None,
        intelligent_tiering_ia_storage_retrieved_time: str | None = None,
        one_zone_ia_size_overhead: int | None = None,
        one_zone_ia_size_overhead_retrieved_time: str | None = None,
        one_zone_ia_storage: int | None = None,
        one_zone_ia_storage_retrieved_time: str | None = None,
        reduced_redundancy_storage: int | None = None,
        reduced_redundancy_storage_retrieved_time: str | None = None,
        standard_ia_object_overhead: int | None = None,
        standard_ia_object_overhead_retrieved_time: str | None = None,
        standard_ia_size_overhead: int | None = None,
        standard_ia_size_overhead_retrieved_time: str | None = None,
        standard_ia_storage: int | None = None,
        standard_ia_storage_retrieved_time: str | None = None,
        standard_storage: int | None = None,
        standard_storage_retrieved_time: str | None = None,
    ) -> None:
        """Constructor for the S3BucketSizeRes class."""

        # Initialize members of the class
        self.deep_archive_object_overhead: int | None = deep_archive_object_overhead
        self.deep_archive_object_overhead_retrieved_time: str | None = (
            deep_archive_object_overhead_retrieved_time
        )
        self.deep_archive_s3_object_overhead: int | None = deep_archive_s3_object_overhead
        self.deep_archive_s3_object_overhead_retrieved_time: str | None = (
            deep_archive_s3_object_overhead_retrieved_time
        )
        self.deep_archive_staging_storage: int | None = deep_archive_staging_storage
        self.deep_archive_staging_storage_retrieved_time: str | None = (
            deep_archive_staging_storage_retrieved_time
        )
        self.deep_archive_storage: int | None = deep_archive_storage
        self.deep_archive_storage_retrieved_time: str | None = deep_archive_storage_retrieved_time
        self.glacier_instant_retrieval_storage: int | None = glacier_instant_retrieval_storage
        self.glacier_instant_retrieval_storage_retrieved_time: str | None = (
            glacier_instant_retrieval_storage_retrieved_time
        )
        self.glacier_object_overhead: int | None = glacier_object_overhead
        self.glacier_object_overhead_retrieved_time: str | None = (
            glacier_object_overhead_retrieved_time
        )
        self.glacier_s3_object_overhead: int | None = glacier_s3_object_overhead
        self.glacier_s3_object_overhead_retrieved_time: str | None = (
            glacier_s3_object_overhead_retrieved_time
        )
        self.glacier_staging_storage: int | None = glacier_staging_storage
        self.glacier_staging_storage_retrieved_time: str | None = (
            glacier_staging_storage_retrieved_time
        )
        self.glacier_storage: int | None = glacier_storage
        self.glacier_storage_retrieved_time: str | None = glacier_storage_retrieved_time
        self.intelligent_tiering_aa_storage: int | None = intelligent_tiering_aa_storage
        self.intelligent_tiering_aa_storage_retrieved_time: str | None = (
            intelligent_tiering_aa_storage_retrieved_time
        )
        self.intelligent_tiering_aia_storage: int | None = intelligent_tiering_aia_storage
        self.intelligent_tiering_aia_storage_retrieved_time: str | None = (
            intelligent_tiering_aia_storage_retrieved_time
        )
        self.intelligent_tiering_daa_storage: int | None = intelligent_tiering_daa_storage
        self.intelligent_tiering_daa_storage_retrieved_time: str | None = (
            intelligent_tiering_daa_storage_retrieved_time
        )
        self.intelligent_tiering_fa_storage: int | None = intelligent_tiering_fa_storage
        self.intelligent_tiering_fa_storage_retrieved_time: str | None = (
            intelligent_tiering_fa_storage_retrieved_time
        )
        self.intelligent_tiering_ia_storage: int | None = intelligent_tiering_ia_storage
        self.intelligent_tiering_ia_storage_retrieved_time: str | None = (
            intelligent_tiering_ia_storage_retrieved_time
        )
        self.one_zone_ia_size_overhead: int | None = one_zone_ia_size_overhead
        self.one_zone_ia_size_overhead_retrieved_time: str | None = (
            one_zone_ia_size_overhead_retrieved_time
        )
        self.one_zone_ia_storage: int | None = one_zone_ia_storage
        self.one_zone_ia_storage_retrieved_time: str | None = one_zone_ia_storage_retrieved_time
        self.reduced_redundancy_storage: int | None = reduced_redundancy_storage
        self.reduced_redundancy_storage_retrieved_time: str | None = (
            reduced_redundancy_storage_retrieved_time
        )
        self.standard_ia_object_overhead: int | None = standard_ia_object_overhead
        self.standard_ia_object_overhead_retrieved_time: str | None = (
            standard_ia_object_overhead_retrieved_time
        )
        self.standard_ia_size_overhead: int | None = standard_ia_size_overhead
        self.standard_ia_size_overhead_retrieved_time: str | None = (
            standard_ia_size_overhead_retrieved_time
        )
        self.standard_ia_storage: int | None = standard_ia_storage
        self.standard_ia_storage_retrieved_time: str | None = standard_ia_storage_retrieved_time
        self.standard_storage: int | None = standard_storage
        self.standard_storage_retrieved_time: str | None = standard_storage_retrieved_time

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
