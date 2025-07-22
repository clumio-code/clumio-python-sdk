#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import policy_details as policy_details_

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
    _names: dict[str, str] = {
        'description': 'description',
        'inline_policies': 'inline_policies',
        'managed_policies': 'managed_policies',
        'steps': 'steps',
        'trust_policy': 'trust_policy',
    }

    def __init__(
        self,
        description: str,
        inline_policies: Sequence[policy_details_.PolicyDetails],
        managed_policies: Sequence[policy_details_.PolicyDetails],
        steps: str,
        trust_policy: object,
    ) -> None:
        """Constructor for the ClumioRoleResource class."""

        # Initialize members of the class
        self.description: str = description
        self.inline_policies: Sequence[policy_details_.PolicyDetails] = inline_policies
        self.managed_policies: Sequence[policy_details_.PolicyDetails] = managed_policies
        self.steps: str = steps
        self.trust_policy: object = trust_policy

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
        val = dictionary['description']
        val_description = val

        val = dictionary['inline_policies']

        val_inline_policies = None
        if val:
            val_inline_policies = list()
            for value in val:
                val_inline_policies.append(policy_details_.PolicyDetails.from_dictionary(value))

        val = dictionary['managed_policies']

        val_managed_policies = None
        if val:
            val_managed_policies = list()
            for value in val:
                val_managed_policies.append(policy_details_.PolicyDetails.from_dictionary(value))

        val = dictionary['steps']
        val_steps = val

        val = dictionary['trust_policy']
        val_trust_policy = val

        # Return an object of this model
        return cls(
            val_description,  # type: ignore
            val_inline_policies,  # type: ignore
            val_managed_policies,  # type: ignore
            val_steps,  # type: ignore
            val_trust_policy,  # type: ignore
        )
