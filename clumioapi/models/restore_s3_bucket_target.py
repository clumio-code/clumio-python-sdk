#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model as aws_tag_common_model_

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
    _names: dict[str, str] = {
        'bucket_name': 'bucket_name',
        'environment_id': 'environment_id',
        'prefix': 'prefix',
        'storage_class': 'storage_class',
        'tags': 'tags',
    }

    def __init__(
        self,
        bucket_name: str | None = None,
        environment_id: str | None = None,
        prefix: str | None = None,
        storage_class: str | None = None,
        tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None,
    ) -> None:
        """Constructor for the RestoreS3BucketTarget class."""

        # Initialize members of the class
        self.bucket_name: str | None = bucket_name
        self.environment_id: str | None = environment_id
        self.prefix: str | None = prefix
        self.storage_class: str | None = storage_class
        self.tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = tags

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
        val = dictionary.get('bucket_name', None)
        val_bucket_name = val

        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('prefix', None)
        val_prefix = val

        val = dictionary.get('storage_class', None)
        val_storage_class = val

        val = dictionary.get('tags', None)

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_bucket_name,
            val_environment_id,
            val_prefix,
            val_storage_class,
            val_tags,
        )
