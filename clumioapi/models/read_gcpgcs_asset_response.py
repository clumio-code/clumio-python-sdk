#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import gcpgcs_asset_embedded as gcpgcs_asset_embedded_
from clumioapi.models import gcpgcs_asset_links as gcpgcs_asset_links_
import requests

T = TypeVar('T', bound='ReadGCPGCSAssetResponse')


@dataclasses.dataclass
class ReadGCPGCSAssetResponse:
    """Implementation of the 'ReadGCPGCSAssetResponse' model.

    Attributes:
        Embedded

        Etag

        Links

        AddedBy:
            Indicates how the bucket was added to the protection group. possible values
            include `user` and `bucket_rule`.

        AddedWith:
            Lists all methods by which the bucket was added to the protection group.

        BackupTargetRegion:
            The backup target region configured for the gcs asset, if any.

        BucketId:
            The clumio-assigned id of the bucket associated with this gcs asset.

        BucketName:
            The name of the gcs bucket associated with this gcs asset.

        CreatedTimestamp:
            Creation time of the gcs asset in rfc-3339 format.

        DeletedTimestamp:
            Deletion time of the gcs asset in rfc-3339 format.

        Id:
            The clumio-assigned id that represents the bucket within the protection group.

        IsDeleted:
            Indicates whether the gcs asset has been deleted (`true`) or is still active
            (`false`).

        LastBackupTimestamp:
            Time of the last backup in rfc-3339 format.

        Name:
            The display name of the gcs asset.

        NativeId:
            The clumio-assigned native id of the gcs asset.

        ObjectCount:
            The number of objects that have been backed up in this gcs asset.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the gcs asset.

        ProjectUuid:
            The clumio-assigned uuid of the gcp project associated with this gcs asset.

        ProtectionGroupId:
            The clumio-assigned id of the protection group associated with this gcs asset.

        ProtectionGroupName:
            The user-assigned name of the protection group associated with this gcs asset.
            omitted when the parent protection group could not be resolved or has no name.

        RegionUuid:
            The clumio-assigned uuid of the gcp region associated with this gcs asset.

        SizeBytes:
            Total size in bytes of all objects that have been backed up in this gcs asset.

        UpdatedTimestamp:
            Last update time of the gcs asset in rfc-3339 format.

        Version:
            The resource version of the gcs asset.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Embedded': '_embedded',
        'Etag': '_etag',
        'Links': '_links',
    }

    Embedded: gcpgcs_asset_embedded_.GCPGCSAssetEmbedded | None = None
    Etag: str | None = None
    Links: gcpgcs_asset_links_.GCPGCSAssetLinks | None = None
    AddedBy: str | None = None
    AddedWith: Sequence[str] | None = None
    BackupTargetRegion: str | None = None
    BucketId: str | None = None
    BucketName: str | None = None
    CreatedTimestamp: str | None = None
    DeletedTimestamp: str | None = None
    Id: str | None = None
    IsDeleted: bool | None = None
    LastBackupTimestamp: str | None = None
    Name: str | None = None
    NativeId: str | None = None
    ObjectCount: int | None = None
    OrganizationalUnitId: str | None = None
    ProjectUuid: str | None = None
    ProtectionGroupId: str | None = None
    ProtectionGroupName: str | None = None
    RegionUuid: str | None = None
    SizeBytes: int | None = None
    UpdatedTimestamp: str | None = None
    Version: int | None = None
    raw_response: Optional[requests.Response] = None

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
        val = dictionary.get('_embedded', None)
        val_embedded = gcpgcs_asset_embedded_.GCPGCSAssetEmbedded.from_dictionary(val)

        val = dictionary.get('_etag', None)
        val_etag = val

        val = dictionary.get('_links', None)
        val_links = gcpgcs_asset_links_.GCPGCSAssetLinks.from_dictionary(val)

        val = dictionary.get('added_by', None)
        val_added_by = val

        val = dictionary.get('added_with', None)
        val_added_with = val

        val = dictionary.get('backup_target_region', None)
        val_backup_target_region = val

        val = dictionary.get('bucket_id', None)
        val_bucket_id = val

        val = dictionary.get('bucket_name', None)
        val_bucket_name = val

        val = dictionary.get('created_timestamp', None)
        val_created_timestamp = val

        val = dictionary.get('deleted_timestamp', None)
        val_deleted_timestamp = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('is_deleted', None)
        val_is_deleted = val

        val = dictionary.get('last_backup_timestamp', None)
        val_last_backup_timestamp = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('native_id', None)
        val_native_id = val

        val = dictionary.get('object_count', None)
        val_object_count = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('project_uuid', None)
        val_project_uuid = val

        val = dictionary.get('protection_group_id', None)
        val_protection_group_id = val

        val = dictionary.get('protection_group_name', None)
        val_protection_group_name = val

        val = dictionary.get('region_uuid', None)
        val_region_uuid = val

        val = dictionary.get('size_bytes', None)
        val_size_bytes = val

        val = dictionary.get('updated_timestamp', None)
        val_updated_timestamp = val

        val = dictionary.get('version', None)
        val_version = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_etag,
            val_links,
            val_added_by,
            val_added_with,
            val_backup_target_region,
            val_bucket_id,
            val_bucket_name,
            val_created_timestamp,
            val_deleted_timestamp,
            val_id,
            val_is_deleted,
            val_last_backup_timestamp,
            val_name,
            val_native_id,
            val_object_count,
            val_organizational_unit_id,
            val_project_uuid,
            val_protection_group_id,
            val_protection_group_name,
            val_region_uuid,
            val_size_bytes,
            val_updated_timestamp,
            val_version,
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
        model_instance.raw_response = response
        return model_instance
