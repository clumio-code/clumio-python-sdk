#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import s3_replica_modifications as s3_replica_modifications_
from clumioapi.models import s3_sse_kms_encrypted_objects as s3_sse_kms_encrypted_objects_
import requests

T = TypeVar('T', bound='S3SourceSelectionCriteria')


@dataclasses.dataclass
class S3SourceSelectionCriteria:
    """Implementation of the 'S3SourceSelectionCriteria' model.

    A container that describes additional filters for identifyingthe source objects
    that you want to replicate.

    Attributes:
        ReplicaModifications:
            A filter that you can specify for selection for modifications on replicas.

        SseKmsEncryptedObjects:
            A container for filter information for the selection of
            s3 objects encrypted with aws kms.

    """

    ReplicaModifications: s3_replica_modifications_.S3ReplicaModifications | None = None
    SseKmsEncryptedObjects: s3_sse_kms_encrypted_objects_.S3SseKmsEncryptedObjects | None = None

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
        val = dictionary.get('replica_modifications', None)
        val_replica_modifications = (
            s3_replica_modifications_.S3ReplicaModifications.from_dictionary(val)
        )

        val = dictionary.get('sse_kms_encrypted_objects', None)
        val_sse_kms_encrypted_objects = (
            s3_sse_kms_encrypted_objects_.S3SseKmsEncryptedObjects.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_replica_modifications,
            val_sse_kms_encrypted_objects,
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
