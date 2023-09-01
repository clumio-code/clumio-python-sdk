#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import protection_group_s3_asset_backup_links

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
    _names = {
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
        links: protection_group_s3_asset_backup_links.ProtectionGroupS3AssetBackupLinks = None,
        aws_region: str = None,
        backed_up_object_count: int = None,
        backed_up_size_bytes: int = None,
        bucket_id: str = None,
        bucket_name: str = None,
        expiration_timestamp: str = None,
        failed_object_count: int = None,
        failed_size_bytes: int = None,
        p_id: str = None,
        protection_group_id: str = None,
        protection_group_s3_asset_id: str = None,
        protection_group_version: int = None,
        start_timestamp: str = None,
        p_type: str = None,
    ) -> None:
        """Constructor for the ReadProtectionGroupS3AssetBackupResponse class."""

        # Initialize members of the class
        self.links: protection_group_s3_asset_backup_links.ProtectionGroupS3AssetBackupLinks = links
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
        key = '_links'
        links = (
            protection_group_s3_asset_backup_links.ProtectionGroupS3AssetBackupLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        aws_region = dictionary.get('aws_region')
        backed_up_object_count = dictionary.get('backed_up_object_count')
        backed_up_size_bytes = dictionary.get('backed_up_size_bytes')
        bucket_id = dictionary.get('bucket_id')
        bucket_name = dictionary.get('bucket_name')
        expiration_timestamp = dictionary.get('expiration_timestamp')
        failed_object_count = dictionary.get('failed_object_count')
        failed_size_bytes = dictionary.get('failed_size_bytes')
        p_id = dictionary.get('id')
        protection_group_id = dictionary.get('protection_group_id')
        protection_group_s3_asset_id = dictionary.get('protection_group_s3_asset_id')
        protection_group_version = dictionary.get('protection_group_version')
        start_timestamp = dictionary.get('start_timestamp')
        p_type = dictionary.get('type')
        # Return an object of this model
        return cls(
            links,
            aws_region,
            backed_up_object_count,
            backed_up_size_bytes,
            bucket_id,
            bucket_name,
            expiration_timestamp,
            failed_object_count,
            failed_size_bytes,
            p_id,
            protection_group_id,
            protection_group_s3_asset_id,
            protection_group_version,
            start_timestamp,
            p_type,
        )
