#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import protection_group_bucket_embedded
from clumioapi.models import protection_group_bucket_links
from clumioapi.models import protection_info_with_rule

T = TypeVar('T', bound='ProtectionGroupBucket')


class ProtectionGroupBucket:
    """Implementation of the 'ProtectionGroupBucket' model.

    Attributes:
        embedded:

        links:

        account_native_id:
            The AWS-assigned ID of the account associated with the DynamoDB table.
        added_by_bucket_rule:
            Whether this bucket was added to this protection group by the bucket rule
        added_by_user:
            Whether this bucket was added to this protection group by the user
        aws_region:
            The AWS region associated with the DynamoDB table.
        bucket_id:
            The Clumio-assigned ID of the bucket
        bucket_name:
            The name of the bucket
        compliance_status:
            The compliance status of the protected protection group. Possible values include
            "compliant" and "noncompliant". If the table is not protected, then this field
            has
            a value of `null`.
        created_timestamp:
            Creation time of the protection group in RFC-3339 format.
        environment_id:
            The Clumio-assigned ID of the AWS environment associated with the protection
            group.
        group_id:
            The Clumio-assigned ID of the protection group
        group_name:
            The name of the protection group
        id:
            The Clumio-assigned ID that represents the bucket within the protection group.
        is_deleted:
            Determines whether the protection group bucket has been deleted
        last_backup_timestamp:
            Time of the last backup in RFC-3339 format.
        last_continuous_backup_timestamp:
            Time of the last successful continuous backup in RFC-3339 format.
        last_discover_sync_timestamp:
            Time of the last discover sync in RFC-3339 format.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the protection
            group.
        protection_info:
            The protection policy applied to this resource. If the resource is not
            protected, then this field has a value of `null`.
        protection_status:
            The protection status of the protection group. Possible values include
            "protected",
            "unprotected", and "unsupported". If the protection group does not support
            backups, then
            this field has a value of `unsupported`.
        total_backed_up_object_count:
            Cumulative count of all unexpired objects in each backup (any new or updated
            since
            the last backup) that have been backed up as part of this protection group
        total_backed_up_size_bytes:
            Cumulative size of all unexpired objects in each backup (any new or updated
            since
            the last backup) that have been backed up as part of this protection group
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'account_native_id': 'account_native_id',
        'added_by_bucket_rule': 'added_by_bucket_rule',
        'added_by_user': 'added_by_user',
        'aws_region': 'aws_region',
        'bucket_id': 'bucket_id',
        'bucket_name': 'bucket_name',
        'compliance_status': 'compliance_status',
        'created_timestamp': 'created_timestamp',
        'environment_id': 'environment_id',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'id': 'id',
        'is_deleted': 'is_deleted',
        'last_backup_timestamp': 'last_backup_timestamp',
        'last_continuous_backup_timestamp': 'last_continuous_backup_timestamp',
        'last_discover_sync_timestamp': 'last_discover_sync_timestamp',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
        'protection_status': 'protection_status',
        'total_backed_up_object_count': 'total_backed_up_object_count',
        'total_backed_up_size_bytes': 'total_backed_up_size_bytes',
    }

    def __init__(
        self,
        embedded: protection_group_bucket_embedded.ProtectionGroupBucketEmbedded = None,
        links: protection_group_bucket_links.ProtectionGroupBucketLinks = None,
        account_native_id: str = None,
        added_by_bucket_rule: bool = None,
        added_by_user: bool = None,
        aws_region: str = None,
        bucket_id: str = None,
        bucket_name: str = None,
        compliance_status: str = None,
        created_timestamp: str = None,
        environment_id: str = None,
        group_id: str = None,
        group_name: str = None,
        id: str = None,
        is_deleted: bool = None,
        last_backup_timestamp: str = None,
        last_continuous_backup_timestamp: str = None,
        last_discover_sync_timestamp: str = None,
        organizational_unit_id: str = None,
        protection_info: protection_info_with_rule.ProtectionInfoWithRule = None,
        protection_status: str = None,
        total_backed_up_object_count: int = None,
        total_backed_up_size_bytes: int = None,
    ) -> None:
        """Constructor for the ProtectionGroupBucket class."""

        # Initialize members of the class
        self.embedded: protection_group_bucket_embedded.ProtectionGroupBucketEmbedded = embedded
        self.links: protection_group_bucket_links.ProtectionGroupBucketLinks = links
        self.account_native_id: str = account_native_id
        self.added_by_bucket_rule: bool = added_by_bucket_rule
        self.added_by_user: bool = added_by_user
        self.aws_region: str = aws_region
        self.bucket_id: str = bucket_id
        self.bucket_name: str = bucket_name
        self.compliance_status: str = compliance_status
        self.created_timestamp: str = created_timestamp
        self.environment_id: str = environment_id
        self.group_id: str = group_id
        self.group_name: str = group_name
        self.id: str = id
        self.is_deleted: bool = is_deleted
        self.last_backup_timestamp: str = last_backup_timestamp
        self.last_continuous_backup_timestamp: str = last_continuous_backup_timestamp
        self.last_discover_sync_timestamp: str = last_discover_sync_timestamp
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info_with_rule.ProtectionInfoWithRule = protection_info
        self.protection_status: str = protection_status
        self.total_backed_up_object_count: int = total_backed_up_object_count
        self.total_backed_up_size_bytes: int = total_backed_up_size_bytes

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
            protection_group_bucket_embedded.ProtectionGroupBucketEmbedded.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            protection_group_bucket_links.ProtectionGroupBucketLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        account_native_id = dictionary.get('account_native_id')
        added_by_bucket_rule = dictionary.get('added_by_bucket_rule')
        added_by_user = dictionary.get('added_by_user')
        aws_region = dictionary.get('aws_region')
        bucket_id = dictionary.get('bucket_id')
        bucket_name = dictionary.get('bucket_name')
        compliance_status = dictionary.get('compliance_status')
        created_timestamp = dictionary.get('created_timestamp')
        environment_id = dictionary.get('environment_id')
        group_id = dictionary.get('group_id')
        group_name = dictionary.get('group_name')
        id = dictionary.get('id')
        is_deleted = dictionary.get('is_deleted')
        last_backup_timestamp = dictionary.get('last_backup_timestamp')
        last_continuous_backup_timestamp = dictionary.get('last_continuous_backup_timestamp')
        last_discover_sync_timestamp = dictionary.get('last_discover_sync_timestamp')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        key = 'protection_info'
        protection_info = (
            protection_info_with_rule.ProtectionInfoWithRule.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        protection_status = dictionary.get('protection_status')
        total_backed_up_object_count = dictionary.get('total_backed_up_object_count')
        total_backed_up_size_bytes = dictionary.get('total_backed_up_size_bytes')
        # Return an object of this model
        return cls(
            embedded,
            links,
            account_native_id,
            added_by_bucket_rule,
            added_by_user,
            aws_region,
            bucket_id,
            bucket_name,
            compliance_status,
            created_timestamp,
            environment_id,
            group_id,
            group_name,
            id,
            is_deleted,
            last_backup_timestamp,
            last_continuous_backup_timestamp,
            last_discover_sync_timestamp,
            organizational_unit_id,
            protection_info,
            protection_status,
            total_backed_up_object_count,
            total_backed_up_size_bytes,
        )
