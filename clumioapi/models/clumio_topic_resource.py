#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import policy_details as policy_details_
import requests

T = TypeVar('T', bound='ClumioTopicResource')


@dataclasses.dataclass
class ClumioTopicResource:
    """Implementation of the 'ClumioTopicResource' model.

    Details for the SNS Topic

    Attributes:
        Policies:
            "policies" stores all the policies to be attached to the topic.

        Steps:
            "steps" refers to commands to be executed.

    """

    Policies: Sequence[policy_details_.PolicyDetails] | None = None
    Steps: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
        val = dictionary.get('policies', None)

        val_policies = []
        if val:
            for value in val:
                val_policies.append(policy_details_.PolicyDetails.from_dictionary(value))

        val = dictionary.get('steps', None)
        val_steps = val

        # Return an object of this model
        return cls(
            val_policies,
            val_steps,
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
