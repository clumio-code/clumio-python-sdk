#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model
from clumioapi.models import global_secondary_index
from clumioapi.models import local_secondary_index
from clumioapi.models import provisioned_throughput
from clumioapi.models import replica_description
from clumioapi.models import sse_specification
from clumioapi.models import stream_specification

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
    _names = {
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
        billing_mode: str = None,
        contributor_insights_status: bool = None,
        deletion_protection_enabled: bool = None,
        environment_id: str = None,
        global_secondary_indexes: Sequence[global_secondary_index.GlobalSecondaryIndex] = None,
        global_table_version: str = None,
        local_secondary_indexes: Sequence[local_secondary_index.LocalSecondaryIndex] = None,
        pitr_status: bool = None,
        provisioned_throughput: provisioned_throughput.ProvisionedThroughput = None,
        replicas: Sequence[replica_description.ReplicaDescription] = None,
        sse_specification: sse_specification.SSESpecification = None,
        stream_specification: stream_specification.StreamSpecification = None,
        table_class: str = None,
        table_name: str = None,
        tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = None,
    ) -> None:
        """Constructor for the DynamoDBTableRestoreTarget class."""

        # Initialize members of the class
        self.billing_mode: str = billing_mode
        self.contributor_insights_status: bool = contributor_insights_status
        self.deletion_protection_enabled: bool = deletion_protection_enabled
        self.environment_id: str = environment_id
        self.global_secondary_indexes: Sequence[global_secondary_index.GlobalSecondaryIndex] = (
            global_secondary_indexes
        )
        self.global_table_version: str = global_table_version
        self.local_secondary_indexes: Sequence[local_secondary_index.LocalSecondaryIndex] = (
            local_secondary_indexes
        )
        self.pitr_status: bool = pitr_status
        self.provisioned_throughput: provisioned_throughput.ProvisionedThroughput = (
            provisioned_throughput
        )
        self.replicas: Sequence[replica_description.ReplicaDescription] = replicas
        self.sse_specification: sse_specification.SSESpecification = sse_specification
        self.stream_specification: stream_specification.StreamSpecification = stream_specification
        self.table_class: str = table_class
        self.table_name: str = table_name
        self.tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = tags

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
        billing_mode = dictionary.get('billing_mode')
        contributor_insights_status = dictionary.get('contributor_insights_status')
        deletion_protection_enabled = dictionary.get('deletion_protection_enabled')
        environment_id = dictionary.get('environment_id')
        global_secondary_indexes = None
        if dictionary.get('global_secondary_indexes'):
            global_secondary_indexes = list()
            for value in dictionary.get('global_secondary_indexes'):
                global_secondary_indexes.append(
                    global_secondary_index.GlobalSecondaryIndex.from_dictionary(value)
                )

        global_table_version = dictionary.get('global_table_version')
        local_secondary_indexes = None
        if dictionary.get('local_secondary_indexes'):
            local_secondary_indexes = list()
            for value in dictionary.get('local_secondary_indexes'):
                local_secondary_indexes.append(
                    local_secondary_index.LocalSecondaryIndex.from_dictionary(value)
                )

        pitr_status = dictionary.get('pitr_status')
        key = 'provisioned_throughput'
        p_provisioned_throughput = (
            provisioned_throughput.ProvisionedThroughput.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        replicas = None
        if dictionary.get('replicas'):
            replicas = list()
            for value in dictionary.get('replicas'):
                replicas.append(replica_description.ReplicaDescription.from_dictionary(value))

        key = 'sse_specification'
        p_sse_specification = (
            sse_specification.SSESpecification.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'stream_specification'
        p_stream_specification = (
            stream_specification.StreamSpecification.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        table_class = dictionary.get('table_class')
        table_name = dictionary.get('table_name')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(aws_tag_common_model.AwsTagCommonModel.from_dictionary(value))

        # Return an object of this model
        return cls(
            billing_mode,
            contributor_insights_status,
            deletion_protection_enabled,
            environment_id,
            global_secondary_indexes,
            global_table_version,
            local_secondary_indexes,
            pitr_status,
            p_provisioned_throughput,
            replicas,
            p_sse_specification,
            p_stream_specification,
            table_class,
            table_name,
            tags,
        )
