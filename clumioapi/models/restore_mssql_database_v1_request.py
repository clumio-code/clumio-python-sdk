#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import mssql_restore_source, mssql_restore_target

T = TypeVar('T', bound='RestoreMssqlDatabaseV1Request')


class RestoreMssqlDatabaseV1Request:
    """Implementation of the 'RestoreMssqlDatabaseV1Request' model.

    Attributes:
        source:
            The MSSQL database backup to be restored. Only one of `backup` or `pitr`
            should be set.
        target:
            The configuration of the MSSQL database to which the data has to be restored.
    """

    # Create a mapping from Model property names to API property names
    _names = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: mssql_restore_source.MssqlRestoreSource = None,
        target: mssql_restore_target.MssqlRestoreTarget = None,
    ) -> None:
        """Constructor for the RestoreMssqlDatabaseV1Request class."""

        # Initialize members of the class
        self.source: mssql_restore_source.MssqlRestoreSource = source
        self.target: mssql_restore_target.MssqlRestoreTarget = target

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
            mssql_restore_source.MssqlRestoreSource.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'target'
        target = (
            mssql_restore_target.MssqlRestoreTarget.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(source, target)
