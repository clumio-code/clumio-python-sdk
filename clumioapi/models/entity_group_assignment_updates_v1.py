#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='EntityGroupAssignmentUpdatesV1')


class EntityGroupAssignmentUpdatesV1:
    """Implementation of the 'EntityGroupAssignmentUpdatesV1' model.

    Updates to the organizational unit assignments.

    Attributes:
        add:
            The Clumio-assigned IDs of the organizational units to be assigned to the user.
        remove:
            The Clumio-assigned IDs of the organizational units to be unassigned to the
            user.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'add': 'add', 'remove': 'remove'}

    def __init__(
        self, add: Sequence[str] | None = None, remove: Sequence[str] | None = None
    ) -> None:
        """Constructor for the EntityGroupAssignmentUpdatesV1 class."""

        # Initialize members of the class
        self.add: Sequence[str] | None = add
        self.remove: Sequence[str] | None = remove

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
        val_add = val

        val = dictionary.get('remove', None)
        val_remove = val

        # Return an object of this model
        return cls(
            val_add,
            val_remove,
        )
