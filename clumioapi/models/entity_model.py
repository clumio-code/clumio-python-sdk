#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import organizational_unit_parent_entity as organizational_unit_parent_entity_
from clumioapi.models import \
    organizational_unit_primary_entity as organizational_unit_primary_entity_

T = TypeVar('T', bound='EntityModel')


class EntityModel:
    """Implementation of the 'EntityModel' model.

    entityModel denotes the entityModel

    Attributes:
        parent_entity:
            The parent object of the primary entity associated with the organizational unit.
            The parent object is optional and can be omitted.
        primary_entity:
            The primary object associated with the organizational unit. Examples of primary
            entities include "aws_environment".
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'parent_entity': 'parent_entity', 'primary_entity': 'primary_entity'}

    def __init__(
        self,
        parent_entity: organizational_unit_parent_entity_.OrganizationalUnitParentEntity,
        primary_entity: organizational_unit_primary_entity_.OrganizationalUnitPrimaryEntity,
    ) -> None:
        """Constructor for the EntityModel class."""

        # Initialize members of the class
        self.parent_entity: organizational_unit_parent_entity_.OrganizationalUnitParentEntity = (
            parent_entity
        )
        self.primary_entity: organizational_unit_primary_entity_.OrganizationalUnitPrimaryEntity = (
            primary_entity
        )

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
        val = dictionary['parent_entity']
        val_parent_entity = (
            organizational_unit_parent_entity_.OrganizationalUnitParentEntity.from_dictionary(val)
        )

        val = dictionary['primary_entity']
        val_primary_entity = (
            organizational_unit_primary_entity_.OrganizationalUnitPrimaryEntity.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_parent_entity,  # type: ignore
            val_primary_entity,  # type: ignore
        )
