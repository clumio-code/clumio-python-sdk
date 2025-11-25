#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    s3_server_side_encryption_by_default as s3_server_side_encryption_by_default_
import requests

T = TypeVar('T', bound='S3ServerSideEncryptionRule')


@dataclasses.dataclass
class S3ServerSideEncryptionRule:
    """Implementation of the 'S3ServerSideEncryptionRule' model.

    Specifies the default server-side encryption configuration.

    Attributes:
        ApplyServerSideEncryptionByDefault:
            Describes the default server-side encryption to apply to new objects in the
            bucket.

        BucketKeyEnabled:
            Specifies whether amazon s3 should use an s3 bucket key with server-side
            encryption using kms (sse-kms) for new objects in the bucket.

    """

    ApplyServerSideEncryptionByDefault: (
        s3_server_side_encryption_by_default_.S3ServerSideEncryptionByDefault | None
    ) = None
    BucketKeyEnabled: bool | None = None

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
        val = dictionary.get('apply_server_side_encryption_by_default', None)
        val_apply_server_side_encryption_by_default = (
            s3_server_side_encryption_by_default_.S3ServerSideEncryptionByDefault.from_dictionary(
                val
            )
        )

        val = dictionary.get('bucket_key_enabled', None)
        val_bucket_key_enabled = val

        # Return an object of this model
        return cls(
            val_apply_server_side_encryption_by_default,
            val_bucket_key_enabled,
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
