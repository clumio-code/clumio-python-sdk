#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_common_links as hateoas_common_links_

T = TypeVar('T', bound='FileSystem')


class FileSystem:
    """Implementation of the 'FileSystem' model.

    Attributes:
        links:
            HateoasCommonLinks are the common fields for HATEOAS response.
        available:
            The amount of available memory on the filesystem in bytes. Does not include
            reserved memory.
        filesystem_native_id:
            The filesystem UUID produced by the `lsblk` linux command. If this filesystem
            was not given a UUID in the host environment, then this field has a value of
            `null`.
        p_id:
            The Clumio-assigned ID of the filesystem.
        indexing_failed_reason:
            The reason why file indexing failed. If file indexing succeeded, then this field
            has a value of `null`. Possible values include "unsupported" and "encrypted".
        is_encrypted:
            Determines whether the file system was encrypted.
        is_indexed:
            Determines whether the file system has been indexed.
            If `true`, file indexing completed successfully.
        mount_path:
            The location of this filesystem in the host environment. Only identifies mount
            points that correspond to Windows drive letters. All other mount points are
            identified by a '/'.
        num_files_indexed:
            The number of files (including directories) indexed in the file system.
        size:
            The total amount of memory available to the filesystem in bytes.
        p_type:
            The type of the filesystem. This field is populated with values returned from
            the lsblk command. Possible values include `ntfs`, `xfs`, and `ext3`.
        used:
            The amount of memory used by the filesystem in bytes.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'links': '_links',
        'available': 'available',
        'filesystem_native_id': 'filesystem_native_id',
        'p_id': 'id',
        'indexing_failed_reason': 'indexing_failed_reason',
        'is_encrypted': 'is_encrypted',
        'is_indexed': 'is_indexed',
        'mount_path': 'mount_path',
        'num_files_indexed': 'num_files_indexed',
        'size': 'size',
        'p_type': 'type',
        'used': 'used',
    }

    def __init__(
        self,
        links: hateoas_common_links_.HateoasCommonLinks | None = None,
        available: int | None = None,
        filesystem_native_id: str | None = None,
        p_id: str | None = None,
        indexing_failed_reason: str | None = None,
        is_encrypted: bool | None = None,
        is_indexed: bool | None = None,
        mount_path: str | None = None,
        num_files_indexed: int | None = None,
        size: int | None = None,
        p_type: str | None = None,
        used: int | None = None,
    ) -> None:
        """Constructor for the FileSystem class."""

        # Initialize members of the class
        self.links: hateoas_common_links_.HateoasCommonLinks | None = links
        self.available: int | None = available
        self.filesystem_native_id: str | None = filesystem_native_id
        self.p_id: str | None = p_id
        self.indexing_failed_reason: str | None = indexing_failed_reason
        self.is_encrypted: bool | None = is_encrypted
        self.is_indexed: bool | None = is_indexed
        self.mount_path: str | None = mount_path
        self.num_files_indexed: int | None = num_files_indexed
        self.size: int | None = size
        self.p_type: str | None = p_type
        self.used: int | None = used

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
        val = dictionary.get('_links', None)
        val_links = hateoas_common_links_.HateoasCommonLinks.from_dictionary(val)

        val = dictionary.get('available', None)
        val_available = val

        val = dictionary.get('filesystem_native_id', None)
        val_filesystem_native_id = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('indexing_failed_reason', None)
        val_indexing_failed_reason = val

        val = dictionary.get('is_encrypted', None)
        val_is_encrypted = val

        val = dictionary.get('is_indexed', None)
        val_is_indexed = val

        val = dictionary.get('mount_path', None)
        val_mount_path = val

        val = dictionary.get('num_files_indexed', None)
        val_num_files_indexed = val

        val = dictionary.get('size', None)
        val_size = val

        val = dictionary.get('type', None)
        val_p_type = val

        val = dictionary.get('used', None)
        val_used = val

        # Return an object of this model
        return cls(
            val_links,
            val_available,
            val_filesystem_native_id,
            val_p_id,
            val_indexing_failed_reason,
            val_is_encrypted,
            val_is_indexed,
            val_mount_path,
            val_num_files_indexed,
            val_size,
            val_p_type,
            val_used,
        )
