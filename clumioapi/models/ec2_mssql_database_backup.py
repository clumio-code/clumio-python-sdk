#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    ec2_mssql_database_backup_embedded as ec2_mssql_database_backup_embedded_
from clumioapi.models import ec2_mssql_database_backup_links as ec2_mssql_database_backup_links_
from clumioapi.models import mssql_database_file as mssql_database_file_

T = TypeVar('T', bound='EC2MSSQLDatabaseBackup')


class EC2MSSQLDatabaseBackup:
    """Implementation of the 'EC2MSSQLDatabaseBackup' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        database_files:
            List of database files at the time of backup.
        database_id:
            The Clumio-assigned ID of the database associated with this backup.
        engine:
            The Microsoft SQL database engine at the time of backup.
        engine_version:
            The Microsoft SQL database engine version at the time of backup.
        environment_id:
            The Clumio-assigned ID of the AWS environment associated with the database at
            the time of backup.
        expiration_timestamp:
            The timestamp of when this backup expires. Represented in RFC-3339 format.
        host_endpoint:
            The user-provided endpoint of the host containing the given database at the time
            of backup.
        host_id:
            The Clumio-assigned ID of the host associated with the database at the time of
            backup.
        p_id:
            The Clumio-assigned ID of the backup.
        instance_id:
            The Clumio-assigned instance id at the time of backup.
        instance_name:
            The instance name at the time of backup.
        start_timestamp:
            The timestamp of when this backup started. Represented in RFC-3339 format.
        p_type:
            The type of backup.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'database_files': 'database_files',
        'database_id': 'database_id',
        'engine': 'engine',
        'engine_version': 'engine_version',
        'environment_id': 'environment_id',
        'expiration_timestamp': 'expiration_timestamp',
        'host_endpoint': 'host_endpoint',
        'host_id': 'host_id',
        'p_id': 'id',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'start_timestamp': 'start_timestamp',
        'p_type': 'type',
    }

    def __init__(
        self,
        embedded: ec2_mssql_database_backup_embedded_.EC2MSSQLDatabaseBackupEmbedded | None = None,
        links: ec2_mssql_database_backup_links_.EC2MSSQLDatabaseBackupLinks | None = None,
        database_files: Sequence[mssql_database_file_.MssqlDatabaseFile] | None = None,
        database_id: str | None = None,
        engine: str | None = None,
        engine_version: str | None = None,
        environment_id: str | None = None,
        expiration_timestamp: str | None = None,
        host_endpoint: str | None = None,
        host_id: str | None = None,
        p_id: str | None = None,
        instance_id: str | None = None,
        instance_name: str | None = None,
        start_timestamp: str | None = None,
        p_type: str | None = None,
    ) -> None:
        """Constructor for the EC2MSSQLDatabaseBackup class."""

        # Initialize members of the class
        self.embedded: ec2_mssql_database_backup_embedded_.EC2MSSQLDatabaseBackupEmbedded | None = (
            embedded
        )
        self.links: ec2_mssql_database_backup_links_.EC2MSSQLDatabaseBackupLinks | None = links
        self.database_files: Sequence[mssql_database_file_.MssqlDatabaseFile] | None = (
            database_files
        )
        self.database_id: str | None = database_id
        self.engine: str | None = engine
        self.engine_version: str | None = engine_version
        self.environment_id: str | None = environment_id
        self.expiration_timestamp: str | None = expiration_timestamp
        self.host_endpoint: str | None = host_endpoint
        self.host_id: str | None = host_id
        self.p_id: str | None = p_id
        self.instance_id: str | None = instance_id
        self.instance_name: str | None = instance_name
        self.start_timestamp: str | None = start_timestamp
        self.p_type: str | None = p_type

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
        val = dictionary.get('_embedded', None)
        val_embedded = (
            ec2_mssql_database_backup_embedded_.EC2MSSQLDatabaseBackupEmbedded.from_dictionary(val)
        )

        val = dictionary.get('_links', None)
        val_links = ec2_mssql_database_backup_links_.EC2MSSQLDatabaseBackupLinks.from_dictionary(
            val
        )

        val = dictionary.get('database_files', None)

        val_database_files = None
        if val:
            val_database_files = list()
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
        val_p_id = val

        val = dictionary.get('instance_id', None)
        val_instance_id = val

        val = dictionary.get('instance_name', None)
        val_instance_name = val

        val = dictionary.get('start_timestamp', None)
        val_start_timestamp = val

        val = dictionary.get('type', None)
        val_p_type = val

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
            val_p_id,
            val_instance_id,
            val_instance_name,
            val_start_timestamp,
            val_p_type,
        )
