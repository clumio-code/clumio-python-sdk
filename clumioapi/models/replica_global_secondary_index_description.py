#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import on_demand_throughput_override as on_demand_throughput_override_
from clumioapi.models import provisioned_throughput_override as provisioned_throughput_override_
import requests

T = TypeVar('T', bound='ReplicaGlobalSecondaryIndexDescription')


@dataclasses.dataclass
class ReplicaGlobalSecondaryIndexDescription:
    """Implementation of the 'ReplicaGlobalSecondaryIndexDescription' model.

    Represents the properties of a replica global secondary index.

    Attributes:
        IndexName:
            The name of the global secondary index.

        OnDemandThroughputOverride:
            Replica-specific ondemand throughput settings. if not specified, uses the source table's ondemand throughput settings.

        ProvisionedThroughputOverride:
            Replica-specific provisioned throughput settings. if not specified, uses the source table's provisioned throughput settings.

    """

    IndexName: str | None = None
    OnDemandThroughputOverride: on_demand_throughput_override_.OnDemandThroughputOverride | None = (
        None
    )
    ProvisionedThroughputOverride: (
        provisioned_throughput_override_.ProvisionedThroughputOverride | None
    ) = None

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
