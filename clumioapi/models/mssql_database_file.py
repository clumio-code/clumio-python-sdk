#
# Copyright 2023. Clumio, A Commvault Company.
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
    _names: dict[str, str] = {'name': 'name', 'p_type': 'type'}

    def __init__(self, name: str, p_type: str) -> None:
        """Constructor for the MssqlDatabaseFile class."""

        # Initialize members of the class
        self.name: str = name
        self.p_type: str = p_type

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

        val = dictionary['type']
        val_p_type = val

        # Return an object of this model
        return cls(
            val_name,  # type: ignore
            val_p_type,  # type: ignore
        )
