#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='S3InstantAccessEndpointRole')


@dataclasses.dataclass
class S3InstantAccessEndpointRole:
    """Implementation of the 'S3InstantAccessEndpointRole' model.

    IAM role which is allowed access to the OLAP endpoint.

    Attributes:
        Alias:
            The alias of the iam role given by the user in the ui.

        Arn:
            The arn of the iam role.

        Id:
            The id of the iam role. used as an identifier in the api url.

        LastModifiedTimestamp:
            The time when the role was last modified, in rfc-3339 format.

    """

    Alias: str | None = None
    Arn: str | None = None
    Id: str | None = None
    LastModifiedTimestamp: str | None = None

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
        val = dictionary.get('alias', None)
        val_alias = val

        val = dictionary.get('arn', None)
        val_arn = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('last_modified_timestamp', None)
        val_last_modified_timestamp = val

        # Return an object of this model
        return cls(
            val_alias,
            val_arn,
            val_id,
            val_last_modified_timestamp,
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
