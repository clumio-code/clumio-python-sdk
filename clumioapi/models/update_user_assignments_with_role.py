#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import user_with_role as user_with_role_

T = TypeVar('T', bound='UpdateUserAssignmentsWithRole')


class UpdateUserAssignmentsWithRole:
    """Implementation of the 'UpdateUserAssignmentsWithRole' model.

    UpdateUserAssignmentsWithRole denotes the users to be added or removed along
    with the role.

    Attributes:
        add:
            List of user IDs with role to assign this organizational unit.
        remove:
            List of user IDs with role to un-assign this organizational unit.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'add': 'add', 'remove': 'remove'}

    def __init__(
        self,
        add: Sequence[user_with_role_.UserWithRole],
        remove: Sequence[user_with_role_.UserWithRole],
    ) -> None:
        """Constructor for the UpdateUserAssignmentsWithRole class."""

        # Initialize members of the class
        self.add: Sequence[user_with_role_.UserWithRole] = add
        self.remove: Sequence[user_with_role_.UserWithRole] = remove

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
        val = dictionary['add']

        val_add = None
        if val:
            val_add = list()
            for value in val:
                val_add.append(user_with_role_.UserWithRole.from_dictionary(value))

        val = dictionary['remove']

        val_remove = None
        if val:
            val_remove = list()
            for value in val:
                val_remove.append(user_with_role_.UserWithRole.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_add,  # type: ignore
            val_remove,  # type: ignore
        )
