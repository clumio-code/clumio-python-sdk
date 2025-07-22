#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import assign_policy_action as assign_policy_action_

T = TypeVar('T', bound='RuleAction')


class RuleAction:
    """Implementation of the 'RuleAction' model.

    An action to be applied subject to the rule criteria.

    Attributes:
        assign_policy:
            Apply a policy to assets.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'assign_policy': 'assign_policy'}

    def __init__(self, assign_policy: assign_policy_action_.AssignPolicyAction) -> None:
        """Constructor for the RuleAction class."""

        # Initialize members of the class
        self.assign_policy: assign_policy_action_.AssignPolicyAction = assign_policy

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
        val = dictionary['assign_policy']
        val_assign_policy = assign_policy_action_.AssignPolicyAction.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_assign_policy,  # type: ignore
        )
