#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='EC2MSSQLRestoreTarget')


class EC2MSSQLRestoreTarget:
    """Implementation of the 'EC2MSSQLRestoreTarget' model.

    The configuration of the EC2 MSSQL database to which the data has to be
    restored.

    Attributes:
        data_files_path:
            The target location within the instance to restore data files. For example,
            `C:\\Programe Files\\clumio\restored-data-files\\`. If this field is empty, we
            will restore data files into the same location as the source database.
        database_name:
            The user-assigned name of the database.
        final_database_state:
            Final database state after clumio restored the database. If final_database_state
            is set to empty then clumio will make database in online state.
            Possible vales are `RESTORING` or `ONLINE`
        instance_id:
            The Clumio-assigned ID of the instance to restore the database into.
            Use the [GET /datasources/aws/ec2-mssql/instances](#operation/list-ec2-mssql-
            instances) to fetch valid values.
        log_files_path:
            The target location within the instance to restore log files. For example,
            `C:\\Programe Files\\clumio\restored-log-files\\`. If this field is empty, we
            will restore log files into the same location as the source database.
        restore_as_new_database:
            The boolean value representing if the database has to be restored as new
            database.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'data_files_path': 'data_files_path',
        'database_name': 'database_name',
        'final_database_state': 'final_database_state',
        'instance_id': 'instance_id',
        'log_files_path': 'log_files_path',
        'restore_as_new_database': 'restore_as_new_database',
    }

    def __init__(
        self,
        data_files_path: str = None,
        database_name: str = None,
        final_database_state: str = None,
        instance_id: str = None,
        log_files_path: str = None,
        restore_as_new_database: bool = None,
    ) -> None:
        """Constructor for the EC2MSSQLRestoreTarget class."""

        # Initialize members of the class
        self.data_files_path: str = data_files_path
        self.database_name: str = database_name
        self.final_database_state: str = final_database_state
        self.instance_id: str = instance_id
        self.log_files_path: str = log_files_path
        self.restore_as_new_database: bool = restore_as_new_database

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
        data_files_path = dictionary.get('data_files_path')
        database_name = dictionary.get('database_name')
        final_database_state = dictionary.get('final_database_state')
        instance_id = dictionary.get('instance_id')
        log_files_path = dictionary.get('log_files_path')
        restore_as_new_database = dictionary.get('restore_as_new_database')
        # Return an object of this model
        return cls(
            data_files_path,
            database_name,
            final_database_state,
            instance_id,
            log_files_path,
            restore_as_new_database,
        )
