#
# Copyright 2023. Clumio, Inc.
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
    _names = {'assign': 'assign', 'unassign': 'unassign'}

    def __init__(self, assign: Sequence[str] = None, unassign: Sequence[str] = None) -> None:
        """Constructor for the UpdateProtectionGroupAssignments class."""

        # Initialize members of the class
        self.assign: Sequence[str] = assign
        self.unassign: Sequence[str] = unassign

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
        assign = dictionary.get('assign')
        unassign = dictionary.get('unassign')
        # Return an object of this model
        return cls(assign, unassign)
