#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import user_with_role

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
    _names = {'add': 'add', 'remove': 'remove'}

    def __init__(
        self,
        add: Sequence[user_with_role.UserWithRole] = None,
        remove: Sequence[user_with_role.UserWithRole] = None,
    ) -> None:
        """Constructor for the UpdateUserAssignmentsWithRole class."""

        # Initialize members of the class
        self.add: Sequence[user_with_role.UserWithRole] = add
        self.remove: Sequence[user_with_role.UserWithRole] = remove

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
                add.append(user_with_role.UserWithRole.from_dictionary(value))

        remove = None
        if dictionary.get('remove'):
            remove = list()
            for value in dictionary.get('remove'):
                remove.append(user_with_role.UserWithRole.from_dictionary(value))

        # Return an object of this model
        return cls(add, remove)
