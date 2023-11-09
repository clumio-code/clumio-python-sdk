#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import directory_links

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
    _names = {
        'links': '_links',
        'directory_id': 'directory_id',
        'is_directory': 'is_directory',
        'modified_timestamp': 'modified_timestamp',
        'name': 'name',
        'size': 'size',
    }

    def __init__(
        self,
        links: directory_links.DirectoryLinks = None,
        directory_id: str = None,
        is_directory: bool = None,
        modified_timestamp: str = None,
        name: str = None,
        size: int = None,
    ) -> None:
        """Constructor for the Directory class."""

        # Initialize members of the class
        self.links: directory_links.DirectoryLinks = links
        self.directory_id: str = directory_id
        self.is_directory: bool = is_directory
        self.modified_timestamp: str = modified_timestamp
        self.name: str = name
        self.size: int = size

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
            directory_links.DirectoryLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        directory_id = dictionary.get('directory_id')
        is_directory = dictionary.get('is_directory')
        modified_timestamp = dictionary.get('modified_timestamp')
        name = dictionary.get('name')
        size = dictionary.get('size')
        # Return an object of this model
        return cls(links, directory_id, is_directory, modified_timestamp, name, size)
