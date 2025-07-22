#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ProvisionedThroughput')


class ProvisionedThroughput:
    """Implementation of the 'ProvisionedThroughput' model.

    Represents the provisioned throughput settings for a DynamoDB table.

    Attributes:
        read_capacity_units:
            The maximum number of strongly consistent reads consumed per second.
        write_capacity_units:
            The maximum number of writes consumed per second.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'read_capacity_units': 'read_capacity_units',
        'write_capacity_units': 'write_capacity_units',
    }

    def __init__(self, read_capacity_units: int, write_capacity_units: int) -> None:
        """Constructor for the ProvisionedThroughput class."""

        # Initialize members of the class
        self.read_capacity_units: int = read_capacity_units
        self.write_capacity_units: int = write_capacity_units

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

        # Extract variables from the dictionary
        val = dictionary['read_capacity_units']
        val_read_capacity_units = val

        val = dictionary['write_capacity_units']
        val_write_capacity_units = val

        # Return an object of this model
        return cls(
            val_read_capacity_units,  # type: ignore
            val_write_capacity_units,  # type: ignore
        )
