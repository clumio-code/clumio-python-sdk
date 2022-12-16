#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import provisioned_throughput_override

T = TypeVar('T', bound='ReplicaGlobalSecondaryIndexDescription')


class ReplicaGlobalSecondaryIndexDescription:
    """Implementation of the 'ReplicaGlobalSecondaryIndexDescription' model.

    Represents the properties of a replica global secondary index.

    Attributes:
        index_name:
            The name of the global secondary index.
        provisioned_throughput_override:
            Replica-specific provisioned throughput settings. If not specified, uses the
            source table's provisioned throughput settings.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'index_name': 'index_name',
        'provisioned_throughput_override': 'provisioned_throughput_override',
    }

    def __init__(
        self,
        index_name: str = None,
        provisioned_throughput_override: provisioned_throughput_override.ProvisionedThroughputOverride = None,
    ) -> None:
        """Constructor for the ReplicaGlobalSecondaryIndexDescription class."""

        # Initialize members of the class
        self.index_name: str = index_name
        self.provisioned_throughput_override: provisioned_throughput_override.ProvisionedThroughputOverride = (
            provisioned_throughput_override
        )

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
        index_name = dictionary.get('index_name')
        key = 'provisioned_throughput_override'
        p_provisioned_throughput_override = (
            provisioned_throughput_override.ProvisionedThroughputOverride.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(index_name, p_provisioned_throughput_override)
