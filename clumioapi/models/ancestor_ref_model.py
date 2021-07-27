#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AncestorRefModel')


class AncestorRefModel:
    """Implementation of the 'AncestorRefModel' model.

    Attributes:
        id:
            A VMware-assigned ID for this ancestor.
        is_root:
            Determines whether this ancestor is a hidden root object. If `true`, this
            ancestor is a hidden root object.
        name:
            The name of the ancestor.
        type:
            The type of vCenter object that this ancestor represents. For example, a data
            center can be an ancestor of a data center folder.
    """

    # Create a mapping from Model property names to API property names
    _names = {'id': 'id', 'is_root': 'is_root', 'name': 'name', 'type': 'type'}

    def __init__(
        self, id: str = None, is_root: bool = None, name: str = None, type: str = None
    ) -> None:
        """Constructor for the AncestorRefModel class."""

        # Initialize members of the class
        self.id: str = id
        self.is_root: bool = is_root
        self.name: str = name
        self.type: str = type

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
        id = dictionary.get('id')
        is_root = dictionary.get('is_root')
        name = dictionary.get('name')
        type = dictionary.get('type')
        # Return an object of this model
        return cls(id, is_root, name, type)
