#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import assign_policy_action

T = TypeVar('T', bound='RuleAction')


class RuleAction:
    """Implementation of the 'RuleAction' model.

    An action to be applied subject to the rule criteria.

    Attributes:
        assign_policy:
            Apply a policy to assets.
    """

    # Create a mapping from Model property names to API property names
    _names = {'assign_policy': 'assign_policy'}

    def __init__(self, assign_policy: assign_policy_action.AssignPolicyAction = None) -> None:
        """Constructor for the RuleAction class."""

        # Initialize members of the class
        self.assign_policy: assign_policy_action.AssignPolicyAction = assign_policy

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
        key = 'assign_policy'
        assign_policy = (
            assign_policy_action.AssignPolicyAction.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(assign_policy)
