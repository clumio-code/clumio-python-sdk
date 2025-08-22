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

T = TypeVar('T', bound='ReadBucketResponse')


class ReadBucketResponse:
    """Implementation of the 'ReadBucketResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        etag:
            The ETag value.
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
        'etag': '_etag',
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
        embedded: object | None = None,
        etag: str | None = None,
        links: bucket_links_.BucketLinks | None = None,
        account_native_id: str | None = None,
        aws_region: str | None = None,
        bucket_size_bytes_breakdown: (
            s3_buckets_inventory_summary_bucket_size_breakdown_.S3BucketsInventorySummaryBucketSizeBreakdown
            | None
        ) = None,
        cloudwatch_metrics: s3_cloudwatch_metrics_.S3CloudwatchMetrics | None = None,
        creation_timestamp: str | None = None,
        encryption_setting: s3_encryption_output_.S3EncryptionOutput | None = None,
        environment_id: str | None = None,
        event_bridge_enabled: bool | None = None,
        p_id: str | None = None,
        is_encryption_enabled: bool | None = None,
        is_replication_enabled: bool | None = None,
        is_versioning_enabled: bool | None = None,
        last_backtrack_sync_timestamp: str | None = None,
        last_backup_timestamp: str | None = None,
        last_continuous_backup_timestamp: str | None = None,
        name: str | None = None,
        object_count: int | None = None,
        organizational_unit_id: str | None = None,
        protection_group_count: int | None = None,
        replication_setting: s3_replication_output_.S3ReplicationOutput | None = None,
        size_bytes: int | None = None,
        tags: Sequence[aws_tag_model_.AwsTagModel] | None = None,
        versioning_setting: s3_versioning_output_.S3VersioningOutput | None = None,
    ) -> None:
        """Constructor for the ReadBucketResponse class."""

        # Initialize members of the class
        self.embedded: object | None = embedded
        self.etag: str | None = etag
        self.links: bucket_links_.BucketLinks | None = links
        self.account_native_id: str | None = account_native_id
        self.aws_region: str | None = aws_region
        self.bucket_size_bytes_breakdown: (
            s3_buckets_inventory_summary_bucket_size_breakdown_.S3BucketsInventorySummaryBucketSizeBreakdown
            | None
        ) = bucket_size_bytes_breakdown
        self.cloudwatch_metrics: s3_cloudwatch_metrics_.S3CloudwatchMetrics | None = (
            cloudwatch_metrics
        )
        self.creation_timestamp: str | None = creation_timestamp
        self.encryption_setting: s3_encryption_output_.S3EncryptionOutput | None = (
            encryption_setting
        )
        self.environment_id: str | None = environment_id
        self.event_bridge_enabled: bool | None = event_bridge_enabled
        self.p_id: str | None = p_id
        self.is_encryption_enabled: bool | None = is_encryption_enabled
        self.is_replication_enabled: bool | None = is_replication_enabled
        self.is_versioning_enabled: bool | None = is_versioning_enabled
        self.last_backtrack_sync_timestamp: str | None = last_backtrack_sync_timestamp
        self.last_backup_timestamp: str | None = last_backup_timestamp
        self.last_continuous_backup_timestamp: str | None = last_continuous_backup_timestamp
        self.name: str | None = name
        self.object_count: int | None = object_count
        self.organizational_unit_id: str | None = organizational_unit_id
        self.protection_group_count: int | None = protection_group_count
        self.replication_setting: s3_replication_output_.S3ReplicationOutput | None = (
            replication_setting
        )
        self.size_bytes: int | None = size_bytes
        self.tags: Sequence[aws_tag_model_.AwsTagModel] | None = tags
        self.versioning_setting: s3_versioning_output_.S3VersioningOutput | None = (
            versioning_setting
        )

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
        val = dictionary.get('_embedded', None)
        val_embedded = val

        val = dictionary.get('_etag', None)
        val_etag = val

        val = dictionary.get('_links', None)
        val_links = bucket_links_.BucketLinks.from_dictionary(val)

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('bucket_size_bytes_breakdown', None)
        val_bucket_size_bytes_breakdown = s3_buckets_inventory_summary_bucket_size_breakdown_.S3BucketsInventorySummaryBucketSizeBreakdown.from_dictionary(
            val
        )

        val = dictionary.get('cloudwatch_metrics', None)
        val_cloudwatch_metrics = s3_cloudwatch_metrics_.S3CloudwatchMetrics.from_dictionary(val)

        val = dictionary.get('creation_timestamp', None)
        val_creation_timestamp = val

        val = dictionary.get('encryption_setting', None)
        val_encryption_setting = s3_encryption_output_.S3EncryptionOutput.from_dictionary(val)

        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('event_bridge_enabled', None)
        val_event_bridge_enabled = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('is_encryption_enabled', None)
        val_is_encryption_enabled = val

        val = dictionary.get('is_replication_enabled', None)
        val_is_replication_enabled = val

        val = dictionary.get('is_versioning_enabled', None)
        val_is_versioning_enabled = val

        val = dictionary.get('last_backtrack_sync_timestamp', None)
        val_last_backtrack_sync_timestamp = val

        val = dictionary.get('last_backup_timestamp', None)
        val_last_backup_timestamp = val

        val = dictionary.get('last_continuous_backup_timestamp', None)
        val_last_continuous_backup_timestamp = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('object_count', None)
        val_object_count = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('protection_group_count', None)
        val_protection_group_count = val

        val = dictionary.get('replication_setting', None)
        val_replication_setting = s3_replication_output_.S3ReplicationOutput.from_dictionary(val)

        val = dictionary.get('size_bytes', None)
        val_size_bytes = val

        val = dictionary.get('tags', None)

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_model_.AwsTagModel.from_dictionary(value))

        val = dictionary.get('versioning_setting', None)
        val_versioning_setting = s3_versioning_output_.S3VersioningOutput.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_embedded,
            val_etag,
            val_links,
            val_account_native_id,
            val_aws_region,
            val_bucket_size_bytes_breakdown,
            val_cloudwatch_metrics,
            val_creation_timestamp,
            val_encryption_setting,
            val_environment_id,
            val_event_bridge_enabled,
            val_p_id,
            val_is_encryption_enabled,
            val_is_replication_enabled,
            val_is_versioning_enabled,
            val_last_backtrack_sync_timestamp,
            val_last_backup_timestamp,
            val_last_continuous_backup_timestamp,
            val_name,
            val_object_count,
            val_organizational_unit_id,
            val_protection_group_count,
            val_replication_setting,
            val_size_bytes,
            val_tags,
            val_versioning_setting,
        )
