#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import file_version_hateoas

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
    _names = {
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
        links: file_version_hateoas.FileVersionHateoas = None,
        backup_id: str = None,
        filesystem_id: str = None,
        modified_timestamp: str = None,
        path: str = None,
        size: int = None,
        start_timestamp: str = None,
    ) -> None:
        """Constructor for the FileVersion class."""

        # Initialize members of the class
        self.links: file_version_hateoas.FileVersionHateoas = links
        self.backup_id: str = backup_id
        self.filesystem_id: str = filesystem_id
        self.modified_timestamp: str = modified_timestamp
        self.path: str = path
        self.size: int = size
        self.start_timestamp: str = start_timestamp

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
            file_version_hateoas.FileVersionHateoas.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        backup_id = dictionary.get('backup_id')
        filesystem_id = dictionary.get('filesystem_id')
        modified_timestamp = dictionary.get('modified_timestamp')
        path = dictionary.get('path')
        size = dictionary.get('size')
        start_timestamp = dictionary.get('start_timestamp')
        # Return an object of this model
        return cls(links, backup_id, filesystem_id, modified_timestamp, path, size, start_timestamp)
