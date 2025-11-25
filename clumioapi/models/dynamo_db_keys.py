#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import attribute_definition as attribute_definition_
import requests

T = TypeVar('T', bound='DynamoDBKeys')


@dataclasses.dataclass
class DynamoDBKeys:
    """Implementation of the 'DynamoDBKeys' model.

    Represents the DynamoDB table keys.

    Attributes:
        PartitionKey:
            Represents the attributes within a dynamodb table by the name
            and the data type (`s` for string, `n` for number, `b` for binary).

        SortKey:
            Represents the attributes within a dynamodb table by the name
            and the data type (`s` for string, `n` for number, `b` for binary).

    """

    PartitionKey: attribute_definition_.AttributeDefinition | None = None
    SortKey: attribute_definition_.AttributeDefinition | None = None

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
        val = dictionary.get('partition_key', None)
        val_partition_key = attribute_definition_.AttributeDefinition.from_dictionary(val)

        val = dictionary.get('sort_key', None)
        val_sort_key = attribute_definition_.AttributeDefinition.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_partition_key,
            val_sort_key,
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
