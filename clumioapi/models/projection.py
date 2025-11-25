#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='Projection')


@dataclasses.dataclass
class Projection:
    """Implementation of the 'Projection' model.

    Represents attributes that are copied (projected) from the table into an index.
    These are in addition to theprimary key attributes and index key attributes,
    which are automatically projected.

    Attributes:
        NonKeyAttributes:
            Represents the non-key attribute names which will be projected into the index.
            for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this
            must be empty if
            'projection_type' is all or keys_only, and non-empty if 'projection_type' is
            include.

        ProjectionType:
            All, keys_only, include.

    """

    NonKeyAttributes: Sequence[str] | None = None
    ProjectionType: str | None = None

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
        val = dictionary.get('non_key_attributes', None)
        val_non_key_attributes = val

        val = dictionary.get('projection_type', None)
        val_projection_type = val

        # Return an object of this model
        return cls(
            val_non_key_attributes,
            val_projection_type,
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
