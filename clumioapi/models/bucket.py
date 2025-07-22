#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_model as aws_tag_model_
from clumioapi.models import bucket_links as bucket_links_
from clumioapi.models import \
    s3_buckets_inventory_summary_bucket_size_breakdown as \
    s3_buckets_inventory_summary_bucket_size_breakdown_
from clumioapi.models import s3_cloudwatch_metrics as s3_cloudwatch_metrics_
from clumioapi.models import s3_encryption_output as s3_encryption_output_
from clumioapi.models import s3_replication_output as s3_replication_output_
from clumioapi.models import s3_versioning_output as s3_versioning_output_

T = TypeVar('T', bound='Bucket')


class Bucket:
    """Implementation of the 'Bucket' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        account_native_id:
            The AWS-assigned ID of the account associated with the S3 bucket.
        aws_region:
            The AWS region associated with the S3 bucket.
        bucket_size_bytes_breakdown:
            The total size breakdown of S3 buckets in bytes per storage class. This
            parameter aggregates relevant fields from cloudwatch_metrics >
            size_bytes_per_storage_class
        cloudwatch_metrics:
            The Cloudwatch metrics of the bucket.
        creation_timestamp:
            The timestamp of when the bucket was created. Represented in RFC-3339 format.
        encryption_setting:
            The AWS encryption output of the bucket.
        environment_id:
            The Clumio-assigned ID of the AWS environment associated with the S3 bucket.
        event_bridge_enabled:
            The EventBridge enablement state for the S3 bucket.
        p_id:
            The Clumio-assigned ID of the bucket.
        is_encryption_enabled:
            The Encryption enablement state for the S3 bucket.
        is_replication_enabled:
            The Replication enablement state for the S3 bucket.
        is_versioning_enabled:
            The Versioning enablement state for the S3 bucket.
        last_backtrack_sync_timestamp:
            Time of the last S3 Backtrack sync in RFC-3339 format.
        last_backup_timestamp:
            Time of the last backup in RFC-3339 format.
        last_continuous_backup_timestamp:
            Time of the last continuous backup in RFC-3339 format.
        name:
            The AWS-assigned name of the bucket.
        object_count:
            Number of objects in bucket.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the S3 bucket.
        protection_group_count:
            Protection group count reflects how many protection groups are linked to this
            bucket.
        replication_setting:
            The AWS replication output of the bucket.
        size_bytes:
            Size of bucket in bytes.
        tags:
            The AWS tags applied to the S3 bucket.
        versioning_setting:
            The AWS versioning output of the bucket.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'account_native_id': 'account_native_id',
        'aws_region': 'aws_region',
        'bucket_size_bytes_breakdown': 'bucket_size_bytes_breakdown',
        'cloudwatch_metrics': 'cloudwatch_metrics',
        'creation_timestamp': 'creation_timestamp',
        'encryption_setting': 'encryption_setting',
        'environment_id': 'environment_id',
        'event_bridge_enabled': 'event_bridge_enabled',
        'p_id': 'id',
        'is_encryption_enabled': 'is_encryption_enabled',
        'is_replication_enabled': 'is_replication_enabled',
        'is_versioning_enabled': 'is_versioning_enabled',
        'last_backtrack_sync_timestamp': 'last_backtrack_sync_timestamp',
        'last_backup_timestamp': 'last_backup_timestamp',
        'last_continuous_backup_timestamp': 'last_continuous_backup_timestamp',
        'name': 'name',
        'object_count': 'object_count',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_group_count': 'protection_group_count',
        'replication_setting': 'replication_setting',
        'size_bytes': 'size_bytes',
        'tags': 'tags',
        'versioning_setting': 'versioning_setting',
    }

    def __init__(
        self,
        embedded: object,
        links: bucket_links_.BucketLinks,
        account_native_id: str,
        aws_region: str,
        bucket_size_bytes_breakdown: s3_buckets_inventory_summary_bucket_size_breakdown_.S3BucketsInventorySummaryBucketSizeBreakdown,
        cloudwatch_metrics: s3_cloudwatch_metrics_.S3CloudwatchMetrics,
        creation_timestamp: str,
        encryption_setting: s3_encryption_output_.S3EncryptionOutput,
        environment_id: str,
        event_bridge_enabled: bool,
        p_id: str,
        is_encryption_enabled: bool,
        is_replication_enabled: bool,
        is_versioning_enabled: bool,
        last_backtrack_sync_timestamp: str,
        last_backup_timestamp: str,
        last_continuous_backup_timestamp: str,
        name: str,
        object_count: int,
        organizational_unit_id: str,
        protection_group_count: int,
        replication_setting: s3_replication_output_.S3ReplicationOutput,
        size_bytes: int,
        tags: Sequence[aws_tag_model_.AwsTagModel],
        versioning_setting: s3_versioning_output_.S3VersioningOutput,
    ) -> None:
        """Constructor for the Bucket class."""

        # Initialize members of the class
        self.embedded: object = embedded
        self.links: bucket_links_.BucketLinks = links
        self.account_native_id: str = account_native_id
        self.aws_region: str = aws_region
        self.bucket_size_bytes_breakdown: (
            s3_buckets_inventory_summary_bucket_size_breakdown_.S3BucketsInventorySummaryBucketSizeBreakdown
        ) = bucket_size_bytes_breakdown
        self.cloudwatch_metrics: s3_cloudwatch_metrics_.S3CloudwatchMetrics = cloudwatch_metrics
        self.creation_timestamp: str = creation_timestamp
        self.encryption_setting: s3_encryption_output_.S3EncryptionOutput = encryption_setting
        self.environment_id: str = environment_id
        self.event_bridge_enabled: bool = event_bridge_enabled
        self.p_id: str = p_id
        self.is_encryption_enabled: bool = is_encryption_enabled
        self.is_replication_enabled: bool = is_replication_enabled
        self.is_versioning_enabled: bool = is_versioning_enabled
        self.last_backtrack_sync_timestamp: str = last_backtrack_sync_timestamp
        self.last_backup_timestamp: str = last_backup_timestamp
        self.last_continuous_backup_timestamp: str = last_continuous_backup_timestamp
        self.name: str = name
        self.object_count: int = object_count
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_group_count: int = protection_group_count
        self.replication_setting: s3_replication_output_.S3ReplicationOutput = replication_setting
        self.size_bytes: int = size_bytes
        self.tags: Sequence[aws_tag_model_.AwsTagModel] = tags
        self.versioning_setting: s3_versioning_output_.S3VersioningOutput = versioning_setting

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
        val = dictionary['_embedded']
        val_embedded = val

        val = dictionary['_links']
        val_links = bucket_links_.BucketLinks.from_dictionary(val)

        val = dictionary['account_native_id']
        val_account_native_id = val

        val = dictionary['aws_region']
        val_aws_region = val

        val = dictionary['bucket_size_bytes_breakdown']
        val_bucket_size_bytes_breakdown = s3_buckets_inventory_summary_bucket_size_breakdown_.S3BucketsInventorySummaryBucketSizeBreakdown.from_dictionary(
            val
        )

        val = dictionary['cloudwatch_metrics']
        val_cloudwatch_metrics = s3_cloudwatch_metrics_.S3CloudwatchMetrics.from_dictionary(val)

        val = dictionary['creation_timestamp']
        val_creation_timestamp = val

        val = dictionary['encryption_setting']
        val_encryption_setting = s3_encryption_output_.S3EncryptionOutput.from_dictionary(val)

        val = dictionary['environment_id']
        val_environment_id = val

        val = dictionary['event_bridge_enabled']
        val_event_bridge_enabled = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['is_encryption_enabled']
        val_is_encryption_enabled = val

        val = dictionary['is_replication_enabled']
        val_is_replication_enabled = val

        val = dictionary['is_versioning_enabled']
        val_is_versioning_enabled = val

        val = dictionary['last_backtrack_sync_timestamp']
        val_last_backtrack_sync_timestamp = val

        val = dictionary['last_backup_timestamp']
        val_last_backup_timestamp = val

        val = dictionary['last_continuous_backup_timestamp']
        val_last_continuous_backup_timestamp = val

        val = dictionary['name']
        val_name = val

        val = dictionary['object_count']
        val_object_count = val

        val = dictionary['organizational_unit_id']
        val_organizational_unit_id = val

        val = dictionary['protection_group_count']
        val_protection_group_count = val

        val = dictionary['replication_setting']
        val_replication_setting = s3_replication_output_.S3ReplicationOutput.from_dictionary(val)

        val = dictionary['size_bytes']
        val_size_bytes = val

        val = dictionary['tags']

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_model_.AwsTagModel.from_dictionary(value))

        val = dictionary['versioning_setting']
        val_versioning_setting = s3_versioning_output_.S3VersioningOutput.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_account_native_id,  # type: ignore
            val_aws_region,  # type: ignore
            val_bucket_size_bytes_breakdown,  # type: ignore
            val_cloudwatch_metrics,  # type: ignore
            val_creation_timestamp,  # type: ignore
            val_encryption_setting,  # type: ignore
            val_environment_id,  # type: ignore
            val_event_bridge_enabled,  # type: ignore
            val_p_id,  # type: ignore
            val_is_encryption_enabled,  # type: ignore
            val_is_replication_enabled,  # type: ignore
            val_is_versioning_enabled,  # type: ignore
            val_last_backtrack_sync_timestamp,  # type: ignore
            val_last_backup_timestamp,  # type: ignore
            val_last_continuous_backup_timestamp,  # type: ignore
            val_name,  # type: ignore
            val_object_count,  # type: ignore
            val_organizational_unit_id,  # type: ignore
            val_protection_group_count,  # type: ignore
            val_replication_setting,  # type: ignore
            val_size_bytes,  # type: ignore
            val_tags,  # type: ignore
            val_versioning_setting,  # type: ignore
        )
