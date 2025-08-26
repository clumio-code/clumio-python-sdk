#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    restore_s3_bucket_source_pitr_options as restore_s3_bucket_source_pitr_options_
from clumioapi.models import \
    restore_s3_bucket_source_undo_delete_marker_options as \
    restore_s3_bucket_source_undo_delete_marker_options_
from clumioapi.models import source_object_filters_v2 as source_object_filters_v2_
import requests

T = TypeVar('T', bound='PreviewAwsS3BucketV1Request')

TypeValues = [
    'Rollback',
    'Undo delete marker',
]


@dataclasses.dataclass
class PreviewAwsS3BucketV1Request:
    """Implementation of the 'PreviewAwsS3BucketV1Request' model.

        Attributes:
            ObjectFilters:
                Search for or restore only objects that pass the source object filter.

            PointInTimeRecovery:
                This field is required when the request type is 'rollback'. the parameters for initiating a point in time restore.

            Type:
                Type to be used during preview. if not specified, the default value is "rollback".
    "rollback" and "undo delete marker" value will be deprecated. use "rollback" and "undo_delete_marker" respectively.

            UndoDeleteMarkerOptions:
                This field is required when the request type is 'undo delete marker'.

    """

    ObjectFilters: source_object_filters_v2_.SourceObjectFiltersV2 | None = None
    PointInTimeRecovery: (
        restore_s3_bucket_source_pitr_options_.RestoreS3BucketSourcePitrOptions | None
    ) = None

    Type: str | None = None
    UndoDeleteMarkerOptions: (
        restore_s3_bucket_source_undo_delete_marker_options_.RestoreS3BucketSourceUndoDeleteMarkerOptions
        | None
    ) = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
        val_type = val

        val = dictionary.get('undo_delete_marker_options', None)
        val_undo_delete_marker_options = restore_s3_bucket_source_undo_delete_marker_options_.RestoreS3BucketSourceUndoDeleteMarkerOptions.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_object_filters,
            val_point_in_time_recovery,
            val_type,
            val_undo_delete_marker_options,
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
