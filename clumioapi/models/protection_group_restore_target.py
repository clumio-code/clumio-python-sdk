#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model as aws_tag_common_model_

T = TypeVar('T', bound='ProtectionGroupRestoreTarget')


class ProtectionGroupRestoreTarget:
    """Implementation of the 'ProtectionGroupRestoreTarget' model.

    The destination where the protection group will be restored.

    Attributes:
        bucket_id:
            The Clumio-assigned ID of the bucket to which the backup must be restored.
            Use the [GET /datasources/aws/s3-buckets](#operation/list-aws-s3-buckets)
            endpoint
            to fetch valid values.
        environment_id:
            The Clumio-assigned ID of the AWS environment to be used as the restore
            destination.
            Use the [GET /datasources/aws/s3-buckets/{bucket_id}](#operation/read-
            aws-s3-bucket) endpoint
            to fetch the environment ID for a bucket.
        overwrite:
            If overwrite is set to true, we will overwrite an object if it exists. If it's
            set to false,
            then we will fail the restore if an object already exists.
        prefix:
            Prefix to restore the objects under. If more than one bucket is restored, the
            bucket name will be appended to the prefix.
        restore_original_storage_class:
            Whether to restore objects with their original storage class or not.
            If it is `true`, `storage_class` must be empty.
            Otherwise, `storage_class` must be given.
        storage_class:
            Storage class for restored objects. Valid values are: `S3 Standard`, `S3
            Standard-IA`,
            `S3 Intelligent-Tiering` and `S3 One Zone-IA`.
            Note that this must be given unless `restore_original_storage_class` is `true`.
        tags:
            The AWS tags to be applied to the restored objects.
            The restored objects will not have any tags applied if this is specified as
            `null`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'bucket_id': 'bucket_id',
        'environment_id': 'environment_id',
        'overwrite': 'overwrite',
        'prefix': 'prefix',
        'restore_original_storage_class': 'restore_original_storage_class',
        'storage_class': 'storage_class',
        'tags': 'tags',
    }

    def __init__(
        self,
        bucket_id: str | None = None,
        environment_id: str | None = None,
        overwrite: bool | None = None,
        prefix: str | None = None,
        restore_original_storage_class: bool | None = None,
        storage_class: str | None = None,
        tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None,
    ) -> None:
        """Constructor for the ProtectionGroupRestoreTarget class."""

        # Initialize members of the class
        self.bucket_id: str | None = bucket_id
        self.environment_id: str | None = environment_id
        self.overwrite: bool | None = overwrite
        self.prefix: str | None = prefix
        self.restore_original_storage_class: bool | None = restore_original_storage_class
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
        val = dictionary.get('bucket_id', None)
        val_bucket_id = val

        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('overwrite', None)
        val_overwrite = val

        val = dictionary.get('prefix', None)
        val_prefix = val

        val = dictionary.get('restore_original_storage_class', None)
        val_restore_original_storage_class = val

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
            val_bucket_id,
            val_environment_id,
            val_overwrite,
            val_prefix,
            val_restore_original_storage_class,
            val_storage_class,
            val_tags,
        )
