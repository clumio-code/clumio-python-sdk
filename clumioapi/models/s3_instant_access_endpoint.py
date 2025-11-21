#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    s3_instant_access_endpoint_embedded as s3_instant_access_endpoint_embedded_
from clumioapi.models import s3_instant_access_endpoint_links as s3_instant_access_endpoint_links_
import requests

T = TypeVar('T', bound='S3InstantAccessEndpoint')


@dataclasses.dataclass
class S3InstantAccessEndpoint:
    """Implementation of the 'S3InstantAccessEndpoint' model.

    S3InstantAccessEndpoint

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        AwsAccountId:
            The aws-assigned id of the account associated with the s3 instant access
            endpoint.

        BackupRegion:
            The aws region of the s3 instant access endpoint and its source backup.

        BucketName:
            The name of source bucket.

        CreatedTimestamp:
            The time that this endpoint was created, in rfc-3339 format.

        EndpointStatus:
            The status of the s3 instant access endpoint. possible values include
            "preparing",
            "active", "expiring", and "expired".

        ExpiryTimestamp:
            The time that this endpoint expires, in rfc-3339 format.

        Id:
            The clumio-assigned id of the s3 instant access endpoint.

        Name:
            The user-assigned name of the s3 instant access endpoint.

        ObjectsCreatedAfter:
            The time in rfc-3339 format that the restored objects are backed up from.

        ObjectsCreatedBefore:
            The time in rfc-3339 format that the restored objects are backed up to.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the s3 instant
            access endpoint.

        ProtectionGroupId:
            The clumio-assigned id of the protection group this endpoint is created for.

        ProtectionGroupName:
            The user-assigned name of the protection group this endpoints is created for.

        ProtectionGroupS3AssetId:
            The clumio-assigned id of the bucket protection group.

        Region:
            The aws region of the source bucket.

        RestoreTimestamp:
            The time at which the backup was restored from this endpoint in rfc-3339 format.
            deprecated.

        UpdatedTimestamp:
            The time that this endpoint was last updated, in rfc-3339 format.

    """

    Embedded: s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded | None = None
    Links: s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks | None = None
    AwsAccountId: str | None = None
    BackupRegion: str | None = None
    BucketName: str | None = None
    CreatedTimestamp: str | None = None
    EndpointStatus: str | None = None
    ExpiryTimestamp: str | None = None
    Id: str | None = None
    Name: str | None = None
    ObjectsCreatedAfter: str | None = None
    ObjectsCreatedBefore: str | None = None
    OrganizationalUnitId: str | None = None
    ProtectionGroupId: str | None = None
    ProtectionGroupName: str | None = None
    ProtectionGroupS3AssetId: str | None = None
    Region: str | None = None
    RestoreTimestamp: str | None = None
    UpdatedTimestamp: str | None = None

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
        val_embedded = (
            s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded.from_dictionary(
                val
            )
        )

        val = dictionary.get('_links', None)
        val_links = s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks.from_dictionary(
            val
        )

        val = dictionary.get('aws_account_id', None)
        val_aws_account_id = val

        val = dictionary.get('backup_region', None)
        val_backup_region = val

        val = dictionary.get('bucket_name', None)
        val_bucket_name = val

        val = dictionary.get('created_timestamp', None)
        val_created_timestamp = val

        val = dictionary.get('endpoint_status', None)
        val_endpoint_status = val

        val = dictionary.get('expiry_timestamp', None)
        val_expiry_timestamp = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('objects_created_after', None)
        val_objects_created_after = val

        val = dictionary.get('objects_created_before', None)
        val_objects_created_before = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('protection_group_id', None)
        val_protection_group_id = val

        val = dictionary.get('protection_group_name', None)
        val_protection_group_name = val

        val = dictionary.get('protection_group_s3_asset_id', None)
        val_protection_group_s3_asset_id = val

        val = dictionary.get('region', None)
        val_region = val

        val = dictionary.get('restore_timestamp', None)
        val_restore_timestamp = val

        val = dictionary.get('updated_timestamp', None)
        val_updated_timestamp = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_aws_account_id,
            val_backup_region,
            val_bucket_name,
            val_created_timestamp,
            val_endpoint_status,
            val_expiry_timestamp,
            val_id,
            val_name,
            val_objects_created_after,
            val_objects_created_before,
            val_organizational_unit_id,
            val_protection_group_id,
            val_protection_group_name,
            val_protection_group_s3_asset_id,
            val_region,
            val_restore_timestamp,
            val_updated_timestamp,
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
