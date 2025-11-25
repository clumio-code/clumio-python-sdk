#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import restore_s3_bucket_source as restore_s3_bucket_source_
from clumioapi.models import restore_s3_bucket_target as restore_s3_bucket_target_
import requests

T = TypeVar('T', bound='RestoreAwsS3BucketV1Request')

TypeValues = [
    'Rollback',
    'Undo delete marker',
]


@dataclasses.dataclass
class RestoreAwsS3BucketV1Request:
    """Implementation of the 'RestoreAwsS3BucketV1Request' model.

    Attributes:
        Source:
            The parameters for initiating an s3 bucket restore.

        Target:
            The destination where the s3 bucket will be restored.

        Type:
            Type to be used during restore. if not specified, the default value is
            "rollback".
            "rollback" and "undo delete marker" value will be deprecated. use "rollback" and
            "undo_delete_marker" respectively.

    """

    Source: restore_s3_bucket_source_.RestoreS3BucketSource | None = None
    Target: restore_s3_bucket_target_.RestoreS3BucketTarget | None = None

    Type: str | None = None

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
        val = dictionary.get('source', None)
        val_source = restore_s3_bucket_source_.RestoreS3BucketSource.from_dictionary(val)

        val = dictionary.get('target', None)
        val_target = restore_s3_bucket_target_.RestoreS3BucketTarget.from_dictionary(val)

        val = dictionary.get('type', None)
        val_type = val

        # Return an object of this model
        return cls(
            val_source,
            val_target,
            val_type,
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
