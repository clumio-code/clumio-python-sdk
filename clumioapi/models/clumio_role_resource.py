#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import policy_details as policy_details_
import requests

T = TypeVar('T', bound='ClumioRoleResource')


@dataclasses.dataclass
class ClumioRoleResource:
    """Implementation of the 'ClumioRoleResource' model.

    Details for the IAM Role

    Attributes:
        Description

        InlinePolicies:
            "inline_policies" stores all the customer inline policies to be attached to the
            role.

        ManagedPolicies:
            "managed_policies" stores all the customer managed policies to be attached to
            the role.

        Steps

        TrustPolicy:
            "trust_policy" stores the trust relationship policy for the role. it is a
            stringified json blob.
            the user has to jsonify it and then paste the jsonified blob in aws console
            while creating the role.

    """

    Description: str | None = None
    InlinePolicies: Sequence[policy_details_.PolicyDetails] | None = None
    ManagedPolicies: Sequence[policy_details_.PolicyDetails] | None = None
    Steps: str | None = None
    TrustPolicy: object | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('inline_policies', None)

        val_inline_policies = []
        if val:
            for value in val:
                val_inline_policies.append(policy_details_.PolicyDetails.from_dictionary(value))

        val = dictionary.get('managed_policies', None)

        val_managed_policies = []
        if val:
            for value in val:
                val_managed_policies.append(policy_details_.PolicyDetails.from_dictionary(value))

        val = dictionary.get('steps', None)
        val_steps = val

        val = dictionary.get('trust_policy', None)
        val_trust_policy = val

        # Return an object of this model
        return cls(
            val_description,
            val_inline_policies,
            val_managed_policies,
            val_steps,
            val_trust_policy,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
