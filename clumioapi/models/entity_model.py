#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import organizational_unit_parent_entity as organizational_unit_parent_entity_
from clumioapi.models import \
    organizational_unit_primary_entity as organizational_unit_primary_entity_
import requests

T = TypeVar('T', bound='EntityModel')


@dataclasses.dataclass
class EntityModel:
    """Implementation of the 'EntityModel' model.

    entityModel denotes the entityModel

    Attributes:
        ParentEntity:
            The parent object is optional and can be omitted.

        PrimaryEntity

    """

    ParentEntity: organizational_unit_parent_entity_.OrganizationalUnitParentEntity | None = None
    PrimaryEntity: organizational_unit_primary_entity_.OrganizationalUnitPrimaryEntity | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return api_helper.to_dictionary(self)

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('parent_entity', None)
        val_parent_entity = (
            organizational_unit_parent_entity_.OrganizationalUnitParentEntity.from_dictionary(val)
        )

        val = dictionary.get('primary_entity', None)
        val_primary_entity = (
            organizational_unit_primary_entity_.OrganizationalUnitPrimaryEntity.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_parent_entity,
            val_primary_entity,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
