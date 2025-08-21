#
# Copyright 2023. Clumio, A Commvault Company.
#
from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.exceptions import clumio_exception
from clumioapi.models import restore_s3_bucket_source as restore_s3_bucket_source_
from clumioapi.models import restore_s3_bucket_target as restore_s3_bucket_target_

T = TypeVar('T', bound='RestoreAwsS3BucketV1Request')

TypeValues = [
    'Rollback',
    'Undo delete marker',
]


class RestoreAwsS3BucketV1Request:
    """Implementation of the 'RestoreAwsS3BucketV1Request' model.

    Attributes:
        source:
            The parameters for initiating an S3 bucket restore.
        target:
            The destination where the S3 bucket will be restored.
        p_type:
            Type to be used during restore. If not specified, the default value is
            "Rollback".
            "Rollback" and "Undo delete marker" value will be deprecated. Use "rollback" and
            "undo_delete_marker" respectively.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'source': 'source', 'target': 'target', 'p_type': 'type'}

    def __init__(
        self,
        source: restore_s3_bucket_source_.RestoreS3BucketSource | None = None,
        target: restore_s3_bucket_target_.RestoreS3BucketTarget | None = None,
        p_type: str | None = None,
    ) -> None:
        """Constructor for the RestoreAwsS3BucketV1Request class."""

        # Initialize members of the class
        self.source: restore_s3_bucket_source_.RestoreS3BucketSource | None = source
        self.target: restore_s3_bucket_target_.RestoreS3BucketTarget | None = target

        if p_type not in TypeValues:
            raise clumio_exception.ClumioException(
                f'Invalid value for p_type: { p_type }. Valid values are { TypeValues }.'
            )
        self.p_type: str | None = p_type

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

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('source', None)
        val_source = restore_s3_bucket_source_.RestoreS3BucketSource.from_dictionary(val)

        val = dictionary.get('target', None)
        val_target = restore_s3_bucket_target_.RestoreS3BucketTarget.from_dictionary(val)

        val = dictionary.get('type', None)
        val_p_type = val

        # Return an object of this model
        return cls(
            val_source,
            val_target,
            val_p_type,
        )
