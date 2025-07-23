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
    _names: dict[str, str] = {
        'data_files_path': 'data_files_path',
        'database_name': 'database_name',
        'final_database_state': 'final_database_state',
        'instance_id': 'instance_id',
        'log_files_path': 'log_files_path',
        'restore_as_new_database': 'restore_as_new_database',
    }

    def __init__(
        self,
        data_files_path: str | None = None,
        database_name: str | None = None,
        final_database_state: str | None = None,
        instance_id: str | None = None,
        log_files_path: str | None = None,
        restore_as_new_database: bool | None = None,
    ) -> None:
        """Constructor for the EC2MSSQLRestoreTarget class."""

        # Initialize members of the class
        self.data_files_path: str | None = data_files_path
        self.database_name: str | None = database_name
        self.final_database_state: str | None = final_database_state
        self.instance_id: str | None = instance_id
        self.log_files_path: str | None = log_files_path
        self.restore_as_new_database: bool | None = restore_as_new_database

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
        val = dictionary.get('data_files_path', None)
        val_data_files_path = val

        val = dictionary.get('database_name', None)
        val_database_name = val

        val = dictionary.get('final_database_state', None)
        val_final_database_state = val

        val = dictionary.get('instance_id', None)
        val_instance_id = val

        val = dictionary.get('log_files_path', None)
        val_log_files_path = val

        val = dictionary.get('restore_as_new_database', None)
        val_restore_as_new_database = val

        # Return an object of this model
        return cls(
            val_data_files_path,
            val_database_name,
            val_final_database_state,
            val_instance_id,
            val_log_files_path,
            val_restore_as_new_database,
        )
