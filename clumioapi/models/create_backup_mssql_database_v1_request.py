#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='CreateBackupMssqlDatabaseV1Request')


class CreateBackupMssqlDatabaseV1Request:
    """Implementation of the 'CreateBackupMssqlDatabaseV1Request' model.

    Attributes:
        asset_id:
            Performs the operation on the Mssql asset with the specified Clumio-assigned ID.
        type:
            The type of the backup. Possible values - `mssql_database_backup`,
            `mssql_log_backup`.
    """

    # Create a mapping from Model property names to API property names
    _names = {'asset_id': 'asset_id', 'type': 'type'}

    def __init__(self, asset_id: str = None, type: str = None) -> None:
        """Constructor for the CreateBackupMssqlDatabaseV1Request class."""

        # Initialize members of the class
        self.asset_id: str = asset_id
        self.type: str = type

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
        asset_id = dictionary.get('asset_id')
        type = dictionary.get('type')
        # Return an object of this model
        return cls(asset_id, type)
