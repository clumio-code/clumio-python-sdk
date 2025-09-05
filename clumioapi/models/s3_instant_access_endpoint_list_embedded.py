#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import s3_instant_access_endpoint as s3_instant_access_endpoint_
import requests

T = TypeVar('T', bound='S3InstantAccessEndpointListEmbedded')


@dataclasses.dataclass
class S3InstantAccessEndpointListEmbedded:
    """Implementation of the 'S3InstantAccessEndpointListEmbedded' model.

        Embedded responses related to the resource.

        Attributes:
            Items:
    A collection of requested items.

    """

    Items: Sequence[s3_instant_access_endpoint_.S3InstantAccessEndpoint] | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self,
            dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v not in [None, {}]},
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
        val = dictionary.get('items', None)

        val_items = []
        if val:
            for value in val:
                val_items.append(
                    s3_instant_access_endpoint_.S3InstantAccessEndpoint.from_dictionary(value)
                )

        # Return an object of this model
        return cls(
            val_items,
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
