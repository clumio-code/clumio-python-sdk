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
        links: directory_links_.DirectoryLinks,
        directory_id: str,
        is_directory: bool,
        modified_timestamp: str,
        name: str,
        size: int,
    ) -> None:
        """Constructor for the Directory class."""

        # Initialize members of the class
        self.links: directory_links_.DirectoryLinks = links
        self.directory_id: str = directory_id
        self.is_directory: bool = is_directory
        self.modified_timestamp: str = modified_timestamp
        self.name: str = name
        self.size: int = size

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
        val = dictionary['_links']
        val_links = directory_links_.DirectoryLinks.from_dictionary(val)

        val = dictionary['directory_id']
        val_directory_id = val

        val = dictionary['is_directory']
        val_is_directory = val

        val = dictionary['modified_timestamp']
        val_modified_timestamp = val

        val = dictionary['name']
        val_name = val

        val = dictionary['size']
        val_size = val

        # Return an object of this model
        return cls(
            val_links,  # type: ignore
            val_directory_id,  # type: ignore
            val_is_directory,  # type: ignore
            val_modified_timestamp,  # type: ignore
            val_name,  # type: ignore
            val_size,  # type: ignore
        )
