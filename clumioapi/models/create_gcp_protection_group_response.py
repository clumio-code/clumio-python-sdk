#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import backup_status_stats as backup_status_stats_
from clumioapi.models import gcp_bucket_rule_model as gcp_bucket_rule_model_
from clumioapi.models import gcp_label_model as gcp_label_model_
from clumioapi.models import gcp_protection_group_embedded as gcp_protection_group_embedded_
from clumioapi.models import gcp_protection_group_filter as gcp_protection_group_filter_
from clumioapi.models import gcp_protection_group_links as gcp_protection_group_links_
from clumioapi.models import gcp_protection_info_model as gcp_protection_info_model_
import requests

T = TypeVar('T', bound='CreateGCPProtectionGroupResponse')


@dataclasses.dataclass
class CreateGCPProtectionGroupResponse:
    """Implementation of the 'CreateGCPProtectionGroupResponse' model.

    Attributes:
        Embedded

        Etag

        Links

        BackupStatusStats:
            Represents the aggregated stats for backup status.

        BucketCount:
            The total number of unique buckets in this protection group
            (manual + rule-matched, deduplicated).

        BucketRule

        BucketRuleMatchedBucketCount:
            The number of buckets auto-included by the bucket rule.

        BucketRuleMatchedBucketUuids:
            A bucket that is both directly assigned and rule-matched will appear
            in both bucket_uuids and this field. deduplicate before computing totals.
            always returned on read/create/update. on the list endpoint, only
            returned when bucket_uuid_detail is "all" or "bucket_rule".

        BucketUuids:
            The set of bucket uuids directly assigned to this protection group
            (via manual membership). does not include buckets auto-included by a
            bucket rule; see bucket_rule_matched_bucket_uuids for those.
            always returned on read/create/update. on the list endpoint, only
            returned when bucket_uuid_detail is "all" or "manual".

        CreatedTimestamp:
            Creation time of the protection group in rfc-3339 format.

        Filter

        Id:
            The clumio-assigned id of the protection group.

        IsDeleted:
            Determines whether the protection group is active or has been deleted.

        Labels:
            Gcp labels (key-value pairs) associated with the protection group.

        LastBackupTimestamp:
            Time of the last backup in rfc-3339 format.

        Location:
            The location of the protection group (e.g., "us-central1", "us", "us-west1").

        LocationType:
            The location type of the protection group (e.g., "region", "dual-region",
            "multi-region").

        ManualAddedBucketCount:
            The number of buckets directly assigned to this protection group
            (via manual membership). does not include buckets auto-included by a
            bucket rule; see bucket_rule_matched_bucket_count for those.

        ModifiedTimestamp:
            Modified time of the protection group in rfc-3339 format.

        Name:
            The user-assigned name of the protection group.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the protection
            group.

        ProtectionInfo

        ProtectionStatus:
            The protection status of this resource. possible values include
            "protected", "unprotected".

        TotalBackedUpObjectCount:
            Cumulative count of all unexpired objects in each backup (any new or updated
            since
            the last backup) that have been backed up as part of this protection group.

        TotalBackedUpSizeBytes:
            Cumulative size of all unexpired objects in each backup (any new or updated
            since
            the last backup) that have been backed up as part of this protection group.

        Version:
            Version of the protection group. the version number is incremented every time
            a change is made to the protection group.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Embedded': '_embedded',
        'Etag': '_etag',
        'Links': '_links',
    }

    Embedded: gcp_protection_group_embedded_.GCPProtectionGroupEmbedded | None = None
    Etag: str | None = None
    Links: gcp_protection_group_links_.GCPProtectionGroupLinks | None = None
    BackupStatusStats: backup_status_stats_.BackupStatusStats | None = None
    BucketCount: int | None = None
    BucketRule: gcp_bucket_rule_model_.GCPBucketRuleModel | None = None
    BucketRuleMatchedBucketCount: int | None = None
    BucketRuleMatchedBucketUuids: Sequence[str] | None = None
    BucketUuids: Sequence[str] | None = None
    CreatedTimestamp: str | None = None
    Filter: gcp_protection_group_filter_.GCPProtectionGroupFilter | None = None
    Id: str | None = None
    IsDeleted: bool | None = None
    Labels: Sequence[gcp_label_model_.GcpLabelModel] | None = None
    LastBackupTimestamp: str | None = None
    Location: str | None = None
    LocationType: str | None = None
    ManualAddedBucketCount: int | None = None
    ModifiedTimestamp: str | None = None
    Name: str | None = None
    OrganizationalUnitId: str | None = None
    ProtectionInfo: gcp_protection_info_model_.GCPProtectionInfoModel | None = None
    ProtectionStatus: str | None = None
    TotalBackedUpObjectCount: int | None = None
    TotalBackedUpSizeBytes: int | None = None
    Version: int | None = None
    raw_response: Optional[requests.Response] = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return api_helper.to_dictionary(self)

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
        val_embedded = gcp_protection_group_embedded_.GCPProtectionGroupEmbedded.from_dictionary(
            val
        )

        val = dictionary.get('_etag', None)
        val_etag = val

        val = dictionary.get('_links', None)
        val_links = gcp_protection_group_links_.GCPProtectionGroupLinks.from_dictionary(val)

        val = dictionary.get('backup_status_stats', None)
        val_backup_status_stats = backup_status_stats_.BackupStatusStats.from_dictionary(val)

        val = dictionary.get('bucket_count', None)
        val_bucket_count = val

        val = dictionary.get('bucket_rule', None)
        val_bucket_rule = gcp_bucket_rule_model_.GCPBucketRuleModel.from_dictionary(val)

        val = dictionary.get('bucket_rule_matched_bucket_count', None)
        val_bucket_rule_matched_bucket_count = val

        val = dictionary.get('bucket_rule_matched_bucket_uuids', None)
        val_bucket_rule_matched_bucket_uuids = val

        val = dictionary.get('bucket_uuids', None)
        val_bucket_uuids = val

        val = dictionary.get('created_timestamp', None)
        val_created_timestamp = val

        val = dictionary.get('filter', None)
        val_filter = gcp_protection_group_filter_.GCPProtectionGroupFilter.from_dictionary(val)

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('is_deleted', None)
        val_is_deleted = val

        val = dictionary.get('labels', None)

        val_labels = []
        if val:
            for value in val:
                val_labels.append(gcp_label_model_.GcpLabelModel.from_dictionary(value))

        val = dictionary.get('last_backup_timestamp', None)
        val_last_backup_timestamp = val

        val = dictionary.get('location', None)
        val_location = val

        val = dictionary.get('location_type', None)
        val_location_type = val

        val = dictionary.get('manual_added_bucket_count', None)
        val_manual_added_bucket_count = val

        val = dictionary.get('modified_timestamp', None)
        val_modified_timestamp = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('protection_info', None)
        val_protection_info = gcp_protection_info_model_.GCPProtectionInfoModel.from_dictionary(val)

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
            val_etag,
            val_links,
            val_backup_status_stats,
            val_bucket_count,
            val_bucket_rule,
            val_bucket_rule_matched_bucket_count,
            val_bucket_rule_matched_bucket_uuids,
            val_bucket_uuids,
            val_created_timestamp,
            val_filter,
            val_id,
            val_is_deleted,
            val_labels,
            val_last_backup_timestamp,
            val_location,
            val_location_type,
            val_manual_added_bucket_count,
            val_modified_timestamp,
            val_name,
            val_organizational_unit_id,
            val_protection_info,
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
        model_instance.raw_response = response
        return model_instance
