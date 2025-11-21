#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='StreamSpecification')


@dataclasses.dataclass
class StreamSpecification:
    """Implementation of the 'StreamSpecification' model.

    Represents the DynamoDB Streams configuration for a table in DynamoDB.and the
    data type (`S` for string, `N` for number, `B` for binary).

    Attributes:
        Enabled:
            Indicates whether dynamodb streams is enabled (true) or disabled (false)
            on the table.

        ViewType:
            When an item in the table is modified, viewtype determines what information
            is written to the stream for this table. valid values for viewtype
            are:

            keys_only - only the key attributes of the modified item are written
            to the stream.

            new_image - the entire item, as it appears after it was modified, is
            written to the stream.

            old_image - the entire item, as it appeared before it was modified,
            is written to the stream.

            new_and_old_images - both the new and the old item images of the item
            are written to the stream.

    """

    Enabled: bool | None = None
    ViewType: str | None = None

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
        val = dictionary.get('enabled', None)
        val_enabled = val

        val = dictionary.get('view_type', None)
        val_view_type = val

        # Return an object of this model
        return cls(
            val_enabled,
            val_view_type,
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
