#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='DynamoDBGRRAttributeFilter')


@dataclasses.dataclass
class DynamoDBGRRAttributeFilter:
    """Implementation of the 'DynamoDBGRRAttributeFilter' model.

    Attributes:
        Condition:
            String and binary.                               |
            |                      |                                                       |
            +----------------------+-------------------------------------------------------+

        Name:
            Dynamodb attribute name.

        Type:
            Data-type of the dynamodb attribute.

            +----------------+
            | allowed values |
            +================+
            | string         |
            +----------------+
            | number         |
            +----------------+
            | binary         |
            +----------------+
            | boolean        |
            +----------------+
            | null           |
            +----------------+

        Values:
            Values for the attribute filter.

    """

    Condition: str | None = None
    Name: str | None = None
    Type: str | None = None
    Values: Sequence[str] | None = None

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
        val = dictionary.get('condition', None)
        val_condition = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('type', None)
        val_type = val

        val = dictionary.get('values', None)
        val_values = val

        # Return an object of this model
        return cls(
            val_condition,
            val_name,
            val_type,
            val_values,
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
