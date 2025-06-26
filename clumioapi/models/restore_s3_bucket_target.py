#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model

T = TypeVar('T', bound='RestoreS3BucketTarget')


class RestoreS3BucketTarget:
    """Implementation of the 'RestoreS3BucketTarget' model.

    The destination where the S3 bucket will be restored.

    Attributes:
        bucket_name:
            The name of the destination bucket.
        environment_id:
            The Clumio-assigned ID of the AWS environment to be used as the restore
            destination. Use the
            [GET /datasources/aws/s3-buckets/{bucket_id}](#operation/read-aws-s3-bucket)
            endpoint
            to fetch the environment ID for a bucket.
        prefix:
            Prefix to restore the objects under.
        storage_class:
            Storage class for restored objects. Valid values are: `S3 Standard`, `S3
            Standard-IA`,
            `S3 Intelligent-Tiering` and `S3 One Zone-IA`.
            If not given or empty, objects are restored with their original storage classes.
        tags:
            The AWS tags to be applied to the restored objects.
            The restored objects will not have any tags applied if this is specified as
            `null`.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'bucket_name': 'bucket_name',
        'environment_id': 'environment_id',
        'prefix': 'prefix',
        'storage_class': 'storage_class',
        'tags': 'tags',
    }

    def __init__(
        self,
        bucket_name: str = None,
        environment_id: str = None,
        prefix: str = None,
        storage_class: str = None,
        tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = None,
    ) -> None:
        """Constructor for the RestoreS3BucketTarget class."""

        # Initialize members of the class
        self.bucket_name: str = bucket_name
        self.environment_id: str = environment_id
        self.prefix: str = prefix
        self.storage_class: str = storage_class
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
        bucket_name = dictionary.get('bucket_name')
        environment_id = dictionary.get('environment_id')
        prefix = dictionary.get('prefix')
        storage_class = dictionary.get('storage_class')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(aws_tag_common_model.AwsTagCommonModel.from_dictionary(value))

        # Return an object of this model
        return cls(bucket_name, environment_id, prefix, storage_class, tags)
