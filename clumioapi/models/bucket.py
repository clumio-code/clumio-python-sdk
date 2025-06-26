#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_model
from clumioapi.models import bucket_links
from clumioapi.models import s3_buckets_inventory_summary_bucket_size_breakdown
from clumioapi.models import s3_cloudwatch_metrics
from clumioapi.models import s3_encryption_output
from clumioapi.models import s3_replication_output
from clumioapi.models import s3_versioning_output

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
    _names = {
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
        embedded: object = None,
        links: bucket_links.BucketLinks = None,
        account_native_id: str = None,
        aws_region: str = None,
        bucket_size_bytes_breakdown: s3_buckets_inventory_summary_bucket_size_breakdown.S3BucketsInventorySummaryBucketSizeBreakdown = None,
        cloudwatch_metrics: s3_cloudwatch_metrics.S3CloudwatchMetrics = None,
        creation_timestamp: str = None,
        encryption_setting: s3_encryption_output.S3EncryptionOutput = None,
        environment_id: str = None,
        event_bridge_enabled: bool = None,
        p_id: str = None,
        is_encryption_enabled: bool = None,
        is_replication_enabled: bool = None,
        is_versioning_enabled: bool = None,
        last_backtrack_sync_timestamp: str = None,
        last_backup_timestamp: str = None,
        last_continuous_backup_timestamp: str = None,
        name: str = None,
        object_count: int = None,
        organizational_unit_id: str = None,
        protection_group_count: int = None,
        replication_setting: s3_replication_output.S3ReplicationOutput = None,
        size_bytes: int = None,
        tags: Sequence[aws_tag_model.AwsTagModel] = None,
        versioning_setting: s3_versioning_output.S3VersioningOutput = None,
    ) -> None:
        """Constructor for the Bucket class."""

        # Initialize members of the class
        self.embedded: object = embedded
        self.links: bucket_links.BucketLinks = links
        self.account_native_id: str = account_native_id
        self.aws_region: str = aws_region
        self.bucket_size_bytes_breakdown: (
            s3_buckets_inventory_summary_bucket_size_breakdown.S3BucketsInventorySummaryBucketSizeBreakdown
        ) = bucket_size_bytes_breakdown
        self.cloudwatch_metrics: s3_cloudwatch_metrics.S3CloudwatchMetrics = cloudwatch_metrics
        self.creation_timestamp: str = creation_timestamp
        self.encryption_setting: s3_encryption_output.S3EncryptionOutput = encryption_setting
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
        self.replication_setting: s3_replication_output.S3ReplicationOutput = replication_setting
        self.size_bytes: int = size_bytes
        self.tags: Sequence[aws_tag_model.AwsTagModel] = tags
        self.versioning_setting: s3_versioning_output.S3VersioningOutput = versioning_setting

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
        embedded = dictionary.get('_embedded')
        key = '_links'
        links = (
            bucket_links.BucketLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        account_native_id = dictionary.get('account_native_id')
        aws_region = dictionary.get('aws_region')
        key = 'bucket_size_bytes_breakdown'
        bucket_size_bytes_breakdown = (
            s3_buckets_inventory_summary_bucket_size_breakdown.S3BucketsInventorySummaryBucketSizeBreakdown.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'cloudwatch_metrics'
        cloudwatch_metrics = (
            s3_cloudwatch_metrics.S3CloudwatchMetrics.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        creation_timestamp = dictionary.get('creation_timestamp')
        key = 'encryption_setting'
        encryption_setting = (
            s3_encryption_output.S3EncryptionOutput.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        environment_id = dictionary.get('environment_id')
        event_bridge_enabled = dictionary.get('event_bridge_enabled')
        p_id = dictionary.get('id')
        is_encryption_enabled = dictionary.get('is_encryption_enabled')
        is_replication_enabled = dictionary.get('is_replication_enabled')
        is_versioning_enabled = dictionary.get('is_versioning_enabled')
        last_backtrack_sync_timestamp = dictionary.get('last_backtrack_sync_timestamp')
        last_backup_timestamp = dictionary.get('last_backup_timestamp')
        last_continuous_backup_timestamp = dictionary.get('last_continuous_backup_timestamp')
        name = dictionary.get('name')
        object_count = dictionary.get('object_count')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        protection_group_count = dictionary.get('protection_group_count')
        key = 'replication_setting'
        replication_setting = (
            s3_replication_output.S3ReplicationOutput.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        size_bytes = dictionary.get('size_bytes')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(aws_tag_model.AwsTagModel.from_dictionary(value))

        key = 'versioning_setting'
        versioning_setting = (
            s3_versioning_output.S3VersioningOutput.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(
            embedded,
            links,
            account_native_id,
            aws_region,
            bucket_size_bytes_breakdown,
            cloudwatch_metrics,
            creation_timestamp,
            encryption_setting,
            environment_id,
            event_bridge_enabled,
            p_id,
            is_encryption_enabled,
            is_replication_enabled,
            is_versioning_enabled,
            last_backtrack_sync_timestamp,
            last_backup_timestamp,
            last_continuous_backup_timestamp,
            name,
            object_count,
            organizational_unit_id,
            protection_group_count,
            replication_setting,
            size_bytes,
            tags,
            versioning_setting,
        )
