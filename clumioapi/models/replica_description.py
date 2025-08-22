#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import on_demand_throughput_override as on_demand_throughput_override_
from clumioapi.models import provisioned_throughput_override as provisioned_throughput_override_
from clumioapi.models import \
    replica_global_secondary_index_description as replica_global_secondary_index_description_

T = TypeVar('T', bound='ReplicaDescription')


class ReplicaDescription:
    """Implementation of the 'ReplicaDescription' model.

    Contains the details of the replica.

    Attributes:
        global_secondary_indexes:
            The replica-specific global secondary index settings.
        kms_master_key_id:
            The AWS KMS key of the replica that will be used for AWS KMS encryption.
        on_demand_throughput_override:
            Replica-specific ondemand throughput settings. If not specified, uses the source
            table's ondemand throughput settings.
        provisioned_throughput_override:
            Replica-specific provisioned throughput settings. If not specified, uses the
            source table's provisioned throughput settings.
        region_name:
            The name of the Region.
        replica_table_class:
            Replica-specific table class summary.
            Possible values are `STANDARD` or `STANDARD_INFREQUENT_ACCESS`. This is
            defaulted to the
            `STANDARD` storage class if empty.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'global_secondary_indexes': 'global_secondary_indexes',
        'kms_master_key_id': 'kms_master_key_id',
        'on_demand_throughput_override': 'on_demand_throughput_override',
        'provisioned_throughput_override': 'provisioned_throughput_override',
        'region_name': 'region_name',
        'replica_table_class': 'replica_table_class',
    }

    def __init__(
        self,
        global_secondary_indexes: (
            Sequence[
                replica_global_secondary_index_description_.ReplicaGlobalSecondaryIndexDescription
            ]
            | None
        ) = None,
        kms_master_key_id: str | None = None,
        on_demand_throughput_override: (
            on_demand_throughput_override_.OnDemandThroughputOverride | None
        ) = None,
        provisioned_throughput_override: (
            provisioned_throughput_override_.ProvisionedThroughputOverride | None
        ) = None,
        region_name: str | None = None,
        replica_table_class: str | None = None,
    ) -> None:
        """Constructor for the ReplicaDescription class."""

        # Initialize members of the class
        self.global_secondary_indexes: (
            Sequence[
                replica_global_secondary_index_description_.ReplicaGlobalSecondaryIndexDescription
            ]
            | None
        ) = global_secondary_indexes
        self.kms_master_key_id: str | None = kms_master_key_id
        self.on_demand_throughput_override: (
            on_demand_throughput_override_.OnDemandThroughputOverride | None
        ) = on_demand_throughput_override
        self.provisioned_throughput_override: (
            provisioned_throughput_override_.ProvisionedThroughputOverride | None
        ) = provisioned_throughput_override
        self.region_name: str | None = region_name
        self.replica_table_class: str | None = replica_table_class

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
        val = dictionary.get('global_secondary_indexes', None)

        val_global_secondary_indexes = None
        if val:
            val_global_secondary_indexes = list()
            for value in val:
                val_global_secondary_indexes.append(
                    replica_global_secondary_index_description_.ReplicaGlobalSecondaryIndexDescription.from_dictionary(
                        value
                    )
                )

        val = dictionary.get('kms_master_key_id', None)
        val_kms_master_key_id = val

        val = dictionary.get('on_demand_throughput_override', None)
        val_on_demand_throughput_override = (
            on_demand_throughput_override_.OnDemandThroughputOverride.from_dictionary(val)
        )

        val = dictionary.get('provisioned_throughput_override', None)
        val_provisioned_throughput_override = (
            provisioned_throughput_override_.ProvisionedThroughputOverride.from_dictionary(val)
        )

        val = dictionary.get('region_name', None)
        val_region_name = val

        val = dictionary.get('replica_table_class', None)
        val_replica_table_class = val

        # Return an object of this model
        return cls(
            val_global_secondary_indexes,
            val_kms_master_key_id,
            val_on_demand_throughput_override,
            val_provisioned_throughput_override,
            val_region_name,
            val_replica_table_class,
        )
