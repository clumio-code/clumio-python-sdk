#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import update_entities
from clumioapi.models import update_protection_group_assignments
from clumioapi.models import update_user_assignments_with_role

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
    _names = {
        'description': 'description',
        'entities': 'entities',
        'name': 'name',
        'protection_groups': 'protection_groups',
        'users': 'users',
    }

    def __init__(
        self,
        description: str = None,
        entities: update_entities.UpdateEntities = None,
        name: str = None,
        protection_groups: update_protection_group_assignments.UpdateProtectionGroupAssignments = None,
        users: update_user_assignments_with_role.UpdateUserAssignmentsWithRole = None,
    ) -> None:
        """Constructor for the PatchOrganizationalUnitV2Request class."""

        # Initialize members of the class
        self.description: str = description
        self.entities: update_entities.UpdateEntities = entities
        self.name: str = name
        self.protection_groups: (
            update_protection_group_assignments.UpdateProtectionGroupAssignments
        ) = protection_groups
        self.users: update_user_assignments_with_role.UpdateUserAssignmentsWithRole = users

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
        description = dictionary.get('description')
        key = 'entities'
        entities = (
            update_entities.UpdateEntities.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        name = dictionary.get('name')
        key = 'protection_groups'
        protection_groups = (
            update_protection_group_assignments.UpdateProtectionGroupAssignments.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'users'
        users = (
            update_user_assignments_with_role.UpdateUserAssignmentsWithRole.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(description, entities, name, protection_groups, users)
