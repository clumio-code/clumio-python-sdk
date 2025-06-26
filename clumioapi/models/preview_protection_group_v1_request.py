#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import source_object_filters

T = TypeVar('T', bound='PreviewProtectionGroupV1Request')


class PreviewProtectionGroupV1Request:
    """Implementation of the 'PreviewProtectionGroupV1Request' model.

    Attributes:
        backup_id:
            The Clumio-assigned ID of the protection group backup to be restored. Use the
            [GET /backups/protection-groups](#operation/list-backup-protection-groups)
            endpoint to fetch valid values.
        is_sync_preview:
            Whether to wait for the preview task.
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
        protection_group_s3_asset_ids:
            A list of Clumio-assigned IDs of protection group S3 assets, representing the
            buckets within the protection group to restore from. Use the
            [GET /datasources/protection-groups/s3-assets](#operation/list-protection-
            group-s3-assets)
            endpoint to fetch valid values.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'backup_id': 'backup_id',
        'is_sync_preview': 'is_sync_preview',
        'object_filters': 'object_filters',
        'pitr_end_timestamp': 'pitr_end_timestamp',
        'pitr_start_timestamp': 'pitr_start_timestamp',
        'protection_group_s3_asset_ids': 'protection_group_s3_asset_ids',
    }

    def __init__(
        self,
        backup_id: str = None,
        is_sync_preview: bool = None,
        object_filters: source_object_filters.SourceObjectFilters = None,
        pitr_end_timestamp: str = None,
        pitr_start_timestamp: str = None,
        protection_group_s3_asset_ids: Sequence[str] = None,
    ) -> None:
        """Constructor for the PreviewProtectionGroupV1Request class."""

        # Initialize members of the class
        self.backup_id: str = backup_id
        self.is_sync_preview: bool = is_sync_preview
        self.object_filters: source_object_filters.SourceObjectFilters = object_filters
        self.pitr_end_timestamp: str = pitr_end_timestamp
        self.pitr_start_timestamp: str = pitr_start_timestamp
        self.protection_group_s3_asset_ids: Sequence[str] = protection_group_s3_asset_ids

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
        backup_id = dictionary.get('backup_id')
        is_sync_preview = dictionary.get('is_sync_preview')
        key = 'object_filters'
        object_filters = (
            source_object_filters.SourceObjectFilters.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        pitr_end_timestamp = dictionary.get('pitr_end_timestamp')
        pitr_start_timestamp = dictionary.get('pitr_start_timestamp')
        protection_group_s3_asset_ids = dictionary.get('protection_group_s3_asset_ids')
        # Return an object of this model
        return cls(
            backup_id,
            is_sync_preview,
            object_filters,
            pitr_end_timestamp,
            pitr_start_timestamp,
            protection_group_s3_asset_ids,
        )
