#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import file_descriptor

T = TypeVar('T', bound='FileRestoreSource')


class FileRestoreSource:
    """Implementation of the 'FileRestoreSource' model.

    The files to be restored and from which backup they are to be restored from.

    Attributes:
        backup_id:
            The Clumio-assigned ID of the backup containing the files you want to restore.
            Use
            [ GET /backups/files/search/{search_result_id}/versions](#operation/list-file-
            versions)
            to fetch the value.
        files:
            The list of files to be restored.
    """

    # Create a mapping from Model property names to API property names
    _names = {'backup_id': 'backup_id', 'files': 'files'}

    def __init__(
        self, backup_id: str = None, files: Sequence[file_descriptor.FileDescriptor] = None
    ) -> None:
        """Constructor for the FileRestoreSource class."""

        # Initialize members of the class
        self.backup_id: str = backup_id
        self.files: Sequence[file_descriptor.FileDescriptor] = files

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
        backup_id = dictionary.get('backup_id')
        files = None
        if dictionary.get('files'):
            files = list()
            for value in dictionary.get('files'):
                files.append(file_descriptor.FileDescriptor.from_dictionary(value))

        # Return an object of this model
        return cls(backup_id, files)
