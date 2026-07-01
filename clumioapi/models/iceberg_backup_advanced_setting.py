#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
import requests

T = TypeVar('T', bound='IcebergBackupAdvancedSetting')


@dataclasses.dataclass
class IcebergBackupAdvancedSetting:
    """Implementation of the 'IcebergBackupAdvancedSetting' model.

    IcebergBackupAdvancedSetting defines the advanced settings for Iceberg backup
    operations

    Attributes:
        BackupCompactedSnapshotOnly

        BackupLastSnapshotOnly

        BackupTier:
            `standard`.

    """

    BackupCompactedSnapshotOnly: bool | None = None
    BackupLastSnapshotOnly: bool | None = None
    BackupTier: str | None = None

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
        val = dictionary.get('backup_compacted_snapshot_only', None)
        val_backup_compacted_snapshot_only = val

        val = dictionary.get('backup_last_snapshot_only', None)
        val_backup_last_snapshot_only = val

        val = dictionary.get('backup_tier', None)
        val_backup_tier = val

        # Return an object of this model
        return cls(
            val_backup_compacted_snapshot_only,
            val_backup_last_snapshot_only,
            val_backup_tier,
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
