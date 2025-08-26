#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import on_demand_throughput_override as on_demand_throughput_override_
from clumioapi.models import provisioned_throughput_override as provisioned_throughput_override_
from clumioapi.models import \
    replica_global_secondary_index_description as replica_global_secondary_index_description_
import requests

T = TypeVar('T', bound='ReplicaDescription')


@dataclasses.dataclass
class ReplicaDescription:
    """Implementation of the 'ReplicaDescription' model.

        Contains the details of the replica.

        Attributes:
            GlobalSecondaryIndexes:
                The replica-specific global secondary index settings.

            KmsMasterKeyId:
                The aws kms key of the replica that will be used for aws kms encryption.

            OnDemandThroughputOverride:
                Replica-specific ondemand throughput settings. if not specified, uses the source table's ondemand throughput settings.

            ProvisionedThroughputOverride:
                Replica-specific provisioned throughput settings. if not specified, uses the source table's provisioned throughput settings.

            RegionName:
                The name of the region.

            ReplicaTableClass:
                Replica-specific table class summary.
    possible values are `standard` or `standard_infrequent_access`. this is defaulted to the
    `standard` storage class if empty.

    """

    GlobalSecondaryIndexes: (
        Sequence[replica_global_secondary_index_description_.ReplicaGlobalSecondaryIndexDescription]
        | None
    ) = None
    KmsMasterKeyId: str | None = None
    OnDemandThroughputOverride: on_demand_throughput_override_.OnDemandThroughputOverride | None = (
        None
    )
    ProvisionedThroughputOverride: (
        provisioned_throughput_override_.ProvisionedThroughputOverride | None
    ) = None
    RegionName: str | None = None
    ReplicaTableClass: str | None = None

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
        val = dictionary.get('global_secondary_indexes', None)

        val_global_secondary_indexes = []
        if val:
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
