#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import file_descriptor as file_descriptor_
import requests

T = TypeVar('T', bound='FileRestoreSource')


@dataclasses.dataclass
class FileRestoreSource:
    """Implementation of the 'FileRestoreSource' model.

    The files to be restored and from which backup they are to be restored from.

    Attributes:
        BackupId:
            The clumio-assigned id of the backup containing the files you want to restore.
            use
            [ get /backups/files/search/{search_result_id}/versions](#operation/list-file-
            versions)
            to fetch the value.

        Files:
            The list of files to be restored.

    """

    BackupId: str | None = None
    Files: Sequence[file_descriptor_.FileDescriptor] | None = None

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
        val = dictionary.get('backup_id', None)
        val_backup_id = val

        val = dictionary.get('files', None)

        val_files = []
        if val:
            for value in val:
                val_files.append(file_descriptor_.FileDescriptor.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_backup_id,
            val_files,
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
