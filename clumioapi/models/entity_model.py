#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import organizational_unit_parent_entity
from clumioapi.models import organizational_unit_primary_entity

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
    _names = {'parent_entity': 'parent_entity', 'primary_entity': 'primary_entity'}

    def __init__(
        self,
        parent_entity: organizational_unit_parent_entity.OrganizationalUnitParentEntity = None,
        primary_entity: organizational_unit_primary_entity.OrganizationalUnitPrimaryEntity = None,
    ) -> None:
        """Constructor for the EntityModel class."""

        # Initialize members of the class
        self.parent_entity: organizational_unit_parent_entity.OrganizationalUnitParentEntity = (
            parent_entity
        )
        self.primary_entity: organizational_unit_primary_entity.OrganizationalUnitPrimaryEntity = (
            primary_entity
        )

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
        key = 'parent_entity'
        parent_entity = (
            organizational_unit_parent_entity.OrganizationalUnitParentEntity.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'primary_entity'
        primary_entity = (
            organizational_unit_primary_entity.OrganizationalUnitPrimaryEntity.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(parent_entity, primary_entity)
