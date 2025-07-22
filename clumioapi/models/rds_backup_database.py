#
# Copyright 2023. Clumio, A Commvault Company.
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
    _names: dict[str, str] = {'name': 'name'}

    def __init__(self, name: str) -> None:
        """Constructor for the RDSBackupDatabase class."""

        # Initialize members of the class
        self.name: str = name

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
        val = dictionary['name']
        val_name = val

        # Return an object of this model
        return cls(
            val_name,  # type: ignore
        )
