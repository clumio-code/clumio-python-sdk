#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_server_side_encryption_by_default

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
    _names = {
        'apply_server_side_encryption_by_default': 'apply_server_side_encryption_by_default',
        'bucket_key_enabled': 'bucket_key_enabled',
    }

    def __init__(
        self,
        apply_server_side_encryption_by_default: s3_server_side_encryption_by_default.S3ServerSideEncryptionByDefault = None,
        bucket_key_enabled: bool = None,
    ) -> None:
        """Constructor for the S3ServerSideEncryptionRule class."""

        # Initialize members of the class
        self.apply_server_side_encryption_by_default: s3_server_side_encryption_by_default.S3ServerSideEncryptionByDefault = (
            apply_server_side_encryption_by_default
        )
        self.bucket_key_enabled: bool = bucket_key_enabled

    @classmethod
    def from_dictionary(cls: Type, dictionary: Mapping[str, Any]) -> Optional[T]:
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
        key = 'apply_server_side_encryption_by_default'
        apply_server_side_encryption_by_default = (
            s3_server_side_encryption_by_default.S3ServerSideEncryptionByDefault.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        bucket_key_enabled = dictionary.get('bucket_key_enabled')
        # Return an object of this model
        return cls(apply_server_side_encryption_by_default, bucket_key_enabled)
