#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    s3_server_side_encryption_by_default as s3_server_side_encryption_by_default_

T = TypeVar('T', bound='S3ServerSideEncryptionRule')


class S3ServerSideEncryptionRule:
    """Implementation of the 'S3ServerSideEncryptionRule' model.

    Specifies the default server-side encryption configuration.

    Attributes:
        apply_server_side_encryption_by_default:
            Describes the default server-side encryption to apply to new objects in the
            bucket.
        bucket_key_enabled:
            Specifies whether Amazon S3 should use an S3 Bucket Key with server-side
            encryption using KMS (SSE-KMS) for new objects in the bucket.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'apply_server_side_encryption_by_default': 'apply_server_side_encryption_by_default',
        'bucket_key_enabled': 'bucket_key_enabled',
    }

    def __init__(
        self,
        apply_server_side_encryption_by_default: s3_server_side_encryption_by_default_.S3ServerSideEncryptionByDefault,
        bucket_key_enabled: bool,
    ) -> None:
        """Constructor for the S3ServerSideEncryptionRule class."""

        # Initialize members of the class
        self.apply_server_side_encryption_by_default: (
            s3_server_side_encryption_by_default_.S3ServerSideEncryptionByDefault
        ) = apply_server_side_encryption_by_default
        self.bucket_key_enabled: bool = bucket_key_enabled

    @classmethod
    def from_dictionary(cls: Type[T], dictionary: Mapping[str, Any]) -> T:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """

        # Extract variables from the dictionary
        val = dictionary['apply_server_side_encryption_by_default']
        val_apply_server_side_encryption_by_default = (
            s3_server_side_encryption_by_default_.S3ServerSideEncryptionByDefault.from_dictionary(
                val
            )
        )

        val = dictionary['bucket_key_enabled']
        val_bucket_key_enabled = val

        # Return an object of this model
        return cls(
            val_apply_server_side_encryption_by_default,  # type: ignore
            val_bucket_key_enabled,  # type: ignore
        )
