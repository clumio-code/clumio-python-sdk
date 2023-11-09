#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3SseKmsEncryptedObjects')


class S3SseKmsEncryptedObjects:
    """Implementation of the 'S3SseKmsEncryptedObjects' model.

    A container for filter information for the selection ofS3 objects encrypted with
    AWS KMS.

    Attributes:
        status:
            Specifies whether Amazon S3 replicates objects created with server-side
            encryption using an AWS KMS key stored in AWS Key Management Service.
    """

    # Create a mapping from Model property names to API property names
    _names = {'status': 'status'}

    def __init__(self, status: str = None) -> None:
        """Constructor for the S3SseKmsEncryptedObjects class."""

        # Initialize members of the class
        self.status: str = status

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
        status = dictionary.get('status')
        # Return an object of this model
        return cls(status)
