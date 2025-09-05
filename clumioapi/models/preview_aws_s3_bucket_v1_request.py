#
# Copyright 2023. Clumio, A Commvault Company.
#
from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.exceptions import clumio_exception
from clumioapi.models import \
    restore_s3_bucket_source_pitr_options as restore_s3_bucket_source_pitr_options_
from clumioapi.models import \
    restore_s3_bucket_source_undo_delete_marker_options as \
    restore_s3_bucket_source_undo_delete_marker_options_
from clumioapi.models import source_object_filters_v2 as source_object_filters_v2_

T = TypeVar('T', bound='PreviewAwsS3BucketV1Request')

TypeValues = [
    'Rollback',
    'Undo delete marker',
]


class PreviewAwsS3BucketV1Request:
    """Implementation of the 'PreviewAwsS3BucketV1Request' model.

    Attributes:
        object_filters:
            Search for or restore only objects that pass the source object filter.
        point_in_time_recovery:
            This field is required when the request type is 'Rollback'. The parameters for
            initiating a point in time restore.
        p_type:
            Type to be used during preview. If not specified, the default value is
            "Rollback".
            "Rollback" and "Undo delete marker" value will be deprecated. Use "rollback" and
            "undo_delete_marker" respectively.
        undo_delete_marker_options:
            This field is required when the request type is 'Undo delete marker'.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'object_filters': 'object_filters',
        'point_in_time_recovery': 'point_in_time_recovery',
        'p_type': 'type',
        'undo_delete_marker_options': 'undo_delete_marker_options',
    }

    def __init__(
        self,
        object_filters: source_object_filters_v2_.SourceObjectFiltersV2 | None = None,
        point_in_time_recovery: (
            restore_s3_bucket_source_pitr_options_.RestoreS3BucketSourcePitrOptions | None
        ) = None,
        p_type: str | None = None,
        undo_delete_marker_options: (
            restore_s3_bucket_source_undo_delete_marker_options_.RestoreS3BucketSourceUndoDeleteMarkerOptions
            | None
        ) = None,
    ) -> None:
        """Constructor for the PreviewAwsS3BucketV1Request class."""

        # Initialize members of the class
        self.object_filters: source_object_filters_v2_.SourceObjectFiltersV2 | None = object_filters
        self.point_in_time_recovery: (
            restore_s3_bucket_source_pitr_options_.RestoreS3BucketSourcePitrOptions | None
        ) = point_in_time_recovery

        if p_type not in TypeValues:
            raise clumio_exception.ClumioException(
                f'Invalid value for p_type: { p_type }. Valid values are { TypeValues }.'
            )
        self.p_type: str | None = p_type
        self.undo_delete_marker_options: (
            restore_s3_bucket_source_undo_delete_marker_options_.RestoreS3BucketSourceUndoDeleteMarkerOptions
            | None
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

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('object_filters', None)
        val_object_filters = source_object_filters_v2_.SourceObjectFiltersV2.from_dictionary(val)

        val = dictionary.get('point_in_time_recovery', None)
        val_point_in_time_recovery = (
            restore_s3_bucket_source_pitr_options_.RestoreS3BucketSourcePitrOptions.from_dictionary(
                val
            )
        )

        val = dictionary.get('type', None)
        val_p_type = val

        val = dictionary.get('undo_delete_marker_options', None)
        val_undo_delete_marker_options = restore_s3_bucket_source_undo_delete_marker_options_.RestoreS3BucketSourceUndoDeleteMarkerOptions.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_object_filters,
            val_point_in_time_recovery,
            val_p_type,
            val_undo_delete_marker_options,
        )
