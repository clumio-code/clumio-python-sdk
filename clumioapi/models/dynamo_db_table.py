#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import aws_tag_model as aws_tag_model_
from clumioapi.models import backup_status_info as backup_status_info_
from clumioapi.models import dynamo_db_keys as dynamo_db_keys_
from clumioapi.models import dynamo_db_table_embedded as dynamo_db_table_embedded_
from clumioapi.models import dynamo_db_table_links as dynamo_db_table_links_
from clumioapi.models import global_secondary_index as global_secondary_index_
from clumioapi.models import local_secondary_index as local_secondary_index_
from clumioapi.models import protection_info_with_rule as protection_info_with_rule_
from clumioapi.models import provisioned_throughput as provisioned_throughput_
from clumioapi.models import replica_description as replica_description_
from clumioapi.models import sse_specification as sse_specification_
from clumioapi.models import stream_specification as stream_specification_
import requests

T = TypeVar('T', bound='DynamoDBTable')


@dataclasses.dataclass
class DynamoDBTable:
    """Implementation of the 'DynamoDBTable' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        AccountNativeId:
            The aws-assigned id of the account associated with the dynamodb table.

        AwsRegion:
            The aws region associated with the dynamodb table.

        BackupStatusInfo:
            The backup status information applied to this resource.

        BillingMode:
            The billing mode of the dynamodb table. possible values are provisioned or
            pay_per_request.
            for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this
            is defaulted to the
            configuration of source table if both 'billing_mode' and
            'provisioned_throughput' are empty or `null`.

        ContributorInsightsStatus:
            Indicates whether dynamodb contributor insights is enabled (true) or disabled
            (false)
            on the table.
            for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this
            is defaulted to the
            value set in backup if `null`.

        DeletionProtectionEnabled:
            Indicates whether dynamodb deletion protection is enabled (true) or disabled
            (false)
            on the table.
            for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this
            is defaulted to the
            value set in backup if `null`.

        DeletionTimestamp:
            The timestamp of when the table was deleted. represented in rfc-3339 format.
            if this table has not been deleted, then this field has a value of `null`.

        DirectAssignmentPolicyId:
            The clumio-assigned id of the policy directly assigned to the entity.

        EarliestContinuousSnapshotRestorableTimestamp:
            The earliest continuous snapshot restorable time of the dynamodb table for
            point-in-time restore.
            represented in rfc-3339 format. if pitr is not enabled for the table, then this
            field has a value of `null`.

        EnvironmentId:
            The clumio-assigned id of the aws environment associated with the dynamodb
            table.

        GlobalSecondaryIndexes:
            Describes the global secondary indexes of the dynamodb table.
            for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), a
            subset of the source tables'
            global_secondary_indexes can be specified.
            the restored table will not have any global secondary indexes if this is
            specified empty or `null`.

        GlobalTableVersion:
            Describes the version of global tables in use, if the table is replicated across
            aws regions. if the table
            is not a global table, then this field has a value of `null`. possible values
            are 2017.11.29 or 2019.11.21.
            for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), the
            version is defaulted to 2019.11.21.

        HasDirectAssignment:
            Determines whether the table has a direct assignment.

        Id:
            The clumio-assigned id of the dynamodb table.

        IsDeleted:
            Determines whether the dynamodb table has been deleted. if `true`, the table has
            been deleted.

        IsSupported:
            Determines whether the dynamodb table is supported for backups.

        ItemCount:
            The number of items in the dynamodb table.

        LastSnapshotTimestamp:
            The timestamp of the most recent snapshot of the dynamodb table taken as part of
            awssnapmgr. represented in rfc-3339 format. if the table has never been
            snapshotted, then this field has a value of `null`.

        LatestContinuousSnapshotRestorableTimestamp:
            The latest continuous snapshot restorable time of the dynamodb table for point-
            in-time restore.
            represented in rfc-3339 format. if pitr is not enabled for the table, then this
            field has a value of `null`.

        LocalSecondaryIndexes:
            Describes the local secondary indexes of the dynamodb table.
            for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), a
            subset of the source tables'
            local_secondary_indexes can be specified.
            the restored table will not have any local secondary indexes if this is
            specified empty or `null`.

        Name:
            The aws-assigned name of the dynamodb table.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the dynamodb
            table.

        PitrStatus:
            Indicates whether dynamodb continuous backup (pitr) is enabled (true) or
            disabled (false)
            on the table.
            for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this
            is defaulted to the
            value set in backup if `null`.

        ProtectionInfo:
            The protection policy applied to this resource. if the resource is not
            protected, then this field has a value of `null`.

        ProtectionStatus:
            The protection status of the dynamodb table. possible values include
            "protected",
            "unprotected", and "unsupported". if the dynamodb table does not support
            backups, then
            this field has a value of `unsupported`.

        ProvisionedThroughput:
            Represents the provisioned throughput settings for a dynamodb table.

        Replicas:
            Describes the replicas of the table, if the table is replicated across aws
            regions.
            not applicable for [post /restores/aws/dynamodb](#operation/restore-aws-
            dynamodb-table) currently,
            but will be used to specify the replication group information in a future
            release.

        Size:
            The size of the dynamodb table. measured in bytes (b).

        SseSpecification:
            Represents the server-side encryption settings for a table.

        StreamSpecification:
            Represents the dynamodb streams configuration for a table in dynamodb.
            and the data type (`s` for string, `n` for number, `b` for binary).

        TableArn:
            The aws-assigned arn of the dynamodb table.

        TableClass:
            The table class of the dynamodb table. possible values are standard or
            standard_infrequent_access.
            for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this
            is defaulted to the
            standard storage class if empty.

        TableKeys:
            Represents the dynamodb table keys.

        TableNativeId:
            The aws-assigned id of the dynamodb table.

        TableStatus:
            The current state of the table.

        Tags:
            The aws tags applied to the dynamodb table.

        UnsupportedReason:
            The reason why protection is not available. if the table is supported,
            then this field has a value of `null`.

    """

    Embedded: dynamo_db_table_embedded_.DynamoDBTableEmbedded | None = None
    Links: dynamo_db_table_links_.DynamoDBTableLinks | None = None
    AccountNativeId: str | None = None
    AwsRegion: str | None = None
    BackupStatusInfo: backup_status_info_.BackupStatusInfo | None = None
    BillingMode: str | None = None
    ContributorInsightsStatus: bool | None = None
    DeletionProtectionEnabled: bool | None = None
    DeletionTimestamp: str | None = None
    DirectAssignmentPolicyId: str | None = None
    EarliestContinuousSnapshotRestorableTimestamp: str | None = None
    EnvironmentId: str | None = None
    GlobalSecondaryIndexes: Sequence[global_secondary_index_.GlobalSecondaryIndex] | None = None
    GlobalTableVersion: str | None = None
    HasDirectAssignment: bool | None = None
    Id: str | None = None
    IsDeleted: bool | None = None
    IsSupported: bool | None = None
    ItemCount: int | None = None
    LastSnapshotTimestamp: str | None = None
    LatestContinuousSnapshotRestorableTimestamp: str | None = None
    LocalSecondaryIndexes: Sequence[local_secondary_index_.LocalSecondaryIndex] | None = None
    Name: str | None = None
    OrganizationalUnitId: str | None = None
    PitrStatus: bool | None = None
    ProtectionInfo: protection_info_with_rule_.ProtectionInfoWithRule | None = None
    ProtectionStatus: str | None = None
    ProvisionedThroughput: provisioned_throughput_.ProvisionedThroughput | None = None
    Replicas: Sequence[replica_description_.ReplicaDescription] | None = None
    Size: int | None = None
    SseSpecification: sse_specification_.SSESpecification | None = None
    StreamSpecification: stream_specification_.StreamSpecification | None = None
    TableArn: str | None = None
    TableClass: str | None = None
    TableKeys: dynamo_db_keys_.DynamoDBKeys | None = None
    TableNativeId: str | None = None
    TableStatus: str | None = None
    Tags: Sequence[aws_tag_model_.AwsTagModel] | None = None
    UnsupportedReason: str | None = None

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
        val_embedded = dynamo_db_table_embedded_.DynamoDBTableEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = dynamo_db_table_links_.DynamoDBTableLinks.from_dictionary(val)

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('backup_status_info', None)
        val_backup_status_info = backup_status_info_.BackupStatusInfo.from_dictionary(val)

        val = dictionary.get('billing_mode', None)
        val_billing_mode = val

        val = dictionary.get('contributor_insights_status', None)
        val_contributor_insights_status = val

        val = dictionary.get('deletion_protection_enabled', None)
        val_deletion_protection_enabled = val

        val = dictionary.get('deletion_timestamp', None)
        val_deletion_timestamp = val

        val = dictionary.get('direct_assignment_policy_id', None)
        val_direct_assignment_policy_id = val

        val = dictionary.get('earliest_continuous_snapshot_restorable_timestamp', None)
        val_earliest_continuous_snapshot_restorable_timestamp = val

        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('global_secondary_indexes', None)

        val_global_secondary_indexes = []
        if val:
            for value in val:
                val_global_secondary_indexes.append(
                    global_secondary_index_.GlobalSecondaryIndex.from_dictionary(value)
                )

        val = dictionary.get('global_table_version', None)
        val_global_table_version = val

        val = dictionary.get('has_direct_assignment', None)
        val_has_direct_assignment = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('is_deleted', None)
        val_is_deleted = val

        val = dictionary.get('is_supported', None)
        val_is_supported = val

        val = dictionary.get('item_count', None)
        val_item_count = val

        val = dictionary.get('last_snapshot_timestamp', None)
        val_last_snapshot_timestamp = val

        val = dictionary.get('latest_continuous_snapshot_restorable_timestamp', None)
        val_latest_continuous_snapshot_restorable_timestamp = val

        val = dictionary.get('local_secondary_indexes', None)

        val_local_secondary_indexes = []
        if val:
            for value in val:
                val_local_secondary_indexes.append(
                    local_secondary_index_.LocalSecondaryIndex.from_dictionary(value)
                )

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('pitr_status', None)
        val_pitr_status = val

        val = dictionary.get('protection_info', None)
        val_protection_info = protection_info_with_rule_.ProtectionInfoWithRule.from_dictionary(val)

        val = dictionary.get('protection_status', None)
        val_protection_status = val

        val = dictionary.get('provisioned_throughput', None)
        val_provisioned_throughput = provisioned_throughput_.ProvisionedThroughput.from_dictionary(
            val
        )

        val = dictionary.get('replicas', None)

        val_replicas = []
        if val:
            for value in val:
                val_replicas.append(replica_description_.ReplicaDescription.from_dictionary(value))

        val = dictionary.get('size', None)
        val_size = val

        val = dictionary.get('sse_specification', None)
        val_sse_specification = sse_specification_.SSESpecification.from_dictionary(val)

        val = dictionary.get('stream_specification', None)
        val_stream_specification = stream_specification_.StreamSpecification.from_dictionary(val)

        val = dictionary.get('table_arn', None)
        val_table_arn = val

        val = dictionary.get('table_class', None)
        val_table_class = val

        val = dictionary.get('table_keys', None)
        val_table_keys = dynamo_db_keys_.DynamoDBKeys.from_dictionary(val)

        val = dictionary.get('table_native_id', None)
        val_table_native_id = val

        val = dictionary.get('table_status', None)
        val_table_status = val

        val = dictionary.get('tags', None)

        val_tags = []
        if val:
            for value in val:
                val_tags.append(aws_tag_model_.AwsTagModel.from_dictionary(value))

        val = dictionary.get('unsupported_reason', None)
        val_unsupported_reason = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_account_native_id,
            val_aws_region,
            val_backup_status_info,
            val_billing_mode,
            val_contributor_insights_status,
            val_deletion_protection_enabled,
            val_deletion_timestamp,
            val_direct_assignment_policy_id,
            val_earliest_continuous_snapshot_restorable_timestamp,
            val_environment_id,
            val_global_secondary_indexes,
            val_global_table_version,
            val_has_direct_assignment,
            val_id,
            val_is_deleted,
            val_is_supported,
            val_item_count,
            val_last_snapshot_timestamp,
            val_latest_continuous_snapshot_restorable_timestamp,
            val_local_secondary_indexes,
            val_name,
            val_organizational_unit_id,
            val_pitr_status,
            val_protection_info,
            val_protection_status,
            val_provisioned_throughput,
            val_replicas,
            val_size,
            val_sse_specification,
            val_stream_specification,
            val_table_arn,
            val_table_class,
            val_table_keys,
            val_table_native_id,
            val_table_status,
            val_tags,
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
        return model_instance
