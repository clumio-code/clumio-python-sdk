#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
from clumioapi.models import iceberg_table_backup_links as iceberg_table_backup_links_
from clumioapi.models import model_summary as model_summary_
import requests

T = TypeVar('T', bound='IcebergTableBackup')


@dataclasses.dataclass
class IcebergTableBackup:
    """Implementation of the 'IcebergTableBackup' model.

    Attributes:
        Links

        AccountNativeId:
            The aws-assigned id of the account associated with this database at the time of
            backup.

        AwsRegion:
            The aws region associated with this environment.

        BackupAwsRegion:
            The region in which this backup is stored. for policies that keep backups
            in-region, this value will be the same as the source region of the asset backed
            up.
            for out of region policies, this region will the one specified in the policy.

        ExpirationTimestamp:
            The timestamp of when this backup expires. represented in rfc-3339 format.

        Id:
            The clumio-assigned id of the backup.

        NewlyAddedSnapshots:
            The total count of the newly added snapshots in this backup.

        Schema

        SnapshotCreatedAt

        SnapshotId

        StartTimestamp:
            The timestamp of when this backup started. represented in rfc-3339 format.

        Summary

        TableId:
            The clumio-assigned id of the iceberg table.

        TableName:
            The name of the iceberg table.

        Type:
            The type of catalog.
            this field is always set to "iceberg_snapshot" or "iceberg_metadata".

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Links': '_links',
    }

    Links: iceberg_table_backup_links_.IcebergTableBackupLinks | None = None
    AccountNativeId: str | None = None
    AwsRegion: str | None = None
    BackupAwsRegion: str | None = None
    ExpirationTimestamp: str | None = None
    Id: str | None = None
    NewlyAddedSnapshots: int | None = None
    Schema: str | None = None
    SnapshotCreatedAt: str | None = None
    SnapshotId: str | None = None
    StartTimestamp: str | None = None
    Summary: model_summary_.ModelSummary | None = None
    TableId: str | None = None
    TableName: str | None = None
    Type: str | None = None

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
        val = dictionary.get('_links', None)
        val_links = iceberg_table_backup_links_.IcebergTableBackupLinks.from_dictionary(val)

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('backup_aws_region', None)
        val_backup_aws_region = val

        val = dictionary.get('expiration_timestamp', None)
        val_expiration_timestamp = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('newly_added_snapshots', None)
        val_newly_added_snapshots = val

        val = dictionary.get('schema', None)
        val_schema = val

        val = dictionary.get('snapshot_created_at', None)
        val_snapshot_created_at = val

        val = dictionary.get('snapshot_id', None)
        val_snapshot_id = val

        val = dictionary.get('start_timestamp', None)
        val_start_timestamp = val

        val = dictionary.get('summary', None)
        val_summary = model_summary_.ModelSummary.from_dictionary(val)

        val = dictionary.get('table_id', None)
        val_table_id = val

        val = dictionary.get('table_name', None)
        val_table_name = val

        val = dictionary.get('type', None)
        val_type = val

        # Return an object of this model
        return cls(
            val_links,
            val_account_native_id,
            val_aws_region,
            val_backup_aws_region,
            val_expiration_timestamp,
            val_id,
            val_newly_added_snapshots,
            val_schema,
            val_snapshot_created_at,
            val_snapshot_id,
            val_start_timestamp,
            val_summary,
            val_table_id,
            val_table_name,
            val_type,
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
