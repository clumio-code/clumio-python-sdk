#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='MssqlDatabaseFile')


class MssqlDatabaseFile:
    """Implementation of the 'MssqlDatabaseFile' model.

    Attributes:
        name:
            The name of the database file.
        p_type:
            The type of the database file. Possible values include sql_row_file and
            sql_log_file.
    """

    # Create a mapping from Model property names to API property names
    _names = {'name': 'name', 'p_type': 'type'}

    def __init__(self, name: str = None, p_type: str = None) -> None:
        """Constructor for the MssqlDatabaseFile class."""

        # Initialize members of the class
        self.name: str = name
        self.p_type: str = p_type

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
        p_type = dictionary.get('type')
        # Return an object of this model
        return cls(name, p_type)
