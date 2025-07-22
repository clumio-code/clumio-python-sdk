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
        description: str,
        entities: update_entities_.UpdateEntities,
        name: str,
        protection_groups: update_protection_group_assignments_.UpdateProtectionGroupAssignments,
        users: update_user_assignments_with_role_.UpdateUserAssignmentsWithRole,
    ) -> None:
        """Constructor for the PatchOrganizationalUnitV2Request class."""

        # Initialize members of the class
        self.description: str = description
        self.entities: update_entities_.UpdateEntities = entities
        self.name: str = name
        self.protection_groups: (
            update_protection_group_assignments_.UpdateProtectionGroupAssignments
        ) = protection_groups
        self.users: update_user_assignments_with_role_.UpdateUserAssignmentsWithRole = users

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
        val = dictionary['description']
        val_description = val

        val = dictionary['entities']
        val_entities = update_entities_.UpdateEntities.from_dictionary(val)

        val = dictionary['name']
        val_name = val

        val = dictionary['protection_groups']
        val_protection_groups = (
            update_protection_group_assignments_.UpdateProtectionGroupAssignments.from_dictionary(
                val
            )
        )

        val = dictionary['users']
        val_users = (
            update_user_assignments_with_role_.UpdateUserAssignmentsWithRole.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_description,  # type: ignore
            val_entities,  # type: ignore
            val_name,  # type: ignore
            val_protection_groups,  # type: ignore
            val_users,  # type: ignore
        )
