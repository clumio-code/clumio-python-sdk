#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import assignment_input_model

T = TypeVar('T', bound='SetPolicyAssignmentsV1Request')


class SetPolicyAssignmentsV1Request:
    """Implementation of the 'SetPolicyAssignmentsV1Request' model.

    Attributes:
        items:
            Items are inputs that represent the list of assets to which a policy is to be
            assigned or unassigned.
    """

    # Create a mapping from Model property names to API property names
    _names = {'items': 'items'}

    def __init__(self, items: Sequence[assignment_input_model.AssignmentInputModel] = None) -> None:
        """Constructor for the SetPolicyAssignmentsV1Request class."""

        # Initialize members of the class
        self.items: Sequence[assignment_input_model.AssignmentInputModel] = items

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
        items = None
        if dictionary.get('items'):
            items = list()
            for value in dictionary.get('items'):
                items.append(assignment_input_model.AssignmentInputModel.from_dictionary(value))

        # Return an object of this model
        return cls(items)
