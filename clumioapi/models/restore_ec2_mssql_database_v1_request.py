#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_mssql_restore_source as ec2_mssql_restore_source_
from clumioapi.models import ec2_mssql_restore_target as ec2_mssql_restore_target_

T = TypeVar('T', bound='RestoreEc2MssqlDatabaseV1Request')


class RestoreEc2MssqlDatabaseV1Request:
    """Implementation of the 'RestoreEc2MssqlDatabaseV1Request' model.

    Attributes:
        source:
            The EC2 MSSQL database backup to be restored. Only one of `backup` or `pitr`
            should be set.
            `pitr` A database backup at a specific point in time to be restored.
        target:
            The configuration of the EC2 MSSQL database to which the data has to be
            restored.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: ec2_mssql_restore_source_.EC2MSSQLRestoreSource | None = None,
        target: ec2_mssql_restore_target_.EC2MSSQLRestoreTarget | None = None,
    ) -> None:
        """Constructor for the RestoreEc2MssqlDatabaseV1Request class."""

        # Initialize members of the class
        self.source: ec2_mssql_restore_source_.EC2MSSQLRestoreSource | None = source
        self.target: ec2_mssql_restore_target_.EC2MSSQLRestoreTarget | None = target

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
        val = dictionary.get('source', None)
        val_source = ec2_mssql_restore_source_.EC2MSSQLRestoreSource.from_dictionary(val)

        val = dictionary.get('target', None)
        val_target = ec2_mssql_restore_target_.EC2MSSQLRestoreTarget.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_source,
            val_target,
        )
