#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    ec2_mssql_restore_from_backup_options as ec2_mssql_restore_from_backup_options_
from clumioapi.models import ec2_mssql_restore_to_aag_options as ec2_mssql_restore_to_aag_options_
from clumioapi.models import ec2_mssqlpitr_options as ec2_mssqlpitr_options_

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
    _names: dict[str, str] = {
        'backup': 'backup',
        'pitr': 'pitr',
        'restore_to_aag': 'restore_to_aag',
    }

    def __init__(
        self,
        backup: (
            ec2_mssql_restore_from_backup_options_.EC2MSSQLRestoreFromBackupOptions | None
        ) = None,
        pitr: ec2_mssqlpitr_options_.EC2MSSQLPITROptions | None = None,
        restore_to_aag: ec2_mssql_restore_to_aag_options_.EC2MSSQLRestoreToAAGOptions | None = None,
    ) -> None:
        """Constructor for the EC2MSSQLRestoreSource class."""

        # Initialize members of the class
        self.backup: (
            ec2_mssql_restore_from_backup_options_.EC2MSSQLRestoreFromBackupOptions | None
        ) = backup
        self.pitr: ec2_mssqlpitr_options_.EC2MSSQLPITROptions | None = pitr
        self.restore_to_aag: (
            ec2_mssql_restore_to_aag_options_.EC2MSSQLRestoreToAAGOptions | None
        ) = restore_to_aag

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

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('backup', None)
        val_backup = (
            ec2_mssql_restore_from_backup_options_.EC2MSSQLRestoreFromBackupOptions.from_dictionary(
                val
            )
        )

        val = dictionary.get('pitr', None)
        val_pitr = ec2_mssqlpitr_options_.EC2MSSQLPITROptions.from_dictionary(val)

        val = dictionary.get('restore_to_aag', None)
        val_restore_to_aag = (
            ec2_mssql_restore_to_aag_options_.EC2MSSQLRestoreToAAGOptions.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_backup,
            val_pitr,
            val_restore_to_aag,
        )
