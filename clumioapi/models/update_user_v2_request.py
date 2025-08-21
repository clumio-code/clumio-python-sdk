#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import entity_group_assignment_updates as entity_group_assignment_updates_

T = TypeVar('T', bound='UpdateUserV2Request')


class UpdateUserV2Request:
    """Implementation of the 'UpdateUserV2Request' model.

    Attributes:
        access_control_configuration_updates:
            Updates to the organizational units along with the role assigned to the user.
        full_name:
            The full name of the user that is to replace the existing full name.
            For example, enter the user's first name and last name.
        is_enabled:
            If `true`, enables a user who has been disabled from Clumio,
            returning the user to its previous "Activated" or "Invited" status. If `false`,
            disables a user from Clumio.
            The user will not be able log in to Clumio until another Clumio user re-enables
            the account.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'access_control_configuration_updates': 'access_control_configuration_updates',
        'full_name': 'full_name',
        'is_enabled': 'is_enabled',
    }

    def __init__(
        self,
        access_control_configuration_updates: (
            entity_group_assignment_updates_.EntityGroupAssignmentUpdates | None
        ) = None,
        full_name: str | None = None,
        is_enabled: bool | None = None,
    ) -> None:
        """Constructor for the UpdateUserV2Request class."""

        # Initialize members of the class
        self.access_control_configuration_updates: (
            entity_group_assignment_updates_.EntityGroupAssignmentUpdates | None
        ) = access_control_configuration_updates
        self.full_name: str | None = full_name
        self.is_enabled: bool | None = is_enabled

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
        val = dictionary.get('access_control_configuration_updates', None)
        val_access_control_configuration_updates = (
            entity_group_assignment_updates_.EntityGroupAssignmentUpdates.from_dictionary(val)
        )

        val = dictionary.get('full_name', None)
        val_full_name = val

        val = dictionary.get('is_enabled', None)
        val_is_enabled = val

        # Return an object of this model
        return cls(
            val_access_control_configuration_updates,
            val_full_name,
            val_is_enabled,
        )
