#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import protection_group_restore_target
from clumioapi.models import protection_group_s3_asset_restore_source

T = TypeVar('T', bound='RestoreProtectionGroupS3AssetV1Request')


class RestoreProtectionGroupS3AssetV1Request:
    """Implementation of the 'RestoreProtectionGroupS3AssetV1Request' model.

    Attributes:
        source:
            The parameters for initiating a protection group S3 asset restore
            or creation of an instant access endpoint from a backup.
        target:
            The destination where the protection group will be restored.
    """

    # Create a mapping from Model property names to API property names
    _names = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: protection_group_s3_asset_restore_source.ProtectionGroupS3AssetRestoreSource = None,
        target: protection_group_restore_target.ProtectionGroupRestoreTarget = None,
    ) -> None:
        """Constructor for the RestoreProtectionGroupS3AssetV1Request class."""

        # Initialize members of the class
        self.source: (
            protection_group_s3_asset_restore_source.ProtectionGroupS3AssetRestoreSource
        ) = source
        self.target: protection_group_restore_target.ProtectionGroupRestoreTarget = target

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
        key = 'source'
        source = (
            protection_group_s3_asset_restore_source.ProtectionGroupS3AssetRestoreSource.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'target'
        target = (
            protection_group_restore_target.ProtectionGroupRestoreTarget.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(source, target)
