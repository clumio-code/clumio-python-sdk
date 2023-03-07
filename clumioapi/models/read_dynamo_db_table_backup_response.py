#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model
from clumioapi.models import dynamo_db_table_backup_links
from clumioapi.models import global_secondary_index
from clumioapi.models import local_secondary_index
from clumioapi.models import provisioned_throughput
from clumioapi.models import replica_description
from clumioapi.models import sse_specification

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
    _names = {
        'etag': '_etag',
        'links': '_links',
        'account_native_id': 'account_native_id',
        'aws_region': 'aws_region',
        'billing_mode': 'billing_mode',
        'expiration_timestamp': 'expiration_timestamp',
        'global_secondary_indexes': 'global_secondary_indexes',
        'global_table_version': 'global_table_version',
        'p_id': 'id',
        'item_count': 'item_count',
        'local_secondary_indexes': 'local_secondary_indexes',
        'provisioned_throughput': 'provisioned_throughput',
        'replicas': 'replicas',
        'size': 'size',
        'sse_specification': 'sse_specification',
        'start_timestamp': 'start_timestamp',
        'table_class': 'table_class',
        'table_id': 'table_id',
        'table_name': 'table_name',
        'tags': 'tags',
        'p_type': 'type',
    }

    def __init__(
        self,
        etag: str = None,
        links: dynamo_db_table_backup_links.DynamoDBTableBackupLinks = None,
        account_native_id: str = None,
        aws_region: str = None,
        billing_mode: str = None,
        expiration_timestamp: str = None,
        global_secondary_indexes: Sequence[global_secondary_index.GlobalSecondaryIndex] = None,
        global_table_version: str = None,
        p_id: str = None,
        item_count: int = None,
        local_secondary_indexes: Sequence[local_secondary_index.LocalSecondaryIndex] = None,
        provisioned_throughput: provisioned_throughput.ProvisionedThroughput = None,
        replicas: Sequence[replica_description.ReplicaDescription] = None,
        size: int = None,
        sse_specification: sse_specification.SSESpecification = None,
        start_timestamp: str = None,
        table_class: str = None,
        table_id: str = None,
        table_name: str = None,
        tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = None,
        p_type: str = None,
    ) -> None:
        """Constructor for the ReadDynamoDBTableBackupResponse class."""

        # Initialize members of the class
        self.etag: str = etag
        self.links: dynamo_db_table_backup_links.DynamoDBTableBackupLinks = links
        self.account_native_id: str = account_native_id
        self.aws_region: str = aws_region
        self.billing_mode: str = billing_mode
        self.expiration_timestamp: str = expiration_timestamp
        self.global_secondary_indexes: Sequence[
            global_secondary_index.GlobalSecondaryIndex
        ] = global_secondary_indexes
        self.global_table_version: str = global_table_version
        self.p_id: str = p_id
        self.item_count: int = item_count
        self.local_secondary_indexes: Sequence[
            local_secondary_index.LocalSecondaryIndex
        ] = local_secondary_indexes
        self.provisioned_throughput: provisioned_throughput.ProvisionedThroughput = (
            provisioned_throughput
        )
        self.replicas: Sequence[replica_description.ReplicaDescription] = replicas
        self.size: int = size
        self.sse_specification: sse_specification.SSESpecification = sse_specification
        self.start_timestamp: str = start_timestamp
        self.table_class: str = table_class
        self.table_id: str = table_id
        self.table_name: str = table_name
        self.tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = tags
        self.p_type: str = p_type

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
        etag = dictionary.get('_etag')
        key = '_links'
        links = (
            dynamo_db_table_backup_links.DynamoDBTableBackupLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        account_native_id = dictionary.get('account_native_id')
        aws_region = dictionary.get('aws_region')
        billing_mode = dictionary.get('billing_mode')
        expiration_timestamp = dictionary.get('expiration_timestamp')
        global_secondary_indexes = None
        if dictionary.get('global_secondary_indexes'):
            global_secondary_indexes = list()
            for value in dictionary.get('global_secondary_indexes'):
                global_secondary_indexes.append(
                    global_secondary_index.GlobalSecondaryIndex.from_dictionary(value)
                )

        global_table_version = dictionary.get('global_table_version')
        p_id = dictionary.get('id')
        item_count = dictionary.get('item_count')
        local_secondary_indexes = None
        if dictionary.get('local_secondary_indexes'):
            local_secondary_indexes = list()
            for value in dictionary.get('local_secondary_indexes'):
                local_secondary_indexes.append(
                    local_secondary_index.LocalSecondaryIndex.from_dictionary(value)
                )

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

        size = dictionary.get('size')
        key = 'sse_specification'
        p_sse_specification = (
            sse_specification.SSESpecification.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        start_timestamp = dictionary.get('start_timestamp')
        table_class = dictionary.get('table_class')
        table_id = dictionary.get('table_id')
        table_name = dictionary.get('table_name')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(aws_tag_common_model.AwsTagCommonModel.from_dictionary(value))

        p_type = dictionary.get('type')
        # Return an object of this model
        return cls(
            etag,
            links,
            account_native_id,
            aws_region,
            billing_mode,
            expiration_timestamp,
            global_secondary_indexes,
            global_table_version,
            p_id,
            item_count,
            local_secondary_indexes,
            p_provisioned_throughput,
            replicas,
            size,
            p_sse_specification,
            start_timestamp,
            table_class,
            table_id,
            table_name,
            tags,
            p_type,
        )
