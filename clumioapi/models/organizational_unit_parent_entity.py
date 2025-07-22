#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='OrganizationalUnitParentEntity')


class OrganizationalUnitParentEntity:
    """Implementation of the 'OrganizationalUnitParentEntity' model.

    The parent object of the primary entity associated with the organizational
    unit.The parent object is optional and can be omitted.

    Attributes:
        p_id:
            The Clumio assigned ID of the entity.
        p_type:
            The entity type.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'p_id': 'id', 'p_type': 'type'}

    def __init__(self, p_id: str, p_type: str) -> None:
        """Constructor for the OrganizationalUnitParentEntity class."""

        # Initialize members of the class
        self.p_id: str = p_id
        self.p_type: str = p_type

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

        # Extract variables from the dictionary
        val = dictionary['id']
        val_p_id = val

        val = dictionary['type']
        val_p_type = val

        # Return an object of this model
        return cls(
            val_p_id,  # type: ignore
            val_p_type,  # type: ignore
        )
