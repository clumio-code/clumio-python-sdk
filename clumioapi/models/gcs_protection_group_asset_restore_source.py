#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
from clumioapi.models import \
    gcs_protection_group_asset_restore_source_pitr_options as \
    gcs_protection_group_asset_restore_source_pitr_options_
from clumioapi.models import gcs_source_object_filters as gcs_source_object_filters_
import requests

T = TypeVar('T', bound='GCSProtectionGroupAssetRestoreSource')


@dataclasses.dataclass
class GCSProtectionGroupAssetRestoreSource:
    """Implementation of the 'GCSProtectionGroupAssetRestoreSource' model.

    The parameters for initiating a GCS protection group asset restore from a
    backup.

    Attributes:
        BackupId:
            The clumio-assigned id of the protection group gcs asset backup to be restored.
            use the
            [get /backups/gcp/protection-groups/assets](#operation/list-backup-gcs-
            protection-group-assets)
            endpoint to fetch valid values.
            note that only one of `backup_id` or `pitr` must be given.

        ObjectFilters:
            Search for or restore only objects that pass the source object filter.

        Pitr:
            The parameters for initiating a gcs protection group asset restore from a point
            in time.

    """

    BackupId: str | None = None
    ObjectFilters: gcs_source_object_filters_.GCSSourceObjectFilters | None = None
    Pitr: (
        gcs_protection_group_asset_restore_source_pitr_options_.GCSProtectionGroupAssetRestoreSourcePitrOptions
        | None
    ) = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return api_helper.to_dictionary(self)

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('backup_id', None)
        val_backup_id = val

        val = dictionary.get('object_filters', None)
        val_object_filters = gcs_source_object_filters_.GCSSourceObjectFilters.from_dictionary(val)

        val = dictionary.get('pitr', None)
        val_pitr = gcs_protection_group_asset_restore_source_pitr_options_.GCSProtectionGroupAssetRestoreSourcePitrOptions.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_backup_id,
            val_object_filters,
            val_pitr,
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
