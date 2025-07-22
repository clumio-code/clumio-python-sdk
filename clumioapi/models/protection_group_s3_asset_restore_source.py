#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    protection_group_s3_asset_restore_source_pitr_options as \
    protection_group_s3_asset_restore_source_pitr_options_
from clumioapi.models import source_object_filters as source_object_filters_

T = TypeVar('T', bound='ProtectionGroupS3AssetRestoreSource')


class ProtectionGroupS3AssetRestoreSource:
    """Implementation of the 'ProtectionGroupS3AssetRestoreSource' model.

    The parameters for initiating a protection group S3 asset restoreor creation of
    an instant access endpoint from a backup.

    Attributes:
        backup_id:
            The Clumio-assigned ID of the protection group S3 asset backup to be restored.
            Use the
            [GET /backups/protection-groups/s3-assets](#operation/list-backup-protection-
            group-s3-assets)
            endpoint to fetch valid values.
            Note that only one of `backup_id` or `pitr` must be given.
        object_filters:
            Search for or restore only objects that pass the source object filter.
        pitr:
            The parameters for initiating a point in time restore.
            Note that only one of `backup_id` or `pitr` must be given.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'backup_id': 'backup_id',
        'object_filters': 'object_filters',
        'pitr': 'pitr',
    }

    def __init__(
        self,
        backup_id: str,
        object_filters: source_object_filters_.SourceObjectFilters,
        pitr: protection_group_s3_asset_restore_source_pitr_options_.ProtectionGroupS3AssetRestoreSourcePitrOptions,
    ) -> None:
        """Constructor for the ProtectionGroupS3AssetRestoreSource class."""

        # Initialize members of the class
        self.backup_id: str = backup_id
        self.object_filters: source_object_filters_.SourceObjectFilters = object_filters
        self.pitr: (
            protection_group_s3_asset_restore_source_pitr_options_.ProtectionGroupS3AssetRestoreSourcePitrOptions
        ) = pitr

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

        val = dictionary['object_filters']
        val_object_filters = source_object_filters_.SourceObjectFilters.from_dictionary(val)

        val = dictionary['pitr']
        val_pitr = protection_group_s3_asset_restore_source_pitr_options_.ProtectionGroupS3AssetRestoreSourcePitrOptions.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_backup_id,  # type: ignore
            val_object_filters,  # type: ignore
            val_pitr,  # type: ignore
        )
