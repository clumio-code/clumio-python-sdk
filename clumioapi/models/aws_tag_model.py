#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='AwsTagModel')


@dataclasses.dataclass
class AwsTagModel:
    """Implementation of the 'AwsTagModel' model.

    A tag created through AWS console which can be applied to EBS volumes.

    Attributes:
        Id:
            The clumio-assigned id of the aws tag.

        Key:
            The aws-assigned tag key.

        KeyId:
            The clumio-assigned id of the aws key.

        Value:
            The aws-assigned tag value.

    """

    Id: str | None = None
    Key: str | None = None
    KeyId: str | None = None
    Value: str | None = None

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
        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('key', None)
        val_key = val

        val = dictionary.get('key_id', None)
        val_key_id = val

        val = dictionary.get('value', None)
        val_value = val

        # Return an object of this model
        return cls(
            val_id,
            val_key,
            val_key_id,
            val_value,
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
