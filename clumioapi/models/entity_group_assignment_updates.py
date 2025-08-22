#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import role_for_organizational_units as role_for_organizational_units_

T = TypeVar('T', bound='EntityGroupAssignmentUpdates')


class EntityGroupAssignmentUpdates:
    """Implementation of the 'EntityGroupAssignmentUpdates' model.

    Updates to the organizational units along with the role assigned to the user.

    Attributes:
        add:
            The Clumio-assigned IDs of the organizational units, with the Clumio-assigned ID
            of the role
            to be assigned to the user.
        remove:
            The Clumio-assigned IDs of the organizational units, with the Clumio-assigned ID
            of the role
            to be unassigned to the user.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'add': 'add', 'remove': 'remove'}

    def __init__(
        self,
        add: Sequence[role_for_organizational_units_.RoleForOrganizationalUnits] | None = None,
        remove: Sequence[role_for_organizational_units_.RoleForOrganizationalUnits] | None = None,
    ) -> None:
        """Constructor for the EntityGroupAssignmentUpdates class."""

        # Initialize members of the class
        self.add: Sequence[role_for_organizational_units_.RoleForOrganizationalUnits] | None = add
        self.remove: Sequence[role_for_organizational_units_.RoleForOrganizationalUnits] | None = (
            remove
        )

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
        val = dictionary.get('add', None)

        val_add = None
        if val:
            val_add = list()
            for value in val:
                val_add.append(
                    role_for_organizational_units_.RoleForOrganizationalUnits.from_dictionary(value)
                )

        val = dictionary.get('remove', None)

        val_remove = None
        if val:
            val_remove = list()
            for value in val:
                val_remove.append(
                    role_for_organizational_units_.RoleForOrganizationalUnits.from_dictionary(value)
                )

        # Return an object of this model
        return cls(
            val_add,
            val_remove,
        )
