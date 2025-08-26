#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import backup_status_info as backup_status_info_
from clumioapi.models import ec2_mssql_database_embedded as ec2_mssql_database_embedded_
from clumioapi.models import ec2_mssql_database_links as ec2_mssql_database_links_
from clumioapi.models import protection_info as protection_info_

T = TypeVar('T', bound='ReadEC2MSSQLDatabaseResponse')


class ReadEC2MSSQLDatabaseResponse:
    """Implementation of the 'ReadEC2MSSQLDatabaseResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        account_native_id:
            The AWS-assigned ID of the account associated with the EC2 instance the database
            resides in.
        availability_group_id:
            The Clumio-assigned ID of the availability group. It is null in case of a
            standalone database.
        availability_group_name:
            The Microsoft SQL assigned name of the availability group. It is null in case of
            a standalone database.
        aws_region:
            The AWS region associated with the EC2 instance the database resides in.
        backup_status_info:
            The backup status information applied to this resource.
        environment_id:
            The Clumio-assigned ID of the AWS environment associated with the EC2 MSSQL
            database.
        failover_cluster_id:
            The Clumio-assigned ID of the failover cluster.
        failover_cluster_name:
            The Microsoft SQL assigned name of the Failover Cluster
        failover_cluster_protection_status:
            Failovercluster Protection Status is used to indicate the fci protection status
            associated with the
            fci database
        host_connection_id:
            The Clumio-assigned ID of the host connection containing the given database.
        host_endpoint:
            The user-provided endpoint of the host containing the given database.
        host_id:
            The Clumio-assigned ID of the host containing the given database.
        p_id:
            The Clumio-assigned ID of the Database.
        instance_id:
            The Clumio-assigned ID of the instance containing the given database.
        instance_name:
            The name of the Microsoft SQL instance containing the given database.
        is_supported:
            is_supported is true if Clumio supports backup of the database.
        last_backup_timestamp:
            The timestamp of the last time this database was full backed up.
            Represented in RFC-3339 format. If this database has never been backed up,
            this field has a value of `null`.
        last_bulk_recovery_model_log_backup_timestamp:
            The timestamp of the last time this database was log backed up in Bulk Recovery
            Model.
            Represented in RFC-3339 format. If this database has never been backed up,
            this field has a value of `null`.
        last_full_recovery_model_log_backup_timestamp:
            The timestamp of the last time this database was log backed up in Full Recovery
            Model.
            Represented in RFC-3339 format. If this database has never been backed up,
            this field has a value of `null`.
        name:
            The name of the Database.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the database.
        protection_info:
            The protection policy applied to this resource. If the resource is not
            protected, then this field has a value of `null`.
        recovery_model:
            recovery_model is the recovery model of the database. Possible values include
            'simple_recovery_model',
            'bulk_recovery_model', and 'full_recovery_model'.
        size:
            The size of the Database.
        status:
            The status of the database, Possible values include 'active' and 'inactive'.
        p_type:
            The type of the database. Possible values include 'availability_group_database'
            and 'standalone_database'.
        unsupported_reason:
            unsupported_reason is the reason why Clumio doesn't support backup of such
            database,
            possible values include 'filestream_enabled_database'.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'account_native_id': 'account_native_id',
        'availability_group_id': 'availability_group_id',
        'availability_group_name': 'availability_group_name',
        'aws_region': 'aws_region',
        'backup_status_info': 'backup_status_info',
        'environment_id': 'environment_id',
        'failover_cluster_id': 'failover_cluster_id',
        'failover_cluster_name': 'failover_cluster_name',
        'failover_cluster_protection_status': 'failover_cluster_protection_status',
        'host_connection_id': 'host_connection_id',
        'host_endpoint': 'host_endpoint',
        'host_id': 'host_id',
        'p_id': 'id',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'is_supported': 'is_supported',
        'last_backup_timestamp': 'last_backup_timestamp',
        'last_bulk_recovery_model_log_backup_timestamp': 'last_bulk_recovery_model_log_backup_timestamp',
        'last_full_recovery_model_log_backup_timestamp': 'last_full_recovery_model_log_backup_timestamp',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
        'recovery_model': 'recovery_model',
        'size': 'size',
        'status': 'status',
        'p_type': 'type',
        'unsupported_reason': 'unsupported_reason',
    }

    def __init__(
        self,
        embedded: ec2_mssql_database_embedded_.EC2MSSQLDatabaseEmbedded | None = None,
        links: ec2_mssql_database_links_.EC2MSSQLDatabaseLinks | None = None,
        account_native_id: str | None = None,
        availability_group_id: str | None = None,
        availability_group_name: str | None = None,
        aws_region: str | None = None,
        backup_status_info: backup_status_info_.BackupStatusInfo | None = None,
        environment_id: str | None = None,
        failover_cluster_id: str | None = None,
        failover_cluster_name: str | None = None,
        failover_cluster_protection_status: str | None = None,
        host_connection_id: str | None = None,
        host_endpoint: str | None = None,
        host_id: str | None = None,
        p_id: str | None = None,
        instance_id: str | None = None,
        instance_name: str | None = None,
        is_supported: bool | None = None,
        last_backup_timestamp: str | None = None,
        last_bulk_recovery_model_log_backup_timestamp: str | None = None,
        last_full_recovery_model_log_backup_timestamp: str | None = None,
        name: str | None = None,
        organizational_unit_id: str | None = None,
        protection_info: protection_info_.ProtectionInfo | None = None,
        recovery_model: str | None = None,
        size: float | None = None,
        status: str | None = None,
        p_type: str | None = None,
        unsupported_reason: str | None = None,
    ) -> None:
        """Constructor for the ReadEC2MSSQLDatabaseResponse class."""

        # Initialize members of the class
        self.embedded: ec2_mssql_database_embedded_.EC2MSSQLDatabaseEmbedded | None = embedded
        self.links: ec2_mssql_database_links_.EC2MSSQLDatabaseLinks | None = links
        self.account_native_id: str | None = account_native_id
        self.availability_group_id: str | None = availability_group_id
        self.availability_group_name: str | None = availability_group_name
        self.aws_region: str | None = aws_region
        self.backup_status_info: backup_status_info_.BackupStatusInfo | None = backup_status_info
        self.environment_id: str | None = environment_id
        self.failover_cluster_id: str | None = failover_cluster_id
        self.failover_cluster_name: str | None = failover_cluster_name
        self.failover_cluster_protection_status: str | None = failover_cluster_protection_status
        self.host_connection_id: str | None = host_connection_id
        self.host_endpoint: str | None = host_endpoint
        self.host_id: str | None = host_id
        self.p_id: str | None = p_id
        self.instance_id: str | None = instance_id
        self.instance_name: str | None = instance_name
        self.is_supported: bool | None = is_supported
        self.last_backup_timestamp: str | None = last_backup_timestamp
        self.last_bulk_recovery_model_log_backup_timestamp: str | None = (
            last_bulk_recovery_model_log_backup_timestamp
        )
        self.last_full_recovery_model_log_backup_timestamp: str | None = (
            last_full_recovery_model_log_backup_timestamp
        )
        self.name: str | None = name
        self.organizational_unit_id: str | None = organizational_unit_id
        self.protection_info: protection_info_.ProtectionInfo | None = protection_info
        self.recovery_model: str | None = recovery_model
        self.size: float | None = size
        self.status: str | None = status
        self.p_type: str | None = p_type
        self.unsupported_reason: str | None = unsupported_reason

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
        val_embedded = ec2_mssql_database_embedded_.EC2MSSQLDatabaseEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = ec2_mssql_database_links_.EC2MSSQLDatabaseLinks.from_dictionary(val)

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('availability_group_id', None)
        val_availability_group_id = val

        val = dictionary.get('availability_group_name', None)
        val_availability_group_name = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('backup_status_info', None)
        val_backup_status_info = backup_status_info_.BackupStatusInfo.from_dictionary(val)

        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('failover_cluster_id', None)
        val_failover_cluster_id = val

        val = dictionary.get('failover_cluster_name', None)
        val_failover_cluster_name = val

        val = dictionary.get('failover_cluster_protection_status', None)
        val_failover_cluster_protection_status = val

        val = dictionary.get('host_connection_id', None)
        val_host_connection_id = val

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

        val = dictionary.get('is_supported', None)
        val_is_supported = val

        val = dictionary.get('last_backup_timestamp', None)
        val_last_backup_timestamp = val

        val = dictionary.get('last_bulk_recovery_model_log_backup_timestamp', None)
        val_last_bulk_recovery_model_log_backup_timestamp = val

        val = dictionary.get('last_full_recovery_model_log_backup_timestamp', None)
        val_last_full_recovery_model_log_backup_timestamp = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('protection_info', None)
        val_protection_info = protection_info_.ProtectionInfo.from_dictionary(val)

        val = dictionary.get('recovery_model', None)
        val_recovery_model = val

        val = dictionary.get('size', None)
        val_size = val

        val = dictionary.get('status', None)
        val_status = val

        val = dictionary.get('type', None)
        val_p_type = val

        val = dictionary.get('unsupported_reason', None)
        val_unsupported_reason = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_account_native_id,
            val_availability_group_id,
            val_availability_group_name,
            val_aws_region,
            val_backup_status_info,
            val_environment_id,
            val_failover_cluster_id,
            val_failover_cluster_name,
            val_failover_cluster_protection_status,
            val_host_connection_id,
            val_host_endpoint,
            val_host_id,
            val_p_id,
            val_instance_id,
            val_instance_name,
            val_is_supported,
            val_last_backup_timestamp,
            val_last_bulk_recovery_model_log_backup_timestamp,
            val_last_full_recovery_model_log_backup_timestamp,
            val_name,
            val_organizational_unit_id,
            val_protection_info,
            val_recovery_model,
            val_size,
            val_status,
            val_p_type,
            val_unsupported_reason,
        )
