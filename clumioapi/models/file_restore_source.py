#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import file_descriptor as file_descriptor_

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
    _names: dict[str, str] = {'backup_id': 'backup_id', 'files': 'files'}

    def __init__(self, backup_id: str, files: Sequence[file_descriptor_.FileDescriptor]) -> None:
        """Constructor for the FileRestoreSource class."""

        # Initialize members of the class
        self.backup_id: str = backup_id
        self.files: Sequence[file_descriptor_.FileDescriptor] = files

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
        val = dictionary['backup_id']
        val_backup_id = val

        val = dictionary['files']

        val_files = None
        if val:
            val_files = list()
            for value in val:
                val_files.append(file_descriptor_.FileDescriptor.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_backup_id,  # type: ignore
            val_files,  # type: ignore
        )
