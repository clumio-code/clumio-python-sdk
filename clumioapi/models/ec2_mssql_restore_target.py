#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='EC2MSSQLRestoreTarget')


@dataclasses.dataclass
class EC2MSSQLRestoreTarget:
    """Implementation of the 'EC2MSSQLRestoreTarget' model.

        The configuration of the EC2 MSSQL database to which the data has to be
        restored.

        Attributes:
            DataFilesPath:
                The target location within the instance to restore data files. for example,
    `c:\\programe files\\clumio\restored-data-files\\`. if this field is empty, we
    will restore data files into the same location as the source database.

            DatabaseName:
                The user-assigned name of the database.

            FinalDatabaseState:
                Final database state after clumio restored the database. if final_database_state
    is set to empty then clumio will make database in online state.
    possible vales are `restoring` or `online`.

            InstanceId:
                The clumio-assigned id of the instance to restore the database into.
    use the [get /datasources/aws/ec2-mssql/instances](#operation/list-ec2-mssql-instances) to fetch valid values.

            LogFilesPath:
                The target location within the instance to restore log files. for example,
    `c:\\programe files\\clumio\restored-log-files\\`. if this field is empty, we
    will restore log files into the same location as the source database.

            RestoreAsNewDatabase:
                The boolean value representing if the database has to be restored as new database.

    """

    DataFilesPath: str | None = None
    DatabaseName: str | None = None
    FinalDatabaseState: str | None = None
    InstanceId: str | None = None
    LogFilesPath: str | None = None
    RestoreAsNewDatabase: bool | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
