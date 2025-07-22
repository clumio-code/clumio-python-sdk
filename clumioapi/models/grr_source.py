#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='GrrSource')


class GrrSource:
    """Implementation of the 'GrrSource' model.

    The RDS database backup to be queried.

    Attributes:
        backup_id:
            Performs the operation on a database within the specified backup.
            Use the [GET /backups/aws/rds-resources](#operation/list-backup-aws-rds-
            resources)
            endpoint to fetch valid values.
        database_name:
            Performs the operation on the database with the specified name.
            Use the [GET /backups/aws/rds-resources](#operation/list-backup-aws-rds-
            resource-databases)
            endpoint to fetch valid values.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'backup_id': 'backup_id', 'database_name': 'database_name'}

    def __init__(self, backup_id: str, database_name: str) -> None:
        """Constructor for the GrrSource class."""

        # Initialize members of the class
        self.backup_id: str = backup_id
        self.database_name: str = database_name

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
        val = dictionary['backup_id']
        val_backup_id = val

        val = dictionary['database_name']
        val_database_name = val

        # Return an object of this model
        return cls(
            val_backup_id,  # type: ignore
            val_database_name,  # type: ignore
        )
