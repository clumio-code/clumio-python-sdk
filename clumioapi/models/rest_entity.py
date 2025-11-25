#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='RestEntity')


@dataclasses.dataclass
class RestEntity:
    """Implementation of the 'RestEntity' model.

    Attributes:
        Id:
            A system-generated id assigned to this entity.

        Type:
            Type is mostly an asset type or the type of entity. some examples are
            "restored_file", "aws_ebs_volume",  etc.

        Value:
            A system-generated value assigned to the entity. for example, if the primary
            entity type is "aws_ebs_volume", then the value is the name of the ebs.

    """

    Id: str | None = None
    Type: str | None = None
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

        val = dictionary.get('type', None)
        val_type = val

        val = dictionary.get('value', None)
        val_value = val

        # Return an object of this model
        return cls(
            val_id,
            val_type,
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
