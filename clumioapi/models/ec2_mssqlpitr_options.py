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
    _names: dict[str, str] = {
        'database_id': 'database_id',
        'restore_to_latest': 'restore_to_latest',
        'timestamp': 'timestamp',
    }

    def __init__(self, database_id: str, restore_to_latest: bool, timestamp: str) -> None:
        """Constructor for the EC2MSSQLPITROptions class."""

        # Initialize members of the class
        self.database_id: str = database_id
        self.restore_to_latest: bool = restore_to_latest
        self.timestamp: str = timestamp

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
        val = dictionary['database_id']
        val_database_id = val

        val = dictionary['restore_to_latest']
        val_restore_to_latest = val

        val = dictionary['timestamp']
        val_timestamp = val

        # Return an object of this model
        return cls(
            val_database_id,  # type: ignore
            val_restore_to_latest,  # type: ignore
            val_timestamp,  # type: ignore
        )
