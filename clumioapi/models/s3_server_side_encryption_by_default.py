#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3ServerSideEncryptionByDefault')


class S3ServerSideEncryptionByDefault:
    """Implementation of the 'S3ServerSideEncryptionByDefault' model.

    Describes the default server-side encryption to apply to new objects in the
    bucket.

    Attributes:
        kms_master_key_id:
            AWS Key Management Service (KMS) customer AWS KMS key ID to use for the default
            encryption.
        sse_algorithm:
            Server-side encryption algorithm to use for the default encryption.
    """

    # Create a mapping from Model property names to API property names
    _names = {'kms_master_key_id': 'kms_master_key_id', 'sse_algorithm': 'sse_algorithm'}

    def __init__(self, kms_master_key_id: str = None, sse_algorithm: str = None) -> None:
        """Constructor for the S3ServerSideEncryptionByDefault class."""

        # Initialize members of the class
        self.kms_master_key_id: str = kms_master_key_id
        self.sse_algorithm: str = sse_algorithm

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
        kms_master_key_id = dictionary.get('kms_master_key_id')
        sse_algorithm = dictionary.get('sse_algorithm')
        # Return an object of this model
        return cls(kms_master_key_id, sse_algorithm)
