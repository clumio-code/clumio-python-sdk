#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import aws_tag_common_model as aws_tag_common_model_
from clumioapi.models import dynamo_db_table_backup_links as dynamo_db_table_backup_links_
from clumioapi.models import global_secondary_index as global_secondary_index_
from clumioapi.models import local_secondary_index as local_secondary_index_
from clumioapi.models import provisioned_throughput as provisioned_throughput_
from clumioapi.models import replica_description as replica_description_
from clumioapi.models import sse_specification as sse_specification_
from clumioapi.models import stream_specification as stream_specification_
import requests

T = TypeVar('T', bound='ReadDynamoDBTableBackupResponse')


@dataclasses.dataclass
class ReadDynamoDBTableBackupResponse:
    """Implementation of the 'ReadDynamoDBTableBackupResponse' model.

        Attributes:
            Etag:
                The etag value.

            Links:
                Urls to pages related to the resource.

            AccountNativeId:
                The aws-assigned id of the account associated with this database at the time of backup.

            AwsRegion:
                The aws region associated with this environment.

            BillingMode:
                The billing mode of the dynamodb table. possible values are provisioned or pay_per_request.
    for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this is defaulted to the
    configuration of source table if both 'billing_mode' and 'provisioned_throughput' are empty or `null`.

            ContributorInsightsStatus:
                Indicates whether dynamodb contributor insights is enabled (true) or disabled (false)
    on the table.
    for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this is defaulted to the
    value set in backup if `null`.

            DeletionProtectionEnabled:
                Indicates whether dynamodb deletion protection is enabled (true) or disabled (false)
    on the table.
    for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this is defaulted to the
    value set in backup if `null`.

            ExpirationTimestamp:
                The timestamp of when this backup expires. represented in rfc-3339 format.

            GlobalSecondaryIndexes:
                Describes the global secondary indexes of the dynamodb table.
    for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), a subset of the source tables'
    global_secondary_indexes can be specified.
    the restored table will not have any global secondary indexes if this is specified empty or `null`.

            GlobalTableVersion:
                Describes the version of global tables in use, if the table is replicated across aws regions. if the table
    is not a global table, then this field has a value of `null`. possible values are 2017.11.29 or 2019.11.21.
    for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), the version is defaulted to 2019.11.21.

            Id:
                The clumio-assigned id of the backup.

            ItemCount:
                The number of items in dynamodb table backup.

            LocalSecondaryIndexes:
                Describes the local secondary indexes of the dynamodb table.
    for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), a subset of the source tables'
    local_secondary_indexes can be specified.
    the restored table will not have any local secondary indexes if this is specified empty or `null`.

            PitrStatus:
                Indicates whether dynamodb continuous backup (pitr) is enabled (true) or disabled (false)
    on the table.
    for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this is defaulted to the
    value set in backup if `null`.

            ProvisionedThroughput:
                Represents the provisioned throughput settings for a dynamodb table.

            Replicas:
                Describes the replicas of the table, if the table is replicated across aws regions.
    not applicable for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table) currently,
    but will be used to specify the replication group information in a future release.

            Size:
                The size of the dynamodb table backup in bytes.

            SseSpecification:
                Represents the server-side encryption settings for a table.

            StartTimestamp:
                The timestamp of when this backup started. represented in rfc-3339 format.

            StreamSpecification:
                Represents the dynamodb streams configuration for a table in dynamodb.
    and the data type (`s` for string, `n` for number, `b` for binary).

            TableClass:
                The table class of the dynamodb table. possible values are standard or standard_infrequent_access.
    for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this is defaulted to the
    standard storage class if empty.

            TableId:
                The clumio-assigned id of the dynamodb table.

            TableName:
                The name of the dynamodb table.

            Tags:
                The aws tags associated with the table at the time of backup.

            Type:
                The type of backup. possible values include `clumio_backup` and `aws_snapshot`.

    """

    Etag: str | None = None
    Links: dynamo_db_table_backup_links_.DynamoDBTableBackupLinks | None = None
    AccountNativeId: str | None = None
    AwsRegion: str | None = None
    BillingMode: str | None = None
    ContributorInsightsStatus: bool | None = None
    DeletionProtectionEnabled: bool | None = None
    ExpirationTimestamp: str | None = None
    GlobalSecondaryIndexes: Sequence[global_secondary_index_.GlobalSecondaryIndex] | None = None
    GlobalTableVersion: str | None = None
    Id: str | None = None
    ItemCount: int | None = None
    LocalSecondaryIndexes: Sequence[local_secondary_index_.LocalSecondaryIndex] | None = None
    PitrStatus: bool | None = None
    ProvisionedThroughput: provisioned_throughput_.ProvisionedThroughput | None = None
    Replicas: Sequence[replica_description_.ReplicaDescription] | None = None
    Size: int | None = None
    SseSpecification: sse_specification_.SSESpecification | None = None
    StartTimestamp: str | None = None
    StreamSpecification: stream_specification_.StreamSpecification | None = None
    TableClass: str | None = None
    TableId: str | None = None
    TableName: str | None = None
    Tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None
    Type: str | None = None
    raw_response: Optional[requests.Response] = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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

        val_global_secondary_indexes = []
        if val:
            for value in val:
                val_global_secondary_indexes.append(
                    global_secondary_index_.GlobalSecondaryIndex.from_dictionary(value)
                )

        val = dictionary.get('global_table_version', None)
        val_global_table_version = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('item_count', None)
        val_item_count = val

        val = dictionary.get('local_secondary_indexes', None)

        val_local_secondary_indexes = []
        if val:
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

        val_replicas = []
        if val:
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

        val_tags = []
        if val:
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        val = dictionary.get('type', None)
        val_type = val

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
            val_id,
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
            val_type,
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
