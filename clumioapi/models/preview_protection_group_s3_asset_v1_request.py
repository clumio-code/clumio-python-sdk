#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import source_object_filters as source_object_filters_

T = TypeVar('T', bound='PreviewProtectionGroupS3AssetV1Request')


class PreviewProtectionGroupS3AssetV1Request:
    """Implementation of the 'PreviewProtectionGroupS3AssetV1Request' model.

    Attributes:
        backup_id:
            Backup ID.
        is_sync_preview:
            Response type to be sync
        object_filters:
            Search for or restore only objects that pass the source object filter.
        pitr_end_timestamp:
            The end timestamp of the period within which objects are to be restored, in
            RFC-3339
            format. Clumio searches for objects modified before the given time. If
            `pitr_end_timestamp`
            is empty, Clumio searches for objects modified up to the current time of the
            restore request.
             If `pitr_end_timestamp` is given without `pitr_start_timestamp`,
            it is the same as point in time preview.
        pitr_start_timestamp:
            The start timestamp of the period within which objects are to be restored, in
            RFC-3339
            format. Clumio searches for objects modified since the given time. If
            `pitr_start_timestamp`
            is empty, Clumio searches for objects from the beginning of the first backup.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'backup_id': 'backup_id',
        'is_sync_preview': 'is_sync_preview',
        'object_filters': 'object_filters',
        'pitr_end_timestamp': 'pitr_end_timestamp',
        'pitr_start_timestamp': 'pitr_start_timestamp',
    }

    def __init__(
        self,
        backup_id: str,
        is_sync_preview: bool,
        object_filters: source_object_filters_.SourceObjectFilters,
        pitr_end_timestamp: str,
        pitr_start_timestamp: str,
    ) -> None:
        """Constructor for the PreviewProtectionGroupS3AssetV1Request class."""

        # Initialize members of the class
        self.backup_id: str = backup_id
        self.is_sync_preview: bool = is_sync_preview
        self.object_filters: source_object_filters_.SourceObjectFilters = object_filters
        self.pitr_end_timestamp: str = pitr_end_timestamp
        self.pitr_start_timestamp: str = pitr_start_timestamp

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
        val = dictionary['backup_id']
        val_backup_id = val

        val = dictionary['is_sync_preview']
        val_is_sync_preview = val

        val = dictionary['object_filters']
        val_object_filters = source_object_filters_.SourceObjectFilters.from_dictionary(val)

        val = dictionary['pitr_end_timestamp']
        val_pitr_end_timestamp = val

        val = dictionary['pitr_start_timestamp']
        val_pitr_start_timestamp = val

        # Return an object of this model
        return cls(
            val_backup_id,  # type: ignore
            val_is_sync_preview,  # type: ignore
            val_object_filters,  # type: ignore
            val_pitr_end_timestamp,  # type: ignore
            val_pitr_start_timestamp,  # type: ignore
        )
