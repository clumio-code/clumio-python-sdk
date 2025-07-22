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
        etag: str,
        links: dynamo_db_table_backup_links_.DynamoDBTableBackupLinks,
        account_native_id: str,
        aws_region: str,
        billing_mode: str,
        contributor_insights_status: bool,
        deletion_protection_enabled: bool,
        expiration_timestamp: str,
        global_secondary_indexes: Sequence[global_secondary_index_.GlobalSecondaryIndex],
        global_table_version: str,
        p_id: str,
        item_count: int,
        local_secondary_indexes: Sequence[local_secondary_index_.LocalSecondaryIndex],
        pitr_status: bool,
        provisioned_throughput: provisioned_throughput_.ProvisionedThroughput,
        replicas: Sequence[replica_description_.ReplicaDescription],
        size: int,
        sse_specification: sse_specification_.SSESpecification,
        start_timestamp: str,
        stream_specification: stream_specification_.StreamSpecification,
        table_class: str,
        table_id: str,
        table_name: str,
        tags: Sequence[aws_tag_common_model_.AwsTagCommonModel],
        p_type: str,
    ) -> None:
        """Constructor for the ReadDynamoDBTableBackupResponse class."""

        # Initialize members of the class
        self.etag: str = etag
        self.links: dynamo_db_table_backup_links_.DynamoDBTableBackupLinks = links
        self.account_native_id: str = account_native_id
        self.aws_region: str = aws_region
        self.billing_mode: str = billing_mode
        self.contributor_insights_status: bool = contributor_insights_status
        self.deletion_protection_enabled: bool = deletion_protection_enabled
        self.expiration_timestamp: str = expiration_timestamp
        self.global_secondary_indexes: Sequence[global_secondary_index_.GlobalSecondaryIndex] = (
            global_secondary_indexes
        )
        self.global_table_version: str = global_table_version
        self.p_id: str = p_id
        self.item_count: int = item_count
        self.local_secondary_indexes: Sequence[local_secondary_index_.LocalSecondaryIndex] = (
            local_secondary_indexes
        )
        self.pitr_status: bool = pitr_status
        self.provisioned_throughput: provisioned_throughput_.ProvisionedThroughput = (
            provisioned_throughput
        )
        self.replicas: Sequence[replica_description_.ReplicaDescription] = replicas
        self.size: int = size
        self.sse_specification: sse_specification_.SSESpecification = sse_specification
        self.start_timestamp: str = start_timestamp
        self.stream_specification: stream_specification_.StreamSpecification = stream_specification
        self.table_class: str = table_class
        self.table_id: str = table_id
        self.table_name: str = table_name
        self.tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] = tags
        self.p_type: str = p_type

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
        val = dictionary['_etag']
        val_etag = val

        val = dictionary['_links']
        val_links = dynamo_db_table_backup_links_.DynamoDBTableBackupLinks.from_dictionary(val)

        val = dictionary['account_native_id']
        val_account_native_id = val

        val = dictionary['aws_region']
        val_aws_region = val

        val = dictionary['billing_mode']
        val_billing_mode = val

        val = dictionary['contributor_insights_status']
        val_contributor_insights_status = val

        val = dictionary['deletion_protection_enabled']
        val_deletion_protection_enabled = val

        val = dictionary['expiration_timestamp']
        val_expiration_timestamp = val

        val = dictionary['global_secondary_indexes']

        val_global_secondary_indexes = None
        if val:
            val_global_secondary_indexes = list()
            for value in val:
                val_global_secondary_indexes.append(
                    global_secondary_index_.GlobalSecondaryIndex.from_dictionary(value)
                )

        val = dictionary['global_table_version']
        val_global_table_version = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['item_count']
        val_item_count = val

        val = dictionary['local_secondary_indexes']

        val_local_secondary_indexes = None
        if val:
            val_local_secondary_indexes = list()
            for value in val:
                val_local_secondary_indexes.append(
                    local_secondary_index_.LocalSecondaryIndex.from_dictionary(value)
                )

        val = dictionary['pitr_status']
        val_pitr_status = val

        val = dictionary['provisioned_throughput']
        val_provisioned_throughput = provisioned_throughput_.ProvisionedThroughput.from_dictionary(
            val
        )

        val = dictionary['replicas']

        val_replicas = None
        if val:
            val_replicas = list()
            for value in val:
                val_replicas.append(replica_description_.ReplicaDescription.from_dictionary(value))

        val = dictionary['size']
        val_size = val

        val = dictionary['sse_specification']
        val_sse_specification = sse_specification_.SSESpecification.from_dictionary(val)

        val = dictionary['start_timestamp']
        val_start_timestamp = val

        val = dictionary['stream_specification']
        val_stream_specification = stream_specification_.StreamSpecification.from_dictionary(val)

        val = dictionary['table_class']
        val_table_class = val

        val = dictionary['table_id']
        val_table_id = val

        val = dictionary['table_name']
        val_table_name = val

        val = dictionary['tags']

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        val = dictionary['type']
        val_p_type = val

        # Return an object of this model
        return cls(
            val_etag,  # type: ignore
            val_links,  # type: ignore
            val_account_native_id,  # type: ignore
            val_aws_region,  # type: ignore
            val_billing_mode,  # type: ignore
            val_contributor_insights_status,  # type: ignore
            val_deletion_protection_enabled,  # type: ignore
            val_expiration_timestamp,  # type: ignore
            val_global_secondary_indexes,  # type: ignore
            val_global_table_version,  # type: ignore
            val_p_id,  # type: ignore
            val_item_count,  # type: ignore
            val_local_secondary_indexes,  # type: ignore
            val_pitr_status,  # type: ignore
            val_provisioned_throughput,  # type: ignore
            val_replicas,  # type: ignore
            val_size,  # type: ignore
            val_sse_specification,  # type: ignore
            val_start_timestamp,  # type: ignore
            val_stream_specification,  # type: ignore
            val_table_class,  # type: ignore
            val_table_id,  # type: ignore
            val_table_name,  # type: ignore
            val_tags,  # type: ignore
            val_p_type,  # type: ignore
        )
