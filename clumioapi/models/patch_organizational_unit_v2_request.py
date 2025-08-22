#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import update_entities as update_entities_
from clumioapi.models import \
    update_protection_group_assignments as update_protection_group_assignments_
from clumioapi.models import update_user_assignments_with_role as update_user_assignments_with_role_

T = TypeVar('T', bound='PatchOrganizationalUnitV2Request')


class PatchOrganizationalUnitV2Request:
    """Implementation of the 'PatchOrganizationalUnitV2Request' model.

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
        protection_groups:
            UpdateProtectionGroupAssignments denotes the protection groups to be assigned or
            unassigned.
            Updates to the protection group assignments.
        users:
            UpdateUserAssignmentsWithRole denotes the users to be added or removed along
            with the role.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'description': 'description',
        'entities': 'entities',
        'name': 'name',
        'protection_groups': 'protection_groups',
        'users': 'users',
    }

    def __init__(
        self,
        description: str | None = None,
        entities: update_entities_.UpdateEntities | None = None,
        name: str | None = None,
        protection_groups: (
            update_protection_group_assignments_.UpdateProtectionGroupAssignments | None
        ) = None,
        users: update_user_assignments_with_role_.UpdateUserAssignmentsWithRole | None = None,
    ) -> None:
        """Constructor for the PatchOrganizationalUnitV2Request class."""

        # Initialize members of the class
        self.description: str | None = description
        self.entities: update_entities_.UpdateEntities | None = entities
        self.name: str | None = name
        self.protection_groups: (
            update_protection_group_assignments_.UpdateProtectionGroupAssignments | None
        ) = protection_groups
        self.users: update_user_assignments_with_role_.UpdateUserAssignmentsWithRole | None = users

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

        val = dictionary.get('protection_groups', None)
        val_protection_groups = (
            update_protection_group_assignments_.UpdateProtectionGroupAssignments.from_dictionary(
                val
            )
        )

        val = dictionary.get('users', None)
        val_users = (
            update_user_assignments_with_role_.UpdateUserAssignmentsWithRole.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_description,
            val_entities,
            val_name,
            val_protection_groups,
            val_users,
        )
