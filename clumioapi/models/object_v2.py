#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ObjectV2')


class ObjectV2:
    """Implementation of the 'ObjectV2' model.

    ObjectV2 defines one object to restore

    Attributes:
        bucket:
            Bucket the object belongs to
        etag:
            Etag of the contents of the object.
        last_backup_timestamp:
            Last time the object was backed up as an RFC3339 string.
        last_modified_timestamp:
            Last modified time of the object as an RFC3339 string.
        object_key:
            Object key
        protection_group_asset_id:
            The Clumio-assigned ID of a protection group S3 asset,
            which represents the bucket within the protection group to restore from.
        region:
            region of the backup object
        restore_cookie:
            Encrypted metadata for the object to be restored
            You can get `restore_cookie` via
            [POST /restores/protection-
            groups/{protection_group_id}/previews](#operation/preview-protection-group)
        size_in_bytes:
            Size in Bytes
        storage_class:
            Storage class. Valid values are: `S3 Standard`, `S3 Standard-IA`, `S3
            Intelligent-Tiering`,
            and `S3 One Zone-IA`.
        version_id:
            Version ID
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'bucket': 'bucket',
        'etag': 'etag',
        'last_backup_timestamp': 'last_backup_timestamp',
        'last_modified_timestamp': 'last_modified_timestamp',
        'object_key': 'object_key',
        'protection_group_asset_id': 'protection_group_asset_id',
        'region': 'region',
        'restore_cookie': 'restore_cookie',
        'size_in_bytes': 'size_in_bytes',
        'storage_class': 'storage_class',
        'version_id': 'version_id',
    }

    def __init__(
        self,
        bucket: str | None = None,
        etag: str | None = None,
        last_backup_timestamp: str | None = None,
        last_modified_timestamp: str | None = None,
        object_key: str | None = None,
        protection_group_asset_id: str | None = None,
        region: str | None = None,
        restore_cookie: str | None = None,
        size_in_bytes: int | None = None,
        storage_class: str | None = None,
        version_id: str | None = None,
    ) -> None:
        """Constructor for the ObjectV2 class."""

        # Initialize members of the class
        self.bucket: str | None = bucket
        self.etag: str | None = etag
        self.last_backup_timestamp: str | None = last_backup_timestamp
        self.last_modified_timestamp: str | None = last_modified_timestamp
        self.object_key: str | None = object_key
        self.protection_group_asset_id: str | None = protection_group_asset_id
        self.region: str | None = region
        self.restore_cookie: str | None = restore_cookie
        self.size_in_bytes: int | None = size_in_bytes
        self.storage_class: str | None = storage_class
        self.version_id: str | None = version_id

    @classmethod
    def from_dictionary(cls: Type[T], dictionary: Mapping[str, Any]) -> T:
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
        val = dictionary.get('bucket', None)
        val_bucket = val

        val = dictionary.get('etag', None)
        val_etag = val

        val = dictionary.get('last_backup_timestamp', None)
        val_last_backup_timestamp = val

        val = dictionary.get('last_modified_timestamp', None)
        val_last_modified_timestamp = val

        val = dictionary.get('object_key', None)
        val_object_key = val

        val = dictionary.get('protection_group_asset_id', None)
        val_protection_group_asset_id = val

        val = dictionary.get('region', None)
        val_region = val

        val = dictionary.get('restore_cookie', None)
        val_restore_cookie = val

        val = dictionary.get('size_in_bytes', None)
        val_size_in_bytes = val

        val = dictionary.get('storage_class', None)
        val_storage_class = val

        val = dictionary.get('version_id', None)
        val_version_id = val

        # Return an object of this model
        return cls(
            val_bucket,
            val_etag,
            val_last_backup_timestamp,
            val_last_modified_timestamp,
            val_object_key,
            val_protection_group_asset_id,
            val_region,
            val_restore_cookie,
            val_size_in_bytes,
            val_storage_class,
            val_version_id,
        )
