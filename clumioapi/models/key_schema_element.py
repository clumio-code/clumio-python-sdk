#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='KeySchemaElement')


class KeySchemaElement:
    """Implementation of the 'KeySchemaElement' model.

    Represents a single element of a key schema. A key schema specifies the
    attributes that make up the primary keyof a table, or the key attributes of an
    index.

    Attributes:
        attribute_name:
            The name of a key attribute.
        key_type:
            The role that this key attribute will assume.
            Possible values include: `HASH` - partition key and `RANGE` - sort key.
    """

    # Create a mapping from Model property names to API property names
    _names = {'attribute_name': 'attribute_name', 'key_type': 'key_type'}

    def __init__(self, attribute_name: str = None, key_type: str = None) -> None:
        """Constructor for the KeySchemaElement class."""

        # Initialize members of the class
        self.attribute_name: str = attribute_name
        self.key_type: str = key_type

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
        attribute_name = dictionary.get('attribute_name')
        key_type = dictionary.get('key_type')
        # Return an object of this model
        return cls(attribute_name, key_type)
