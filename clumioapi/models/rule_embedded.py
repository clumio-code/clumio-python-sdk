#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='RuleEmbedded')


class RuleEmbedded:
    """Implementation of the 'RuleEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        read_policy_definition:
            Embeds the associated policy of a protected resource in the response if
            requested using the `embed` query parameter. Unprotected resources will not have
            an associated policy.
    """

    # Create a mapping from Model property names to API property names
    _names = {'read_policy_definition': 'read-policy-definition'}

    def __init__(self, read_policy_definition: None = None) -> None:
        """Constructor for the RuleEmbedded class."""

        # Initialize members of the class
        self.read_policy_definition: object = read_policy_definition

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
        read_policy_definition = dictionary.get('read-policy-definition')
        # Return an object of this model
        return cls(read_policy_definition)
