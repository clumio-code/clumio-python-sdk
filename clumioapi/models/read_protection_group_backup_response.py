#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import protection_group_backup_links as protection_group_backup_links_
import requests

T = TypeVar('T', bound='ReadProtectionGroupBackupResponse')


@dataclasses.dataclass
class ReadProtectionGroupBackupResponse:
    """Implementation of the 'ReadProtectionGroupBackupResponse' model.

        Attributes:
            Links:
                Urls to pages related to the resource.

            BackedUpObjectCount:
                The number of objects in the protection group that were successfully backed up.

            BackedUpSizeBytes:
                The total size in bytes of objects in the protection group that were
    successfully backed up.

            ExpirationTimestamp:
                The timestamp of when this backup expires. represented in rfc-3339 format.

            FailedObjectCount:
                The number of objects in the protection group that failed to be backed up.

            FailedSizeBytes:
                The total size in bytes of objects in the protection group that failed
    to be backed up.

            Id:
                The clumio-assigned id of the protection group backup.

            ProtectionGroupId:
                The clumio-assigned id of the protection group.

            ProtectionGroupName:
                The user-assigned name of the protection group.

            ProtectionGroupVersion:
                The version of the protection group at the time the backup was taken.

            StartTimestamp:
                The timestamp of when this backup started. represented in rfc-3339 format.

            Type:
                The type of backup. possible values include `protection_group_backup`.

    """

    Links: protection_group_backup_links_.ProtectionGroupBackupLinks | None = None
    BackedUpObjectCount: int | None = None
    BackedUpSizeBytes: int | None = None
    ExpirationTimestamp: str | None = None
    FailedObjectCount: int | None = None
    FailedSizeBytes: int | None = None
    Id: str | None = None
    ProtectionGroupId: str | None = None
    ProtectionGroupName: str | None = None
    ProtectionGroupVersion: int | None = None
    StartTimestamp: str | None = None
    Type: str | None = None
    raw_response: Optional[requests.Response] = None

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
        val = dictionary.get('_links', None)
        val_links = protection_group_backup_links_.ProtectionGroupBackupLinks.from_dictionary(val)

        val = dictionary.get('backed_up_object_count', None)
        val_backed_up_object_count = val

        val = dictionary.get('backed_up_size_bytes', None)
        val_backed_up_size_bytes = val

        val = dictionary.get('expiration_timestamp', None)
        val_expiration_timestamp = val

        val = dictionary.get('failed_object_count', None)
        val_failed_object_count = val

        val = dictionary.get('failed_size_bytes', None)
        val_failed_size_bytes = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('protection_group_id', None)
        val_protection_group_id = val

        val = dictionary.get('protection_group_name', None)
        val_protection_group_name = val

        val = dictionary.get('protection_group_version', None)
        val_protection_group_version = val

        val = dictionary.get('start_timestamp', None)
        val_start_timestamp = val

        val = dictionary.get('type', None)
        val_type = val

        # Return an object of this model
        return cls(
            val_links,
            val_backed_up_object_count,
            val_backed_up_size_bytes,
            val_expiration_timestamp,
            val_failed_object_count,
            val_failed_size_bytes,
            val_id,
            val_protection_group_id,
            val_protection_group_name,
            val_protection_group_version,
            val_start_timestamp,
            val_type,
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
