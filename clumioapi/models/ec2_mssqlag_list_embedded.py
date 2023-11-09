#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_mssqlag

T = TypeVar('T', bound='EC2MSSQLAGListEmbedded')


class EC2MSSQLAGListEmbedded:
    """Implementation of the 'EC2MSSQLAGListEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        items:
            A collection of requested items.
    """

    # Create a mapping from Model property names to API property names
    _names = {'items': 'items'}

    def __init__(self, items: Sequence[ec2_mssqlag.EC2MSSQLAG] = None) -> None:
        """Constructor for the EC2MSSQLAGListEmbedded class."""

        # Initialize members of the class
        self.items: Sequence[ec2_mssqlag.EC2MSSQLAG] = items

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
        items = None
        if dictionary.get('items'):
            items = list()
            for value in dictionary.get('items'):
                items.append(ec2_mssqlag.EC2MSSQLAG.from_dictionary(value))

        # Return an object of this model
        return cls(items)
