#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import attribute_definition

T = TypeVar('T', bound='DynamoDBKeys')


class DynamoDBKeys:
    """Implementation of the 'DynamoDBKeys' model.

    Represents the DynamoDB table keys.

    Attributes:
        partition_key:
            Represents the attributes within a DynamoDB table by the name
            and the data type (`S` for string, `N` for number, `B` for binary).
        sort_key:
            Represents the attributes within a DynamoDB table by the name
            and the data type (`S` for string, `N` for number, `B` for binary).
    """

    # Create a mapping from Model property names to API property names
    _names = {'partition_key': 'partition_key', 'sort_key': 'sort_key'}

    def __init__(
        self,
        partition_key: attribute_definition.AttributeDefinition = None,
        sort_key: attribute_definition.AttributeDefinition = None,
    ) -> None:
        """Constructor for the DynamoDBKeys class."""

        # Initialize members of the class
        self.partition_key: attribute_definition.AttributeDefinition = partition_key
        self.sort_key: attribute_definition.AttributeDefinition = sort_key

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
        key = 'partition_key'
        partition_key = (
            attribute_definition.AttributeDefinition.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'sort_key'
        sort_key = (
            attribute_definition.AttributeDefinition.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(partition_key, sort_key)
