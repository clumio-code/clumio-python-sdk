#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import s3_instant_access_source as s3_instant_access_source_
import requests

T = TypeVar('T', bound='CreateProtectionGroupInstantAccessEndpointV1Request')


@dataclasses.dataclass
class CreateProtectionGroupInstantAccessEndpointV1Request:
    """Implementation of the 'CreateProtectionGroupInstantAccessEndpointV1Request' model.

    Attributes:
        ExpiryTimestamp:
            The time that this endpoint expires at in rfc-3339 format.

        Name:
            The user-assigned name of the s3 instant access endpoint.

        Source:
            The parameters for creating a s3 instant access endpoint.

    """

    ExpiryTimestamp: str | None = None
    Name: str | None = None
    Source: s3_instant_access_source_.S3InstantAccessSource | None = None

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
        val = dictionary.get('expiry_timestamp', None)
        val_expiry_timestamp = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('source', None)
        val_source = s3_instant_access_source_.S3InstantAccessSource.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_expiry_timestamp,
            val_name,
            val_source,
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
