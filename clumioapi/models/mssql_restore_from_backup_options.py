#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='MssqlRestoreFromBackupOptions')


class MssqlRestoreFromBackupOptions:
    """Implementation of the 'MssqlRestoreFromBackupOptions' model.

    The MSSQL database backup to be restored. Only one of `backup` or `pitr`should
    be specified.

    Attributes:
        backup_id:
            The Clumio-assigned ID of the backup to be restored.
            Use the [GET /backups/mssql/databases](#operation/list-backup-mssql-databases)
            endpoint to fetch valid values.
    """

    # Create a mapping from Model property names to API property names
    _names = {'backup_id': 'backup_id'}

    def __init__(self, backup_id: str = None) -> None:
        """Constructor for the MssqlRestoreFromBackupOptions class."""

        # Initialize members of the class
        self.backup_id: str = backup_id

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
        # Return an object of this model
        return cls(backup_id)
