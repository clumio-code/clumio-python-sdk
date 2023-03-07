#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_mssql_restore_source
from clumioapi.models import ec2_mssql_restore_target

T = TypeVar('T', bound='RestoreEc2MssqlDatabaseV1Request')


class RestoreEc2MssqlDatabaseV1Request:
    """Implementation of the 'RestoreEc2MssqlDatabaseV1Request' model.

    Attributes:
        source:
            The EC2 MSSQL database backup to be restored. Only one of `backup` or `pitr`
            should be set.
        target:
            The configuration of the EC2 MSSQL database to which the data has to be
            restored.
    """

    # Create a mapping from Model property names to API property names
    _names = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: ec2_mssql_restore_source.EC2MSSQLRestoreSource = None,
        target: ec2_mssql_restore_target.EC2MSSQLRestoreTarget = None,
    ) -> None:
        """Constructor for the RestoreEc2MssqlDatabaseV1Request class."""

        # Initialize members of the class
        self.source: ec2_mssql_restore_source.EC2MSSQLRestoreSource = source
        self.target: ec2_mssql_restore_target.EC2MSSQLRestoreTarget = target

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
        key = 'source'
        source = (
            ec2_mssql_restore_source.EC2MSSQLRestoreSource.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'target'
        target = (
            ec2_mssql_restore_target.EC2MSSQLRestoreTarget.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(source, target)
