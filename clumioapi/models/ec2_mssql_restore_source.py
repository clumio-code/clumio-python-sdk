#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    ec2_mssql_restore_from_backup_options as ec2_mssql_restore_from_backup_options_
from clumioapi.models import ec2_mssql_restore_to_aag_options as ec2_mssql_restore_to_aag_options_
from clumioapi.models import ec2_mssqlpitr_options as ec2_mssqlpitr_options_
import requests

T = TypeVar('T', bound='EC2MSSQLRestoreSource')


@dataclasses.dataclass
class EC2MSSQLRestoreSource:
    """Implementation of the 'EC2MSSQLRestoreSource' model.

    The EC2 MSSQL database backup to be restored. Only one of `backup` or
    `pitr`should be set.`pitr` A database backup at a specific point in time to be
    restored.

    Attributes:
        Backup:
            The ec2 mssql database backup to be restored.

        Pitr:
            A database backup at a specific point-in-time to be restored.

        RestoreToAag:
            An ag database to be restored to an aag.

    """

    Backup: ec2_mssql_restore_from_backup_options_.EC2MSSQLRestoreFromBackupOptions | None = None
    Pitr: ec2_mssqlpitr_options_.EC2MSSQLPITROptions | None = None
    RestoreToAag: ec2_mssql_restore_to_aag_options_.EC2MSSQLRestoreToAAGOptions | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
