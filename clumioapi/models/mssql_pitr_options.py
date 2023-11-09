#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='MssqlPITROptions')


class MssqlPITROptions:
    """Implementation of the 'MssqlPITROptions' model.

    A database and a point-in-time to be restored. Only one of `backup` or`pitr`
    should be specified.

    Attributes:
        database_id:
            The Clumio-assigned ID of the MSSQL database to be restored.
            Use the [GET /datasources/mssql/databases](#operation/list-mssql-databases)
            endpoint to fetch valid values.
        timestamp:
            The point in time to be restored in RFC-3339 format.
    """

    # Create a mapping from Model property names to API property names
    _names = {'database_id': 'database_id', 'timestamp': 'timestamp'}

    def __init__(self, database_id: str = None, timestamp: str = None) -> None:
        """Constructor for the MssqlPITROptions class."""

        # Initialize members of the class
        self.database_id: str = database_id
        self.timestamp: str = timestamp

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
        database_id = dictionary.get('database_id')
        timestamp = dictionary.get('timestamp')
        # Return an object of this model
        return cls(database_id, timestamp)
