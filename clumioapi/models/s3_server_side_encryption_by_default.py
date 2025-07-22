#
# Copyright 2023. Clumio, A Commvault Company.
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
    _names: dict[str, str] = {
        'kms_master_key_id': 'kms_master_key_id',
        'sse_algorithm': 'sse_algorithm',
    }

    def __init__(self, kms_master_key_id: str, sse_algorithm: str) -> None:
        """Constructor for the S3ServerSideEncryptionByDefault class."""

        # Initialize members of the class
        self.kms_master_key_id: str = kms_master_key_id
        self.sse_algorithm: str = sse_algorithm

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
        val = dictionary['kms_master_key_id']
        val_kms_master_key_id = val

        val = dictionary['sse_algorithm']
        val_sse_algorithm = val

        # Return an object of this model
        return cls(
            val_kms_master_key_id,  # type: ignore
            val_sse_algorithm,  # type: ignore
        )
