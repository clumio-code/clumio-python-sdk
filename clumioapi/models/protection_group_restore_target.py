#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import aws_tag_common_model as aws_tag_common_model_
import requests

T = TypeVar('T', bound='ProtectionGroupRestoreTarget')


@dataclasses.dataclass
class ProtectionGroupRestoreTarget:
    """Implementation of the 'ProtectionGroupRestoreTarget' model.

        The destination where the protection group will be restored.

        Attributes:
            BucketId:
                The clumio-assigned id of the bucket to which the backup must be restored.
    use the [get /datasources/aws/s3-buckets](#operation/list-aws-s3-buckets) endpoint
    to fetch valid values.

            EnvironmentId:
                The clumio-assigned id of the aws environment to be used as the restore destination.
    use the [get /datasources/aws/s3-buckets/{bucket_id}](#operation/read-aws-s3-bucket) endpoint
    to fetch the environment id for a bucket.

            Overwrite:
                If overwrite is set to true, we will overwrite an object if it exists. if it's set to false,
    then we will fail the restore if an object already exists.

            Prefix:
                Prefix to restore the objects under. if more than one bucket is restored, the
    bucket name will be appended to the prefix.

            RestoreOriginalStorageClass:
                Whether to restore objects with their original storage class or not.
    if it is `true`, `storage_class` must be empty.
    otherwise, `storage_class` must be given.

            StorageClass:
                `s3 standard`, `s3 standard-ia`,
    `s3 intelligent-tiering` and `s3 one zone-ia`.
    note that this must be given unless `restore_original_storage_class` is `true`.

            Tags:
                The aws tags to be applied to the restored objects.
    the restored objects will not have any tags applied if this is specified as `null`.

    """

    BucketId: str | None = None
    EnvironmentId: str | None = None
    Overwrite: bool | None = None
    Prefix: str | None = None
    RestoreOriginalStorageClass: bool | None = None
    StorageClass: str | None = None
    Tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None

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

        val_tags = []
        if val:
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
