#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_instant_access_endpoint_embedded
from clumioapi.models import s3_instant_access_endpoint_links
from clumioapi.models import s3_instant_access_endpoint_role
from clumioapi.models import s3_instant_access_endpoint_stat

T = TypeVar('T', bound='ReadS3InstantAccessEndpointResponse')


class ReadS3InstantAccessEndpointResponse:
    """Implementation of the 'ReadS3InstantAccessEndpointResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        etag:
            The ETag value.
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
        roles:
            The IAM roles allowed to access the endpoint.
        stats:
            The stats associated with the endpoint.
        updated_timestamp:
            The time that this endpoint was last updated, in RFC-3339 format.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'etag': '_etag',
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
        'roles': 'roles',
        'stats': 'stats',
        'updated_timestamp': 'updated_timestamp',
    }

    def __init__(
        self,
        embedded: s3_instant_access_endpoint_embedded.S3InstantAccessEndpointEmbedded = None,
        etag: str = None,
        links: s3_instant_access_endpoint_links.S3InstantAccessEndpointLinks = None,
        aws_account_id: str = None,
        backup_region: str = None,
        bucket_name: str = None,
        created_timestamp: str = None,
        endpoint_status: str = None,
        expiry_timestamp: str = None,
        p_id: str = None,
        name: str = None,
        objects_created_after: str = None,
        objects_created_before: str = None,
        organizational_unit_id: str = None,
        protection_group_id: str = None,
        protection_group_name: str = None,
        protection_group_s3_asset_id: str = None,
        region: str = None,
        restore_timestamp: str = None,
        roles: Sequence[s3_instant_access_endpoint_role.S3InstantAccessEndpointRole] = None,
        stats: Sequence[s3_instant_access_endpoint_stat.S3InstantAccessEndpointStat] = None,
        updated_timestamp: str = None,
    ) -> None:
        """Constructor for the ReadS3InstantAccessEndpointResponse class."""

        # Initialize members of the class
        self.embedded: s3_instant_access_endpoint_embedded.S3InstantAccessEndpointEmbedded = (
            embedded
        )
        self.etag: str = etag
        self.links: s3_instant_access_endpoint_links.S3InstantAccessEndpointLinks = links
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
        self.roles: Sequence[s3_instant_access_endpoint_role.S3InstantAccessEndpointRole] = roles
        self.stats: Sequence[s3_instant_access_endpoint_stat.S3InstantAccessEndpointStat] = stats
        self.updated_timestamp: str = updated_timestamp

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
        key = '_embedded'
        embedded = (
            s3_instant_access_endpoint_embedded.S3InstantAccessEndpointEmbedded.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        etag = dictionary.get('_etag')
        key = '_links'
        links = (
            s3_instant_access_endpoint_links.S3InstantAccessEndpointLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        aws_account_id = dictionary.get('aws_account_id')
        backup_region = dictionary.get('backup_region')
        bucket_name = dictionary.get('bucket_name')
        created_timestamp = dictionary.get('created_timestamp')
        endpoint_status = dictionary.get('endpoint_status')
        expiry_timestamp = dictionary.get('expiry_timestamp')
        p_id = dictionary.get('id')
        name = dictionary.get('name')
        objects_created_after = dictionary.get('objects_created_after')
        objects_created_before = dictionary.get('objects_created_before')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        protection_group_id = dictionary.get('protection_group_id')
        protection_group_name = dictionary.get('protection_group_name')
        protection_group_s3_asset_id = dictionary.get('protection_group_s3_asset_id')
        region = dictionary.get('region')
        restore_timestamp = dictionary.get('restore_timestamp')
        roles = None
        if dictionary.get('roles'):
            roles = list()
            for value in dictionary.get('roles'):
                roles.append(
                    s3_instant_access_endpoint_role.S3InstantAccessEndpointRole.from_dictionary(
                        value
                    )
                )

        stats = None
        if dictionary.get('stats'):
            stats = list()
            for value in dictionary.get('stats'):
                stats.append(
                    s3_instant_access_endpoint_stat.S3InstantAccessEndpointStat.from_dictionary(
                        value
                    )
                )

        updated_timestamp = dictionary.get('updated_timestamp')
        # Return an object of this model
        return cls(
            embedded,
            etag,
            links,
            aws_account_id,
            backup_region,
            bucket_name,
            created_timestamp,
            endpoint_status,
            expiry_timestamp,
            p_id,
            name,
            objects_created_after,
            objects_created_before,
            organizational_unit_id,
            protection_group_id,
            protection_group_name,
            protection_group_s3_asset_id,
            region,
            restore_timestamp,
            roles,
            stats,
            updated_timestamp,
        )
