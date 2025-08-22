#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='FileDescriptor')


class FileDescriptor:
    """Implementation of the 'FileDescriptor' model.

    Specifies a file/directory by providing path and file system.

    Attributes:
        filesystem_id:
            The Clumio-assigned ID of the filesystem within which to restore the file. Use
            [ GET /backups/files/search/{search_result_id}/versions](#operation/list-file-
            versions)
            to fetch the value.
        path:
            The path of the file to be restored. Use
            [GET /backups/files/search](#operation/list-files) to fetch the value.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'filesystem_id': 'filesystem_id', 'path': 'path'}

    def __init__(self, filesystem_id: str | None = None, path: str | None = None) -> None:
        """Constructor for the FileDescriptor class."""

        # Initialize members of the class
        self.filesystem_id: str | None = filesystem_id
        self.path: str | None = path

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
        val = dictionary.get('filesystem_id', None)
        val_filesystem_id = val

        val = dictionary.get('path', None)
        val_path = val

        # Return an object of this model
        return cls(
            val_filesystem_id,
            val_path,
        )
