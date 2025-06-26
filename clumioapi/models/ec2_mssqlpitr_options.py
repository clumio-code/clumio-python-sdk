#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='EC2MSSQLPITROptions')


class EC2MSSQLPITROptions:
    """Implementation of the 'EC2MSSQLPITROptions' model.

    A database backup at a specific point-in-time to be restored.

    Attributes:
        database_id:
            The Clumio-assigned ID of the MSSQL database to be restored.
            Use the [GET /datasources/aws/ec2-mssql/databases](#operation/list-ec2-mssql-
            databases)
            endpoint to fetch valid values.
        restore_to_latest:
            If enabled, performs PITR till the latest possible time.
            Either timestamp or restore_to_latest must be provided, but not both.
        timestamp:
            The point in time to be restored in RFC-3339 format.
            Either timestamp or restore_to_latest must be provided, but not both.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'database_id': 'database_id',
        'restore_to_latest': 'restore_to_latest',
        'timestamp': 'timestamp',
    }

    def __init__(
        self, database_id: str = None, restore_to_latest: bool = None, timestamp: str = None
    ) -> None:
        """Constructor for the EC2MSSQLPITROptions class."""

        # Initialize members of the class
        self.database_id: str = database_id
        self.restore_to_latest: bool = restore_to_latest
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
        restore_to_latest = dictionary.get('restore_to_latest')
        timestamp = dictionary.get('timestamp')
        # Return an object of this model
        return cls(database_id, restore_to_latest, timestamp)
