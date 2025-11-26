#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import aws_tag_model as aws_tag_model_
from clumioapi.models import bucket_links as bucket_links_
from clumioapi.models import \
    s3_buckets_inventory_summary_bucket_size_breakdown as \
    s3_buckets_inventory_summary_bucket_size_breakdown_
from clumioapi.models import s3_cloudwatch_metrics as s3_cloudwatch_metrics_
from clumioapi.models import s3_encryption_output as s3_encryption_output_
from clumioapi.models import s3_replication_output as s3_replication_output_
from clumioapi.models import s3_versioning_output as s3_versioning_output_
import requests

T = TypeVar('T', bound='Bucket')


@dataclasses.dataclass
class Bucket:
    """Implementation of the 'Bucket' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        AccountNativeId:
            The aws-assigned id of the account associated with the s3 bucket.

        AwsRegion:
            The aws region associated with the s3 bucket.

        BucketSizeBytesBreakdown:
            The total size breakdown of s3 buckets in bytes per storage class. this
            parameter aggregates relevant fields from cloudwatch_metrics >
            size_bytes_per_storage_class.

        CloudwatchMetrics:
            The cloudwatch metrics of the bucket.

        CreationTimestamp:
            The timestamp of when the bucket was created. represented in rfc-3339 format.

        EncryptionSetting:
            The aws encryption output of the bucket.

        EnvironmentId:
            The clumio-assigned id of the aws environment associated with the s3 bucket.

        Id:
            The clumio-assigned id of the bucket.

        IsEncryptionEnabled:
            The encryption enablement state for the s3 bucket.

        IsReplicationEnabled:
            The replication enablement state for the s3 bucket.

        IsVersioningEnabled:
            The versioning enablement state for the s3 bucket.

        LastBacktrackSyncTimestamp:
            Time of the last s3 backtrack sync in rfc-3339 format.

        LastBackupTimestamp:
            Time of the last backup in rfc-3339 format.

        LastContinuousBackupTimestamp:
            Time of the last continuous backup in rfc-3339 format.

        Name:
            The aws-assigned name of the bucket.

        ObjectCount:
            Number of objects in bucket.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the s3 bucket.

        ProtectionGroupCount:
            Protection group count reflects how many protection groups are linked to this
            bucket.

        ReplicationSetting:
            The aws replication output of the bucket.

        SizeBytes:
            Size of bucket in bytes.

        Tags:
            The aws tags applied to the s3 bucket.

        VersioningSetting:
            The aws versioning output of the bucket.

    """

    Embedded: object | None = None
    Links: bucket_links_.BucketLinks | None = None
    AccountNativeId: str | None = None
    AwsRegion: str | None = None
    BucketSizeBytesBreakdown: (
        s3_buckets_inventory_summary_bucket_size_breakdown_.S3BucketsInventorySummaryBucketSizeBreakdown
        | None
    ) = None
    CloudwatchMetrics: s3_cloudwatch_metrics_.S3CloudwatchMetrics | None = None
    CreationTimestamp: str | None = None
    EncryptionSetting: s3_encryption_output_.S3EncryptionOutput | None = None
    EnvironmentId: str | None = None
    Id: str | None = None
    IsEncryptionEnabled: bool | None = None
    IsReplicationEnabled: bool | None = None
    IsVersioningEnabled: bool | None = None
    LastBacktrackSyncTimestamp: str | None = None
    LastBackupTimestamp: str | None = None
    LastContinuousBackupTimestamp: str | None = None
    Name: str | None = None
    ObjectCount: int | None = None
    OrganizationalUnitId: str | None = None
    ProtectionGroupCount: int | None = None
    ReplicationSetting: s3_replication_output_.S3ReplicationOutput | None = None
    SizeBytes: int | None = None
    Tags: Sequence[aws_tag_model_.AwsTagModel] | None = None
    VersioningSetting: s3_versioning_output_.S3VersioningOutput | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('_embedded', None)
        val_embedded = val

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

        val = dictionary.get('id', None)
        val_id = val

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

        val_tags = []
        if val:
            for value in val:
                val_tags.append(aws_tag_model_.AwsTagModel.from_dictionary(value))

        val = dictionary.get('versioning_setting', None)
        val_versioning_setting = s3_versioning_output_.S3VersioningOutput.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_account_native_id,
            val_aws_region,
            val_bucket_size_bytes_breakdown,
            val_cloudwatch_metrics,
            val_creation_timestamp,
            val_encryption_setting,
            val_environment_id,
            val_id,
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
        return model_instance
