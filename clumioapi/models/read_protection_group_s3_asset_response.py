#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import backup_status_info as backup_status_info_
from clumioapi.models import backup_tier_stat as backup_tier_stat_
from clumioapi.models import protection_group_bucket_embedded as protection_group_bucket_embedded_
from clumioapi.models import protection_group_bucket_links as protection_group_bucket_links_
from clumioapi.models import protection_info_with_rule as protection_info_with_rule_
import requests

T = TypeVar('T', bound='ReadProtectionGroupS3AssetResponse')


@dataclasses.dataclass
class ReadProtectionGroupS3AssetResponse:
    """Implementation of the 'ReadProtectionGroupS3AssetResponse' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        AccountNativeId:
            The aws-assigned id of the account associated with the dynamodb table.

        AddedByBucketRule:
            Whether this bucket was added to this protection group by the bucket rule.

        AddedByUser:
            Whether this bucket was added to this protection group by the user.

        AwsRegion:
            The aws region associated with the dynamodb table.

        BackupStatusInfo:
            The backup status information applied to this resource.

        BackupTargetAwsRegion:
            The backup target aws region associated with the protection group s3 asset.

        BackupTierStats:
            Totalbackedupsizebytes, totalbackedupobjectcount for each backup tier.

        BucketId:
            The clumio-assigned id of the bucket.

        BucketName:
            The name of the bucket.

        CreatedTimestamp:
            Creation time of the protection group in rfc-3339 format.

        EarliestAvailableBackupTimestamp:
            Timestamp of the earliest protection group backup which has not expired yet.
            represented in
            rfc-3339 format. only available for read api.

        EnvironmentId:
            The clumio-assigned id of the aws environment associated with the protection
            group.

        GroupId:
            The clumio-assigned id of the protection group.

        GroupName:
            The name of the protection group.

        Id:
            The clumio-assigned id that represents the bucket within the protection group.

        IsDeleted:
            Determines whether the protection group bucket has been deleted.

        LastBackupTimestamp:
            Time of the last backup in rfc-3339 format.

        LastContinuousBackupTimestamp:
            Time of the last successful continuous backup in rfc-3339 format.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the protection
            group.

        ProtectionInfo:
            The protection policy applied to this resource. if the resource is not
            protected, then this field has a value of `null`.

        ProtectionStatus:
            The protection status of the protection group. possible values include
            "protected",
            "unprotected", and "unsupported". if the protection group does not support
            backups, then
            this field has a value of `unsupported`.

        TotalBackedUpObjectCount:
            Cumulative count of all unexpired objects in each backup (any new or updated
            since
            the last backup) that have been backed up as part of this protection group.

        TotalBackedUpSizeBytes:
            Cumulative size of all unexpired objects in each backup (any new or updated
            since
            the last backup) that have been backed up as part of this protection group.

        UnsupportedReason:
            The unsupported reason for the s3 bucket.

    """

    Embedded: protection_group_bucket_embedded_.ProtectionGroupBucketEmbedded | None = None
    Links: protection_group_bucket_links_.ProtectionGroupBucketLinks | None = None
    AccountNativeId: str | None = None
    AddedByBucketRule: bool | None = None
    AddedByUser: bool | None = None
    AwsRegion: str | None = None
    BackupStatusInfo: backup_status_info_.BackupStatusInfo | None = None
    BackupTargetAwsRegion: str | None = None
    BackupTierStats: Sequence[backup_tier_stat_.BackupTierStat] | None = None
    BucketId: str | None = None
    BucketName: str | None = None
    CreatedTimestamp: str | None = None
    EarliestAvailableBackupTimestamp: str | None = None
    EnvironmentId: str | None = None
    GroupId: str | None = None
    GroupName: str | None = None
    Id: str | None = None
    IsDeleted: bool | None = None
    LastBackupTimestamp: str | None = None
    LastContinuousBackupTimestamp: str | None = None
    OrganizationalUnitId: str | None = None
    ProtectionInfo: protection_info_with_rule_.ProtectionInfoWithRule | None = None
    ProtectionStatus: str | None = None
    TotalBackedUpObjectCount: int | None = None
    TotalBackedUpSizeBytes: int | None = None
    UnsupportedReason: str | None = None
    raw_response: Optional[requests.Response] = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('_embedded', None)
        val_embedded = (
            protection_group_bucket_embedded_.ProtectionGroupBucketEmbedded.from_dictionary(val)
        )

        val = dictionary.get('_links', None)
        val_links = protection_group_bucket_links_.ProtectionGroupBucketLinks.from_dictionary(val)

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('added_by_bucket_rule', None)
        val_added_by_bucket_rule = val

        val = dictionary.get('added_by_user', None)
        val_added_by_user = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('backup_status_info', None)
        val_backup_status_info = backup_status_info_.BackupStatusInfo.from_dictionary(val)

        val = dictionary.get('backup_target_aws_region', None)
        val_backup_target_aws_region = val

        val = dictionary.get('backup_tier_stats', None)

        val_backup_tier_stats = []
        if val:
            for value in val:
                val_backup_tier_stats.append(
                    backup_tier_stat_.BackupTierStat.from_dictionary(value)
                )

        val = dictionary.get('bucket_id', None)
        val_bucket_id = val

        val = dictionary.get('bucket_name', None)
        val_bucket_name = val

        val = dictionary.get('created_timestamp', None)
        val_created_timestamp = val

        val = dictionary.get('earliest_available_backup_timestamp', None)
        val_earliest_available_backup_timestamp = val

        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('group_id', None)
        val_group_id = val

        val = dictionary.get('group_name', None)
        val_group_name = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('is_deleted', None)
        val_is_deleted = val

        val = dictionary.get('last_backup_timestamp', None)
        val_last_backup_timestamp = val

        val = dictionary.get('last_continuous_backup_timestamp', None)
        val_last_continuous_backup_timestamp = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('protection_info', None)
        val_protection_info = protection_info_with_rule_.ProtectionInfoWithRule.from_dictionary(val)

        val = dictionary.get('protection_status', None)
        val_protection_status = val

        val = dictionary.get('total_backed_up_object_count', None)
        val_total_backed_up_object_count = val

        val = dictionary.get('total_backed_up_size_bytes', None)
        val_total_backed_up_size_bytes = val

        val = dictionary.get('unsupported_reason', None)
        val_unsupported_reason = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_account_native_id,
            val_added_by_bucket_rule,
            val_added_by_user,
            val_aws_region,
            val_backup_status_info,
            val_backup_target_aws_region,
            val_backup_tier_stats,
            val_bucket_id,
            val_bucket_name,
            val_created_timestamp,
            val_earliest_available_backup_timestamp,
            val_environment_id,
            val_group_id,
            val_group_name,
            val_id,
            val_is_deleted,
            val_last_backup_timestamp,
            val_last_continuous_backup_timestamp,
            val_organizational_unit_id,
            val_protection_info,
            val_protection_status,
            val_total_backed_up_object_count,
            val_total_backed_up_size_bytes,
            val_unsupported_reason,
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
        model_instance.raw_response = response
        return model_instance
