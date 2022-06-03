#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='InheritedFrom')


class InheritedFrom:
    """Implementation of the 'InheritedFrom' model.

    Attributes:
        p_id:
            The Clumio-assigned ID of the item.
        name:
            Name of the folder.
        objectType:
            VCenterObjectType denotes the VCenter object type
    """

    # Create a mapping from Model property names to API property names
    _names = {'p_id': 'id', 'name': 'name', 'objectType': 'objectType'}

    def __init__(self, p_id: str = None, name: str = None, objectType: str = None) -> None:
        """Constructor for the InheritedFrom class."""

        # Initialize members of the class
        self.p_id: str = p_id
        self.name: str = name
        self.objectType: str = objectType

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
        p_id = dictionary.get('id')
        name = dictionary.get('name')
        objectType = dictionary.get('objectType')
        # Return an object of this model
        return cls(p_id, name, objectType)
