#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import backup_status_stats as backup_status_stats_
from clumioapi.models import backup_tier_stat as backup_tier_stat_
from clumioapi.models import object_filter as object_filter_
from clumioapi.models import protection_group_embedded as protection_group_embedded_
from clumioapi.models import protection_group_links as protection_group_links_
from clumioapi.models import protection_info_with_rule as protection_info_with_rule_
from clumioapi.models import protection_stats as protection_stats_
import requests

T = TypeVar('T', bound='ProtectionGroup')


@dataclasses.dataclass
class ProtectionGroup:
    """Implementation of the 'ProtectionGroup' model.

        Attributes:
            Embedded:
                Embedded responses related to the resource.

            Links:
                Urls to pages related to the resource.

            BackupStatusStats:
                Represents the aggregated stats for backup status.

            BackupTargetAwsRegion:
                The backup target aws region associated with the protection group, empty if
    in-region or not configured.

            BackupTierStats:
                Totalbackedupsizebytes, totalbackedupobjectcount for each backup tier.

            BucketCount:
                Number of buckets.

            BucketRule:
                `{'$in':[{'key':'environment','value':'prod'}, {'key':'hello', 'value':'world'}]}`.

    +-------------------+-----------------------------+----------------------------+
    |       field       |       rule condition        |        description         |
    +===================+=============================+============================+
    | aws_tag           | $eq, $not_eq, $contains,    | supports filtering by aws  |
    |                   | $not_contains, $all,        | tag(s) using the following |
    |                   | $not_all, $in, $not_in      | operators. for example,    |
    |                   |                             |                            |
    |                   |                             | {"aws_tag":{"$eq":{"key":" |
    |                   |                             | environment",              |
    |                   |                             | "value":"prod"}}}          |
    |                   |                             |                            |
    |                   |                             |                            |
    +-------------------+-----------------------------+----------------------------+
    | account_native_id | $eq, $in                    |                            |
    |                   |                             | this will be deprecated    |
    |                   |                             | and use                    |
    |                   |                             | aws_account_native_id      |
    |                   |                             | instead.                   |
    |                   |                             | supports filtering by aws  |
    |                   |                             | account(s) using the       |
    |                   |                             | following operators. for   |
    |                   |                             | example,                   |
    |                   |                             |                            |
    |                   |                             | {"account_native_id":{"$in |
    |                   |                             | ":["111111111111"]}}       |
    |                   |                             |                            |
    |                   |                             |                            |
    +-------------------+-----------------------------+----------------------------+
    | aws_region        | $eq, $in                    | supports filtering by aws  |
    |                   |                             | region(s) using the        |
    |                   |                             | following operators. for   |
    |                   |                             | example,                   |
    |                   |                             |                            |
    |                   |                             | {"aws_region":{"$eq":"us-  |
    |                   |                             | west-2"}}                  |
    |                   |                             |                            |
    |                   |                             |                            |
    +-------------------+-----------------------------+----------------------------+
    .

            CreatedTimestamp:
                Creation time of the protection group in rfc-3339 format.

            Description:
                The user-assigned description of the protection group.

            EarliestAvailableBackupTimestamp:
                Timestamp of the earliest protection group backup which has not expired yet. represented in
    rfc-3339 format. only available for read api.

            Id:
                The clumio-assigned id of the protection group.

            IsBackupTargetRegionConfigured:
                Whether the protection group already has a backup target configured by a policy, or
    is open to be protected by an in-region or out-of-region s3 policy.

            IsDeleted:
                Determines whether the protection group is active or has been deleted. deleted protection
    groups may be purged after some time once there are no active backups associated with it.

            LastBackupTimestamp:
                Time of the last backup in rfc-3339 format.

            LastContinuousBackupTimestamp:
                Time of the last successful continuous backup in rfc-3339 format.

            ModifiedTimestamp:
                Modified time of the protection group in rfc-3339 format.

            Name:
                The user-assigned name of the protection group.

            ObjectFilter:
                Objectfilter
    defines which objects will be backed up.

            OrganizationalUnitId:
                The clumio-assigned id of the organizational unit associated with the protection group.

            ProtectionInfo:
                The protection policy applied to this resource. if the resource is not protected, then this field has a value of `null`.

            ProtectionStats:
                .

            ProtectionStatus:
                The protection status of the protection group. possible values include "protected",
    "unprotected", and "unsupported". if the protection group does not support backups, then
    this field has a value of `unsupported`.

            TotalBackedUpObjectCount:
                Cumulative count of all unexpired objects in each backup (any new or updated since
    the last backup) that have been backed up as part of this protection group.

            TotalBackedUpSizeBytes:
                Cumulative size of all unexpired objects in each backup (any new or updated since
    the last backup) that have been backed up as part of this protection group.

            Version:
                Version of the protection group. the version number is incremented every time
    a change is made to the protection group.

    """

    Embedded: protection_group_embedded_.ProtectionGroupEmbedded | None = None
    Links: protection_group_links_.ProtectionGroupLinks | None = None
    BackupStatusStats: backup_status_stats_.BackupStatusStats | None = None
    BackupTargetAwsRegion: str | None = None
    BackupTierStats: Sequence[backup_tier_stat_.BackupTierStat] | None = None
    BucketCount: int | None = None
    BucketRule: str | None = None
    CreatedTimestamp: str | None = None
    Description: str | None = None
    EarliestAvailableBackupTimestamp: str | None = None
    Id: str | None = None
    IsBackupTargetRegionConfigured: bool | None = None
    IsDeleted: bool | None = None
    LastBackupTimestamp: str | None = None
    LastContinuousBackupTimestamp: str | None = None
    ModifiedTimestamp: str | None = None
    Name: str | None = None
    ObjectFilter: object_filter_.ObjectFilter | None = None
    OrganizationalUnitId: str | None = None
    ProtectionInfo: protection_info_with_rule_.ProtectionInfoWithRule | None = None
    ProtectionStats: protection_stats_.ProtectionStats | None = None
    ProtectionStatus: str | None = None
    TotalBackedUpObjectCount: int | None = None
    TotalBackedUpSizeBytes: int | None = None
    Version: int | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
        val_embedded = protection_group_embedded_.ProtectionGroupEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = protection_group_links_.ProtectionGroupLinks.from_dictionary(val)

        val = dictionary.get('backup_status_stats', None)
        val_backup_status_stats = backup_status_stats_.BackupStatusStats.from_dictionary(val)

        val = dictionary.get('backup_target_aws_region', None)
        val_backup_target_aws_region = val

        val = dictionary.get('backup_tier_stats', None)

        val_backup_tier_stats = []
        if val:
            for value in val:
                val_backup_tier_stats.append(
                    backup_tier_stat_.BackupTierStat.from_dictionary(value)
                )

        val = dictionary.get('bucket_count', None)
        val_bucket_count = val

        val = dictionary.get('bucket_rule', None)
        val_bucket_rule = val

        val = dictionary.get('created_timestamp', None)
        val_created_timestamp = val

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('earliest_available_backup_timestamp', None)
        val_earliest_available_backup_timestamp = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('is_backup_target_region_configured', None)
        val_is_backup_target_region_configured = val

        val = dictionary.get('is_deleted', None)
        val_is_deleted = val

        val = dictionary.get('last_backup_timestamp', None)
        val_last_backup_timestamp = val

        val = dictionary.get('last_continuous_backup_timestamp', None)
        val_last_continuous_backup_timestamp = val

        val = dictionary.get('modified_timestamp', None)
        val_modified_timestamp = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('object_filter', None)
        val_object_filter = object_filter_.ObjectFilter.from_dictionary(val)

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('protection_info', None)
        val_protection_info = protection_info_with_rule_.ProtectionInfoWithRule.from_dictionary(val)

        val = dictionary.get('protection_stats', None)
        val_protection_stats = protection_stats_.ProtectionStats.from_dictionary(val)

        val = dictionary.get('protection_status', None)
        val_protection_status = val

        val = dictionary.get('total_backed_up_object_count', None)
        val_total_backed_up_object_count = val

        val = dictionary.get('total_backed_up_size_bytes', None)
        val_total_backed_up_size_bytes = val

        val = dictionary.get('version', None)
        val_version = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_backup_status_stats,
            val_backup_target_aws_region,
            val_backup_tier_stats,
            val_bucket_count,
            val_bucket_rule,
            val_created_timestamp,
            val_description,
            val_earliest_available_backup_timestamp,
            val_id,
            val_is_backup_target_region_configured,
            val_is_deleted,
            val_last_backup_timestamp,
            val_last_continuous_backup_timestamp,
            val_modified_timestamp,
            val_name,
            val_object_filter,
            val_organizational_unit_id,
            val_protection_info,
            val_protection_stats,
            val_protection_status,
            val_total_backed_up_object_count,
            val_total_backed_up_size_bytes,
            val_version,
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
        return model_instance
