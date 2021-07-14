#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='CloudConnectorCountByStatus')


class CloudConnectorCountByStatus:
    """Implementation of the 'CloudConnectorCountByStatus' model.

    The number of cloud connectors in this subgroup, aggregated by their status.

    Attributes:
        degraded:
            The number of degraded cloud connectors in this subgroup.
        healthy:
            The number of healthy cloud connectors in this subgroup.
    """

    # Create a mapping from Model property names to API property names
    _names = {'degraded': 'degraded', 'healthy': 'healthy'}

    def __init__(self, degraded: int = None, healthy: int = None) -> None:
        """Constructor for the CloudConnectorCountByStatus class."""

        # Initialize members of the class
        self.degraded: int = degraded
        self.healthy: int = healthy

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
        degraded = dictionary.get('degraded')
        healthy = dictionary.get('healthy')
        # Return an object of this model
        return cls(degraded, healthy)
