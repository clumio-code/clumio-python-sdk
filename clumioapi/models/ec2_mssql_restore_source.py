#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_mssql_restore_from_backup_options
from clumioapi.models import ec2_mssql_restore_to_aag_options
from clumioapi.models import ec2_mssqlpitr_options

T = TypeVar('T', bound='EC2MSSQLRestoreSource')


class EC2MSSQLRestoreSource:
    """Implementation of the 'EC2MSSQLRestoreSource' model.

    The EC2 MSSQL database backup to be restored. Only one of `backup` or
    `pitr`should be set.`pitr` A database backup at a specific point in time to be
    restored.

    Attributes:
        backup:
            The EC2 MSSQL database backup to be restored.
        pitr:
            A database backup at a specific point-in-time to be restored.
        restore_to_aag:
            An AG database to be restored to an AAG.
    """

    # Create a mapping from Model property names to API property names
    _names = {'backup': 'backup', 'pitr': 'pitr', 'restore_to_aag': 'restore_to_aag'}

    def __init__(
        self,
        backup: ec2_mssql_restore_from_backup_options.EC2MSSQLRestoreFromBackupOptions = None,
        pitr: ec2_mssqlpitr_options.EC2MSSQLPITROptions = None,
        restore_to_aag: ec2_mssql_restore_to_aag_options.EC2MSSQLRestoreToAAGOptions = None,
    ) -> None:
        """Constructor for the EC2MSSQLRestoreSource class."""

        # Initialize members of the class
        self.backup: ec2_mssql_restore_from_backup_options.EC2MSSQLRestoreFromBackupOptions = backup
        self.pitr: ec2_mssqlpitr_options.EC2MSSQLPITROptions = pitr
        self.restore_to_aag: ec2_mssql_restore_to_aag_options.EC2MSSQLRestoreToAAGOptions = (
            restore_to_aag
        )

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
            ec2_mssql_restore_from_backup_options.EC2MSSQLRestoreFromBackupOptions.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'pitr'
        pitr = (
            ec2_mssqlpitr_options.EC2MSSQLPITROptions.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'restore_to_aag'
        restore_to_aag = (
            ec2_mssql_restore_to_aag_options.EC2MSSQLRestoreToAAGOptions.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(backup, pitr, restore_to_aag)
