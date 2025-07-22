#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    protection_group_s3_asset_backup_links as protection_group_s3_asset_backup_links_

T = TypeVar('T', bound='ProtectionGroupS3AssetBackup')


class ProtectionGroupS3AssetBackup:
    """Implementation of the 'ProtectionGroupS3AssetBackup' model.

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
        links: protection_group_s3_asset_backup_links_.ProtectionGroupS3AssetBackupLinks,
        aws_region: str,
        backed_up_object_count: int,
        backed_up_size_bytes: int,
        bucket_id: str,
        bucket_name: str,
        expiration_timestamp: str,
        failed_object_count: int,
        failed_size_bytes: int,
        p_id: str,
        protection_group_id: str,
        protection_group_s3_asset_id: str,
        protection_group_version: int,
        start_timestamp: str,
        p_type: str,
    ) -> None:
        """Constructor for the ProtectionGroupS3AssetBackup class."""

        # Initialize members of the class
        self.links: protection_group_s3_asset_backup_links_.ProtectionGroupS3AssetBackupLinks = (
            links
        )
        self.aws_region: str = aws_region
        self.backed_up_object_count: int = backed_up_object_count
        self.backed_up_size_bytes: int = backed_up_size_bytes
        self.bucket_id: str = bucket_id
        self.bucket_name: str = bucket_name
        self.expiration_timestamp: str = expiration_timestamp
        self.failed_object_count: int = failed_object_count
        self.failed_size_bytes: int = failed_size_bytes
        self.p_id: str = p_id
        self.protection_group_id: str = protection_group_id
        self.protection_group_s3_asset_id: str = protection_group_s3_asset_id
        self.protection_group_version: int = protection_group_version
        self.start_timestamp: str = start_timestamp
        self.p_type: str = p_type

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
        val = dictionary['_links']
        val_links = protection_group_s3_asset_backup_links_.ProtectionGroupS3AssetBackupLinks.from_dictionary(
            val
        )

        val = dictionary['aws_region']
        val_aws_region = val

        val = dictionary['backed_up_object_count']
        val_backed_up_object_count = val

        val = dictionary['backed_up_size_bytes']
        val_backed_up_size_bytes = val

        val = dictionary['bucket_id']
        val_bucket_id = val

        val = dictionary['bucket_name']
        val_bucket_name = val

        val = dictionary['expiration_timestamp']
        val_expiration_timestamp = val

        val = dictionary['failed_object_count']
        val_failed_object_count = val

        val = dictionary['failed_size_bytes']
        val_failed_size_bytes = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['protection_group_id']
        val_protection_group_id = val

        val = dictionary['protection_group_s3_asset_id']
        val_protection_group_s3_asset_id = val

        val = dictionary['protection_group_version']
        val_protection_group_version = val

        val = dictionary['start_timestamp']
        val_start_timestamp = val

        val = dictionary['type']
        val_p_type = val

        # Return an object of this model
        return cls(
            val_links,  # type: ignore
            val_aws_region,  # type: ignore
            val_backed_up_object_count,  # type: ignore
            val_backed_up_size_bytes,  # type: ignore
            val_bucket_id,  # type: ignore
            val_bucket_name,  # type: ignore
            val_expiration_timestamp,  # type: ignore
            val_failed_object_count,  # type: ignore
            val_failed_size_bytes,  # type: ignore
            val_p_id,  # type: ignore
            val_protection_group_id,  # type: ignore
            val_protection_group_s3_asset_id,  # type: ignore
            val_protection_group_version,  # type: ignore
            val_start_timestamp,  # type: ignore
            val_p_type,  # type: ignore
        )
