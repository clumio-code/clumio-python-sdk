#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='RdsResourceRestoreSourcePitrOptions')


class RdsResourceRestoreSourcePitrOptions:
    """Implementation of the 'RdsResourceRestoreSourcePitrOptions' model.

    The parameters for initiating an RDS restore from a snapshot.

    Attributes:
        resource_id:
            The Clumio-assigned ID of the RDS resource to be restored.
            Use the [GET /datasources/aws/rds-resources](#operation/list-aws-rds-resources)
            endpoint to fetch valid values.
        timestamp:
            A point in time to be restored in RFC-3339 format.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'resource_id': 'resource_id', 'timestamp': 'timestamp'}

    def __init__(self, resource_id: str | None = None, timestamp: str | None = None) -> None:
        """Constructor for the RdsResourceRestoreSourcePitrOptions class."""

        # Initialize members of the class
        self.resource_id: str | None = resource_id
        self.timestamp: str | None = timestamp

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
        val = dictionary.get('resource_id', None)
        val_resource_id = val

        val = dictionary.get('timestamp', None)
        val_timestamp = val

        # Return an object of this model
        return cls(
            val_resource_id,
            val_timestamp,
        )
