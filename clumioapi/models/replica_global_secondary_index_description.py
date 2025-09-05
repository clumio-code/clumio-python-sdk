#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import on_demand_throughput_override as on_demand_throughput_override_
from clumioapi.models import provisioned_throughput_override as provisioned_throughput_override_

T = TypeVar('T', bound='ReplicaGlobalSecondaryIndexDescription')


class ReplicaGlobalSecondaryIndexDescription:
    """Implementation of the 'ReplicaGlobalSecondaryIndexDescription' model.

    Represents the properties of a replica global secondary index.

    Attributes:
        index_name:
            The name of the global secondary index.
        on_demand_throughput_override:
            Replica-specific ondemand throughput settings. If not specified, uses the source
            table's ondemand throughput settings.
        provisioned_throughput_override:
            Replica-specific provisioned throughput settings. If not specified, uses the
            source table's provisioned throughput settings.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'index_name': 'index_name',
        'on_demand_throughput_override': 'on_demand_throughput_override',
        'provisioned_throughput_override': 'provisioned_throughput_override',
    }

    def __init__(
        self,
        index_name: str | None = None,
        on_demand_throughput_override: (
            on_demand_throughput_override_.OnDemandThroughputOverride | None
        ) = None,
        provisioned_throughput_override: (
            provisioned_throughput_override_.ProvisionedThroughputOverride | None
        ) = None,
    ) -> None:
        """Constructor for the ReplicaGlobalSecondaryIndexDescription class."""

        # Initialize members of the class
        self.index_name: str | None = index_name
        self.on_demand_throughput_override: (
            on_demand_throughput_override_.OnDemandThroughputOverride | None
        ) = on_demand_throughput_override
        self.provisioned_throughput_override: (
            provisioned_throughput_override_.ProvisionedThroughputOverride | None
        ) = provisioned_throughput_override

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
        val = dictionary.get('index_name', None)
        val_index_name = val

        val = dictionary.get('on_demand_throughput_override', None)
        val_on_demand_throughput_override = (
            on_demand_throughput_override_.OnDemandThroughputOverride.from_dictionary(val)
        )

        val = dictionary.get('provisioned_throughput_override', None)
        val_provisioned_throughput_override = (
            provisioned_throughput_override_.ProvisionedThroughputOverride.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_index_name,
            val_on_demand_throughput_override,
            val_provisioned_throughput_override,
        )
