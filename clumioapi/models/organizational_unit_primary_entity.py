#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='OrganizationalUnitPrimaryEntity')


class OrganizationalUnitPrimaryEntity:
    """Implementation of the 'OrganizationalUnitPrimaryEntity' model.

    The primary object associated with the organizational unit. Examples of primary
    entities include "aws_environment" and "vmware_vm".

    Attributes:
        id:
            The Clumio assigned ID of the entity.
        type:
            The entity type.
    """

    # Create a mapping from Model property names to API property names
    _names = {'id': 'id', 'type': 'type'}

    def __init__(self, id: str = None, type: str = None) -> None:
        """Constructor for the OrganizationalUnitPrimaryEntity class."""

        # Initialize members of the class
        self.id: str = id
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
        type = dictionary.get('type')
        # Return an object of this model
        return cls(id, type)
