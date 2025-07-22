#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='UpdateUserAssignments')


class UpdateUserAssignments:
    """Implementation of the 'UpdateUserAssignments' model.

    Updates to the user assignments.

    Attributes:
        add:
            List of user IDs to assign this organizational unit.
        remove:
            List of user IDs to un-assign this organizational unit.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'add': 'add', 'remove': 'remove'}

    def __init__(self, add: Sequence[str], remove: Sequence[str]) -> None:
        """Constructor for the UpdateUserAssignments class."""

        # Initialize members of the class
        self.add: Sequence[str] = add
        self.remove: Sequence[str] = remove

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
        val_add = val

        val = dictionary['remove']
        val_remove = val

        # Return an object of this model
        return cls(
            val_add,  # type: ignore
            val_remove,  # type: ignore
        )
