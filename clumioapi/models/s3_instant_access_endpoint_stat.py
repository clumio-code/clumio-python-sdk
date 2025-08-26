#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='S3InstantAccessEndpointStat')


@dataclasses.dataclass
class S3InstantAccessEndpointStat:
    """Implementation of the 'S3InstantAccessEndpointStat' model.

    S3InstantAccessEndpointStatStatistical metric related to the instant access
    endpoint.S3InstantAccessEndpointStat swagger: model S3InstantAccessEndpointStat

    Attributes:
        Count:
            The unit counts of the metric.

        Name:
            The name of the metric.

        Unit:
            Unit of the metric.

    """

    Count: int | None = None
    Name: str | None = None
    Unit: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
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
        val = dictionary.get('count', None)
        val_count = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('unit', None)
        val_unit = val

        # Return an object of this model
        return cls(
            val_count,
            val_name,
            val_unit,
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
