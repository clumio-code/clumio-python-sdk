#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_model
from clumioapi.models import backup_status_info as backup_status_info_
from clumioapi.models import dynamo_db_keys
from clumioapi.models import dynamo_db_table_embedded
from clumioapi.models import dynamo_db_table_links
from clumioapi.models import global_secondary_index
from clumioapi.models import local_secondary_index
from clumioapi.models import protection_info_with_rule
from clumioapi.models import provisioned_throughput as provisioned_throughput_
from clumioapi.models import replica_description
from clumioapi.models import sse_specification as sse_specification_
from clumioapi.models import stream_specification as stream_specification_

T = TypeVar('T', bound='DynamoDBTable')


class DynamoDBTable:
    """Implementation of the 'DynamoDBTable' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        account_native_id:
            The AWS-assigned ID of the account associated with the DynamoDB table.
        aws_region:
            The AWS region associated with the DynamoDB table.
        backup_status_info:
            The backup status information applied to this resource.
        billing_mode:
            The billing mode of the DynamoDB table. Possible values are PROVISIONED or
            PAY_PER_REQUEST.
            For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this
            is defaulted to the
            configuration of source table if both 'billing_mode' and
            'provisioned_throughput' are empty or `null`.
        contributor_insights_status:
            Indicates whether DynamoDB Contributor Insights is enabled (true) or disabled
            (false)
            on the table.
            For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this
            is defaulted to the
            value set in backup if `null`.
        deletion_protection_enabled:
            Indicates whether DynamoDB Deletion Protection is enabled (true) or disabled
            (false)
            on the table.
            For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this
            is defaulted to the
            value set in backup if `null`.
        deletion_timestamp:
            The timestamp of when the table was deleted. Represented in RFC-3339 format.
            If this table has not been deleted, then this field has a value of `null`.
        direct_assignment_policy_id:
            The Clumio-assigned ID of the policy directly assigned to the entity.
        earliest_continuous_snapshot_restorable_timestamp:
            The earliest continuous snapshot restorable time of the DynamoDB table for
            Point-in-time restore.
            Represented in RFC-3339 format. If PITR is not enabled for the table, then this
            field has a value of `null`.
        environment_id:
            The Clumio-assigned ID of the AWS environment associated with the DynamoDB
            table.
        global_secondary_indexes:
            Describes the global secondary indexes of the DynamoDB table.
            For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), a
            subset of the source tables'
            global_secondary_indexes can be specified.
            The restored table will not have any global secondary indexes if this is
            specified empty or `null`.
        global_table_version:
            Describes the version of global tables in use, if the table is replicated across
            AWS Regions. If the table
            is not a global table, then this field has a value of `null`. Possible values
            are 2017.11.29 or 2019.11.21.
            For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), the
            version is defaulted to 2019.11.21.
        has_direct_assignment:
            Determines whether the table has a direct assignment.
        p_id:
            The Clumio-assigned ID of the DynamoDB table.
        is_deleted:
            Determines whether the DynamoDB table has been deleted. If `true`, the table has
            been deleted.
        is_supported:
            Determines whether the DynamoDB table is supported for backups.
        item_count:
            The number of items in the DynamoDB table.
        last_snapshot_timestamp:
            The timestamp of the most recent snapshot of the DynamoDB table taken as part of
            AwsSnapMgr. Represented in RFC-3339 format. If the table has never been
            snapshotted, then this field has a value of `null`.
        latest_continuous_snapshot_restorable_timestamp:
            The latest continuous snapshot restorable time of the DynamoDB table for Point-
            in-time restore.
            Represented in RFC-3339 format. If PITR is not enabled for the table, then this
            field has a value of `null`.
        local_secondary_indexes:
            Describes the local secondary indexes of the DynamoDB table.
            For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), a
            subset of the source tables'
            local_secondary_indexes can be specified.
            The restored table will not have any local secondary indexes if this is
            specified empty or `null`.
        name:
            The AWS-assigned name of the DynamoDB table.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the DynamoDB
            table.
        pitr_status:
            Indicates whether DynamoDB Continuous Backup (PITR) is enabled (true) or
            disabled (false)
            on the table.
            For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this
            is defaulted to the
            value set in backup if `null`.
        protection_info:
            The protection policy applied to this resource. If the resource is not
            protected, then this field has a value of `null`.
        protection_status:
            The protection status of the DynamoDB table. Possible values include
            "protected",
            "unprotected", and "unsupported". If the DynamoDB table does not support
            backups, then
            this field has a value of `unsupported`.
        provisioned_throughput:
            Represents the provisioned throughput settings for a DynamoDB table.
        replicas:
            Describes the replicas of the table, if the table is replicated across AWS
            Regions.
            Not applicable for [POST /restores/aws/dynamodb](#operation/restore-aws-
            dynamodb-table) currently,
            but will be used to specify the replication group information in a future
            release.
        size:
            The size of the DynamoDB table. Measured in bytes (B).
        sse_specification:
            Represents the server-side encryption settings for a table.
        stream_specification:
            Represents the DynamoDB Streams configuration for a table in DynamoDB.
            and the data type (`S` for string, `N` for number, `B` for binary).
        table_arn:
            The AWS-assigned ARN of the DynamoDB table.
        table_class:
            The table class of the DynamoDB table. Possible values are STANDARD or
            STANDARD_INFREQUENT_ACCESS.
            For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this
            is defaulted to the
            STANDARD storage class if empty.
        table_keys:
            Represents the DynamoDB table keys.
        table_native_id:
            The AWS-assigned ID of the DynamoDB table.
        table_status:
            The current state of the table.
        tags:
            The AWS tags applied to the DynamoDB table.
        unsupported_reason:
            The reason why protection is not available. If the table is supported,
            then this field has a value of `null`.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'account_native_id': 'account_native_id',
        'aws_region': 'aws_region',
        'backup_status_info': 'backup_status_info',
        'billing_mode': 'billing_mode',
        'contributor_insights_status': 'contributor_insights_status',
        'deletion_protection_enabled': 'deletion_protection_enabled',
        'deletion_timestamp': 'deletion_timestamp',
        'direct_assignment_policy_id': 'direct_assignment_policy_id',
        'earliest_continuous_snapshot_restorable_timestamp': 'earliest_continuous_snapshot_restorable_timestamp',
        'environment_id': 'environment_id',
        'global_secondary_indexes': 'global_secondary_indexes',
        'global_table_version': 'global_table_version',
        'has_direct_assignment': 'has_direct_assignment',
        'p_id': 'id',
        'is_deleted': 'is_deleted',
        'is_supported': 'is_supported',
        'item_count': 'item_count',
        'last_snapshot_timestamp': 'last_snapshot_timestamp',
        'latest_continuous_snapshot_restorable_timestamp': 'latest_continuous_snapshot_restorable_timestamp',
        'local_secondary_indexes': 'local_secondary_indexes',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
        'pitr_status': 'pitr_status',
        'protection_info': 'protection_info',
        'protection_status': 'protection_status',
        'provisioned_throughput': 'provisioned_throughput',
        'replicas': 'replicas',
        'size': 'size',
        'sse_specification': 'sse_specification',
        'stream_specification': 'stream_specification',
        'table_arn': 'table_arn',
        'table_class': 'table_class',
        'table_keys': 'table_keys',
        'table_native_id': 'table_native_id',
        'table_status': 'table_status',
        'tags': 'tags',
        'unsupported_reason': 'unsupported_reason',
    }

    def __init__(
        self,
        embedded: dynamo_db_table_embedded.DynamoDBTableEmbedded = None,
        links: dynamo_db_table_links.DynamoDBTableLinks = None,
        account_native_id: str = None,
        aws_region: str = None,
        backup_status_info: backup_status_info_.BackupStatusInfo = None,
        billing_mode: str = None,
        contributor_insights_status: bool = None,
        deletion_protection_enabled: bool = None,
        deletion_timestamp: str = None,
        direct_assignment_policy_id: str = None,
        earliest_continuous_snapshot_restorable_timestamp: str = None,
        environment_id: str = None,
        global_secondary_indexes: Sequence[global_secondary_index.GlobalSecondaryIndex] = None,
        global_table_version: str = None,
        has_direct_assignment: bool = None,
        p_id: str = None,
        is_deleted: bool = None,
        is_supported: bool = None,
        item_count: int = None,
        last_snapshot_timestamp: str = None,
        latest_continuous_snapshot_restorable_timestamp: str = None,
        local_secondary_indexes: Sequence[local_secondary_index.LocalSecondaryIndex] = None,
        name: str = None,
        organizational_unit_id: str = None,
        pitr_status: bool = None,
        protection_info: protection_info_with_rule.ProtectionInfoWithRule = None,
        protection_status: str = None,
        provisioned_throughput: provisioned_throughput_.ProvisionedThroughput = None,
        replicas: Sequence[replica_description.ReplicaDescription] = None,
        size: int = None,
        sse_specification: sse_specification_.SSESpecification = None,
        stream_specification: stream_specification_.StreamSpecification = None,
        table_arn: str = None,
        table_class: str = None,
        table_keys: dynamo_db_keys.DynamoDBKeys = None,
        table_native_id: str = None,
        table_status: str = None,
        tags: Sequence[aws_tag_model.AwsTagModel] = None,
        unsupported_reason: str = None,
    ) -> None:
        """Constructor for the DynamoDBTable class."""

        # Initialize members of the class
        self.embedded: dynamo_db_table_embedded.DynamoDBTableEmbedded = embedded
        self.links: dynamo_db_table_links.DynamoDBTableLinks = links
        self.account_native_id: str = account_native_id
        self.aws_region: str = aws_region
        self.backup_status_info: backup_status_info_.BackupStatusInfo = backup_status_info
        self.billing_mode: str = billing_mode
        self.contributor_insights_status: bool = contributor_insights_status
        self.deletion_protection_enabled: bool = deletion_protection_enabled
        self.deletion_timestamp: str = deletion_timestamp
        self.direct_assignment_policy_id: str = direct_assignment_policy_id
        self.earliest_continuous_snapshot_restorable_timestamp: str = (
            earliest_continuous_snapshot_restorable_timestamp
        )
        self.environment_id: str = environment_id
        self.global_secondary_indexes: Sequence[global_secondary_index.GlobalSecondaryIndex] = (
            global_secondary_indexes
        )
        self.global_table_version: str = global_table_version
        self.has_direct_assignment: bool = has_direct_assignment
        self.p_id: str = p_id
        self.is_deleted: bool = is_deleted
        self.is_supported: bool = is_supported
        self.item_count: int = item_count
        self.last_snapshot_timestamp: str = last_snapshot_timestamp
        self.latest_continuous_snapshot_restorable_timestamp: str = (
            latest_continuous_snapshot_restorable_timestamp
        )
        self.local_secondary_indexes: Sequence[local_secondary_index.LocalSecondaryIndex] = (
            local_secondary_indexes
        )
        self.name: str = name
        self.organizational_unit_id: str = organizational_unit_id
        self.pitr_status: bool = pitr_status
        self.protection_info: protection_info_with_rule.ProtectionInfoWithRule = protection_info
        self.protection_status: str = protection_status
        self.provisioned_throughput: provisioned_throughput_.ProvisionedThroughput = (
            provisioned_throughput
        )
        self.replicas: Sequence[replica_description.ReplicaDescription] = replicas
        self.size: int = size
        self.sse_specification: sse_specification_.SSESpecification = sse_specification
        self.stream_specification: stream_specification_.StreamSpecification = stream_specification
        self.table_arn: str = table_arn
        self.table_class: str = table_class
        self.table_keys: dynamo_db_keys.DynamoDBKeys = table_keys
        self.table_native_id: str = table_native_id
        self.table_status: str = table_status
        self.tags: Sequence[aws_tag_model.AwsTagModel] = tags
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
        val_embedded = (
            dynamo_db_table_embedded.DynamoDBTableEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        val_links = (
            dynamo_db_table_links.DynamoDBTableLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        val_account_native_id = dictionary.get('account_native_id')
        val_aws_region = dictionary.get('aws_region')
        key = 'backup_status_info'
        val_backup_status_info = (
            backup_status_info_.BackupStatusInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        val_billing_mode = dictionary.get('billing_mode')
        val_contributor_insights_status = dictionary.get('contributor_insights_status')
        val_deletion_protection_enabled = dictionary.get('deletion_protection_enabled')
        val_deletion_timestamp = dictionary.get('deletion_timestamp')
        val_direct_assignment_policy_id = dictionary.get('direct_assignment_policy_id')
        val_earliest_continuous_snapshot_restorable_timestamp = dictionary.get(
            'earliest_continuous_snapshot_restorable_timestamp'
        )
        val_environment_id = dictionary.get('environment_id')

        val_global_secondary_indexes = None
        if dictionary.get('global_secondary_indexes'):
            val_global_secondary_indexes = list()
            for value in dictionary.get('global_secondary_indexes'):
                val_global_secondary_indexes.append(
                    global_secondary_index.GlobalSecondaryIndex.from_dictionary(value)
                )

        val_global_table_version = dictionary.get('global_table_version')
        val_has_direct_assignment = dictionary.get('has_direct_assignment')
        val_p_id = dictionary.get('id')
        val_is_deleted = dictionary.get('is_deleted')
        val_is_supported = dictionary.get('is_supported')
        val_item_count = dictionary.get('item_count')
        val_last_snapshot_timestamp = dictionary.get('last_snapshot_timestamp')
        val_latest_continuous_snapshot_restorable_timestamp = dictionary.get(
            'latest_continuous_snapshot_restorable_timestamp'
        )

        val_local_secondary_indexes = None
        if dictionary.get('local_secondary_indexes'):
            val_local_secondary_indexes = list()
            for value in dictionary.get('local_secondary_indexes'):
                val_local_secondary_indexes.append(
                    local_secondary_index.LocalSecondaryIndex.from_dictionary(value)
                )

        val_name = dictionary.get('name')
        val_organizational_unit_id = dictionary.get('organizational_unit_id')
        val_pitr_status = dictionary.get('pitr_status')
        key = 'protection_info'
        val_protection_info = (
            protection_info_with_rule.ProtectionInfoWithRule.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        val_protection_status = dictionary.get('protection_status')
        key = 'provisioned_throughput'
        val_provisioned_throughput = (
            provisioned_throughput_.ProvisionedThroughput.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        val_replicas = None
        if dictionary.get('replicas'):
            val_replicas = list()
            for value in dictionary.get('replicas'):
                val_replicas.append(replica_description.ReplicaDescription.from_dictionary(value))

        val_size = dictionary.get('size')
        key = 'sse_specification'
        val_sse_specification = (
            sse_specification_.SSESpecification.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'stream_specification'
        val_stream_specification = (
            stream_specification_.StreamSpecification.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        val_table_arn = dictionary.get('table_arn')
        val_table_class = dictionary.get('table_class')
        key = 'table_keys'
        val_table_keys = (
            dynamo_db_keys.DynamoDBKeys.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        val_table_native_id = dictionary.get('table_native_id')
        val_table_status = dictionary.get('table_status')

        val_tags = None
        if dictionary.get('tags'):
            val_tags = list()
            for value in dictionary.get('tags'):
                val_tags.append(aws_tag_model.AwsTagModel.from_dictionary(value))

        val_unsupported_reason = dictionary.get('unsupported_reason')
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
            val_p_id,
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
