#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    entity_group_assignment_updates_v1 as entity_group_assignment_updates_v1_

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
    _names: dict[str, str] = {
        'assigned_role': 'assigned_role',
        'full_name': 'full_name',
        'is_enabled': 'is_enabled',
        'organizational_unit_assignment_updates': 'organizational_unit_assignment_updates',
    }

    def __init__(
        self,
        assigned_role: str | None = None,
        full_name: str | None = None,
        is_enabled: bool | None = None,
        organizational_unit_assignment_updates: (
            entity_group_assignment_updates_v1_.EntityGroupAssignmentUpdatesV1 | None
        ) = None,
    ) -> None:
        """Constructor for the UpdateUserV1Request class."""

        # Initialize members of the class
        self.assigned_role: str | None = assigned_role
        self.full_name: str | None = full_name
        self.is_enabled: bool | None = is_enabled
        self.organizational_unit_assignment_updates: (
            entity_group_assignment_updates_v1_.EntityGroupAssignmentUpdatesV1 | None
        ) = organizational_unit_assignment_updates

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
        val = dictionary.get('assigned_role', None)
        val_assigned_role = val

        val = dictionary.get('full_name', None)
        val_full_name = val

        val = dictionary.get('is_enabled', None)
        val_is_enabled = val

        val = dictionary.get('organizational_unit_assignment_updates', None)
        val_organizational_unit_assignment_updates = (
            entity_group_assignment_updates_v1_.EntityGroupAssignmentUpdatesV1.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_assigned_role,
            val_full_name,
            val_is_enabled,
            val_organizational_unit_assignment_updates,
        )
