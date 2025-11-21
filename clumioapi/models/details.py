#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import rest_entity as rest_entity_
import requests

T = TypeVar('T', bound='Details')


@dataclasses.dataclass
class Details:
    """Implementation of the 'Details' model.

    Attributes:
        RequestBody:
            The request body of the api call.

        RequestUrl:
            The request url of the api call. this is omitempty because only internal
            namespace should return a request_url and prod should not see that
            a request_url is being returned.

        Tags:
            The list of various entities related to the operation performed.

    """

    RequestBody: object | None = None
    RequestUrl: str | None = None
    Tags: Sequence[rest_entity_.RestEntity] | None = None

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
        val = dictionary.get('request_body', None)
        val_request_body = val

        val = dictionary.get('request_url', None)
        val_request_url = val

        val = dictionary.get('tags', None)

        val_tags = []
        if val:
            for value in val:
                val_tags.append(rest_entity_.RestEntity.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_request_body,
            val_request_url,
            val_tags,
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
