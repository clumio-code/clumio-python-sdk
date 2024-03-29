#
# Copyright 2023. Clumio, Inc.
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
    _names = {'description': 'description', 'name': 'name', 'policy_document': 'policy_document'}

    def __init__(
        self, description: str = None, name: str = None, policy_document: object = None
    ) -> None:
        """Constructor for the PolicyDetails class."""

        # Initialize members of the class
        self.description: str = description
        self.name: str = name
        self.policy_document: object = policy_document

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
        name = dictionary.get('name')
        policy_document = dictionary.get('policy_document')
        # Return an object of this model
        return cls(description, name, policy_document)
