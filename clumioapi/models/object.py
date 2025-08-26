#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='Object')


@dataclasses.dataclass
class Object:
    """Implementation of the 'Object' model.

        Object defines one object to restore

        Attributes:
            Bucket:
                Bucket the object belongs to.

            Etag:
                Etag of the contents of the object.

            LastBackupTime:
                Last time the object was backed up as an rfc3339 string.

            LastModifiedTime:
                Last modified time of the object as an rfc3339 string.

            ObjectKey:
                Object key.

            ProtectionGroupAssetId:
                The clumio-assigned id of a protection group s3 asset,
    which represents the bucket within the protection group to restore from.

            Region:
                Region of the backup object.

            RestoreCookie:
                Encrypted metadata for the object to be restored
    you can get `restore_cookie` via
    [post /restores/protection-groups/{protection_group_id}/previews](#operation/preview-protection-group).

            SizeInBytes:
                Size in bytes.

            StorageClass:
                `s3 standard`, `s3 standard-ia`, `s3 intelligent-tiering`,
    and `s3 one zone-ia`.

            VersionId:
                Version id.

    """

    Bucket: str | None = None
    Etag: str | None = None
    LastBackupTime: str | None = None
    LastModifiedTime: str | None = None
    ObjectKey: str | None = None
    ProtectionGroupAssetId: str | None = None
    Region: str | None = None
    RestoreCookie: str | None = None
    SizeInBytes: int | None = None
    StorageClass: str | None = None
    VersionId: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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

        val = dictionary.get('last_backup_time', None)
        val_last_backup_time = val

        val = dictionary.get('last_modified_time', None)
        val_last_modified_time = val

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
            val_last_backup_time,
            val_last_modified_time,
            val_object_key,
            val_protection_group_asset_id,
            val_region,
            val_restore_cookie,
            val_size_in_bytes,
            val_storage_class,
            val_version_id,
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
