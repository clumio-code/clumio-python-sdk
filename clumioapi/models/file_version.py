#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import file_version_hateoas as file_version_hateoas_

T = TypeVar('T', bound='FileVersion')


class FileVersion:
    """Implementation of the 'FileVersion' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        backup_id:
            The Clumio-assigned ID of the backup.
        filesystem_id:
            The Clumio-assigned ID of the filesystem within which to restore the file. Use
            [ GET /backups/files/search/{search_result_id}/versions](#operation/list-file-
            versions)
            to fetch the value.
        modified_timestamp:
            The timestamp of the last time the file was modified. Represented in RFC-3339
            format.
        path:
            The path of the file to be restored. Use
            [GET /backups/files/search](#operation/list-files) to fetch the value.
        size:
            The size of the file in bytes.
        start_timestamp:
            The timestamp of when the backup associated with this file started. Represented
            in RFC-3339 format.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'links': '_links',
        'backup_id': 'backup_id',
        'filesystem_id': 'filesystem_id',
        'modified_timestamp': 'modified_timestamp',
        'path': 'path',
        'size': 'size',
        'start_timestamp': 'start_timestamp',
    }

    def __init__(
        self,
        links: file_version_hateoas_.FileVersionHateoas | None = None,
        backup_id: str | None = None,
        filesystem_id: str | None = None,
        modified_timestamp: str | None = None,
        path: str | None = None,
        size: int | None = None,
        start_timestamp: str | None = None,
    ) -> None:
        """Constructor for the FileVersion class."""

        # Initialize members of the class
        self.links: file_version_hateoas_.FileVersionHateoas | None = links
        self.backup_id: str | None = backup_id
        self.filesystem_id: str | None = filesystem_id
        self.modified_timestamp: str | None = modified_timestamp
        self.path: str | None = path
        self.size: int | None = size
        self.start_timestamp: str | None = start_timestamp

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
