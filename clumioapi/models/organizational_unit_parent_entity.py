#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='OrganizationalUnitParentEntity')


class OrganizationalUnitParentEntity:
    """Implementation of the 'OrganizationalUnitParentEntity' model.

    The parent object of the primary entity associated with the organizational unit.
    For example, "vmware_vcenter" is the parent entity of primary entity
    "vmware_vm_folder".The parent object is necessary for VMware entities and can be
    omitted for other data sources.

    Attributes:
        p_id:
            The Clumio assigned ID of the entity.
        p_type:
            The entity type.
    """

    # Create a mapping from Model property names to API property names
    _names = {'p_id': 'id', 'p_type': 'type'}

    def __init__(self, p_id: str = None, p_type: str = None) -> None:
        """Constructor for the OrganizationalUnitParentEntity class."""

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
