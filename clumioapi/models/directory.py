#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
from clumioapi.models import directory_links as directory_links_
import requests

T = TypeVar('T', bound='Directory')


@dataclasses.dataclass
class Directory:
    """Implementation of the 'Directory' model.

    Attributes:
        Links:
            Urls to pages related to the resource.

        DirectoryId:
            The directory id of the file. if the file is not a directory, then this field
            has
            a value of `null`.

        IsDirectory:
            Determines whether or not this file is a directory. if true, then this file
            is a directory.

        ModifiedTimestamp:
            The timestamp of when this file was last modified.

        Name:
            Name of this file.

        Size:
            Size of this file, in bytes.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Links': '_links',
    }

    Links: directory_links_.DirectoryLinks | None = None
    DirectoryId: str | None = None
    IsDirectory: bool | None = None
    ModifiedTimestamp: str | None = None
    Name: str | None = None
    Size: int | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return api_helper.to_dictionary(self)

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
        val_links = directory_links_.DirectoryLinks.from_dictionary(val)

        val = dictionary.get('directory_id', None)
        val_directory_id = val

        val = dictionary.get('is_directory', None)
        val_is_directory = val

        val = dictionary.get('modified_timestamp', None)
        val_modified_timestamp = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('size', None)
        val_size = val

        # Return an object of this model
        return cls(
            val_links,
            val_directory_id,
            val_is_directory,
            val_modified_timestamp,
            val_name,
            val_size,
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
