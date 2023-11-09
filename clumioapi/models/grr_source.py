#
# Copyright 2023. Clumio, Inc.
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
    _names = {'backup_id': 'backup_id', 'database_name': 'database_name'}

    def __init__(self, backup_id: str = None, database_name: str = None) -> None:
        """Constructor for the GrrSource class."""

        # Initialize members of the class
        self.backup_id: str = backup_id
        self.database_name: str = database_name

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
        backup_id = dictionary.get('backup_id')
        database_name = dictionary.get('database_name')
        # Return an object of this model
        return cls(backup_id, database_name)
