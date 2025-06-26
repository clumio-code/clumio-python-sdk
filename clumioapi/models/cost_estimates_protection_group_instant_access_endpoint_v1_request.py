#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_instant_access_source_pitr_options
from clumioapi.models import source_object_filters

T = TypeVar('T', bound='CostEstimatesProtectionGroupInstantAccessEndpointV1Request')


class CostEstimatesProtectionGroupInstantAccessEndpointV1Request:
    """Implementation of the 'CostEstimatesProtectionGroupInstantAccessEndpointV1Request' model.

    Attributes:
        backup_id:
            The Clumio-assigned ID of the protection group S3 asset backup or protection
            group backup to
            be restored. Use the endpoints
            [GET /backups/protection-groups/s3-assets](#operation/list-backup-protection-
            group-s3-assets)
            for protection group S3 asset backup, and
            [GET /backups/protection-groups](#operation/list-backup-protection-groups)
            for protection group backups to fetch valid values.
            Note that only one of either `backup_id` or `pitr` must be provided.
        is_sync:
            Whether to wait for the operation to complete.
        object_filters:
            Search for or restore only objects that pass the source object filter.
        pitr:
            The parameters to initiate a point-in-time creation of S3 instant access
            endpoint.
            Note that only one of either `backup_id` or `pitr` must be provided.
        protection_group_s3_asset_id:
            Clumio-assigned ID of protection group S3 asset, representing the
            bucket within the protection group to restore from. Use the
            [GET /datasources/protection-groups/s3-assets](#operation/list-protection-
            group-s3-assets)
            endpoint to fetch valid values.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'backup_id': 'backup_id',
        'is_sync': 'is_sync',
        'object_filters': 'object_filters',
        'pitr': 'pitr',
        'protection_group_s3_asset_id': 'protection_group_s3_asset_id',
    }

    def __init__(
        self,
        backup_id: str = None,
        is_sync: bool = None,
        object_filters: source_object_filters.SourceObjectFilters = None,
        pitr: s3_instant_access_source_pitr_options.S3InstantAccessSourcePitrOptions = None,
        protection_group_s3_asset_id: str = None,
    ) -> None:
        """Constructor for the CostEstimatesProtectionGroupInstantAccessEndpointV1Request class."""

        # Initialize members of the class
        self.backup_id: str = backup_id
        self.is_sync: bool = is_sync
        self.object_filters: source_object_filters.SourceObjectFilters = object_filters
        self.pitr: s3_instant_access_source_pitr_options.S3InstantAccessSourcePitrOptions = pitr
        self.protection_group_s3_asset_id: str = protection_group_s3_asset_id

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
        is_sync = dictionary.get('is_sync')
        key = 'object_filters'
        object_filters = (
            source_object_filters.SourceObjectFilters.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'pitr'
        pitr = (
            s3_instant_access_source_pitr_options.S3InstantAccessSourcePitrOptions.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        protection_group_s3_asset_id = dictionary.get('protection_group_s3_asset_id')
        # Return an object of this model
        return cls(backup_id, is_sync, object_filters, pitr, protection_group_s3_asset_id)
