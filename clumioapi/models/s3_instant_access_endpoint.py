#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    s3_instant_access_endpoint_embedded as s3_instant_access_endpoint_embedded_
from clumioapi.models import s3_instant_access_endpoint_links as s3_instant_access_endpoint_links_

T = TypeVar('T', bound='S3InstantAccessEndpoint')


class S3InstantAccessEndpoint:
    """Implementation of the 'S3InstantAccessEndpoint' model.

    S3InstantAccessEndpoint

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
        embedded: s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded,
        links: s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks,
        aws_account_id: str,
        backup_region: str,
        bucket_name: str,
        created_timestamp: str,
        endpoint_status: str,
        expiry_timestamp: str,
        p_id: str,
        name: str,
        objects_created_after: str,
        objects_created_before: str,
        organizational_unit_id: str,
        protection_group_id: str,
        protection_group_name: str,
        protection_group_s3_asset_id: str,
        region: str,
        restore_timestamp: str,
        updated_timestamp: str,
    ) -> None:
        """Constructor for the S3InstantAccessEndpoint class."""

        # Initialize members of the class
        self.embedded: s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded = (
            embedded
        )
        self.links: s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks = links
        self.aws_account_id: str = aws_account_id
        self.backup_region: str = backup_region
        self.bucket_name: str = bucket_name
        self.created_timestamp: str = created_timestamp
        self.endpoint_status: str = endpoint_status
        self.expiry_timestamp: str = expiry_timestamp
        self.p_id: str = p_id
        self.name: str = name
        self.objects_created_after: str = objects_created_after
        self.objects_created_before: str = objects_created_before
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_group_id: str = protection_group_id
        self.protection_group_name: str = protection_group_name
        self.protection_group_s3_asset_id: str = protection_group_s3_asset_id
        self.region: str = region
        self.restore_timestamp: str = restore_timestamp
        self.updated_timestamp: str = updated_timestamp

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
        val = dictionary['_embedded']
        val_embedded = (
            s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded.from_dictionary(
                val
            )
        )

        val = dictionary['_links']
        val_links = s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks.from_dictionary(
            val
        )

        val = dictionary['aws_account_id']
        val_aws_account_id = val

        val = dictionary['backup_region']
        val_backup_region = val

        val = dictionary['bucket_name']
        val_bucket_name = val

        val = dictionary['created_timestamp']
        val_created_timestamp = val

        val = dictionary['endpoint_status']
        val_endpoint_status = val

        val = dictionary['expiry_timestamp']
        val_expiry_timestamp = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['name']
        val_name = val

        val = dictionary['objects_created_after']
        val_objects_created_after = val

        val = dictionary['objects_created_before']
        val_objects_created_before = val

        val = dictionary['organizational_unit_id']
        val_organizational_unit_id = val

        val = dictionary['protection_group_id']
        val_protection_group_id = val

        val = dictionary['protection_group_name']
        val_protection_group_name = val

        val = dictionary['protection_group_s3_asset_id']
        val_protection_group_s3_asset_id = val

        val = dictionary['region']
        val_region = val

        val = dictionary['restore_timestamp']
        val_restore_timestamp = val

        val = dictionary['updated_timestamp']
        val_updated_timestamp = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_aws_account_id,  # type: ignore
            val_backup_region,  # type: ignore
            val_bucket_name,  # type: ignore
            val_created_timestamp,  # type: ignore
            val_endpoint_status,  # type: ignore
            val_expiry_timestamp,  # type: ignore
            val_p_id,  # type: ignore
            val_name,  # type: ignore
            val_objects_created_after,  # type: ignore
            val_objects_created_before,  # type: ignore
            val_organizational_unit_id,  # type: ignore
            val_protection_group_id,  # type: ignore
            val_protection_group_name,  # type: ignore
            val_protection_group_s3_asset_id,  # type: ignore
            val_region,  # type: ignore
            val_restore_timestamp,  # type: ignore
            val_updated_timestamp,  # type: ignore
        )
