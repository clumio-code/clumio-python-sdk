#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    ec2_mssql_database_backup_embedded as ec2_mssql_database_backup_embedded_
from clumioapi.models import ec2_mssql_database_backup_links as ec2_mssql_database_backup_links_
from clumioapi.models import mssql_database_file as mssql_database_file_
import requests

T = TypeVar('T', bound='ReadEC2MSSQLDatabaseBackupResponse')


@dataclasses.dataclass
class ReadEC2MSSQLDatabaseBackupResponse:
    """Implementation of the 'ReadEC2MSSQLDatabaseBackupResponse' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        DatabaseFiles:
            List of database files at the time of backup.

        DatabaseId:
            The clumio-assigned id of the database associated with this backup.

        Engine:
            The microsoft sql database engine at the time of backup.

        EngineVersion:
            The microsoft sql database engine version at the time of backup.

        EnvironmentId:
            The clumio-assigned id of the aws environment associated with the database at the time of backup.

        ExpirationTimestamp:
            The timestamp of when this backup expires. represented in rfc-3339 format.

        HostEndpoint:
            The user-provided endpoint of the host containing the given database at the time of backup.

        HostId:
            The clumio-assigned id of the host associated with the database at the time of backup.

        Id:
            The clumio-assigned id of the backup.

        InstanceId:
            The clumio-assigned instance id at the time of backup.

        InstanceName:
            The instance name at the time of backup.

        StartTimestamp:
            The timestamp of when this backup started. represented in rfc-3339 format.

        Type:
            The type of backup.

    """

    Embedded: ec2_mssql_database_backup_embedded_.EC2MSSQLDatabaseBackupEmbedded | None = None
    Links: ec2_mssql_database_backup_links_.EC2MSSQLDatabaseBackupLinks | None = None
    DatabaseFiles: Sequence[mssql_database_file_.MssqlDatabaseFile] | None = None
    DatabaseId: str | None = None
    Engine: str | None = None
    EngineVersion: str | None = None
    EnvironmentId: str | None = None
    ExpirationTimestamp: str | None = None
    HostEndpoint: str | None = None
    HostId: str | None = None
    Id: str | None = None
    InstanceId: str | None = None
    InstanceName: str | None = None
    StartTimestamp: str | None = None
    Type: str | None = None
    raw_response: Optional[requests.Response] = None

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
        val = dictionary.get('_embedded', None)
        val_embedded = (
            ec2_mssql_database_backup_embedded_.EC2MSSQLDatabaseBackupEmbedded.from_dictionary(val)
        )

        val = dictionary.get('_links', None)
        val_links = ec2_mssql_database_backup_links_.EC2MSSQLDatabaseBackupLinks.from_dictionary(
            val
        )

        val = dictionary.get('database_files', None)

        val_database_files = []
        if val:
            for value in val:
                val_database_files.append(
                    mssql_database_file_.MssqlDatabaseFile.from_dictionary(value)
                )

        val = dictionary.get('database_id', None)
        val_database_id = val

        val = dictionary.get('engine', None)
        val_engine = val

        val = dictionary.get('engine_version', None)
        val_engine_version = val

        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('expiration_timestamp', None)
        val_expiration_timestamp = val

        val = dictionary.get('host_endpoint', None)
        val_host_endpoint = val

        val = dictionary.get('host_id', None)
        val_host_id = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('instance_id', None)
        val_instance_id = val

        val = dictionary.get('instance_name', None)
        val_instance_name = val

        val = dictionary.get('start_timestamp', None)
        val_start_timestamp = val

        val = dictionary.get('type', None)
        val_type = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_database_files,
            val_database_id,
            val_engine,
            val_engine_version,
            val_environment_id,
            val_expiration_timestamp,
            val_host_endpoint,
            val_host_id,
            val_id,
            val_instance_id,
            val_instance_name,
            val_start_timestamp,
            val_type,
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
        model_instance.raw_response = response
        return model_instance
