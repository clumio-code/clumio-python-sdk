#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import role_for_organizational_units

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
    _names = {'add': 'add', 'remove': 'remove'}

    def __init__(
        self,
        add: Sequence[role_for_organizational_units.RoleForOrganizationalUnits] = None,
        remove: Sequence[role_for_organizational_units.RoleForOrganizationalUnits] = None,
    ) -> None:
        """Constructor for the EntityGroupAssignmentUpdates class."""

        # Initialize members of the class
        self.add: Sequence[role_for_organizational_units.RoleForOrganizationalUnits] = add
        self.remove: Sequence[role_for_organizational_units.RoleForOrganizationalUnits] = remove

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
        add = None
        if dictionary.get('add'):
            add = list()
            for value in dictionary.get('add'):
                add.append(
                    role_for_organizational_units.RoleForOrganizationalUnits.from_dictionary(value)
                )

        remove = None
        if dictionary.get('remove'):
            remove = list()
            for value in dictionary.get('remove'):
                remove.append(
                    role_for_organizational_units.RoleForOrganizationalUnits.from_dictionary(value)
                )

        # Return an object of this model
        return cls(add, remove)
