#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import backup_status_info
from clumioapi.models import backup_tier_stat
from clumioapi.models import protection_group_bucket_embedded
from clumioapi.models import protection_group_bucket_links
from clumioapi.models import protection_info_with_rule

T = TypeVar('T', bound='ProtectionGroupBucket')


class ProtectionGroupBucket:
    """Implementation of the 'ProtectionGroupBucket' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        account_native_id:
            The AWS-assigned ID of the account associated with the DynamoDB table.
        added_by_bucket_rule:
            Whether this bucket was added to this protection group by the bucket rule
        added_by_user:
            Whether this bucket was added to this protection group by the user
        aws_region:
            The AWS region associated with the DynamoDB table.
        backup_status_info:
            The backup status information applied to this resource.
        backup_target_aws_region:
            The backup target AWS region associated with the protection group S3 asset.
        backup_tier_stats:
            TotalBackedUpSizeBytes, TotalBackedUpObjectCount for each backup tier
        bucket_id:
            The Clumio-assigned ID of the bucket
        bucket_name:
            The name of the bucket
        created_timestamp:
            Creation time of the protection group in RFC-3339 format.
        earliest_available_backup_timestamp:
            Timestamp of the earliest protection group backup which has not expired yet.
            Represented in
            RFC-3339 format. Only available for Read API.
        environment_id:
            The Clumio-assigned ID of the AWS environment associated with the protection
            group.
        group_id:
            The Clumio-assigned ID of the protection group
        group_name:
            The name of the protection group
        p_id:
            The Clumio-assigned ID that represents the bucket within the protection group.
        is_deleted:
            Determines whether the protection group bucket has been deleted
        last_backup_timestamp:
            Time of the last backup in RFC-3339 format.
        last_continuous_backup_timestamp:
            Time of the last successful continuous backup in RFC-3339 format.
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
        unsupported_reason:
            The unsupported reason for the S3 bucket.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'account_native_id': 'account_native_id',
        'added_by_bucket_rule': 'added_by_bucket_rule',
        'added_by_user': 'added_by_user',
        'aws_region': 'aws_region',
        'backup_status_info': 'backup_status_info',
        'backup_target_aws_region': 'backup_target_aws_region',
        'backup_tier_stats': 'backup_tier_stats',
        'bucket_id': 'bucket_id',
        'bucket_name': 'bucket_name',
        'created_timestamp': 'created_timestamp',
        'earliest_available_backup_timestamp': 'earliest_available_backup_timestamp',
        'environment_id': 'environment_id',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'p_id': 'id',
        'is_deleted': 'is_deleted',
        'last_backup_timestamp': 'last_backup_timestamp',
        'last_continuous_backup_timestamp': 'last_continuous_backup_timestamp',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
        'protection_status': 'protection_status',
        'total_backed_up_object_count': 'total_backed_up_object_count',
        'total_backed_up_size_bytes': 'total_backed_up_size_bytes',
        'unsupported_reason': 'unsupported_reason',
    }

    def __init__(
        self,
        embedded: protection_group_bucket_embedded.ProtectionGroupBucketEmbedded = None,
        links: protection_group_bucket_links.ProtectionGroupBucketLinks = None,
        account_native_id: str = None,
        added_by_bucket_rule: bool = None,
        added_by_user: bool = None,
        aws_region: str = None,
        backup_status_info: backup_status_info.BackupStatusInfo = None,
        backup_target_aws_region: str = None,
        backup_tier_stats: Sequence[backup_tier_stat.BackupTierStat] = None,
        bucket_id: str = None,
        bucket_name: str = None,
        created_timestamp: str = None,
        earliest_available_backup_timestamp: str = None,
        environment_id: str = None,
        group_id: str = None,
        group_name: str = None,
        p_id: str = None,
        is_deleted: bool = None,
        last_backup_timestamp: str = None,
        last_continuous_backup_timestamp: str = None,
        organizational_unit_id: str = None,
        protection_info: protection_info_with_rule.ProtectionInfoWithRule = None,
        protection_status: str = None,
        total_backed_up_object_count: int = None,
        total_backed_up_size_bytes: int = None,
        unsupported_reason: str = None,
    ) -> None:
        """Constructor for the ProtectionGroupBucket class."""

        # Initialize members of the class
        self.embedded: protection_group_bucket_embedded.ProtectionGroupBucketEmbedded = embedded
        self.links: protection_group_bucket_links.ProtectionGroupBucketLinks = links
        self.account_native_id: str = account_native_id
        self.added_by_bucket_rule: bool = added_by_bucket_rule
        self.added_by_user: bool = added_by_user
        self.aws_region: str = aws_region
        self.backup_status_info: backup_status_info.BackupStatusInfo = backup_status_info
        self.backup_target_aws_region: str = backup_target_aws_region
        self.backup_tier_stats: Sequence[backup_tier_stat.BackupTierStat] = backup_tier_stats
        self.bucket_id: str = bucket_id
        self.bucket_name: str = bucket_name
        self.created_timestamp: str = created_timestamp
        self.earliest_available_backup_timestamp: str = earliest_available_backup_timestamp
        self.environment_id: str = environment_id
        self.group_id: str = group_id
        self.group_name: str = group_name
        self.p_id: str = p_id
        self.is_deleted: bool = is_deleted
        self.last_backup_timestamp: str = last_backup_timestamp
        self.last_continuous_backup_timestamp: str = last_continuous_backup_timestamp
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info_with_rule.ProtectionInfoWithRule = protection_info
        self.protection_status: str = protection_status
        self.total_backed_up_object_count: int = total_backed_up_object_count
        self.total_backed_up_size_bytes: int = total_backed_up_size_bytes
        self.unsupported_reason: str = unsupported_reason

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
        key = 'backup_status_info'
        p_backup_status_info = (
            backup_status_info.BackupStatusInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        backup_target_aws_region = dictionary.get('backup_target_aws_region')
        backup_tier_stats = None
        if dictionary.get('backup_tier_stats'):
            backup_tier_stats = list()
            for value in dictionary.get('backup_tier_stats'):
                backup_tier_stats.append(backup_tier_stat.BackupTierStat.from_dictionary(value))

        bucket_id = dictionary.get('bucket_id')
        bucket_name = dictionary.get('bucket_name')
        created_timestamp = dictionary.get('created_timestamp')
        earliest_available_backup_timestamp = dictionary.get('earliest_available_backup_timestamp')
        environment_id = dictionary.get('environment_id')
        group_id = dictionary.get('group_id')
        group_name = dictionary.get('group_name')
        p_id = dictionary.get('id')
        is_deleted = dictionary.get('is_deleted')
        last_backup_timestamp = dictionary.get('last_backup_timestamp')
        last_continuous_backup_timestamp = dictionary.get('last_continuous_backup_timestamp')
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
        unsupported_reason = dictionary.get('unsupported_reason')
        # Return an object of this model
        return cls(
            embedded,
            links,
            account_native_id,
            added_by_bucket_rule,
            added_by_user,
            aws_region,
            p_backup_status_info,
            backup_target_aws_region,
            backup_tier_stats,
            bucket_id,
            bucket_name,
            created_timestamp,
            earliest_available_backup_timestamp,
            environment_id,
            group_id,
            group_name,
            p_id,
            is_deleted,
            last_backup_timestamp,
            last_continuous_backup_timestamp,
            organizational_unit_id,
            protection_info,
            protection_status,
            total_backed_up_object_count,
            total_backed_up_size_bytes,
            unsupported_reason,
        )
