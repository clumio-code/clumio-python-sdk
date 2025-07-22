#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model as aws_tag_common_model_
from clumioapi.models import global_secondary_index as global_secondary_index_
from clumioapi.models import local_secondary_index as local_secondary_index_
from clumioapi.models import provisioned_throughput as provisioned_throughput_
from clumioapi.models import replica_description as replica_description_
from clumioapi.models import sse_specification as sse_specification_
from clumioapi.models import stream_specification as stream_specification_

T = TypeVar('T', bound='DynamoDBTableRestoreTarget')


class DynamoDBTableRestoreTarget:
    """Implementation of the 'DynamoDBTableRestoreTarget' model.

    The configuration of the restored DynamoDB table.For restore from snapshot, use
    the DynamoDB table configurations present at time of snapshot obtained from[GET
    /backups/aws/dynamodb-tables/{backup_id}](#operation/read-backup-aws-dynamodb-
    table) and for restoring point-in-time,use the current configuration of the
    table from [GET /datasources/aws/dynamodb-tables/{table_id}](#operation/read-
    aws-dynamodb-table).The table properties are set to empty or to their default
    values if they are specified as `null`.

    Attributes:
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
        environment_id:
            The Clumio-assigned ID of the AWS environment to be used as the restore
            destination.
            Use the [GET /datasources/aws/environments](#operation/list-aws-environments)
            endpoint
            to fetch valid values.
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
        sse_specification:
            Represents the server-side encryption settings for a table.
        stream_specification:
            Represents the DynamoDB Streams configuration for a table in DynamoDB.
            and the data type (`S` for string, `N` for number, `B` for binary).
        table_class:
            The table class of the DynamoDB table. Possible values are STANDARD or
            STANDARD_INFREQUENT_ACCESS.
            For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this
            is defaulted to the
            STANDARD storage class if empty.
        table_name:
            The name of the new table to which the backup must be restored.
        tags:
            The AWS tags to be applied to the restored table. The tags are stored in the AWS
            cloud as part of your AWS account.
            A DynamoDB table can be have multiple tags. To find the tags that were applied
            to the original table,
            use the [GET /datasources/aws/dynamodb-tables/{table_id}](#operation/read-aws-
            dynamodb-table) endpoint to display
            the original table's tag keys (`tags.key`) and tag values (`tags.value`).
            The restored table will not have any tags applied if this is specified as
            `null`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'billing_mode': 'billing_mode',
        'contributor_insights_status': 'contributor_insights_status',
        'deletion_protection_enabled': 'deletion_protection_enabled',
        'environment_id': 'environment_id',
        'global_secondary_indexes': 'global_secondary_indexes',
        'global_table_version': 'global_table_version',
        'local_secondary_indexes': 'local_secondary_indexes',
        'pitr_status': 'pitr_status',
        'provisioned_throughput': 'provisioned_throughput',
        'replicas': 'replicas',
        'sse_specification': 'sse_specification',
        'stream_specification': 'stream_specification',
        'table_class': 'table_class',
        'table_name': 'table_name',
        'tags': 'tags',
    }

    def __init__(
        self,
        billing_mode: str,
        contributor_insights_status: bool,
        deletion_protection_enabled: bool,
        environment_id: str,
        global_secondary_indexes: Sequence[global_secondary_index_.GlobalSecondaryIndex],
        global_table_version: str,
        local_secondary_indexes: Sequence[local_secondary_index_.LocalSecondaryIndex],
        pitr_status: bool,
        provisioned_throughput: provisioned_throughput_.ProvisionedThroughput,
        replicas: Sequence[replica_description_.ReplicaDescription],
        sse_specification: sse_specification_.SSESpecification,
        stream_specification: stream_specification_.StreamSpecification,
        table_class: str,
        table_name: str,
        tags: Sequence[aws_tag_common_model_.AwsTagCommonModel],
    ) -> None:
        """Constructor for the DynamoDBTableRestoreTarget class."""

        # Initialize members of the class
        self.billing_mode: str = billing_mode
        self.contributor_insights_status: bool = contributor_insights_status
        self.deletion_protection_enabled: bool = deletion_protection_enabled
        self.environment_id: str = environment_id
        self.global_secondary_indexes: Sequence[global_secondary_index_.GlobalSecondaryIndex] = (
            global_secondary_indexes
        )
        self.global_table_version: str = global_table_version
        self.local_secondary_indexes: Sequence[local_secondary_index_.LocalSecondaryIndex] = (
            local_secondary_indexes
        )
        self.pitr_status: bool = pitr_status
        self.provisioned_throughput: provisioned_throughput_.ProvisionedThroughput = (
            provisioned_throughput
        )
        self.replicas: Sequence[replica_description_.ReplicaDescription] = replicas
        self.sse_specification: sse_specification_.SSESpecification = sse_specification
        self.stream_specification: stream_specification_.StreamSpecification = stream_specification
        self.table_class: str = table_class
        self.table_name: str = table_name
        self.tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] = tags

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
        val = dictionary['billing_mode']
        val_billing_mode = val

        val = dictionary['contributor_insights_status']
        val_contributor_insights_status = val

        val = dictionary['deletion_protection_enabled']
        val_deletion_protection_enabled = val

        val = dictionary['environment_id']
        val_environment_id = val

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

        val = dictionary['sse_specification']
        val_sse_specification = sse_specification_.SSESpecification.from_dictionary(val)

        val = dictionary['stream_specification']
        val_stream_specification = stream_specification_.StreamSpecification.from_dictionary(val)

        val = dictionary['table_class']
        val_table_class = val

        val = dictionary['table_name']
        val_table_name = val

        val = dictionary['tags']

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_billing_mode,  # type: ignore
            val_contributor_insights_status,  # type: ignore
            val_deletion_protection_enabled,  # type: ignore
            val_environment_id,  # type: ignore
            val_global_secondary_indexes,  # type: ignore
            val_global_table_version,  # type: ignore
            val_local_secondary_indexes,  # type: ignore
            val_pitr_status,  # type: ignore
            val_provisioned_throughput,  # type: ignore
            val_replicas,  # type: ignore
            val_sse_specification,  # type: ignore
            val_stream_specification,  # type: ignore
            val_table_class,  # type: ignore
            val_table_name,  # type: ignore
            val_tags,  # type: ignore
        )
