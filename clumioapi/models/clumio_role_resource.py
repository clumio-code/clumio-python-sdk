#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import policy_details

T = TypeVar('T', bound='ClumioRoleResource')


class ClumioRoleResource:
    """Implementation of the 'ClumioRoleResource' model.

    Details for the IAM Role

    Attributes:
        description:

        inline_policies:
            "inline_policies" stores all the Customer Inline Policies to be attached to the
            role.
        managed_policies:
            "managed_policies" stores all the Customer Managed Policies to be attached to
            the role.
        steps:

        trust_policy:
            "trust_policy" stores the Trust Relationship policy for the role. It is a
            stringified JSON blob.
            The user has to JSONify it and then paste the JSONified blob in aws console
            while creating the role.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'description': 'description',
        'inline_policies': 'inline_policies',
        'managed_policies': 'managed_policies',
        'steps': 'steps',
        'trust_policy': 'trust_policy',
    }

    def __init__(
        self,
        description: str = None,
        inline_policies: Sequence[policy_details.PolicyDetails] = None,
        managed_policies: Sequence[policy_details.PolicyDetails] = None,
        steps: str = None,
        trust_policy: object = None,
    ) -> None:
        """Constructor for the ClumioRoleResource class."""

        # Initialize members of the class
        self.description: str = description
        self.inline_policies: Sequence[policy_details.PolicyDetails] = inline_policies
        self.managed_policies: Sequence[policy_details.PolicyDetails] = managed_policies
        self.steps: str = steps
        self.trust_policy: object = trust_policy

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
        description = dictionary.get('description')
        inline_policies = None
        if dictionary.get('inline_policies'):
            inline_policies = list()
            for value in dictionary.get('inline_policies'):
                inline_policies.append(policy_details.PolicyDetails.from_dictionary(value))

        managed_policies = None
        if dictionary.get('managed_policies'):
            managed_policies = list()
            for value in dictionary.get('managed_policies'):
                managed_policies.append(policy_details.PolicyDetails.from_dictionary(value))

        steps = dictionary.get('steps')
        trust_policy = dictionary.get('trust_policy')
        # Return an object of this model
        return cls(description, inline_policies, managed_policies, steps, trust_policy)
