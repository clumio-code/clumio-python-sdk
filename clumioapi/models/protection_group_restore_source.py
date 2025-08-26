#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    protection_group_restore_source_pitr_options as protection_group_restore_source_pitr_options_
from clumioapi.models import source_object_filters as source_object_filters_

T = TypeVar('T', bound='ProtectionGroupRestoreSource')


class ProtectionGroupRestoreSource:
    """Implementation of the 'ProtectionGroupRestoreSource' model.

    The parameters for initiating a protection group restore from a backup.

    Attributes:
        backup_id:
            The Clumio-assigned ID of the protection group backup to be restored. Use the
            [GET /backups/protection-groups](#operation/list-backup-protection-groups)
            endpoint to fetch valid values.
            Note that only one of `backup_id` or `pitr` must be given.
        object_filters:
            Search for or restore only objects that pass the source object filter.
        pitr:
            The parameters for initiating a point in time restore.
            Note that only one of `backup_id` or `pitr` must be given.
        protection_group_s3_asset_ids:
            A list of Clumio-assigned IDs of protection group S3 assets, representing the
            buckets within the protection group to restore from. Use the
            [GET /datasources/protection-groups/s3-assets](#operation/list-protection-
            group-s3-assets)
            endpoint to fetch valid values.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'backup_id': 'backup_id',
        'object_filters': 'object_filters',
        'pitr': 'pitr',
        'protection_group_s3_asset_ids': 'protection_group_s3_asset_ids',
    }

    def __init__(
        self,
        backup_id: str | None = None,
        object_filters: source_object_filters_.SourceObjectFilters | None = None,
        pitr: (
            protection_group_restore_source_pitr_options_.ProtectionGroupRestoreSourcePitrOptions
            | None
        ) = None,
        protection_group_s3_asset_ids: Sequence[str] | None = None,
    ) -> None:
        """Constructor for the ProtectionGroupRestoreSource class."""

        # Initialize members of the class
        self.backup_id: str | None = backup_id
        self.object_filters: source_object_filters_.SourceObjectFilters | None = object_filters
        self.pitr: (
            protection_group_restore_source_pitr_options_.ProtectionGroupRestoreSourcePitrOptions
            | None
        ) = pitr
        self.protection_group_s3_asset_ids: Sequence[str] | None = protection_group_s3_asset_ids

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
        val = dictionary.get('backup_id', None)
        val_backup_id = val

        val = dictionary.get('object_filters', None)
        val_object_filters = source_object_filters_.SourceObjectFilters.from_dictionary(val)

        val = dictionary.get('pitr', None)
        val_pitr = protection_group_restore_source_pitr_options_.ProtectionGroupRestoreSourcePitrOptions.from_dictionary(
            val
        )

        val = dictionary.get('protection_group_s3_asset_ids', None)
        val_protection_group_s3_asset_ids = val

        # Return an object of this model
        return cls(
            val_backup_id,
            val_object_filters,
            val_pitr,
            val_protection_group_s3_asset_ids,
        )
