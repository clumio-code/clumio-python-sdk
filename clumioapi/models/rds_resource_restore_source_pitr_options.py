#
# Copyright 2023. Clumio, Inc.
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
    _names = {'resource_id': 'resource_id', 'timestamp': 'timestamp'}

    def __init__(self, resource_id: str = None, timestamp: str = None) -> None:
        """Constructor for the RdsResourceRestoreSourcePitrOptions class."""

        # Initialize members of the class
        self.resource_id: str = resource_id
        self.timestamp: str = timestamp

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
        resource_id = dictionary.get('resource_id')
        timestamp = dictionary.get('timestamp')
        # Return an object of this model
        return cls(resource_id, timestamp)
