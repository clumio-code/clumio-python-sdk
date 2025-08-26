#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='FileDescriptor')


@dataclasses.dataclass
class FileDescriptor:
    """Implementation of the 'FileDescriptor' model.

        Specifies a file/directory by providing path and file system.

        Attributes:
            FilesystemId:
                The clumio-assigned id of the filesystem within which to restore the file. use
    [ get /backups/files/search/{search_result_id}/versions](#operation/list-file-versions)
    to fetch the value.

            Path:
                The path of the file to be restored. use
    [get /backups/files/search](#operation/list-files) to fetch the value.

    """

    FilesystemId: str | None = None
    Path: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
