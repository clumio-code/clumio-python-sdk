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
    _names = {'filesystem_id': 'filesystem_id', 'path': 'path'}

    def __init__(self, filesystem_id: str = None, path: str = None) -> None:
        """Constructor for the FileDescriptor class."""

        # Initialize members of the class
        self.filesystem_id: str = filesystem_id
        self.path: str = path

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
        filesystem_id = dictionary.get('filesystem_id')
        path = dictionary.get('path')
        # Return an object of this model
        return cls(filesystem_id, path)
