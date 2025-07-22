#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import backup_status_info as backup_status_info_
from clumioapi.models import backup_tier_stat as backup_tier_stat_
from clumioapi.models import protection_group_bucket_embedded as protection_group_bucket_embedded_
from clumioapi.models import protection_group_bucket_links as protection_group_bucket_links_
from clumioapi.models import protection_info_with_rule as protection_info_with_rule_

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
    _names: dict[str, str] = {
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
        embedded: protection_group_bucket_embedded_.ProtectionGroupBucketEmbedded,
        links: protection_group_bucket_links_.ProtectionGroupBucketLinks,
        account_native_id: str,
        added_by_bucket_rule: bool,
        added_by_user: bool,
        aws_region: str,
        backup_status_info: backup_status_info_.BackupStatusInfo,
        backup_target_aws_region: str,
        backup_tier_stats: Sequence[backup_tier_stat_.BackupTierStat],
        bucket_id: str,
        bucket_name: str,
        created_timestamp: str,
        earliest_available_backup_timestamp: str,
        environment_id: str,
        group_id: str,
        group_name: str,
        p_id: str,
        is_deleted: bool,
        last_backup_timestamp: str,
        last_continuous_backup_timestamp: str,
        organizational_unit_id: str,
        protection_info: protection_info_with_rule_.ProtectionInfoWithRule,
        protection_status: str,
        total_backed_up_object_count: int,
        total_backed_up_size_bytes: int,
        unsupported_reason: str,
    ) -> None:
        """Constructor for the ProtectionGroupBucket class."""

        # Initialize members of the class
        self.embedded: protection_group_bucket_embedded_.ProtectionGroupBucketEmbedded = embedded
        self.links: protection_group_bucket_links_.ProtectionGroupBucketLinks = links
        self.account_native_id: str = account_native_id
        self.added_by_bucket_rule: bool = added_by_bucket_rule
        self.added_by_user: bool = added_by_user
        self.aws_region: str = aws_region
        self.backup_status_info: backup_status_info_.BackupStatusInfo = backup_status_info
        self.backup_target_aws_region: str = backup_target_aws_region
        self.backup_tier_stats: Sequence[backup_tier_stat_.BackupTierStat] = backup_tier_stats
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
        self.protection_info: protection_info_with_rule_.ProtectionInfoWithRule = protection_info
        self.protection_status: str = protection_status
        self.total_backed_up_object_count: int = total_backed_up_object_count
        self.total_backed_up_size_bytes: int = total_backed_up_size_bytes
        self.unsupported_reason: str = unsupported_reason

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
            protection_group_bucket_embedded_.ProtectionGroupBucketEmbedded.from_dictionary(val)
        )

        val = dictionary['_links']
        val_links = protection_group_bucket_links_.ProtectionGroupBucketLinks.from_dictionary(val)

        val = dictionary['account_native_id']
        val_account_native_id = val

        val = dictionary['added_by_bucket_rule']
        val_added_by_bucket_rule = val

        val = dictionary['added_by_user']
        val_added_by_user = val

        val = dictionary['aws_region']
        val_aws_region = val

        val = dictionary['backup_status_info']
        val_backup_status_info = backup_status_info_.BackupStatusInfo.from_dictionary(val)

        val = dictionary['backup_target_aws_region']
        val_backup_target_aws_region = val

        val = dictionary['backup_tier_stats']

        val_backup_tier_stats = None
        if val:
            val_backup_tier_stats = list()
            for value in val:
                val_backup_tier_stats.append(
                    backup_tier_stat_.BackupTierStat.from_dictionary(value)
                )

        val = dictionary['bucket_id']
        val_bucket_id = val

        val = dictionary['bucket_name']
        val_bucket_name = val

        val = dictionary['created_timestamp']
        val_created_timestamp = val

        val = dictionary['earliest_available_backup_timestamp']
        val_earliest_available_backup_timestamp = val

        val = dictionary['environment_id']
        val_environment_id = val

        val = dictionary['group_id']
        val_group_id = val

        val = dictionary['group_name']
        val_group_name = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['is_deleted']
        val_is_deleted = val

        val = dictionary['last_backup_timestamp']
        val_last_backup_timestamp = val

        val = dictionary['last_continuous_backup_timestamp']
        val_last_continuous_backup_timestamp = val

        val = dictionary['organizational_unit_id']
        val_organizational_unit_id = val

        val = dictionary['protection_info']
        val_protection_info = protection_info_with_rule_.ProtectionInfoWithRule.from_dictionary(val)

        val = dictionary['protection_status']
        val_protection_status = val

        val = dictionary['total_backed_up_object_count']
        val_total_backed_up_object_count = val

        val = dictionary['total_backed_up_size_bytes']
        val_total_backed_up_size_bytes = val

        val = dictionary['unsupported_reason']
        val_unsupported_reason = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_account_native_id,  # type: ignore
            val_added_by_bucket_rule,  # type: ignore
            val_added_by_user,  # type: ignore
            val_aws_region,  # type: ignore
            val_backup_status_info,  # type: ignore
            val_backup_target_aws_region,  # type: ignore
            val_backup_tier_stats,  # type: ignore
            val_bucket_id,  # type: ignore
            val_bucket_name,  # type: ignore
            val_created_timestamp,  # type: ignore
            val_earliest_available_backup_timestamp,  # type: ignore
            val_environment_id,  # type: ignore
            val_group_id,  # type: ignore
            val_group_name,  # type: ignore
            val_p_id,  # type: ignore
            val_is_deleted,  # type: ignore
            val_last_backup_timestamp,  # type: ignore
            val_last_continuous_backup_timestamp,  # type: ignore
            val_organizational_unit_id,  # type: ignore
            val_protection_info,  # type: ignore
            val_protection_status,  # type: ignore
            val_total_backed_up_object_count,  # type: ignore
            val_total_backed_up_size_bytes,  # type: ignore
            val_unsupported_reason,  # type: ignore
        )
