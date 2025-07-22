#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import backup_tier_stat as backup_tier_stat_
from clumioapi.models import object_filter as object_filter_
from clumioapi.models import protection_group_version_links as protection_group_version_links_

T = TypeVar('T', bound='UpdateProtectionGroupResponse')


class UpdateProtectionGroupResponse:
    """Implementation of the 'UpdateProtectionGroupResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
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
        'backup_target_aws_region': 'backup_target_aws_region',
        'backup_tier_stats': 'backup_tier_stats',
        'bucket_count': 'bucket_count',
        'bucket_rule': 'bucket_rule',
        'created_timestamp': 'created_timestamp',
        'description': 'description',
        'p_id': 'id',
        'is_backup_target_region_configured': 'is_backup_target_region_configured',
        'is_deleted': 'is_deleted',
        'last_backup_timestamp': 'last_backup_timestamp',
        'last_continuous_backup_timestamp': 'last_continuous_backup_timestamp',
        'modified_timestamp': 'modified_timestamp',
        'name': 'name',
        'object_filter': 'object_filter',
        'organizational_unit_id': 'organizational_unit_id',
        'total_backed_up_object_count': 'total_backed_up_object_count',
        'total_backed_up_size_bytes': 'total_backed_up_size_bytes',
        'version': 'version',
    }

    def __init__(
        self,
        embedded: object,
        links: protection_group_version_links_.ProtectionGroupVersionLinks,
        backup_target_aws_region: str,
        backup_tier_stats: Sequence[backup_tier_stat_.BackupTierStat],
        bucket_count: int,
        bucket_rule: str,
        created_timestamp: str,
        description: str,
        p_id: str,
        is_backup_target_region_configured: bool,
        is_deleted: bool,
        last_backup_timestamp: str,
        last_continuous_backup_timestamp: str,
        modified_timestamp: str,
        name: str,
        object_filter: object_filter_.ObjectFilter,
        organizational_unit_id: str,
        total_backed_up_object_count: int,
        total_backed_up_size_bytes: int,
        version: int,
    ) -> None:
        """Constructor for the UpdateProtectionGroupResponse class."""

        # Initialize members of the class
        self.embedded: object = embedded
        self.links: protection_group_version_links_.ProtectionGroupVersionLinks = links
        self.backup_target_aws_region: str = backup_target_aws_region
        self.backup_tier_stats: Sequence[backup_tier_stat_.BackupTierStat] = backup_tier_stats
        self.bucket_count: int = bucket_count
        self.bucket_rule: str = bucket_rule
        self.created_timestamp: str = created_timestamp
        self.description: str = description
        self.p_id: str = p_id
        self.is_backup_target_region_configured: bool = is_backup_target_region_configured
        self.is_deleted: bool = is_deleted
        self.last_backup_timestamp: str = last_backup_timestamp
        self.last_continuous_backup_timestamp: str = last_continuous_backup_timestamp
        self.modified_timestamp: str = modified_timestamp
        self.name: str = name
        self.object_filter: object_filter_.ObjectFilter = object_filter
        self.organizational_unit_id: str = organizational_unit_id
        self.total_backed_up_object_count: int = total_backed_up_object_count
        self.total_backed_up_size_bytes: int = total_backed_up_size_bytes
        self.version: int = version

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
        val_embedded = val

        val = dictionary['_links']
        val_links = protection_group_version_links_.ProtectionGroupVersionLinks.from_dictionary(val)

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

        val = dictionary['bucket_count']
        val_bucket_count = val

        val = dictionary['bucket_rule']
        val_bucket_rule = val

        val = dictionary['created_timestamp']
        val_created_timestamp = val

        val = dictionary['description']
        val_description = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['is_backup_target_region_configured']
        val_is_backup_target_region_configured = val

        val = dictionary['is_deleted']
        val_is_deleted = val

        val = dictionary['last_backup_timestamp']
        val_last_backup_timestamp = val

        val = dictionary['last_continuous_backup_timestamp']
        val_last_continuous_backup_timestamp = val

        val = dictionary['modified_timestamp']
        val_modified_timestamp = val

        val = dictionary['name']
        val_name = val

        val = dictionary['object_filter']
        val_object_filter = object_filter_.ObjectFilter.from_dictionary(val)

        val = dictionary['organizational_unit_id']
        val_organizational_unit_id = val

        val = dictionary['total_backed_up_object_count']
        val_total_backed_up_object_count = val

        val = dictionary['total_backed_up_size_bytes']
        val_total_backed_up_size_bytes = val

        val = dictionary['version']
        val_version = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_backup_target_aws_region,  # type: ignore
            val_backup_tier_stats,  # type: ignore
            val_bucket_count,  # type: ignore
            val_bucket_rule,  # type: ignore
            val_created_timestamp,  # type: ignore
            val_description,  # type: ignore
            val_p_id,  # type: ignore
            val_is_backup_target_region_configured,  # type: ignore
            val_is_deleted,  # type: ignore
            val_last_backup_timestamp,  # type: ignore
            val_last_continuous_backup_timestamp,  # type: ignore
            val_modified_timestamp,  # type: ignore
            val_name,  # type: ignore
            val_object_filter,  # type: ignore
            val_organizational_unit_id,  # type: ignore
            val_total_backed_up_object_count,  # type: ignore
            val_total_backed_up_size_bytes,  # type: ignore
            val_version,  # type: ignore
        )
