#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import file_version_hateoas as file_version_hateoas_
import requests

T = TypeVar('T', bound='FileVersion')


@dataclasses.dataclass
class FileVersion:
    """Implementation of the 'FileVersion' model.

    Attributes:
        Links:
            Urls to pages related to the resource.

        BackupId:
            The clumio-assigned id of the backup.

        FilesystemId:
            The clumio-assigned id of the filesystem within which to restore the file. use
            [ get /backups/files/search/{search_result_id}/versions](#operation/list-file-
            versions)
            to fetch the value.

        ModifiedTimestamp:
            The timestamp of the last time the file was modified. represented in rfc-3339
            format.

        Path:
            The path of the file to be restored. use
            [get /backups/files/search](#operation/list-files) to fetch the value.

        Size:
            The size of the file in bytes.

        StartTimestamp:
            The timestamp of when the backup associated with this file started. represented
            in rfc-3339 format.

    """

    Links: file_version_hateoas_.FileVersionHateoas | None = None
    BackupId: str | None = None
    FilesystemId: str | None = None
    ModifiedTimestamp: str | None = None
    Path: str | None = None
    Size: int | None = None
    StartTimestamp: str | None = None

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
        val_links = file_version_hateoas_.FileVersionHateoas.from_dictionary(val)

        val = dictionary.get('backup_id', None)
        val_backup_id = val

        val = dictionary.get('filesystem_id', None)
        val_filesystem_id = val

        val = dictionary.get('modified_timestamp', None)
        val_modified_timestamp = val

        val = dictionary.get('path', None)
        val_path = val

        val = dictionary.get('size', None)
        val_size = val

        val = dictionary.get('start_timestamp', None)
        val_start_timestamp = val

        # Return an object of this model
        return cls(
            val_links,
            val_backup_id,
            val_filesystem_id,
            val_modified_timestamp,
            val_path,
            val_size,
            val_start_timestamp,
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
