#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    protection_group_s3_asset_backup_links as protection_group_s3_asset_backup_links_

T = TypeVar('T', bound='ReadProtectionGroupS3AssetBackupResponse')


class ReadProtectionGroupS3AssetBackupResponse:
    """Implementation of the 'ReadProtectionGroupS3AssetBackupResponse' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        aws_region:
            The AWS region in which the instance backup resides. For example, `us-west-2`.
        backed_up_object_count:
            The number of objects in the protection group S3 asset that were successfully
            backed up.
        backed_up_size_bytes:
            The total size in bytes of objects in the protection group S3 asset that were
            successfully backed up.
        bucket_id:
            The Clumio-assigned ID of the bucket.
        bucket_name:
            The name of the bucket.
        expiration_timestamp:
            The timestamp of when this backup expires. Represented in RFC-3339 format.
        failed_object_count:
            The number of objects in the protection group S3 asset that failed to be backed
            up.
        failed_size_bytes:
            The total size in bytes of objects in the protection group S3 asset that failed
            to be backed up.
        p_id:
            The Clumio-assigned ID of the protection group S3 asset backup.
        protection_group_id:
            The Clumio-assigned ID of the protection group.
        protection_group_s3_asset_id:
            The Clumio-assigned ID of the protection group S3 asset.
        protection_group_version:
            The version of the protection group at the time the backup was taken.
        start_timestamp:
            The timestamp of when this backup started. Represented in RFC-3339 format.
        p_type:
            The type of backup. Possible values include `protection_group_s3_asset_backup`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'links': '_links',
        'aws_region': 'aws_region',
        'backed_up_object_count': 'backed_up_object_count',
        'backed_up_size_bytes': 'backed_up_size_bytes',
        'bucket_id': 'bucket_id',
        'bucket_name': 'bucket_name',
        'expiration_timestamp': 'expiration_timestamp',
        'failed_object_count': 'failed_object_count',
        'failed_size_bytes': 'failed_size_bytes',
        'p_id': 'id',
        'protection_group_id': 'protection_group_id',
        'protection_group_s3_asset_id': 'protection_group_s3_asset_id',
        'protection_group_version': 'protection_group_version',
        'start_timestamp': 'start_timestamp',
        'p_type': 'type',
    }

    def __init__(
        self,
        links: (
            protection_group_s3_asset_backup_links_.ProtectionGroupS3AssetBackupLinks | None
        ) = None,
        aws_region: str | None = None,
        backed_up_object_count: int | None = None,
        backed_up_size_bytes: int | None = None,
        bucket_id: str | None = None,
        bucket_name: str | None = None,
        expiration_timestamp: str | None = None,
        failed_object_count: int | None = None,
        failed_size_bytes: int | None = None,
        p_id: str | None = None,
        protection_group_id: str | None = None,
        protection_group_s3_asset_id: str | None = None,
        protection_group_version: int | None = None,
        start_timestamp: str | None = None,
        p_type: str | None = None,
    ) -> None:
        """Constructor for the ReadProtectionGroupS3AssetBackupResponse class."""

        # Initialize members of the class
        self.links: (
            protection_group_s3_asset_backup_links_.ProtectionGroupS3AssetBackupLinks | None
        ) = links
        self.aws_region: str | None = aws_region
        self.backed_up_object_count: int | None = backed_up_object_count
        self.backed_up_size_bytes: int | None = backed_up_size_bytes
        self.bucket_id: str | None = bucket_id
        self.bucket_name: str | None = bucket_name
        self.expiration_timestamp: str | None = expiration_timestamp
        self.failed_object_count: int | None = failed_object_count
        self.failed_size_bytes: int | None = failed_size_bytes
        self.p_id: str | None = p_id
        self.protection_group_id: str | None = protection_group_id
        self.protection_group_s3_asset_id: str | None = protection_group_s3_asset_id
        self.protection_group_version: int | None = protection_group_version
        self.start_timestamp: str | None = start_timestamp
        self.p_type: str | None = p_type

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
        val = dictionary.get('_links', None)
        val_links = protection_group_s3_asset_backup_links_.ProtectionGroupS3AssetBackupLinks.from_dictionary(
            val
        )

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('backed_up_object_count', None)
        val_backed_up_object_count = val

        val = dictionary.get('backed_up_size_bytes', None)
        val_backed_up_size_bytes = val

        val = dictionary.get('bucket_id', None)
        val_bucket_id = val

        val = dictionary.get('bucket_name', None)
        val_bucket_name = val

        val = dictionary.get('expiration_timestamp', None)
        val_expiration_timestamp = val

        val = dictionary.get('failed_object_count', None)
        val_failed_object_count = val

        val = dictionary.get('failed_size_bytes', None)
        val_failed_size_bytes = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('protection_group_id', None)
        val_protection_group_id = val

        val = dictionary.get('protection_group_s3_asset_id', None)
        val_protection_group_s3_asset_id = val

        val = dictionary.get('protection_group_version', None)
        val_protection_group_version = val

        val = dictionary.get('start_timestamp', None)
        val_start_timestamp = val

        val = dictionary.get('type', None)
        val_p_type = val

        # Return an object of this model
        return cls(
            val_links,
            val_aws_region,
            val_backed_up_object_count,
            val_backed_up_size_bytes,
            val_bucket_id,
            val_bucket_name,
            val_expiration_timestamp,
            val_failed_object_count,
            val_failed_size_bytes,
            val_p_id,
            val_protection_group_id,
            val_protection_group_s3_asset_id,
            val_protection_group_version,
            val_start_timestamp,
            val_p_type,
        )
