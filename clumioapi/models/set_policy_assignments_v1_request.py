#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import assignment_input_model as assignment_input_model_

T = TypeVar('T', bound='SetPolicyAssignmentsV1Request')


class SetPolicyAssignmentsV1Request:
    """Implementation of the 'SetPolicyAssignmentsV1Request' model.

    Attributes:
        items:
            Items are inputs that represent the list of assets to which a policy is to be
            assigned or unassigned.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'items': 'items'}

    def __init__(
        self, items: Sequence[assignment_input_model_.AssignmentInputModel] | None = None
    ) -> None:
        """Constructor for the SetPolicyAssignmentsV1Request class."""

        # Initialize members of the class
        self.items: Sequence[assignment_input_model_.AssignmentInputModel] | None = items

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
        val = dictionary.get('items', None)

        val_items = None
        if val:
            val_items = list()
            for value in val:
                val_items.append(
                    assignment_input_model_.AssignmentInputModel.from_dictionary(value)
                )

        # Return an object of this model
        return cls(
            val_items,
        )
