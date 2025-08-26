#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    protection_group_restore_source_pitr_options as protection_group_restore_source_pitr_options_
from clumioapi.models import source_object_filters as source_object_filters_
import requests

T = TypeVar('T', bound='ProtectionGroupRestoreSource')


@dataclasses.dataclass
class ProtectionGroupRestoreSource:
    """Implementation of the 'ProtectionGroupRestoreSource' model.

        The parameters for initiating a protection group restore from a backup.

        Attributes:
            BackupId:
                The clumio-assigned id of the protection group backup to be restored. use the
    [get /backups/protection-groups](#operation/list-backup-protection-groups)
    endpoint to fetch valid values.
    note that only one of `backup_id` or `pitr` must be given.

            ObjectFilters:
                Search for or restore only objects that pass the source object filter.

            Pitr:
                The parameters for initiating a point in time restore.
    note that only one of `backup_id` or `pitr` must be given.

            ProtectionGroupS3AssetIds:
                A list of clumio-assigned ids of protection group s3 assets, representing the
    buckets within the protection group to restore from. use the
    [get /datasources/protection-groups/s3-assets](#operation/list-protection-group-s3-assets)
    endpoint to fetch valid values.

    """

    BackupId: str | None = None
    ObjectFilters: source_object_filters_.SourceObjectFilters | None = None
    Pitr: (
        protection_group_restore_source_pitr_options_.ProtectionGroupRestoreSourcePitrOptions | None
    ) = None
    ProtectionGroupS3AssetIds: Sequence[str] | None = None

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
