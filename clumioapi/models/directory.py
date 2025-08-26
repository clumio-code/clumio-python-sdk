#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import directory_links as directory_links_

T = TypeVar('T', bound='Directory')


class Directory:
    """Implementation of the 'Directory' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        directory_id:
            The directory ID of the file. If the file is not a directory, then this field
            has
            a value of `null`.
        is_directory:
            Determines whether or not this file is a directory. If true, then this file
            is a directory.
        modified_timestamp:
            The timestamp of when this file was last modified.
        name:
            Name of this file.
        size:
            Size of this file, in bytes.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'links': '_links',
        'directory_id': 'directory_id',
        'is_directory': 'is_directory',
        'modified_timestamp': 'modified_timestamp',
        'name': 'name',
        'size': 'size',
    }

    def __init__(
        self,
        links: directory_links_.DirectoryLinks | None = None,
        directory_id: str | None = None,
        is_directory: bool | None = None,
        modified_timestamp: str | None = None,
        name: str | None = None,
        size: int | None = None,
    ) -> None:
        """Constructor for the Directory class."""

        # Initialize members of the class
        self.links: directory_links_.DirectoryLinks | None = links
        self.directory_id: str | None = directory_id
        self.is_directory: bool | None = is_directory
        self.modified_timestamp: str | None = modified_timestamp
        self.name: str | None = name
        self.size: int | None = size

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
