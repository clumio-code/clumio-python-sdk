#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3EncryptionConfiguration')


class S3EncryptionConfiguration:
    """Implementation of the 'S3EncryptionConfiguration' model.

    Specifies encryption-related information for an Amazon S3 bucketthat is a
    destination for replicated objects.

    Attributes:
        replica_kms_key_id:
            Specifies the ID (Key ARN or Alias ARN) of the customer managed
            AWS KMS key stored in AWS Key Management Service (KMS) for the
            destination bucket.
    """

    # Create a mapping from Model property names to API property names
    _names = {'replica_kms_key_id': 'replica_kms_key_id'}

    def __init__(self, replica_kms_key_id: str = None) -> None:
        """Constructor for the S3EncryptionConfiguration class."""

        # Initialize members of the class
        self.replica_kms_key_id: str = replica_kms_key_id

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
        replica_kms_key_id = dictionary.get('replica_kms_key_id')
        # Return an object of this model
        return cls(replica_kms_key_id)
