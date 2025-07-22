#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import policy_details as policy_details_

T = TypeVar('T', bound='ClumioTopicResource')


class ClumioTopicResource:
    """Implementation of the 'ClumioTopicResource' model.

    Details for the SNS Topic

    Attributes:
        policies:
            "policies" stores all the policies to be attached to the topic.
        steps:
            "steps" refers to commands to be executed
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'policies': 'policies', 'steps': 'steps'}

    def __init__(self, policies: Sequence[policy_details_.PolicyDetails], steps: str) -> None:
        """Constructor for the ClumioTopicResource class."""

        # Initialize members of the class
        self.policies: Sequence[policy_details_.PolicyDetails] = policies
        self.steps: str = steps

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
        val = dictionary['policies']

        val_policies = None
        if val:
            val_policies = list()
            for value in val:
                val_policies.append(policy_details_.PolicyDetails.from_dictionary(value))

        val = dictionary['steps']
        val_steps = val

        # Return an object of this model
        return cls(
            val_policies,  # type: ignore
            val_steps,  # type: ignore
        )
