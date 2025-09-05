#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import update_entities as update_entities_
from clumioapi.models import update_user_assignments as update_user_assignments_

T = TypeVar('T', bound='PatchOrganizationalUnitV1Request')


class PatchOrganizationalUnitV1Request:
    """Implementation of the 'PatchOrganizationalUnitV1Request' model.

    Attributes:
        description:
            A description of the organizational unit.
        entities:
            Updates to the entities in the organizational unit.
            Adding or removing entities from the OU is an asynchronous operation.
            The response has a task ID which can be used to track the progress of the
            operation.
        name:
            Unique name assigned to the organizational unit.
        users:
            Updates to the user assignments.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'description': 'description',
        'entities': 'entities',
        'name': 'name',
        'users': 'users',
    }

    def __init__(
        self,
        description: str | None = None,
        entities: update_entities_.UpdateEntities | None = None,
        name: str | None = None,
        users: update_user_assignments_.UpdateUserAssignments | None = None,
    ) -> None:
        """Constructor for the PatchOrganizationalUnitV1Request class."""

        # Initialize members of the class
        self.description: str | None = description
        self.entities: update_entities_.UpdateEntities | None = entities
        self.name: str | None = name
        self.users: update_user_assignments_.UpdateUserAssignments | None = users

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

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('entities', None)
        val_entities = update_entities_.UpdateEntities.from_dictionary(val)

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('users', None)
        val_users = update_user_assignments_.UpdateUserAssignments.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_description,
            val_entities,
            val_name,
            val_users,
        )
