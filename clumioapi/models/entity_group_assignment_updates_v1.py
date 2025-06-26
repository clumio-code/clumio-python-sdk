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
    _names = {'add': 'add', 'remove': 'remove'}

    def __init__(self, add: Sequence[str] = None, remove: Sequence[str] = None) -> None:
        """Constructor for the EntityGroupAssignmentUpdatesV1 class."""

        # Initialize members of the class
        self.add: Sequence[str] = add
        self.remove: Sequence[str] = remove

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
        add = dictionary.get('add')
        remove = dictionary.get('remove')
        # Return an object of this model
        return cls(add, remove)
