#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import mssql_database_backup_embedded
from clumioapi.models import mssql_database_backup_links
from clumioapi.models import mssql_database_file

T = TypeVar('T', bound='ReadMssqlDatabaseBackupResponse')


class ReadMssqlDatabaseBackupResponse:
    """Implementation of the 'ReadMssqlDatabaseBackupResponse' model.

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
        expiration_timestamp:
            The timestamp of when this backup expires. Represented in RFC-3339 format.
        group_id:
            The Clumio-assigned ID of the management group associated with the database at
            the time of backup.
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
        subgroup_id:
            The Clumio-assigned ID of the management subgroup associated with the database
            at the time of backup.
        p_type:
            The type of backup. Possible values include `mssql_database_backup`,
            `mssql_log_backup_full_recovery_model` and `mssql_log_backup_bulk_logged_model`.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'database_files': 'database_files',
        'database_id': 'database_id',
        'engine': 'engine',
        'engine_version': 'engine_version',
        'expiration_timestamp': 'expiration_timestamp',
        'group_id': 'group_id',
        'host_endpoint': 'host_endpoint',
        'host_id': 'host_id',
        'p_id': 'id',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'start_timestamp': 'start_timestamp',
        'subgroup_id': 'subgroup_id',
        'p_type': 'type',
    }

    def __init__(
        self,
        embedded: mssql_database_backup_embedded.MssqlDatabaseBackupEmbedded = None,
        links: mssql_database_backup_links.MssqlDatabaseBackupLinks = None,
        database_files: Sequence[mssql_database_file.MssqlDatabaseFile] = None,
        database_id: str = None,
        engine: str = None,
        engine_version: str = None,
        expiration_timestamp: str = None,
        group_id: str = None,
        host_endpoint: str = None,
        host_id: str = None,
        p_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        start_timestamp: str = None,
        subgroup_id: str = None,
        p_type: str = None,
    ) -> None:
        """Constructor for the ReadMssqlDatabaseBackupResponse class."""

        # Initialize members of the class
        self.embedded: mssql_database_backup_embedded.MssqlDatabaseBackupEmbedded = embedded
        self.links: mssql_database_backup_links.MssqlDatabaseBackupLinks = links
        self.database_files: Sequence[mssql_database_file.MssqlDatabaseFile] = database_files
        self.database_id: str = database_id
        self.engine: str = engine
        self.engine_version: str = engine_version
        self.expiration_timestamp: str = expiration_timestamp
        self.group_id: str = group_id
        self.host_endpoint: str = host_endpoint
        self.host_id: str = host_id
        self.p_id: str = p_id
        self.instance_id: str = instance_id
        self.instance_name: str = instance_name
        self.start_timestamp: str = start_timestamp
        self.subgroup_id: str = subgroup_id
        self.p_type: str = p_type

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
        key = '_embedded'
        embedded = (
            mssql_database_backup_embedded.MssqlDatabaseBackupEmbedded.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            mssql_database_backup_links.MssqlDatabaseBackupLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        database_files = None
        if dictionary.get('database_files'):
            database_files = list()
            for value in dictionary.get('database_files'):
                database_files.append(mssql_database_file.MssqlDatabaseFile.from_dictionary(value))

        database_id = dictionary.get('database_id')
        engine = dictionary.get('engine')
        engine_version = dictionary.get('engine_version')
        expiration_timestamp = dictionary.get('expiration_timestamp')
        group_id = dictionary.get('group_id')
        host_endpoint = dictionary.get('host_endpoint')
        host_id = dictionary.get('host_id')
        p_id = dictionary.get('id')
        instance_id = dictionary.get('instance_id')
        instance_name = dictionary.get('instance_name')
        start_timestamp = dictionary.get('start_timestamp')
        subgroup_id = dictionary.get('subgroup_id')
        p_type = dictionary.get('type')
        # Return an object of this model
        return cls(
            embedded,
            links,
            database_files,
            database_id,
            engine,
            engine_version,
            expiration_timestamp,
            group_id,
            host_endpoint,
            host_id,
            p_id,
            instance_id,
            instance_name,
            start_timestamp,
            subgroup_id,
            p_type,
        )
