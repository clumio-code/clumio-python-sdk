#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import backup_status_info
from clumioapi.models import ec2_mssql_database_embedded
from clumioapi.models import ec2_mssql_database_links
from clumioapi.models import protection_info

T = TypeVar('T', bound='EC2MSSQLDatabase')


class EC2MSSQLDatabase:
    """Implementation of the 'EC2MSSQLDatabase' model.

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
    _names = {
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
        embedded: ec2_mssql_database_embedded.EC2MSSQLDatabaseEmbedded = None,
        links: ec2_mssql_database_links.EC2MSSQLDatabaseLinks = None,
        account_native_id: str = None,
        availability_group_id: str = None,
        availability_group_name: str = None,
        aws_region: str = None,
        backup_status_info: backup_status_info.BackupStatusInfo = None,
        environment_id: str = None,
        failover_cluster_id: str = None,
        failover_cluster_name: str = None,
        failover_cluster_protection_status: str = None,
        host_connection_id: str = None,
        host_endpoint: str = None,
        host_id: str = None,
        p_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        is_supported: bool = None,
        last_backup_timestamp: str = None,
        last_bulk_recovery_model_log_backup_timestamp: str = None,
        last_full_recovery_model_log_backup_timestamp: str = None,
        name: str = None,
        organizational_unit_id: str = None,
        protection_info: protection_info.ProtectionInfo = None,
        recovery_model: str = None,
        size: float = None,
        status: str = None,
        p_type: str = None,
        unsupported_reason: str = None,
    ) -> None:
        """Constructor for the EC2MSSQLDatabase class."""

        # Initialize members of the class
        self.embedded: ec2_mssql_database_embedded.EC2MSSQLDatabaseEmbedded = embedded
        self.links: ec2_mssql_database_links.EC2MSSQLDatabaseLinks = links
        self.account_native_id: str = account_native_id
        self.availability_group_id: str = availability_group_id
        self.availability_group_name: str = availability_group_name
        self.aws_region: str = aws_region
        self.backup_status_info: backup_status_info.BackupStatusInfo = backup_status_info
        self.environment_id: str = environment_id
        self.failover_cluster_id: str = failover_cluster_id
        self.failover_cluster_name: str = failover_cluster_name
        self.failover_cluster_protection_status: str = failover_cluster_protection_status
        self.host_connection_id: str = host_connection_id
        self.host_endpoint: str = host_endpoint
        self.host_id: str = host_id
        self.p_id: str = p_id
        self.instance_id: str = instance_id
        self.instance_name: str = instance_name
        self.is_supported: bool = is_supported
        self.last_backup_timestamp: str = last_backup_timestamp
        self.last_bulk_recovery_model_log_backup_timestamp: str = (
            last_bulk_recovery_model_log_backup_timestamp
        )
        self.last_full_recovery_model_log_backup_timestamp: str = (
            last_full_recovery_model_log_backup_timestamp
        )
        self.name: str = name
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info.ProtectionInfo = protection_info
        self.recovery_model: str = recovery_model
        self.size: float = size
        self.status: str = status
        self.p_type: str = p_type
        self.unsupported_reason: str = unsupported_reason

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
            ec2_mssql_database_embedded.EC2MSSQLDatabaseEmbedded.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            ec2_mssql_database_links.EC2MSSQLDatabaseLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        account_native_id = dictionary.get('account_native_id')
        availability_group_id = dictionary.get('availability_group_id')
        availability_group_name = dictionary.get('availability_group_name')
        aws_region = dictionary.get('aws_region')
        key = 'backup_status_info'
        p_backup_status_info = (
            backup_status_info.BackupStatusInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        environment_id = dictionary.get('environment_id')
        failover_cluster_id = dictionary.get('failover_cluster_id')
        failover_cluster_name = dictionary.get('failover_cluster_name')
        failover_cluster_protection_status = dictionary.get('failover_cluster_protection_status')
        host_connection_id = dictionary.get('host_connection_id')
        host_endpoint = dictionary.get('host_endpoint')
        host_id = dictionary.get('host_id')
        p_id = dictionary.get('id')
        instance_id = dictionary.get('instance_id')
        instance_name = dictionary.get('instance_name')
        is_supported = dictionary.get('is_supported')
        last_backup_timestamp = dictionary.get('last_backup_timestamp')
        last_bulk_recovery_model_log_backup_timestamp = dictionary.get(
            'last_bulk_recovery_model_log_backup_timestamp'
        )
        last_full_recovery_model_log_backup_timestamp = dictionary.get(
            'last_full_recovery_model_log_backup_timestamp'
        )
        name = dictionary.get('name')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        key = 'protection_info'
        p_protection_info = (
            protection_info.ProtectionInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        recovery_model = dictionary.get('recovery_model')
        size = dictionary.get('size')
        status = dictionary.get('status')
        p_type = dictionary.get('type')
        unsupported_reason = dictionary.get('unsupported_reason')
        # Return an object of this model
        return cls(
            embedded,
            links,
            account_native_id,
            availability_group_id,
            availability_group_name,
            aws_region,
            p_backup_status_info,
            environment_id,
            failover_cluster_id,
            failover_cluster_name,
            failover_cluster_protection_status,
            host_connection_id,
            host_endpoint,
            host_id,
            p_id,
            instance_id,
            instance_name,
            is_supported,
            last_backup_timestamp,
            last_bulk_recovery_model_log_backup_timestamp,
            last_full_recovery_model_log_backup_timestamp,
            name,
            organizational_unit_id,
            p_protection_info,
            recovery_model,
            size,
            status,
            p_type,
            unsupported_reason,
        )
