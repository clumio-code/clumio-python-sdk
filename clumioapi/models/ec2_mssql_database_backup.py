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
        embedded: ec2_mssql_database_backup_embedded_.EC2MSSQLDatabaseBackupEmbedded,
        links: ec2_mssql_database_backup_links_.EC2MSSQLDatabaseBackupLinks,
        database_files: Sequence[mssql_database_file_.MssqlDatabaseFile],
        database_id: str,
        engine: str,
        engine_version: str,
        environment_id: str,
        expiration_timestamp: str,
        host_endpoint: str,
        host_id: str,
        p_id: str,
        instance_id: str,
        instance_name: str,
        start_timestamp: str,
        p_type: str,
    ) -> None:
        """Constructor for the EC2MSSQLDatabaseBackup class."""

        # Initialize members of the class
        self.embedded: ec2_mssql_database_backup_embedded_.EC2MSSQLDatabaseBackupEmbedded = embedded
        self.links: ec2_mssql_database_backup_links_.EC2MSSQLDatabaseBackupLinks = links
        self.database_files: Sequence[mssql_database_file_.MssqlDatabaseFile] = database_files
        self.database_id: str = database_id
        self.engine: str = engine
        self.engine_version: str = engine_version
        self.environment_id: str = environment_id
        self.expiration_timestamp: str = expiration_timestamp
        self.host_endpoint: str = host_endpoint
        self.host_id: str = host_id
        self.p_id: str = p_id
        self.instance_id: str = instance_id
        self.instance_name: str = instance_name
        self.start_timestamp: str = start_timestamp
        self.p_type: str = p_type

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

        # Extract variables from the dictionary
        val = dictionary['_embedded']
        val_embedded = (
            ec2_mssql_database_backup_embedded_.EC2MSSQLDatabaseBackupEmbedded.from_dictionary(val)
        )

        val = dictionary['_links']
        val_links = ec2_mssql_database_backup_links_.EC2MSSQLDatabaseBackupLinks.from_dictionary(
            val
        )

        val = dictionary['database_files']

        val_database_files = None
        if val:
            val_database_files = list()
            for value in val:
                val_database_files.append(
                    mssql_database_file_.MssqlDatabaseFile.from_dictionary(value)
                )

        val = dictionary['database_id']
        val_database_id = val

        val = dictionary['engine']
        val_engine = val

        val = dictionary['engine_version']
        val_engine_version = val

        val = dictionary['environment_id']
        val_environment_id = val

        val = dictionary['expiration_timestamp']
        val_expiration_timestamp = val

        val = dictionary['host_endpoint']
        val_host_endpoint = val

        val = dictionary['host_id']
        val_host_id = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['instance_id']
        val_instance_id = val

        val = dictionary['instance_name']
        val_instance_name = val

        val = dictionary['start_timestamp']
        val_start_timestamp = val

        val = dictionary['type']
        val_p_type = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_database_files,  # type: ignore
            val_database_id,  # type: ignore
            val_engine,  # type: ignore
            val_engine_version,  # type: ignore
            val_environment_id,  # type: ignore
            val_expiration_timestamp,  # type: ignore
            val_host_endpoint,  # type: ignore
            val_host_id,  # type: ignore
            val_p_id,  # type: ignore
            val_instance_id,  # type: ignore
            val_instance_name,  # type: ignore
            val_start_timestamp,  # type: ignore
            val_p_type,  # type: ignore
        )
