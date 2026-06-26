#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import gcp_label_model as gcp_label_model_
from clumioapi.models import gcs_bucket_links as gcs_bucket_links_
import requests

T = TypeVar('T', bound='ReadGCSBucketResponse')


@dataclasses.dataclass
class ReadGCSBucketResponse:
    """Implementation of the 'ReadGCSBucketResponse' model.

    Attributes:
        Embedded

        Etag

        Links

        BucketName:
            The name of the bucket.

        CreatedTimestamp:
            Creation time of the bucket in rfc-3339 format.

        Id:
            The clumio-assigned id that represents the bucket.

        IsDeleted:
            Determines whether the bucket has been deleted.

        IsVersioningEnabled:
            Determines whether versioning is enabled for the bucket.

        Labels:
            Gcp labels (key-value pairs) associated with the bucket, similar to aws tags.

        LastBackupTimestamp:
            Time of the last backup in rfc-3339 format.

        Location:
            The gcp location associated with the bucket.

        LocationType:
            The location type of the bucket (e.g., "region", "dual-region", "multi-region").

        LocationUuid:
            The clumio-assigned uuid of the gcp location associated with the bucket.

        ObjectCount:
            The number of objects in the bucket.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the bucket.

        ProjectId:
            The gcp project id associated with the bucket.

        ProjectUuid:
            The clumio-assigned uuid of the gcp project associated with the bucket.

        ProtectionGroupCount:
            The number of protection groups associated with the bucket.

        SizeBytes:
            Total size in bytes of all objects in the bucket.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Embedded': '_embedded',
        'Etag': '_etag',
        'Links': '_links',
    }

    Embedded: object | None = None
    Etag: str | None = None
    Links: gcs_bucket_links_.GCSBucketLinks | None = None
    BucketName: str | None = None
    CreatedTimestamp: str | None = None
    Id: str | None = None
    IsDeleted: bool | None = None
    IsVersioningEnabled: bool | None = None
    Labels: Sequence[gcp_label_model_.GcpLabelModel] | None = None
    LastBackupTimestamp: str | None = None
    Location: str | None = None
    LocationType: str | None = None
    LocationUuid: str | None = None
    ObjectCount: int | None = None
    OrganizationalUnitId: str | None = None
    ProjectId: str | None = None
    ProjectUuid: str | None = None
    ProtectionGroupCount: int | None = None
    SizeBytes: int | None = None
    raw_response: Optional[requests.Response] = None

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
        val = dictionary.get('_embedded', None)
        val_embedded = val

        val = dictionary.get('_etag', None)
        val_etag = val

        val = dictionary.get('_links', None)
        val_links = gcs_bucket_links_.GCSBucketLinks.from_dictionary(val)

        val = dictionary.get('bucket_name', None)
        val_bucket_name = val

        val = dictionary.get('created_timestamp', None)
        val_created_timestamp = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('is_deleted', None)
        val_is_deleted = val

        val = dictionary.get('is_versioning_enabled', None)
        val_is_versioning_enabled = val

        val = dictionary.get('labels', None)

        val_labels = []
        if val:
            for value in val:
                val_labels.append(gcp_label_model_.GcpLabelModel.from_dictionary(value))

        val = dictionary.get('last_backup_timestamp', None)
        val_last_backup_timestamp = val

        val = dictionary.get('location', None)
        val_location = val

        val = dictionary.get('location_type', None)
        val_location_type = val

        val = dictionary.get('location_uuid', None)
        val_location_uuid = val

        val = dictionary.get('object_count', None)
        val_object_count = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('project_id', None)
        val_project_id = val

        val = dictionary.get('project_uuid', None)
        val_project_uuid = val

        val = dictionary.get('protection_group_count', None)
        val_protection_group_count = val

        val = dictionary.get('size_bytes', None)
        val_size_bytes = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_etag,
            val_links,
            val_bucket_name,
            val_created_timestamp,
            val_id,
            val_is_deleted,
            val_is_versioning_enabled,
            val_labels,
            val_last_backup_timestamp,
            val_location,
            val_location_type,
            val_location_uuid,
            val_object_count,
            val_organizational_unit_id,
            val_project_id,
            val_project_uuid,
            val_protection_group_count,
            val_size_bytes,
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
        model_instance.raw_response = response
        return model_instance
