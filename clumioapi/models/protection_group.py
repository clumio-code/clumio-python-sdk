#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import object_filter
from clumioapi.models import protection_compliance_stats_with_seeding
from clumioapi.models import protection_group_embedded
from clumioapi.models import protection_group_links
from clumioapi.models import protection_info_with_rule

T = TypeVar('T', bound='ProtectionGroup')


class ProtectionGroup:
    """Implementation of the 'ProtectionGroup' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        bucket_count:
            Number of buckets
        bucket_rule:
            The following table describes the possible conditions for a bucket to be
            automatically added to a protection group.

            +---------+----------------+---------------------------------------------------+
            |  Field  | Rule Condition |                    Description                    |
            +=========+================+===================================================+
            | aws_tag | $eq            | Denotes the AWS tag(s) to conditionalize on       |
            |         |                |                                                   |
            |         |                | {"aws_tag":{"$eq":{"key":"Environment",           |
            |         |                | "value":"Prod"}}}                                 |
            |         |                |                                                   |
            |         |                |                                                   |
            +---------+----------------+---------------------------------------------------+
        compliance_stats:
            The compliance statistics of workloads associated with this entity.
        compliance_status:
            The compliance status of the protected protection group. Possible values include
            "compliant" and "noncompliant". If the table is not protected, then this field
            has
            a value of `null`.
        created_timestamp:
            Creation time of the protection group in RFC-3339 format.
        description:
            The user-assigned description of the protection group.
        id:
            The Clumio-assigned ID of the protection group.
        last_backup_timestamp:
            Time of the last backup in RFC-3339 format.
        last_continuous_backup_timestamp:
            Time of the last successful continuous backup in RFC-3339 format.
        last_discover_sync_timestamp:
            Time of the last discover sync in RFC-3339 format.
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
        version:
            Version of the protection group. The version number is incremented every time
            a change is made to the protection group.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'bucket_count': 'bucket_count',
        'bucket_rule': 'bucket_rule',
        'compliance_stats': 'compliance_stats',
        'compliance_status': 'compliance_status',
        'created_timestamp': 'created_timestamp',
        'description': 'description',
        'id': 'id',
        'last_backup_timestamp': 'last_backup_timestamp',
        'last_continuous_backup_timestamp': 'last_continuous_backup_timestamp',
        'last_discover_sync_timestamp': 'last_discover_sync_timestamp',
        'modified_timestamp': 'modified_timestamp',
        'name': 'name',
        'object_filter': 'object_filter',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
        'protection_status': 'protection_status',
        'total_backed_up_object_count': 'total_backed_up_object_count',
        'total_backed_up_size_bytes': 'total_backed_up_size_bytes',
        'version': 'version',
    }

    def __init__(
        self,
        embedded: protection_group_embedded.ProtectionGroupEmbedded = None,
        links: protection_group_links.ProtectionGroupLinks = None,
        bucket_count: int = None,
        bucket_rule: str = None,
        compliance_stats: protection_compliance_stats_with_seeding.ProtectionComplianceStatsWithSeeding = None,
        compliance_status: str = None,
        created_timestamp: str = None,
        description: str = None,
        id: str = None,
        last_backup_timestamp: str = None,
        last_continuous_backup_timestamp: str = None,
        last_discover_sync_timestamp: str = None,
        modified_timestamp: str = None,
        name: str = None,
        object_filter: object_filter.ObjectFilter = None,
        organizational_unit_id: str = None,
        protection_info: protection_info_with_rule.ProtectionInfoWithRule = None,
        protection_status: str = None,
        total_backed_up_object_count: int = None,
        total_backed_up_size_bytes: int = None,
        version: int = None,
    ) -> None:
        """Constructor for the ProtectionGroup class."""

        # Initialize members of the class
        self.embedded: protection_group_embedded.ProtectionGroupEmbedded = embedded
        self.links: protection_group_links.ProtectionGroupLinks = links
        self.bucket_count: int = bucket_count
        self.bucket_rule: str = bucket_rule
        self.compliance_stats: protection_compliance_stats_with_seeding.ProtectionComplianceStatsWithSeeding = (
            compliance_stats
        )
        self.compliance_status: str = compliance_status
        self.created_timestamp: str = created_timestamp
        self.description: str = description
        self.id: str = id
        self.last_backup_timestamp: str = last_backup_timestamp
        self.last_continuous_backup_timestamp: str = last_continuous_backup_timestamp
        self.last_discover_sync_timestamp: str = last_discover_sync_timestamp
        self.modified_timestamp: str = modified_timestamp
        self.name: str = name
        self.object_filter: object_filter.ObjectFilter = object_filter
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info_with_rule.ProtectionInfoWithRule = protection_info
        self.protection_status: str = protection_status
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

        bucket_count = dictionary.get('bucket_count')
        bucket_rule = dictionary.get('bucket_rule')
        key = 'compliance_stats'
        compliance_stats = (
            protection_compliance_stats_with_seeding.ProtectionComplianceStatsWithSeeding.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        compliance_status = dictionary.get('compliance_status')
        created_timestamp = dictionary.get('created_timestamp')
        description = dictionary.get('description')
        id = dictionary.get('id')
        last_backup_timestamp = dictionary.get('last_backup_timestamp')
        last_continuous_backup_timestamp = dictionary.get('last_continuous_backup_timestamp')
        last_discover_sync_timestamp = dictionary.get('last_discover_sync_timestamp')
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

        protection_status = dictionary.get('protection_status')
        total_backed_up_object_count = dictionary.get('total_backed_up_object_count')
        total_backed_up_size_bytes = dictionary.get('total_backed_up_size_bytes')
        version = dictionary.get('version')
        # Return an object of this model
        return cls(
            embedded,
            links,
            bucket_count,
            bucket_rule,
            compliance_stats,
            compliance_status,
            created_timestamp,
            description,
            id,
            last_backup_timestamp,
            last_continuous_backup_timestamp,
            last_discover_sync_timestamp,
            modified_timestamp,
            name,
            p_object_filter,
            organizational_unit_id,
            protection_info,
            protection_status,
            total_backed_up_object_count,
            total_backed_up_size_bytes,
            version,
        )
