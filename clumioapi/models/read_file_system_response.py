#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_common_links

T = TypeVar('T', bound='ReadFileSystemResponse')


class ReadFileSystemResponse:
    """Implementation of the 'ReadFileSystemResponse' model.

    Attributes:
        links:

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
    _names = {
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
        links: hateoas_common_links.HateoasCommonLinks = None,
        available: int = None,
        filesystem_native_id: str = None,
        p_id: str = None,
        indexing_failed_reason: str = None,
        is_encrypted: bool = None,
        is_indexed: bool = None,
        mount_path: str = None,
        num_files_indexed: int = None,
        size: int = None,
        p_type: str = None,
        used: int = None,
    ) -> None:
        """Constructor for the ReadFileSystemResponse class."""

        # Initialize members of the class
        self.links: hateoas_common_links.HateoasCommonLinks = links
        self.available: int = available
        self.filesystem_native_id: str = filesystem_native_id
        self.p_id: str = p_id
        self.indexing_failed_reason: str = indexing_failed_reason
        self.is_encrypted: bool = is_encrypted
        self.is_indexed: bool = is_indexed
        self.mount_path: str = mount_path
        self.num_files_indexed: int = num_files_indexed
        self.size: int = size
        self.p_type: str = p_type
        self.used: int = used

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
        key = '_links'
        links = (
            hateoas_common_links.HateoasCommonLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        available = dictionary.get('available')
        filesystem_native_id = dictionary.get('filesystem_native_id')
        p_id = dictionary.get('id')
        indexing_failed_reason = dictionary.get('indexing_failed_reason')
        is_encrypted = dictionary.get('is_encrypted')
        is_indexed = dictionary.get('is_indexed')
        mount_path = dictionary.get('mount_path')
        num_files_indexed = dictionary.get('num_files_indexed')
        size = dictionary.get('size')
        p_type = dictionary.get('type')
        used = dictionary.get('used')
        # Return an object of this model
        return cls(
            links,
            available,
            filesystem_native_id,
            p_id,
            indexing_failed_reason,
            is_encrypted,
            is_indexed,
            mount_path,
            num_files_indexed,
            size,
            p_type,
            used,
        )
