#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AttributeDefinition')


class AttributeDefinition:
    """Implementation of the 'AttributeDefinition' model.

    Represents the attributes within a DynamoDB table by the nameand the data type
    (`S` for string, `N` for number, `B` for binary).

    Attributes:
        name:

        p_type:

    """

    # Create a mapping from Model property names to API property names
    _names = {'name': 'name', 'p_type': 'type'}

    def __init__(self, name: str = None, p_type: str = None) -> None:
        """Constructor for the AttributeDefinition class."""

        # Initialize members of the class
        self.name: str = name
        self.p_type: str = p_type

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
        name = dictionary.get('name')
        p_type = dictionary.get('type')
        # Return an object of this model
        return cls(name, p_type)
