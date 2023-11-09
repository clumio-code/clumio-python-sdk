#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import provisioned_throughput_override
from clumioapi.models import replica_global_secondary_index_description

T = TypeVar('T', bound='ReplicaDescription')


class ReplicaDescription:
    """Implementation of the 'ReplicaDescription' model.

    Contains the details of the replica.

    Attributes:
        global_secondary_indexes:
            The replica-specific global secondary index settings.
        kms_master_key_id:
            The AWS KMS key of the replica that will be used for AWS KMS encryption.
        provisioned_throughput_override:
            Replica-specific provisioned throughput settings. If not specified, uses the
            source table's provisioned throughput settings.
        region_name:
            The name of the Region.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'global_secondary_indexes': 'global_secondary_indexes',
        'kms_master_key_id': 'kms_master_key_id',
        'provisioned_throughput_override': 'provisioned_throughput_override',
        'region_name': 'region_name',
    }

    def __init__(
        self,
        global_secondary_indexes: Sequence[
            replica_global_secondary_index_description.ReplicaGlobalSecondaryIndexDescription
        ] = None,
        kms_master_key_id: str = None,
        provisioned_throughput_override: provisioned_throughput_override.ProvisionedThroughputOverride = None,
        region_name: str = None,
    ) -> None:
        """Constructor for the ReplicaDescription class."""

        # Initialize members of the class
        self.global_secondary_indexes: Sequence[
            replica_global_secondary_index_description.ReplicaGlobalSecondaryIndexDescription
        ] = global_secondary_indexes
        self.kms_master_key_id: str = kms_master_key_id
        self.provisioned_throughput_override: provisioned_throughput_override.ProvisionedThroughputOverride = (
            provisioned_throughput_override
        )
        self.region_name: str = region_name

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
        global_secondary_indexes = None
        if dictionary.get('global_secondary_indexes'):
            global_secondary_indexes = list()
            for value in dictionary.get('global_secondary_indexes'):
                global_secondary_indexes.append(
                    replica_global_secondary_index_description.ReplicaGlobalSecondaryIndexDescription.from_dictionary(
                        value
                    )
                )

        kms_master_key_id = dictionary.get('kms_master_key_id')
        key = 'provisioned_throughput_override'
        p_provisioned_throughput_override = (
            provisioned_throughput_override.ProvisionedThroughputOverride.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        region_name = dictionary.get('region_name')
        # Return an object of this model
        return cls(
            global_secondary_indexes,
            kms_master_key_id,
            p_provisioned_throughput_override,
            region_name,
        )
