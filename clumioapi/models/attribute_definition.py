#
# Copyright 2023. Clumio, A Commvault Company.
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
    _names: dict[str, str] = {'name': 'name', 'p_type': 'type'}

    def __init__(self, name: str | None = None, p_type: str | None = None) -> None:
        """Constructor for the AttributeDefinition class."""

        # Initialize members of the class
        self.name: str | None = name
        self.p_type: str | None = p_type

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
        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('type', None)
        val_p_type = val

        # Return an object of this model
        return cls(
            val_name,
            val_p_type,
        )
