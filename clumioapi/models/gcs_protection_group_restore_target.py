#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import gcp_label_model as gcp_label_model_
import requests

T = TypeVar('T', bound='GCSProtectionGroupRestoreTarget')


@dataclasses.dataclass
class GCSProtectionGroupRestoreTarget:
    """Implementation of the 'GCSProtectionGroupRestoreTarget' model.

    The destination where the GCS protection group will be restored.

    Attributes:
        BucketId:
            The clumio-assigned id of the bucket to which the backup must be restored.
            use the [get /datasources/gcp/cloud-storage-buckets](#operation/list-gcp-cloud-
            storage-buckets) endpoint
            to fetch valid values.

        DefaultObjectChecksumAlgorithm:
            `crc32c`, `md5`.
            note that this will be applied when backup didn't have checksum algorithm
            information.

        Labels:
            The gcp labels to be applied to the restored objects.
            the restored objects will not have any labels applied if this is specified as
            `null`.

        Overwrite:
            If overwrite is set to true, we will overwrite an object if it exists. if it's
            set to false,
            then we will fail the restore if an object already exists.

        Prefix:
            Prefix to restore the objects under. if more than one bucket is restored, the
            bucket name will be appended to the prefix.

        ProjectId:
            The clumio-assigned id of the gcp project to be used as the restore destination.
            use the [get /datasources/gcp/cloud-storage-
            buckets/{bucket_id}](#operation/read-gcp-cloud-storage-bucket) endpoint
            to fetch the project id for a bucket.

        RestoreOriginalStorageClass:
            Whether to restore objects with their original storage class or not.
            if it is `true`, `storage_class` must be empty.
            otherwise, `storage_class` must be given.

        StorageClass:
            `standard`, `nearline`,
            `coldline`, `archive`.
            note that this must be given unless `restore_original_storage_class` is `true`.

    """

    BucketId: str | None = None
    DefaultObjectChecksumAlgorithm: str | None = None
    Labels: Sequence[gcp_label_model_.GcpLabelModel] | None = None
    Overwrite: bool | None = None
    Prefix: str | None = None
    ProjectId: str | None = None
    RestoreOriginalStorageClass: bool | None = None
    StorageClass: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return api_helper.to_dictionary(self)

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
        val = dictionary.get('bucket_id', None)
        val_bucket_id = val

        val = dictionary.get('default_object_checksum_algorithm', None)
        val_default_object_checksum_algorithm = val

        val = dictionary.get('labels', None)

        val_labels = []
        if val:
            for value in val:
                val_labels.append(gcp_label_model_.GcpLabelModel.from_dictionary(value))

        val = dictionary.get('overwrite', None)
        val_overwrite = val

        val = dictionary.get('prefix', None)
        val_prefix = val

        val = dictionary.get('project_id', None)
        val_project_id = val

        val = dictionary.get('restore_original_storage_class', None)
        val_restore_original_storage_class = val

        val = dictionary.get('storage_class', None)
        val_storage_class = val

        # Return an object of this model
        return cls(
            val_bucket_id,
            val_default_object_checksum_algorithm,
            val_labels,
            val_overwrite,
            val_prefix,
            val_project_id,
            val_restore_original_storage_class,
            val_storage_class,
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
