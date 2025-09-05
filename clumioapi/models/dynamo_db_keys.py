#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import attribute_definition as attribute_definition_

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
    _names: dict[str, str] = {'partition_key': 'partition_key', 'sort_key': 'sort_key'}

    def __init__(
        self,
        partition_key: attribute_definition_.AttributeDefinition | None = None,
        sort_key: attribute_definition_.AttributeDefinition | None = None,
    ) -> None:
        """Constructor for the DynamoDBKeys class."""

        # Initialize members of the class
        self.partition_key: attribute_definition_.AttributeDefinition | None = partition_key
        self.sort_key: attribute_definition_.AttributeDefinition | None = sort_key

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
        val = dictionary.get('partition_key', None)
        val_partition_key = attribute_definition_.AttributeDefinition.from_dictionary(val)

        val = dictionary.get('sort_key', None)
        val_sort_key = attribute_definition_.AttributeDefinition.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_partition_key,
            val_sort_key,
        )
