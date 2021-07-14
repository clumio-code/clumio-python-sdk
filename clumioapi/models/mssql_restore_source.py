#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import mssql_pitr_options
from clumioapi.models import mssql_restore_from_backup_options

T = TypeVar('T', bound='MssqlRestoreSource')


class MssqlRestoreSource:
    """Implementation of the 'MssqlRestoreSource' model.

    The MSSQL database backup to be restored. Only one of `backup` or `pitr`should
    be set.

    Attributes:
        backup:
            The MSSQL database backup to be restored. Only one of `backup` or `pitr`
            should be specified.
        pitr:
            A database and a point-in-time to be restored. Only one of `backup` or
            `pitr` should be specified.
    """

    # Create a mapping from Model property names to API property names
    _names = {'backup': 'backup', 'pitr': 'pitr'}

    def __init__(
        self,
        backup: mssql_restore_from_backup_options.MssqlRestoreFromBackupOptions = None,
        pitr: mssql_pitr_options.MssqlPITROptions = None,
    ) -> None:
        """Constructor for the MssqlRestoreSource class."""

        # Initialize members of the class
        self.backup: mssql_restore_from_backup_options.MssqlRestoreFromBackupOptions = backup
        self.pitr: mssql_pitr_options.MssqlPITROptions = pitr

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
        key = 'backup'
        backup = (
            mssql_restore_from_backup_options.MssqlRestoreFromBackupOptions.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'pitr'
        pitr = (
            mssql_pitr_options.MssqlPITROptions.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(backup, pitr)
