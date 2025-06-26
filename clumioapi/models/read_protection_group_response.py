#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import backup_status_stats
from clumioapi.models import backup_tier_stat
from clumioapi.models import object_filter
from clumioapi.models import protection_group_embedded
from clumioapi.models import protection_group_links
from clumioapi.models import protection_info_with_rule
from clumioapi.models import protection_stats

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
            'value':'Prod'}}`. For all other other operations, a list is provided:
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
    _names = {
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
        embedded: protection_group_embedded.ProtectionGroupEmbedded = None,
        links: protection_group_links.ProtectionGroupLinks = None,
        backup_status_stats: backup_status_stats.BackupStatusStats = None,
        backup_target_aws_region: str = None,
        backup_tier_stats: Sequence[backup_tier_stat.BackupTierStat] = None,
        bucket_count: int = None,
        bucket_rule: str = None,
        created_timestamp: str = None,
        description: str = None,
        earliest_available_backup_timestamp: str = None,
        p_id: str = None,
        is_backup_target_region_configured: bool = None,
        is_deleted: bool = None,
        last_backup_timestamp: str = None,
        last_continuous_backup_timestamp: str = None,
        modified_timestamp: str = None,
        name: str = None,
        object_filter: object_filter.ObjectFilter = None,
        organizational_unit_id: str = None,
        protection_info: protection_info_with_rule.ProtectionInfoWithRule = None,
        protection_stats: protection_stats.ProtectionStats = None,
        protection_status: str = None,
        regions: Sequence[str] = None,
        total_backed_up_object_count: int = None,
        total_backed_up_size_bytes: int = None,
        version: int = None,
    ) -> None:
        """Constructor for the ReadProtectionGroupResponse class."""

        # Initialize members of the class
        self.embedded: protection_group_embedded.ProtectionGroupEmbedded = embedded
        self.links: protection_group_links.ProtectionGroupLinks = links
        self.backup_status_stats: backup_status_stats.BackupStatusStats = backup_status_stats
        self.backup_target_aws_region: str = backup_target_aws_region
        self.backup_tier_stats: Sequence[backup_tier_stat.BackupTierStat] = backup_tier_stats
        self.bucket_count: int = bucket_count
        self.bucket_rule: str = bucket_rule
        self.created_timestamp: str = created_timestamp
        self.description: str = description
        self.earliest_available_backup_timestamp: str = earliest_available_backup_timestamp
        self.p_id: str = p_id
        self.is_backup_target_region_configured: bool = is_backup_target_region_configured
        self.is_deleted: bool = is_deleted
        self.last_backup_timestamp: str = last_backup_timestamp
        self.last_continuous_backup_timestamp: str = last_continuous_backup_timestamp
        self.modified_timestamp: str = modified_timestamp
        self.name: str = name
        self.object_filter: object_filter.ObjectFilter = object_filter
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info_with_rule.ProtectionInfoWithRule = protection_info
        self.protection_stats: protection_stats.ProtectionStats = protection_stats
        self.protection_status: str = protection_status
        self.regions: Sequence[str] = regions
        self.total_backed_up_object_count: int = total_backed_up_object_count
        self.total_backed_up_size_bytes: int = total_backed_up_size_bytes
        self.version: int = version

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
            protection_group_embedded.ProtectionGroupEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            protection_group_links.ProtectionGroupLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'backup_status_stats'
        p_backup_status_stats = (
            backup_status_stats.BackupStatusStats.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        backup_target_aws_region = dictionary.get('backup_target_aws_region')
        backup_tier_stats = None
        if dictionary.get('backup_tier_stats'):
            backup_tier_stats = list()
            for value in dictionary.get('backup_tier_stats'):
                backup_tier_stats.append(backup_tier_stat.BackupTierStat.from_dictionary(value))

        bucket_count = dictionary.get('bucket_count')
        bucket_rule = dictionary.get('bucket_rule')
        created_timestamp = dictionary.get('created_timestamp')
        description = dictionary.get('description')
        earliest_available_backup_timestamp = dictionary.get('earliest_available_backup_timestamp')
        p_id = dictionary.get('id')
        is_backup_target_region_configured = dictionary.get('is_backup_target_region_configured')
        is_deleted = dictionary.get('is_deleted')
        last_backup_timestamp = dictionary.get('last_backup_timestamp')
        last_continuous_backup_timestamp = dictionary.get('last_continuous_backup_timestamp')
        modified_timestamp = dictionary.get('modified_timestamp')
        name = dictionary.get('name')
        key = 'object_filter'
        p_object_filter = (
            object_filter.ObjectFilter.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        organizational_unit_id = dictionary.get('organizational_unit_id')
        key = 'protection_info'
        protection_info = (
            protection_info_with_rule.ProtectionInfoWithRule.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'protection_stats'
        p_protection_stats = (
            protection_stats.ProtectionStats.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        protection_status = dictionary.get('protection_status')
        regions = dictionary.get('regions')
        total_backed_up_object_count = dictionary.get('total_backed_up_object_count')
        total_backed_up_size_bytes = dictionary.get('total_backed_up_size_bytes')
        version = dictionary.get('version')
        # Return an object of this model
        return cls(
            embedded,
            links,
            p_backup_status_stats,
            backup_target_aws_region,
            backup_tier_stats,
            bucket_count,
            bucket_rule,
            created_timestamp,
            description,
            earliest_available_backup_timestamp,
            p_id,
            is_backup_target_region_configured,
            is_deleted,
            last_backup_timestamp,
            last_continuous_backup_timestamp,
            modified_timestamp,
            name,
            p_object_filter,
            organizational_unit_id,
            protection_info,
            p_protection_stats,
            protection_status,
            regions,
            total_backed_up_object_count,
            total_backed_up_size_bytes,
            version,
        )
