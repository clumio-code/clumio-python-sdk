#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2 as ec2_

T = TypeVar('T', bound='Ec2InstanceListEmbedded')


class Ec2InstanceListEmbedded:
    """Implementation of the 'Ec2InstanceListEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        items:
            A collection of requested items.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'items': 'items'}

    def __init__(self, items: Sequence[ec2_.EC2] | None = None) -> None:
        """Constructor for the Ec2InstanceListEmbedded class."""

        # Initialize members of the class
        self.items: Sequence[ec2_.EC2] | None = items

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
        val = dictionary.get('items', None)

        val_items = None
        if val:
            val_items = list()
            for value in val:
                val_items.append(ec2_.EC2.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_items,
        )
