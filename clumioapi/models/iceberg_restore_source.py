#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
import requests

T = TypeVar('T', bound='IcebergRestoreSource')


@dataclasses.dataclass
class IcebergRestoreSource:
    """Implementation of the 'IcebergRestoreSource' model.

    IcebergRestoreSourceThe Iceberg Snapshot records to be restored.

    Attributes:
        AssetId:
            The asset id of the iceberg table where the backup is stored.

        BackupIds:
            The list of backup ids to restore.
            required for backup id based restore. optional for interval restore, where
            `asset_id`, `region`, `start_timestamp`, and `end_timestamp` are used instead.

        EndTimestamp

        MainSnapshotBackupId:
            The main iceberg table snapshot backup id to restore.
            if not specified, the latest snapshot will be used as the main snapshot.
            main refers the branch of the iceberg table (default branch).

        Region:
            The region where the backup is stored.

        StartTimestamp:
            The start and end times of restored snapshot for interval restore.

    """

    AssetId: str | None = None
    BackupIds: Sequence[str] | None = None
    EndTimestamp: str | None = None
    MainSnapshotBackupId: str | None = None
    Region: str | None = None
    StartTimestamp: str | None = None

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
        val = dictionary.get('asset_id', None)
        val_asset_id = val

        val = dictionary.get('backup_ids', None)
        val_backup_ids = val

        val = dictionary.get('end_timestamp', None)
        val_end_timestamp = val

        val = dictionary.get('main_snapshot_backup_id', None)
        val_main_snapshot_backup_id = val

        val = dictionary.get('region', None)
        val_region = val

        val = dictionary.get('start_timestamp', None)
        val_start_timestamp = val

        # Return an object of this model
        return cls(
            val_asset_id,
            val_backup_ids,
            val_end_timestamp,
            val_main_snapshot_backup_id,
            val_region,
            val_start_timestamp,
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
