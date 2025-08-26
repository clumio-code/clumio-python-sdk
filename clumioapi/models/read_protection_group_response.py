#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import backup_status_stats as backup_status_stats_
from clumioapi.models import backup_tier_stat as backup_tier_stat_
from clumioapi.models import object_filter as object_filter_
from clumioapi.models import protection_group_embedded as protection_group_embedded_
from clumioapi.models import protection_group_links as protection_group_links_
from clumioapi.models import protection_info_with_rule as protection_info_with_rule_
from clumioapi.models import protection_stats as protection_stats_

T = TypeVar('T', bound='ReadProtectionGroupResponse')


class ReadProtectionGroupResponse:
    """Implementation of the 'ReadProtectionGroupResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        backup_status_stats:
            Represents the aggregated stats for backup status.
        backup_target_aws_region:
            The backup target AWS region associated with the protection group, empty if
            in-region or not configured.
        backup_tier_stats:
            TotalBackedUpSizeBytes, TotalBackedUpObjectCount for each backup tier
        bucket_count:
            Number of buckets
        bucket_rule:
            The following table describes the possible conditions for a bucket to be
            automatically added to a protection group.
            Denotes the properties to conditionalize on. For `$eq`, `$not_eq`, `$contains`
            and `$not_contains` a single element is provided: `{'$eq':{'key':'Environment',
            'value':'Prod'}}`. For all other operations, a list is provided:
            `{'$in':[{'key':'Environment','value':'Prod'}, {'key':'Hello',
            'value':'World'}]}`.

            +-------------------+-----------------------------+----------------------------+
            |       Field       |       Rule Condition        |        Description         |
            +===================+=============================+============================+
            | aws_tag           | $eq, $not_eq, $contains,    | Supports filtering by AWS  |
            |                   | $not_contains, $all,        | tag(s) using the following |
            |                   | $not_all, $in, $not_in      | operators. For example,    |
            |                   |                             |                            |
            |                   |                             | {"aws_tag":{"$eq":{"key":" |
            |                   |                             | Environment",              |
            |                   |                             | "value":"Prod"}}}          |
            |                   |                             |                            |
            |                   |                             |                            |
            +-------------------+-----------------------------+----------------------------+
            | account_native_id | $eq, $in                    |                            |
            |                   |                             | This will be deprecated    |
            |                   |                             | and use                    |
            |                   |                             | aws_account_native_id      |
            |                   |                             | instead.                   |
            |                   |                             | Supports filtering by AWS  |
            |                   |                             | account(s) using the       |
            |                   |                             | following operators. For   |
            |                   |                             | example,                   |
            |                   |                             |                            |
            |                   |                             | {"account_native_id":{"$in |
            |                   |                             | ":["111111111111"]}}       |
            |                   |                             |                            |
            |                   |                             |                            |
            +-------------------+-----------------------------+----------------------------+
            | aws_region        | $eq, $in                    | Supports filtering by AWS  |
            |                   |                             | region(s) using the        |
            |                   |                             | following operators. For   |
            |                   |                             | example,                   |
            |                   |                             |                            |
            |                   |                             | {"aws_region":{"$eq":"us-  |
            |                   |                             | west-2"}}                  |
            |                   |                             |                            |
            |                   |                             |                            |
            +-------------------+-----------------------------+----------------------------+
        created_timestamp:
            Creation time of the protection group in RFC-3339 format.
        description:
            The user-assigned description of the protection group.
        earliest_available_backup_timestamp:
            Timestamp of the earliest protection group backup which has not expired yet.
            Represented in
            RFC-3339 format. Only available for Read API.
        p_id:
            The Clumio-assigned ID of the protection group.
        is_backup_target_region_configured:
            Whether the protection group already has a backup target configured by a policy,
            or
            is open to be protected by an in-region or out-of-region S3 policy.
        is_deleted:
            Determines whether the protection group is active or has been deleted. Deleted
            protection
            groups may be purged after some time once there are no active backups associated
            with it.
        last_backup_timestamp:
            Time of the last backup in RFC-3339 format.
        last_continuous_backup_timestamp:
            Time of the last successful continuous backup in RFC-3339 format.
        modified_timestamp:
            Modified time of the protection group in RFC-3339 format.
        name:
            The user-assigned name of the protection group.
        object_filter:
            ObjectFilter
            defines which objects will be backed up.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the Protection
            Group.
        protection_info:
            The protection policy applied to this resource. If the resource is not
            protected, then this field has a value of `null`.
        protection_stats:

        protection_status:
            The protection status of the protection group. Possible values include
            "protected",
            "unprotected", and "unsupported". If the protection group does not support
            backups, then
            this field has a value of `unsupported`.
        regions:
            The list of AWS regions that this protection group is linked to
        total_backed_up_object_count:
            Cumulative count of all unexpired objects in each backup (any new or updated
            since
            the last backup) that have been backed up as part of this protection group
        total_backed_up_size_bytes:
            Cumulative size of all unexpired objects in each backup (any new or updated
            since
            the last backup) that have been backed up as part of this protection group
        version:
            Version of the protection group. The version number is incremented every time
            a change is made to the protection group.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'backup_status_stats': 'backup_status_stats',
        'backup_target_aws_region': 'backup_target_aws_region',
        'backup_tier_stats': 'backup_tier_stats',
        'bucket_count': 'bucket_count',
        'bucket_rule': 'bucket_rule',
        'created_timestamp': 'created_timestamp',
        'description': 'description',
        'earliest_available_backup_timestamp': 'earliest_available_backup_timestamp',
        'p_id': 'id',
        'is_backup_target_region_configured': 'is_backup_target_region_configured',
        'is_deleted': 'is_deleted',
        'last_backup_timestamp': 'last_backup_timestamp',
        'last_continuous_backup_timestamp': 'last_continuous_backup_timestamp',
        'modified_timestamp': 'modified_timestamp',
        'name': 'name',
        'object_filter': 'object_filter',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
        'protection_stats': 'protection_stats',
        'protection_status': 'protection_status',
        'regions': 'regions',
        'total_backed_up_object_count': 'total_backed_up_object_count',
        'total_backed_up_size_bytes': 'total_backed_up_size_bytes',
        'version': 'version',
    }

    def __init__(
        self,
        embedded: protection_group_embedded_.ProtectionGroupEmbedded | None = None,
        links: protection_group_links_.ProtectionGroupLinks | None = None,
        backup_status_stats: backup_status_stats_.BackupStatusStats | None = None,
        backup_target_aws_region: str | None = None,
        backup_tier_stats: Sequence[backup_tier_stat_.BackupTierStat] | None = None,
        bucket_count: int | None = None,
        bucket_rule: str | None = None,
        created_timestamp: str | None = None,
        description: str | None = None,
        earliest_available_backup_timestamp: str | None = None,
        p_id: str | None = None,
        is_backup_target_region_configured: bool | None = None,
        is_deleted: bool | None = None,
        last_backup_timestamp: str | None = None,
        last_continuous_backup_timestamp: str | None = None,
        modified_timestamp: str | None = None,
        name: str | None = None,
        object_filter: object_filter_.ObjectFilter | None = None,
        organizational_unit_id: str | None = None,
        protection_info: protection_info_with_rule_.ProtectionInfoWithRule | None = None,
        protection_stats: protection_stats_.ProtectionStats | None = None,
        protection_status: str | None = None,
        regions: Sequence[str] | None = None,
        total_backed_up_object_count: int | None = None,
        total_backed_up_size_bytes: int | None = None,
        version: int | None = None,
    ) -> None:
        """Constructor for the ReadProtectionGroupResponse class."""

        # Initialize members of the class
        self.embedded: protection_group_embedded_.ProtectionGroupEmbedded | None = embedded
        self.links: protection_group_links_.ProtectionGroupLinks | None = links
        self.backup_status_stats: backup_status_stats_.BackupStatusStats | None = (
            backup_status_stats
        )
        self.backup_target_aws_region: str | None = backup_target_aws_region
        self.backup_tier_stats: Sequence[backup_tier_stat_.BackupTierStat] | None = (
            backup_tier_stats
        )
        self.bucket_count: int | None = bucket_count
        self.bucket_rule: str | None = bucket_rule
        self.created_timestamp: str | None = created_timestamp
        self.description: str | None = description
        self.earliest_available_backup_timestamp: str | None = earliest_available_backup_timestamp
        self.p_id: str | None = p_id
        self.is_backup_target_region_configured: bool | None = is_backup_target_region_configured
        self.is_deleted: bool | None = is_deleted
        self.last_backup_timestamp: str | None = last_backup_timestamp
        self.last_continuous_backup_timestamp: str | None = last_continuous_backup_timestamp
        self.modified_timestamp: str | None = modified_timestamp
        self.name: str | None = name
        self.object_filter: object_filter_.ObjectFilter | None = object_filter
        self.organizational_unit_id: str | None = organizational_unit_id
        self.protection_info: protection_info_with_rule_.ProtectionInfoWithRule | None = (
            protection_info
        )
        self.protection_stats: protection_stats_.ProtectionStats | None = protection_stats
        self.protection_status: str | None = protection_status
        self.regions: Sequence[str] | None = regions
        self.total_backed_up_object_count: int | None = total_backed_up_object_count
        self.total_backed_up_size_bytes: int | None = total_backed_up_size_bytes
        self.version: int | None = version

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
        val_embedded = protection_group_embedded_.ProtectionGroupEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = protection_group_links_.ProtectionGroupLinks.from_dictionary(val)

        val = dictionary.get('backup_status_stats', None)
        val_backup_status_stats = backup_status_stats_.BackupStatusStats.from_dictionary(val)

        val = dictionary.get('backup_target_aws_region', None)
        val_backup_target_aws_region = val

        val = dictionary.get('backup_tier_stats', None)

        val_backup_tier_stats = None
        if val:
            val_backup_tier_stats = list()
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
        val_p_id = val

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

        val = dictionary.get('regions', None)
        val_regions = val

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
            val_p_id,
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
            val_regions,
            val_total_backed_up_object_count,
            val_total_backed_up_size_bytes,
            val_version,
        )
