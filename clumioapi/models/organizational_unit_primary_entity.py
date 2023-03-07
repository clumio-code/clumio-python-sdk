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
        p_id:
            The Clumio assigned ID of the entity.
        p_type:
            The entity type.
    """

    # Create a mapping from Model property names to API property names
    _names = {'p_id': 'id', 'p_type': 'type'}

    def __init__(self, p_id: str = None, p_type: str = None) -> None:
        """Constructor for the OrganizationalUnitPrimaryEntity class."""

        # Initialize members of the class
        self.p_id: str = p_id
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
        p_id = dictionary.get('id')
        p_type = dictionary.get('type')
        # Return an object of this model
        return cls(p_id, p_type)
