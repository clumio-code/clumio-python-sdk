#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='S3ServerSideEncryptionByDefault')


@dataclasses.dataclass
class S3ServerSideEncryptionByDefault:
    """Implementation of the 'S3ServerSideEncryptionByDefault' model.

    Describes the default server-side encryption to apply to new objects in the
    bucket.

    Attributes:
        KmsMasterKeyId:
            Aws key management service (kms) customer aws kms key id to use for the default encryption.

        SseAlgorithm:
            Server-side encryption algorithm to use for the default encryption.

    """

    KmsMasterKeyId: str | None = None
    SseAlgorithm: str | None = None

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
        val = dictionary.get('kms_master_key_id', None)
        val_kms_master_key_id = val

        val = dictionary.get('sse_algorithm', None)
        val_sse_algorithm = val

        # Return an object of this model
        return cls(
            val_kms_master_key_id,
            val_sse_algorithm,
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
