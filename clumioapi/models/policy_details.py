#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='PolicyDetails')


class PolicyDetails:
    """Implementation of the 'PolicyDetails' model.

    Attributes:
        description:
            "description" is a Clumio assigned term. User can choose to ignore it.
        name:
            "name" is a Clumio assigned term. User can choose to ignore it.
        policy_document:
            "policy_document" has stringified JSON blob. The user has to JSONify it and then
            paste
            the JSONified blob in aws console while creating the policy.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'description': 'description',
        'name': 'name',
        'policy_document': 'policy_document',
    }

    def __init__(
        self,
        description: str | None = None,
        name: str | None = None,
        policy_document: object | None = None,
    ) -> None:
        """Constructor for the PolicyDetails class."""

        # Initialize members of the class
        self.description: str | None = description
        self.name: str | None = name
        self.policy_document: object | None = policy_document

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
