#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='RDSBackupDatabase')


class RDSBackupDatabase:
    """Implementation of the 'RDSBackupDatabase' model.

    Attributes:
        name:
            The name of the database.
    """

    # Create a mapping from Model property names to API property names
    _names = {'name': 'name'}

    def __init__(self, name: str = None) -> None:
        """Constructor for the RDSBackupDatabase class."""

        # Initialize members of the class
        self.name: str = name

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
        name = dictionary.get('name')
        # Return an object of this model
        return cls(name)
