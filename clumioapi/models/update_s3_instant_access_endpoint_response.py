#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    s3_instant_access_endpoint_embedded as s3_instant_access_endpoint_embedded_
from clumioapi.models import s3_instant_access_endpoint_links as s3_instant_access_endpoint_links_

T = TypeVar('T', bound='UpdateS3InstantAccessEndpointResponse')


class UpdateS3InstantAccessEndpointResponse:
    """Implementation of the 'UpdateS3InstantAccessEndpointResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        aws_account_id:
            The AWS-assigned ID of the account associated with the S3 instant access
            endpoint.
        backup_region:
            The AWS region of the S3 instant access endpoint and its source backup.
        bucket_name:
            The name of source bucket.
        created_timestamp:
            The time that this endpoint was created, in RFC-3339 format.
        endpoint_status:
            The status of the S3 instant access endpoint. Possible values include
            "preparing",
            "active", "expiring", and "expired".
        expiry_timestamp:
            The time that this endpoint expires, in RFC-3339 format.
        p_id:
            The Clumio-assigned ID of the S3 instant access endpoint.
        name:
            The user-assigned name of the S3 instant access endpoint.
        objects_created_after:
            The time in RFC-3339 format that the restored objects are backed up from.
        objects_created_before:
            The time in RFC-3339 format that the restored objects are backed up to.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the S3 instant
            access endpoint.
        protection_group_id:
            The Clumio-assigned ID of the protection group this endpoint is created for.
        protection_group_name:
            The user-assigned name of the protection group this endpoints is created for.
        protection_group_s3_asset_id:
            The Clumio-assigned ID of the bucket protection group.
        region:
            The AWS region of the source bucket.
        restore_timestamp:
            The time at which the backup was restored from this endpoint in RFC-3339 format.
            Deprecated.
        updated_timestamp:
            The time that this endpoint was last updated, in RFC-3339 format.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'aws_account_id': 'aws_account_id',
        'backup_region': 'backup_region',
        'bucket_name': 'bucket_name',
        'created_timestamp': 'created_timestamp',
        'endpoint_status': 'endpoint_status',
        'expiry_timestamp': 'expiry_timestamp',
        'p_id': 'id',
        'name': 'name',
        'objects_created_after': 'objects_created_after',
        'objects_created_before': 'objects_created_before',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_group_id': 'protection_group_id',
        'protection_group_name': 'protection_group_name',
        'protection_group_s3_asset_id': 'protection_group_s3_asset_id',
        'region': 'region',
        'restore_timestamp': 'restore_timestamp',
        'updated_timestamp': 'updated_timestamp',
    }

    def __init__(
        self,
        embedded: (
            s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded | None
        ) = None,
        links: s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks | None = None,
        aws_account_id: str | None = None,
        backup_region: str | None = None,
        bucket_name: str | None = None,
        created_timestamp: str | None = None,
        endpoint_status: str | None = None,
        expiry_timestamp: str | None = None,
        p_id: str | None = None,
        name: str | None = None,
        objects_created_after: str | None = None,
        objects_created_before: str | None = None,
        organizational_unit_id: str | None = None,
        protection_group_id: str | None = None,
        protection_group_name: str | None = None,
        protection_group_s3_asset_id: str | None = None,
        region: str | None = None,
        restore_timestamp: str | None = None,
        updated_timestamp: str | None = None,
    ) -> None:
        """Constructor for the UpdateS3InstantAccessEndpointResponse class."""

        # Initialize members of the class
        self.embedded: (
            s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded | None
        ) = embedded
        self.links: s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks | None = links
        self.aws_account_id: str | None = aws_account_id
        self.backup_region: str | None = backup_region
        self.bucket_name: str | None = bucket_name
        self.created_timestamp: str | None = created_timestamp
        self.endpoint_status: str | None = endpoint_status
        self.expiry_timestamp: str | None = expiry_timestamp
        self.p_id: str | None = p_id
        self.name: str | None = name
        self.objects_created_after: str | None = objects_created_after
        self.objects_created_before: str | None = objects_created_before
        self.organizational_unit_id: str | None = organizational_unit_id
        self.protection_group_id: str | None = protection_group_id
        self.protection_group_name: str | None = protection_group_name
        self.protection_group_s3_asset_id: str | None = protection_group_s3_asset_id
        self.region: str | None = region
        self.restore_timestamp: str | None = restore_timestamp
        self.updated_timestamp: str | None = updated_timestamp

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
        val = dictionary.get('_embedded', None)
        val_embedded = (
            s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded.from_dictionary(
                val
            )
        )

        val = dictionary.get('_links', None)
        val_links = s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks.from_dictionary(
            val
        )

        val = dictionary.get('aws_account_id', None)
        val_aws_account_id = val

        val = dictionary.get('backup_region', None)
        val_backup_region = val

        val = dictionary.get('bucket_name', None)
        val_bucket_name = val

        val = dictionary.get('created_timestamp', None)
        val_created_timestamp = val

        val = dictionary.get('endpoint_status', None)
        val_endpoint_status = val

        val = dictionary.get('expiry_timestamp', None)
        val_expiry_timestamp = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('objects_created_after', None)
        val_objects_created_after = val

        val = dictionary.get('objects_created_before', None)
        val_objects_created_before = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('protection_group_id', None)
        val_protection_group_id = val

        val = dictionary.get('protection_group_name', None)
        val_protection_group_name = val

        val = dictionary.get('protection_group_s3_asset_id', None)
        val_protection_group_s3_asset_id = val

        val = dictionary.get('region', None)
        val_region = val

        val = dictionary.get('restore_timestamp', None)
        val_restore_timestamp = val

        val = dictionary.get('updated_timestamp', None)
        val_updated_timestamp = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_aws_account_id,
            val_backup_region,
            val_bucket_name,
            val_created_timestamp,
            val_endpoint_status,
            val_expiry_timestamp,
            val_p_id,
            val_name,
            val_objects_created_after,
            val_objects_created_before,
            val_organizational_unit_id,
            val_protection_group_id,
            val_protection_group_name,
            val_protection_group_s3_asset_id,
            val_region,
            val_restore_timestamp,
            val_updated_timestamp,
        )
