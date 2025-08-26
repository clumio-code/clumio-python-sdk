#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    s3_instant_access_source_pitr_options as s3_instant_access_source_pitr_options_
from clumioapi.models import source_object_filters as source_object_filters_
import requests

T = TypeVar('T', bound='S3InstantAccessSource')


@dataclasses.dataclass
class S3InstantAccessSource:
    """Implementation of the 'S3InstantAccessSource' model.

        The parameters for creating a S3 instant access endpoint.

        Attributes:
            BackupId:
                The clumio-assigned id of the protection group s3 asset backup or protection group backup to
    be restored. use the endpoints
    [get /backups/protection-groups/s3-assets](#operation/list-backup-protection-group-s3-assets)
    for protection group s3 asset backup, and
    [get /backups/protection-groups](#operation/list-backup-protection-groups)
    for protection group backups to fetch valid values.
    note that only one of either `backup_id` or `pitr` must be provided.

            ObjectFilters:
                Search for or restore only objects that pass the source object filter.

            Pitr:
                The parameters to initiate a point-in-time creation of s3 instant access endpoint.
    note that only one of either `backup_id` or `pitr` must be provided.

            ProtectionGroupS3AssetId:
                Clumio-assigned id of protection group s3 asset, representing the
    bucket within the protection group to restore from. use the
    [get /datasources/protection-groups/s3-assets](#operation/list-protection-group-s3-assets)
    endpoint to fetch valid values.

    """

    BackupId: str | None = None
    ObjectFilters: source_object_filters_.SourceObjectFilters | None = None
    Pitr: s3_instant_access_source_pitr_options_.S3InstantAccessSourcePitrOptions | None = None
    ProtectionGroupS3AssetId: str | None = None

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
        val_pitr = (
            s3_instant_access_source_pitr_options_.S3InstantAccessSourcePitrOptions.from_dictionary(
                val
            )
        )

        val = dictionary.get('protection_group_s3_asset_id', None)
        val_protection_group_s3_asset_id = val

        # Return an object of this model
        return cls(
            val_backup_id,
            val_object_filters,
            val_pitr,
            val_protection_group_s3_asset_id,
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
