#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import file_system

T = TypeVar('T', bound='FileSystemListEmbedded')


class FileSystemListEmbedded:
    """Implementation of the 'FileSystemListEmbedded' model.

    _embedded contains the list of items of a file_system list query

    Attributes:
        items:
            items denotes the list of file_system instances in the current scope.
    """

    # Create a mapping from Model property names to API property names
    _names = {'items': 'items'}

    def __init__(self, items: Sequence[file_system.FileSystem] = None) -> None:
        """Constructor for the FileSystemListEmbedded class."""

        # Initialize members of the class
        self.items: Sequence[file_system.FileSystem] = items

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
        items = None
        if dictionary.get('items'):
            items = list()
            for value in dictionary.get('items'):
                items.append(file_system.FileSystem.from_dictionary(value))

        # Return an object of this model
        return cls(items)
