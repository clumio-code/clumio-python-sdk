#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='PolicyDetails')


@dataclasses.dataclass
class PolicyDetails:
    """Implementation of the 'PolicyDetails' model.

        Attributes:
            Description:
                "description" is a clumio assigned term. user can choose to ignore it.

            Name:
                "name" is a clumio assigned term. user can choose to ignore it.

            PolicyDocument:
                "policy_document" has stringified json blob. the user has to jsonify it and then paste
    the jsonified blob in aws console while creating the policy.

    """

    Description: str | None = None
    Name: str | None = None
    PolicyDocument: object | None = None

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
        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('policy_document', None)
        val_policy_document = val

        # Return an object of this model
        return cls(
            val_description,
            val_name,
            val_policy_document,
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
