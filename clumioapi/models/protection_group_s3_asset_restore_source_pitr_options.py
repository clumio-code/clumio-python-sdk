#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ProtectionGroupS3AssetRestoreSourcePitrOptions')


class ProtectionGroupS3AssetRestoreSourcePitrOptions:
    """Implementation of the 'ProtectionGroupS3AssetRestoreSourcePitrOptions' model.

    The parameters for initiating a point in time restore.<br>Note that only one of
    `backup_id` or `pitr` must be given.

    Attributes:
        protection_group_s3_asset_id:
            Clumio-assigned ID of protection group S3 asset, representing the
            bucket within the protection group to restore from. Use the
            [GET /datasources/protection-groups/s3-assets](#operation/list-protection-
            group-s3-assets)
            endpoint to fetch valid values.
        restore_end_timestamp:
            The ending time to be restored in RFC-3339 format.
            We will restore last objects modified before the given time.
            If `restore_end_timestamp` is given without `restore_start_timestamp`,
            it is the same as point in time restore.
        restore_start_timestamp:
            The starting time to be restored in RFC-3339 format.
            We will restore objects modified since the given time.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'protection_group_s3_asset_id': 'protection_group_s3_asset_id',
        'restore_end_timestamp': 'restore_end_timestamp',
        'restore_start_timestamp': 'restore_start_timestamp',
    }

    def __init__(
        self,
        protection_group_s3_asset_id: str = None,
        restore_end_timestamp: str = None,
        restore_start_timestamp: str = None,
    ) -> None:
        """Constructor for the ProtectionGroupS3AssetRestoreSourcePitrOptions class."""

        # Initialize members of the class
        self.protection_group_s3_asset_id: str = protection_group_s3_asset_id
        self.restore_end_timestamp: str = restore_end_timestamp
        self.restore_start_timestamp: str = restore_start_timestamp

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
        protection_group_s3_asset_id = dictionary.get('protection_group_s3_asset_id')
        restore_end_timestamp = dictionary.get('restore_end_timestamp')
        restore_start_timestamp = dictionary.get('restore_start_timestamp')
        # Return an object of this model
        return cls(protection_group_s3_asset_id, restore_end_timestamp, restore_start_timestamp)
