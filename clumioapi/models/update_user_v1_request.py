#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import entity_group_assignment_updates_v1

T = TypeVar('T', bound='UpdateUserV1Request')


class UpdateUserV1Request:
    """Implementation of the 'UpdateUserV1Request' model.

    Attributes:
        assigned_role:
            Updates the role assigned to the user.
            The available roles can be retrieved via the [GET /roles](#operation/list-roles)
            API.
        full_name:
            The full name of the user that is to replace the existing full name.
            For example, enter the user's first name and last name.
        is_enabled:
            If `true`, enables a user who has been disabled from Clumio,
            returning the user to its previous "Activated" or "Invited" status. If `false`,
            disables a user from Clumio.
            The user will not be able log in to Clumio until another Clumio user re-enables
            the account.
        organizational_unit_assignment_updates:
            Updates to the organizational unit assignments.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'assigned_role': 'assigned_role',
        'full_name': 'full_name',
        'is_enabled': 'is_enabled',
        'organizational_unit_assignment_updates': 'organizational_unit_assignment_updates',
    }

    def __init__(
        self,
        assigned_role: str = None,
        full_name: str = None,
        is_enabled: bool = None,
        organizational_unit_assignment_updates: entity_group_assignment_updates_v1.EntityGroupAssignmentUpdatesV1 = None,
    ) -> None:
        """Constructor for the UpdateUserV1Request class."""

        # Initialize members of the class
        self.assigned_role: str = assigned_role
        self.full_name: str = full_name
        self.is_enabled: bool = is_enabled
        self.organizational_unit_assignment_updates: entity_group_assignment_updates_v1.EntityGroupAssignmentUpdatesV1 = (
            organizational_unit_assignment_updates
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
        assigned_role = dictionary.get('assigned_role')
        full_name = dictionary.get('full_name')
        is_enabled = dictionary.get('is_enabled')
        key = 'organizational_unit_assignment_updates'
        organizational_unit_assignment_updates = (
            entity_group_assignment_updates_v1.EntityGroupAssignmentUpdatesV1.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(assigned_role, full_name, is_enabled, organizational_unit_assignment_updates)
