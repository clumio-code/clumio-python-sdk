#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='Object')


class Object:
    """Implementation of the 'Object' model.

    Object defines one object to restore

    Attributes:
        bucket:
            Bucket the object belongs to
        etag:
            Etag of the contents of the object.
        last_backup_time:
            Last time the object was backed up as an RFC3339 string.
        last_modified_time:
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
    _names = {
        'bucket': 'bucket',
        'etag': 'etag',
        'last_backup_time': 'last_backup_time',
        'last_modified_time': 'last_modified_time',
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
        bucket: str = None,
        etag: str = None,
        last_backup_time: str = None,
        last_modified_time: str = None,
        object_key: str = None,
        protection_group_asset_id: str = None,
        region: str = None,
        restore_cookie: str = None,
        size_in_bytes: int = None,
        storage_class: str = None,
        version_id: str = None,
    ) -> None:
        """Constructor for the Object class."""

        # Initialize members of the class
        self.bucket: str = bucket
        self.etag: str = etag
        self.last_backup_time: str = last_backup_time
        self.last_modified_time: str = last_modified_time
        self.object_key: str = object_key
        self.protection_group_asset_id: str = protection_group_asset_id
        self.region: str = region
        self.restore_cookie: str = restore_cookie
        self.size_in_bytes: int = size_in_bytes
        self.storage_class: str = storage_class
        self.version_id: str = version_id

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
        bucket = dictionary.get('bucket')
        etag = dictionary.get('etag')
        last_backup_time = dictionary.get('last_backup_time')
        last_modified_time = dictionary.get('last_modified_time')
        object_key = dictionary.get('object_key')
        protection_group_asset_id = dictionary.get('protection_group_asset_id')
        region = dictionary.get('region')
        restore_cookie = dictionary.get('restore_cookie')
        size_in_bytes = dictionary.get('size_in_bytes')
        storage_class = dictionary.get('storage_class')
        version_id = dictionary.get('version_id')
        # Return an object of this model
        return cls(
            bucket,
            etag,
            last_backup_time,
            last_modified_time,
            object_key,
            protection_group_asset_id,
            region,
            restore_cookie,
            size_in_bytes,
            storage_class,
            version_id,
        )
