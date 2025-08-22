#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model as aws_tag_common_model_
from clumioapi.models import dynamo_db_table_backup_links as dynamo_db_table_backup_links_
from clumioapi.models import global_secondary_index as global_secondary_index_
from clumioapi.models import local_secondary_index as local_secondary_index_
from clumioapi.models import provisioned_throughput as provisioned_throughput_
from clumioapi.models import replica_description as replica_description_
from clumioapi.models import sse_specification as sse_specification_
from clumioapi.models import stream_specification as stream_specification_

T = TypeVar('T', bound='ReadDynamoDBTableBackupResponse')


class ReadDynamoDBTableBackupResponse:
    """Implementation of the 'ReadDynamoDBTableBackupResponse' model.

    Attributes:
        etag:
            The ETag value.
        links:
            URLs to pages related to the resource.
        account_native_id:
            The AWS-assigned ID of the account associated with this database at the time of
            backup.
        aws_region:
            The AWS region associated with this environment.
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
        expiration_timestamp:
            The timestamp of when this backup expires. Represented in RFC-3339 format.
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
        p_id:
            The Clumio-assigned ID of the backup.
        item_count:
            The number of items in DynamoDB table backup.
        local_secondary_indexes:
            Describes the local secondary indexes of the DynamoDB table.
            For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), a
            subset of the source tables'
            local_secondary_indexes can be specified.
            The restored table will not have any local secondary indexes if this is
            specified empty or `null`.
        pitr_status:
            Indicates whether DynamoDB Continuous Backup (PITR) is enabled (true) or
            disabled (false)
            on the table.
            For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this
            is defaulted to the
            value set in backup if `null`.
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
            The size of the DynamoDB table backup in bytes.
        sse_specification:
            Represents the server-side encryption settings for a table.
        start_timestamp:
            The timestamp of when this backup started. Represented in RFC-3339 format.
        stream_specification:
            Represents the DynamoDB Streams configuration for a table in DynamoDB.
            and the data type (`S` for string, `N` for number, `B` for binary).
        table_class:
            The table class of the DynamoDB table. Possible values are STANDARD or
            STANDARD_INFREQUENT_ACCESS.
            For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this
            is defaulted to the
            STANDARD storage class if empty.
        table_id:
            The Clumio-assigned ID of the DynamoDB table.
        table_name:
            The name of the DynamoDB table.
        tags:
            The AWS tags associated with the table at the time of backup.
        p_type:
            The type of backup. Possible values include `clumio_backup` and `aws_snapshot`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'etag': '_etag',
        'links': '_links',
        'account_native_id': 'account_native_id',
        'aws_region': 'aws_region',
        'billing_mode': 'billing_mode',
        'contributor_insights_status': 'contributor_insights_status',
        'deletion_protection_enabled': 'deletion_protection_enabled',
        'expiration_timestamp': 'expiration_timestamp',
        'global_secondary_indexes': 'global_secondary_indexes',
        'global_table_version': 'global_table_version',
        'p_id': 'id',
        'item_count': 'item_count',
        'local_secondary_indexes': 'local_secondary_indexes',
        'pitr_status': 'pitr_status',
        'provisioned_throughput': 'provisioned_throughput',
        'replicas': 'replicas',
        'size': 'size',
        'sse_specification': 'sse_specification',
        'start_timestamp': 'start_timestamp',
        'stream_specification': 'stream_specification',
        'table_class': 'table_class',
        'table_id': 'table_id',
        'table_name': 'table_name',
        'tags': 'tags',
        'p_type': 'type',
    }

    def __init__(
        self,
        etag: str | None = None,
        links: dynamo_db_table_backup_links_.DynamoDBTableBackupLinks | None = None,
        account_native_id: str | None = None,
        aws_region: str | None = None,
        billing_mode: str | None = None,
        contributor_insights_status: bool | None = None,
        deletion_protection_enabled: bool | None = None,
        expiration_timestamp: str | None = None,
        global_secondary_indexes: (
            Sequence[global_secondary_index_.GlobalSecondaryIndex] | None
        ) = None,
        global_table_version: str | None = None,
        p_id: str | None = None,
        item_count: int | None = None,
        local_secondary_indexes: Sequence[local_secondary_index_.LocalSecondaryIndex] | None = None,
        pitr_status: bool | None = None,
        provisioned_throughput: provisioned_throughput_.ProvisionedThroughput | None = None,
        replicas: Sequence[replica_description_.ReplicaDescription] | None = None,
        size: int | None = None,
        sse_specification: sse_specification_.SSESpecification | None = None,
        start_timestamp: str | None = None,
        stream_specification: stream_specification_.StreamSpecification | None = None,
        table_class: str | None = None,
        table_id: str | None = None,
        table_name: str | None = None,
        tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None,
        p_type: str | None = None,
    ) -> None:
        """Constructor for the ReadDynamoDBTableBackupResponse class."""

        # Initialize members of the class
        self.etag: str | None = etag
        self.links: dynamo_db_table_backup_links_.DynamoDBTableBackupLinks | None = links
        self.account_native_id: str | None = account_native_id
        self.aws_region: str | None = aws_region
        self.billing_mode: str | None = billing_mode
        self.contributor_insights_status: bool | None = contributor_insights_status
        self.deletion_protection_enabled: bool | None = deletion_protection_enabled
        self.expiration_timestamp: str | None = expiration_timestamp
        self.global_secondary_indexes: (
            Sequence[global_secondary_index_.GlobalSecondaryIndex] | None
        ) = global_secondary_indexes
        self.global_table_version: str | None = global_table_version
        self.p_id: str | None = p_id
        self.item_count: int | None = item_count
        self.local_secondary_indexes: (
            Sequence[local_secondary_index_.LocalSecondaryIndex] | None
        ) = local_secondary_indexes
        self.pitr_status: bool | None = pitr_status
        self.provisioned_throughput: provisioned_throughput_.ProvisionedThroughput | None = (
            provisioned_throughput
        )
        self.replicas: Sequence[replica_description_.ReplicaDescription] | None = replicas
        self.size: int | None = size
        self.sse_specification: sse_specification_.SSESpecification | None = sse_specification
        self.start_timestamp: str | None = start_timestamp
        self.stream_specification: stream_specification_.StreamSpecification | None = (
            stream_specification
        )
        self.table_class: str | None = table_class
        self.table_id: str | None = table_id
        self.table_name: str | None = table_name
        self.tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = tags
        self.p_type: str | None = p_type

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
        val = dictionary.get('_etag', None)
        val_etag = val

        val = dictionary.get('_links', None)
        val_links = dynamo_db_table_backup_links_.DynamoDBTableBackupLinks.from_dictionary(val)

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('billing_mode', None)
        val_billing_mode = val

        val = dictionary.get('contributor_insights_status', None)
        val_contributor_insights_status = val

        val = dictionary.get('deletion_protection_enabled', None)
        val_deletion_protection_enabled = val

        val = dictionary.get('expiration_timestamp', None)
        val_expiration_timestamp = val

        val = dictionary.get('global_secondary_indexes', None)

        val_global_secondary_indexes = None
        if val:
            val_global_secondary_indexes = list()
            for value in val:
                val_global_secondary_indexes.append(
                    global_secondary_index_.GlobalSecondaryIndex.from_dictionary(value)
                )

        val = dictionary.get('global_table_version', None)
        val_global_table_version = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('item_count', None)
        val_item_count = val

        val = dictionary.get('local_secondary_indexes', None)

        val_local_secondary_indexes = None
        if val:
            val_local_secondary_indexes = list()
            for value in val:
                val_local_secondary_indexes.append(
                    local_secondary_index_.LocalSecondaryIndex.from_dictionary(value)
                )

        val = dictionary.get('pitr_status', None)
        val_pitr_status = val

        val = dictionary.get('provisioned_throughput', None)
        val_provisioned_throughput = provisioned_throughput_.ProvisionedThroughput.from_dictionary(
            val
        )

        val = dictionary.get('replicas', None)

        val_replicas = None
        if val:
            val_replicas = list()
            for value in val:
                val_replicas.append(replica_description_.ReplicaDescription.from_dictionary(value))

        val = dictionary.get('size', None)
        val_size = val

        val = dictionary.get('sse_specification', None)
        val_sse_specification = sse_specification_.SSESpecification.from_dictionary(val)

        val = dictionary.get('start_timestamp', None)
        val_start_timestamp = val

        val = dictionary.get('stream_specification', None)
        val_stream_specification = stream_specification_.StreamSpecification.from_dictionary(val)

        val = dictionary.get('table_class', None)
        val_table_class = val

        val = dictionary.get('table_id', None)
        val_table_id = val

        val = dictionary.get('table_name', None)
        val_table_name = val

        val = dictionary.get('tags', None)

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        val = dictionary.get('type', None)
        val_p_type = val

        # Return an object of this model
        return cls(
            val_etag,
            val_links,
            val_account_native_id,
            val_aws_region,
            val_billing_mode,
            val_contributor_insights_status,
            val_deletion_protection_enabled,
            val_expiration_timestamp,
            val_global_secondary_indexes,
            val_global_table_version,
            val_p_id,
            val_item_count,
            val_local_secondary_indexes,
            val_pitr_status,
            val_provisioned_throughput,
            val_replicas,
            val_size,
            val_sse_specification,
            val_start_timestamp,
            val_stream_specification,
            val_table_class,
            val_table_id,
            val_table_name,
            val_tags,
            val_p_type,
        )
