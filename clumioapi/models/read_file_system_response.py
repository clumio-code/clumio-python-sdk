#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import hateoas_common_links as hateoas_common_links_
import requests

T = TypeVar('T', bound='ReadFileSystemResponse')


@dataclasses.dataclass
class ReadFileSystemResponse:
    """Implementation of the 'ReadFileSystemResponse' model.

    Attributes:
        Links:
            Hateoascommonlinks are the common fields for hateoas response.

        Available:
            The amount of available memory on the filesystem in bytes. does not include
            reserved memory.

        FilesystemNativeId:
            The filesystem uuid produced by the `lsblk` linux command. if this filesystem
            was not given a uuid in the host environment, then this field has a value of
            `null`.

        Id:
            The clumio-assigned id of the filesystem.

        IndexingFailedReason:
            The reason why file indexing failed. if file indexing succeeded, then this field
            has a value of `null`. possible values include "unsupported" and "encrypted".

        IsEncrypted:
            Determines whether the file system was encrypted.

        IsIndexed:
            Determines whether the file system has been indexed.
            if `true`, file indexing completed successfully.

        MountPath:
            The location of this filesystem in the host environment. only identifies mount
            points that correspond to windows drive letters. all other mount points are
            identified by a '/'.

        NumFilesIndexed:
            The number of files (including directories) indexed in the file system.

        Size:
            The total amount of memory available to the filesystem in bytes.

        Type:
            The type of the filesystem. this field is populated with values returned from
            the lsblk command. possible values include `ntfs`, `xfs`, and `ext3`.

        Used:
            The amount of memory used by the filesystem in bytes.

    """

    Links: hateoas_common_links_.HateoasCommonLinks | None = None
    Available: int | None = None
    FilesystemNativeId: str | None = None
    Id: str | None = None
    IndexingFailedReason: str | None = None
    IsEncrypted: bool | None = None
    IsIndexed: bool | None = None
    MountPath: str | None = None
    NumFilesIndexed: int | None = None
    Size: int | None = None
    Type: str | None = None
    Used: int | None = None
    raw_response: Optional[requests.Response] = None

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
        val = dictionary.get('_links', None)
        val_links = hateoas_common_links_.HateoasCommonLinks.from_dictionary(val)

        val = dictionary.get('available', None)
        val_available = val

        val = dictionary.get('filesystem_native_id', None)
        val_filesystem_native_id = val

        val = dictionary.get('id', None)
        val_id = val

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
        val_type = val

        val = dictionary.get('used', None)
        val_used = val

        # Return an object of this model
        return cls(
            val_links,
            val_available,
            val_filesystem_native_id,
            val_id,
            val_indexing_failed_reason,
            val_is_encrypted,
            val_is_indexed,
            val_mount_path,
            val_num_files_indexed,
            val_size,
            val_type,
            val_used,
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
