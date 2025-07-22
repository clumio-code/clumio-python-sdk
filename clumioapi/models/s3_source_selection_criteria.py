#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_replica_modifications as s3_replica_modifications_
from clumioapi.models import s3_sse_kms_encrypted_objects as s3_sse_kms_encrypted_objects_

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
    _names: dict[str, str] = {
        'replica_modifications': 'replica_modifications',
        'sse_kms_encrypted_objects': 'sse_kms_encrypted_objects',
    }

    def __init__(
        self,
        replica_modifications: s3_replica_modifications_.S3ReplicaModifications,
        sse_kms_encrypted_objects: s3_sse_kms_encrypted_objects_.S3SseKmsEncryptedObjects,
    ) -> None:
        """Constructor for the S3SourceSelectionCriteria class."""

        # Initialize members of the class
        self.replica_modifications: s3_replica_modifications_.S3ReplicaModifications = (
            replica_modifications
        )
        self.sse_kms_encrypted_objects: s3_sse_kms_encrypted_objects_.S3SseKmsEncryptedObjects = (
            sse_kms_encrypted_objects
        )

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
        val = dictionary['replica_modifications']
        val_replica_modifications = (
            s3_replica_modifications_.S3ReplicaModifications.from_dictionary(val)
        )

        val = dictionary['sse_kms_encrypted_objects']
        val_sse_kms_encrypted_objects = (
            s3_sse_kms_encrypted_objects_.S3SseKmsEncryptedObjects.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_replica_modifications,  # type: ignore
            val_sse_kms_encrypted_objects,  # type: ignore
        )
