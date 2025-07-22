#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import protection_group_backup_links as protection_group_backup_links_

T = TypeVar('T', bound='ProtectionGroupBackup')


class ProtectionGroupBackup:
    """Implementation of the 'ProtectionGroupBackup' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        backed_up_object_count:
            The number of objects in the protection group that were successfully backed up.
        backed_up_size_bytes:
            The total size in bytes of objects in the protection group that were
            successfully backed up.
        expiration_timestamp:
            The timestamp of when this backup expires. Represented in RFC-3339 format.
        failed_object_count:
            The number of objects in the protection group that failed to be backed up.
        failed_size_bytes:
            The total size in bytes of objects in the protection group that failed
            to be backed up.
        p_id:
            The Clumio-assigned ID of the protection group backup.
        protection_group_id:
            The Clumio-assigned ID of the protection group.
        protection_group_name:
            The user-assigned name of the protection group.
        protection_group_version:
            The version of the protection group at the time the backup was taken.
        start_timestamp:
            The timestamp of when this backup started. Represented in RFC-3339 format.
        p_type:
            The type of backup. Possible values include `protection_group_backup`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'links': '_links',
        'backed_up_object_count': 'backed_up_object_count',
        'backed_up_size_bytes': 'backed_up_size_bytes',
        'expiration_timestamp': 'expiration_timestamp',
        'failed_object_count': 'failed_object_count',
        'failed_size_bytes': 'failed_size_bytes',
        'p_id': 'id',
        'protection_group_id': 'protection_group_id',
        'protection_group_name': 'protection_group_name',
        'protection_group_version': 'protection_group_version',
        'start_timestamp': 'start_timestamp',
        'p_type': 'type',
    }

    def __init__(
        self,
        links: protection_group_backup_links_.ProtectionGroupBackupLinks,
        backed_up_object_count: int,
        backed_up_size_bytes: int,
        expiration_timestamp: str,
        failed_object_count: int,
        failed_size_bytes: int,
        p_id: str,
        protection_group_id: str,
        protection_group_name: str,
        protection_group_version: int,
        start_timestamp: str,
        p_type: str,
    ) -> None:
        """Constructor for the ProtectionGroupBackup class."""

        # Initialize members of the class
        self.links: protection_group_backup_links_.ProtectionGroupBackupLinks = links
        self.backed_up_object_count: int = backed_up_object_count
        self.backed_up_size_bytes: int = backed_up_size_bytes
        self.expiration_timestamp: str = expiration_timestamp
        self.failed_object_count: int = failed_object_count
        self.failed_size_bytes: int = failed_size_bytes
        self.p_id: str = p_id
        self.protection_group_id: str = protection_group_id
        self.protection_group_name: str = protection_group_name
        self.protection_group_version: int = protection_group_version
        self.start_timestamp: str = start_timestamp
        self.p_type: str = p_type

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

        # Extract variables from the dictionary
        val = dictionary['_links']
        val_links = protection_group_backup_links_.ProtectionGroupBackupLinks.from_dictionary(val)

        val = dictionary['backed_up_object_count']
        val_backed_up_object_count = val

        val = dictionary['backed_up_size_bytes']
        val_backed_up_size_bytes = val

        val = dictionary['expiration_timestamp']
        val_expiration_timestamp = val

        val = dictionary['failed_object_count']
        val_failed_object_count = val

        val = dictionary['failed_size_bytes']
        val_failed_size_bytes = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['protection_group_id']
        val_protection_group_id = val

        val = dictionary['protection_group_name']
        val_protection_group_name = val

        val = dictionary['protection_group_version']
        val_protection_group_version = val

        val = dictionary['start_timestamp']
        val_start_timestamp = val

        val = dictionary['type']
        val_p_type = val

        # Return an object of this model
        return cls(
            val_links,  # type: ignore
            val_backed_up_object_count,  # type: ignore
            val_backed_up_size_bytes,  # type: ignore
            val_expiration_timestamp,  # type: ignore
            val_failed_object_count,  # type: ignore
            val_failed_size_bytes,  # type: ignore
            val_p_id,  # type: ignore
            val_protection_group_id,  # type: ignore
            val_protection_group_name,  # type: ignore
            val_protection_group_version,  # type: ignore
            val_start_timestamp,  # type: ignore
            val_p_type,  # type: ignore
        )
