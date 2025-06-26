#
# Copyright 2023. Clumio, Inc.
#
from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.exceptions import clumio_exception
from clumioapi.models import restore_s3_bucket_source
from clumioapi.models import restore_s3_bucket_target

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
    _names = {'source': 'source', 'target': 'target', 'p_type': 'type'}

    def __init__(
        self,
        source: restore_s3_bucket_source.RestoreS3BucketSource = None,
        target: restore_s3_bucket_target.RestoreS3BucketTarget = None,
        p_type: str = None,
    ) -> None:
        """Constructor for the RestoreAwsS3BucketV1Request class."""

        # Initialize members of the class
        self.source: restore_s3_bucket_source.RestoreS3BucketSource = source
        self.target: restore_s3_bucket_target.RestoreS3BucketTarget = target

        if p_type not in TypeValues:
            raise clumio_exception.ClumioException(
                f'Invalid value for p_type: { p_type }. Valid values are { TypeValues }.',
                None,
            )
        self.p_type: str = p_type

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
        key = 'source'
        source = (
            restore_s3_bucket_source.RestoreS3BucketSource.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'target'
        target = (
            restore_s3_bucket_target.RestoreS3BucketTarget.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        p_type = dictionary.get('type')
        # Return an object of this model
        return cls(source, target, p_type)
