#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_replica_modifications
from clumioapi.models import s3_sse_kms_encrypted_objects

T = TypeVar('T', bound='S3SourceSelectionCriteria')


class S3SourceSelectionCriteria:
    """Implementation of the 'S3SourceSelectionCriteria' model.

    A container that describes additional filters for identifyingthe source objects
    that you want to replicate.

    Attributes:
        replica_modifications:
            A filter that you can specify for selection for modifications on replicas.
        sse_kms_encrypted_objects:
            A container for filter information for the selection of
            S3 objects encrypted with AWS KMS.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'replica_modifications': 'replica_modifications',
        'sse_kms_encrypted_objects': 'sse_kms_encrypted_objects',
    }

    def __init__(
        self,
        replica_modifications: s3_replica_modifications.S3ReplicaModifications = None,
        sse_kms_encrypted_objects: s3_sse_kms_encrypted_objects.S3SseKmsEncryptedObjects = None,
    ) -> None:
        """Constructor for the S3SourceSelectionCriteria class."""

        # Initialize members of the class
        self.replica_modifications: s3_replica_modifications.S3ReplicaModifications = (
            replica_modifications
        )
        self.sse_kms_encrypted_objects: s3_sse_kms_encrypted_objects.S3SseKmsEncryptedObjects = (
            sse_kms_encrypted_objects
        )

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
        key = 'replica_modifications'
        replica_modifications = (
            s3_replica_modifications.S3ReplicaModifications.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'sse_kms_encrypted_objects'
        sse_kms_encrypted_objects = (
            s3_sse_kms_encrypted_objects.S3SseKmsEncryptedObjects.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(replica_modifications, sse_kms_encrypted_objects)
