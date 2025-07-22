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
        bucket: str,
        etag: str,
        last_backup_timestamp: str,
        last_modified_timestamp: str,
        object_key: str,
        protection_group_asset_id: str,
        region: str,
        restore_cookie: str,
        size_in_bytes: int,
        storage_class: str,
        version_id: str,
    ) -> None:
        """Constructor for the ObjectV2 class."""

        # Initialize members of the class
        self.bucket: str = bucket
        self.etag: str = etag
        self.last_backup_timestamp: str = last_backup_timestamp
        self.last_modified_timestamp: str = last_modified_timestamp
        self.object_key: str = object_key
        self.protection_group_asset_id: str = protection_group_asset_id
        self.region: str = region
        self.restore_cookie: str = restore_cookie
        self.size_in_bytes: int = size_in_bytes
        self.storage_class: str = storage_class
        self.version_id: str = version_id

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

        # Extract variables from the dictionary
        val = dictionary['bucket']
        val_bucket = val

        val = dictionary['etag']
        val_etag = val

        val = dictionary['last_backup_timestamp']
        val_last_backup_timestamp = val

        val = dictionary['last_modified_timestamp']
        val_last_modified_timestamp = val

        val = dictionary['object_key']
        val_object_key = val

        val = dictionary['protection_group_asset_id']
        val_protection_group_asset_id = val

        val = dictionary['region']
        val_region = val

        val = dictionary['restore_cookie']
        val_restore_cookie = val

        val = dictionary['size_in_bytes']
        val_size_in_bytes = val

        val = dictionary['storage_class']
        val_storage_class = val

        val = dictionary['version_id']
        val_version_id = val

        # Return an object of this model
        return cls(
            val_bucket,  # type: ignore
            val_etag,  # type: ignore
            val_last_backup_timestamp,  # type: ignore
            val_last_modified_timestamp,  # type: ignore
            val_object_key,  # type: ignore
            val_protection_group_asset_id,  # type: ignore
            val_region,  # type: ignore
            val_restore_cookie,  # type: ignore
            val_size_in_bytes,  # type: ignore
            val_storage_class,  # type: ignore
            val_version_id,  # type: ignore
        )
