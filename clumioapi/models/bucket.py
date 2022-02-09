#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_model
from clumioapi.models import bucket_links
from clumioapi.models import s3_cloudwatch_metrics

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
        cloudwatch_metrics:
            The Cloudwatch metrics of the bucket.
        creation_timestamp:
            The timestamp of when the bucket was created. Represented in RFC-3339 format.
        encryption_configuration:
            Encryption configuration of the bucket
        environment_id:
            The Clumio-assigned ID of the AWS environment associated with the S3 bucket.
        id:
            The Clumio-assigned ID of the bucket.
        name:
            The AWS-assigned name of the bucket.
        object_count:
            Number of objects in bucket.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the S3 bucket.
        protection_group_count:
            Protection group count reflects how many protection groups are linked to this
            bucket
        replication_configuration:
            Replication configuration of the bucket
        size_bytes:
            Size of bucket in bytes.
        tags:
            The AWS tags applied to the S3 bucket.
        version_configuration:
            Version configuration of the bucket
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'account_native_id': 'account_native_id',
        'aws_region': 'aws_region',
        'cloudwatch_metrics': 'cloudwatch_metrics',
        'creation_timestamp': 'creation_timestamp',
        'encryption_configuration': 'encryption_configuration',
        'environment_id': 'environment_id',
        'id': 'id',
        'name': 'name',
        'object_count': 'object_count',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_group_count': 'protection_group_count',
        'replication_configuration': 'replication_configuration',
        'size_bytes': 'size_bytes',
        'tags': 'tags',
        'version_configuration': 'version_configuration',
    }

    def __init__(
        self,
        embedded: object = None,
        links: bucket_links.BucketLinks = None,
        account_native_id: str = None,
        aws_region: str = None,
        cloudwatch_metrics: s3_cloudwatch_metrics.S3CloudwatchMetrics = None,
        creation_timestamp: str = None,
        encryption_configuration: str = None,
        environment_id: str = None,
        id: str = None,
        name: str = None,
        object_count: int = None,
        organizational_unit_id: str = None,
        protection_group_count: int = None,
        replication_configuration: str = None,
        size_bytes: int = None,
        tags: Sequence[aws_tag_model.AwsTagModel] = None,
        version_configuration: str = None,
    ) -> None:
        """Constructor for the Bucket class."""

        # Initialize members of the class
        self.embedded: object = embedded
        self.links: bucket_links.BucketLinks = links
        self.account_native_id: str = account_native_id
        self.aws_region: str = aws_region
        self.cloudwatch_metrics: s3_cloudwatch_metrics.S3CloudwatchMetrics = cloudwatch_metrics
        self.creation_timestamp: str = creation_timestamp
        self.encryption_configuration: str = encryption_configuration
        self.environment_id: str = environment_id
        self.id: str = id
        self.name: str = name
        self.object_count: int = object_count
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_group_count: int = protection_group_count
        self.replication_configuration: str = replication_configuration
        self.size_bytes: int = size_bytes
        self.tags: Sequence[aws_tag_model.AwsTagModel] = tags
        self.version_configuration: str = version_configuration

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
        key = 'cloudwatch_metrics'
        cloudwatch_metrics = (
            s3_cloudwatch_metrics.S3CloudwatchMetrics.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        creation_timestamp = dictionary.get('creation_timestamp')
        encryption_configuration = dictionary.get('encryption_configuration')
        environment_id = dictionary.get('environment_id')
        id = dictionary.get('id')
        name = dictionary.get('name')
        object_count = dictionary.get('object_count')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        protection_group_count = dictionary.get('protection_group_count')
        replication_configuration = dictionary.get('replication_configuration')
        size_bytes = dictionary.get('size_bytes')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(aws_tag_model.AwsTagModel.from_dictionary(value))

        version_configuration = dictionary.get('version_configuration')
        # Return an object of this model
        return cls(
            embedded,
            links,
            account_native_id,
            aws_region,
            cloudwatch_metrics,
            creation_timestamp,
            encryption_configuration,
            environment_id,
            id,
            name,
            object_count,
            organizational_unit_id,
            protection_group_count,
            replication_configuration,
            size_bytes,
            tags,
            version_configuration,
        )
