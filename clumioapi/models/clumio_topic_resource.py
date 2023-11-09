#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import policy_details

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
    _names = {'policies': 'policies', 'steps': 'steps'}

    def __init__(
        self, policies: Sequence[policy_details.PolicyDetails] = None, steps: str = None
    ) -> None:
        """Constructor for the ClumioTopicResource class."""

        # Initialize members of the class
        self.policies: Sequence[policy_details.PolicyDetails] = policies
        self.steps: str = steps

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
        policies = None
        if dictionary.get('policies'):
            policies = list()
            for value in dictionary.get('policies'):
                policies.append(policy_details.PolicyDetails.from_dictionary(value))

        steps = dictionary.get('steps')
        # Return an object of this model
        return cls(policies, steps)
