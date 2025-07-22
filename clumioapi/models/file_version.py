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
        links: file_version_hateoas_.FileVersionHateoas,
        backup_id: str,
        filesystem_id: str,
        modified_timestamp: str,
        path: str,
        size: int,
        start_timestamp: str,
    ) -> None:
        """Constructor for the FileVersion class."""

        # Initialize members of the class
        self.links: file_version_hateoas_.FileVersionHateoas = links
        self.backup_id: str = backup_id
        self.filesystem_id: str = filesystem_id
        self.modified_timestamp: str = modified_timestamp
        self.path: str = path
        self.size: int = size
        self.start_timestamp: str = start_timestamp

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
        val_links = file_version_hateoas_.FileVersionHateoas.from_dictionary(val)

        val = dictionary['backup_id']
        val_backup_id = val

        val = dictionary['filesystem_id']
        val_filesystem_id = val

        val = dictionary['modified_timestamp']
        val_modified_timestamp = val

        val = dictionary['path']
        val_path = val

        val = dictionary['size']
        val_size = val

        val = dictionary['start_timestamp']
        val_start_timestamp = val

        # Return an object of this model
        return cls(
            val_links,  # type: ignore
            val_backup_id,  # type: ignore
            val_filesystem_id,  # type: ignore
            val_modified_timestamp,  # type: ignore
            val_path,  # type: ignore
            val_size,  # type: ignore
            val_start_timestamp,  # type: ignore
        )
