#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    restore_s3_bucket_source_pitr_options as restore_s3_bucket_source_pitr_options_
from clumioapi.models import \
    restore_s3_bucket_source_undo_delete_marker_options as \
    restore_s3_bucket_source_undo_delete_marker_options_
from clumioapi.models import source_object_filters_v2 as source_object_filters_v2_

T = TypeVar('T', bound='RestoreS3BucketSource')


class RestoreS3BucketSource:
    """Implementation of the 'RestoreS3BucketSource' model.

    The parameters for initiating an S3 bucket restore.

    Attributes:
        bucket_id:
            The Clumio-assigned ID of the bucket to be restored. Use the
            [GET /datasources/aws/s3-buckets](#operation/list-aws-s3-buckets) endpoint
            to fetch valid values.
        object_filters:
            Search for or restore only objects that pass the source object filter.
        point_in_time_recovery:
            This field is required when the request type is 'Rollback'. The parameters for
            initiating a point in time restore.
        undo_delete_marker_options:
            This field is required when the request type is 'Undo delete marker'.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'bucket_id': 'bucket_id',
        'object_filters': 'object_filters',
        'point_in_time_recovery': 'point_in_time_recovery',
        'undo_delete_marker_options': 'undo_delete_marker_options',
    }

    def __init__(
        self,
        bucket_id: str,
        object_filters: source_object_filters_v2_.SourceObjectFiltersV2,
        point_in_time_recovery: restore_s3_bucket_source_pitr_options_.RestoreS3BucketSourcePitrOptions,
        undo_delete_marker_options: restore_s3_bucket_source_undo_delete_marker_options_.RestoreS3BucketSourceUndoDeleteMarkerOptions,
    ) -> None:
        """Constructor for the RestoreS3BucketSource class."""

        # Initialize members of the class
        self.bucket_id: str = bucket_id
        self.object_filters: source_object_filters_v2_.SourceObjectFiltersV2 = object_filters
        self.point_in_time_recovery: (
            restore_s3_bucket_source_pitr_options_.RestoreS3BucketSourcePitrOptions
        ) = point_in_time_recovery
        self.undo_delete_marker_options: (
            restore_s3_bucket_source_undo_delete_marker_options_.RestoreS3BucketSourceUndoDeleteMarkerOptions
        ) = undo_delete_marker_options

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
        val = dictionary['bucket_id']
        val_bucket_id = val

        val = dictionary['object_filters']
        val_object_filters = source_object_filters_v2_.SourceObjectFiltersV2.from_dictionary(val)

        val = dictionary['point_in_time_recovery']
        val_point_in_time_recovery = (
            restore_s3_bucket_source_pitr_options_.RestoreS3BucketSourcePitrOptions.from_dictionary(
                val
            )
        )

        val = dictionary['undo_delete_marker_options']
        val_undo_delete_marker_options = restore_s3_bucket_source_undo_delete_marker_options_.RestoreS3BucketSourceUndoDeleteMarkerOptions.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_bucket_id,  # type: ignore
            val_object_filters,  # type: ignore
            val_point_in_time_recovery,  # type: ignore
            val_undo_delete_marker_options,  # type: ignore
        )
