#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import entity_group_assignment_updates

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
    _names = {
        'access_control_configuration_updates': 'access_control_configuration_updates',
        'full_name': 'full_name',
        'is_enabled': 'is_enabled',
    }

    def __init__(
        self,
        access_control_configuration_updates: entity_group_assignment_updates.EntityGroupAssignmentUpdates = None,
        full_name: str = None,
        is_enabled: bool = None,
    ) -> None:
        """Constructor for the UpdateUserV2Request class."""

        # Initialize members of the class
        self.access_control_configuration_updates: (
            entity_group_assignment_updates.EntityGroupAssignmentUpdates
        ) = access_control_configuration_updates
        self.full_name: str = full_name
        self.is_enabled: bool = is_enabled

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
        key = 'access_control_configuration_updates'
        access_control_configuration_updates = (
            entity_group_assignment_updates.EntityGroupAssignmentUpdates.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        full_name = dictionary.get('full_name')
        is_enabled = dictionary.get('is_enabled')
        # Return an object of this model
        return cls(access_control_configuration_updates, full_name, is_enabled)
