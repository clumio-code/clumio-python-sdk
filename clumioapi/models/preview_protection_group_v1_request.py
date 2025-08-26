#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import source_object_filters as source_object_filters_
import requests

T = TypeVar('T', bound='PreviewProtectionGroupV1Request')


@dataclasses.dataclass
class PreviewProtectionGroupV1Request:
    """Implementation of the 'PreviewProtectionGroupV1Request' model.

        Attributes:
            BackupId:
                The clumio-assigned id of the protection group backup to be restored. use the
    [get /backups/protection-groups](#operation/list-backup-protection-groups)
    endpoint to fetch valid values.

            IsSyncPreview:
                Whether to wait for the preview task.

            ObjectFilters:
                Search for or restore only objects that pass the source object filter.

            PitrEndTimestamp:
                The end timestamp of the period within which objects are to be restored, in rfc-3339
    format. clumio searches for objects modified before the given time. if `pitr_end_timestamp`
    is empty, clumio searches for objects modified up to the current time of the restore request.
     if `pitr_end_timestamp` is given without `pitr_start_timestamp`,
    it is the same as point in time preview.

            PitrStartTimestamp:
                The start timestamp of the period within which objects are to be restored, in rfc-3339
    format. clumio searches for objects modified since the given time. if `pitr_start_timestamp`
    is empty, clumio searches for objects from the beginning of the first backup.

            ProtectionGroupS3AssetIds:
                A list of clumio-assigned ids of protection group s3 assets, representing the
    buckets within the protection group to restore from. use the
    [get /datasources/protection-groups/s3-assets](#operation/list-protection-group-s3-assets)
    endpoint to fetch valid values.

    """

    BackupId: str | None = None
    IsSyncPreview: bool | None = None
    ObjectFilters: source_object_filters_.SourceObjectFilters | None = None
    PitrEndTimestamp: str | None = None
    PitrStartTimestamp: str | None = None
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

        val = dictionary.get('is_sync_preview', None)
        val_is_sync_preview = val

        val = dictionary.get('object_filters', None)
        val_object_filters = source_object_filters_.SourceObjectFilters.from_dictionary(val)

        val = dictionary.get('pitr_end_timestamp', None)
        val_pitr_end_timestamp = val

        val = dictionary.get('pitr_start_timestamp', None)
        val_pitr_start_timestamp = val

        val = dictionary.get('protection_group_s3_asset_ids', None)
        val_protection_group_s3_asset_ids = val

        # Return an object of this model
        return cls(
            val_backup_id,
            val_is_sync_preview,
            val_object_filters,
            val_pitr_end_timestamp,
            val_pitr_start_timestamp,
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
