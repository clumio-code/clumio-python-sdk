#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='UpdateProtectionGroupAssignments')


class UpdateProtectionGroupAssignments:
    """Implementation of the 'UpdateProtectionGroupAssignments' model.

    UpdateProtectionGroupAssignments denotes the protection groups to be assigned
    orunassigned.Updates to the protection group assignments.

    Attributes:
        assign:
            List of protection group IDs to assign to this organizational unit.
        unassign:
            List of protection group IDs to un-assign from this organizational unit.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'assign': 'assign', 'unassign': 'unassign'}

    def __init__(
        self, assign: Sequence[str] | None = None, unassign: Sequence[str] | None = None
    ) -> None:
        """Constructor for the UpdateProtectionGroupAssignments class."""

        # Initialize members of the class
        self.assign: Sequence[str] | None = assign
        self.unassign: Sequence[str] | None = unassign

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
        val = dictionary.get('assign', None)
        val_assign = val

        val = dictionary.get('unassign', None)
        val_unassign = val

        # Return an object of this model
        return cls(
            val_assign,
            val_unassign,
        )
