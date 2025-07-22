#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import backup_status_info as backup_status_info_
from clumioapi.models import ec2_mssql_database_embedded as ec2_mssql_database_embedded_
from clumioapi.models import ec2_mssql_database_links as ec2_mssql_database_links_
from clumioapi.models import protection_info as protection_info_

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
        embedded: ec2_mssql_database_embedded_.EC2MSSQLDatabaseEmbedded,
        links: ec2_mssql_database_links_.EC2MSSQLDatabaseLinks,
        account_native_id: str,
        availability_group_id: str,
        availability_group_name: str,
        aws_region: str,
        backup_status_info: backup_status_info_.BackupStatusInfo,
        environment_id: str,
        failover_cluster_id: str,
        failover_cluster_name: str,
        failover_cluster_protection_status: str,
        host_connection_id: str,
        host_endpoint: str,
        host_id: str,
        p_id: str,
        instance_id: str,
        instance_name: str,
        is_supported: bool,
        last_backup_timestamp: str,
        last_bulk_recovery_model_log_backup_timestamp: str,
        last_full_recovery_model_log_backup_timestamp: str,
        name: str,
        organizational_unit_id: str,
        protection_info: protection_info_.ProtectionInfo,
        recovery_model: str,
        size: float,
        status: str,
        p_type: str,
        unsupported_reason: str,
    ) -> None:
        """Constructor for the EC2MSSQLDatabase class."""

        # Initialize members of the class
        self.embedded: ec2_mssql_database_embedded_.EC2MSSQLDatabaseEmbedded = embedded
        self.links: ec2_mssql_database_links_.EC2MSSQLDatabaseLinks = links
        self.account_native_id: str = account_native_id
        self.availability_group_id: str = availability_group_id
        self.availability_group_name: str = availability_group_name
        self.aws_region: str = aws_region
        self.backup_status_info: backup_status_info_.BackupStatusInfo = backup_status_info
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
        self.protection_info: protection_info_.ProtectionInfo = protection_info
        self.recovery_model: str = recovery_model
        self.size: float = size
        self.status: str = status
        self.p_type: str = p_type
        self.unsupported_reason: str = unsupported_reason

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
        val_embedded = ec2_mssql_database_embedded_.EC2MSSQLDatabaseEmbedded.from_dictionary(val)

        val = dictionary['_links']
        val_links = ec2_mssql_database_links_.EC2MSSQLDatabaseLinks.from_dictionary(val)

        val = dictionary['account_native_id']
        val_account_native_id = val

        val = dictionary['availability_group_id']
        val_availability_group_id = val

        val = dictionary['availability_group_name']
        val_availability_group_name = val

        val = dictionary['aws_region']
        val_aws_region = val

        val = dictionary['backup_status_info']
        val_backup_status_info = backup_status_info_.BackupStatusInfo.from_dictionary(val)

        val = dictionary['environment_id']
        val_environment_id = val

        val = dictionary['failover_cluster_id']
        val_failover_cluster_id = val

        val = dictionary['failover_cluster_name']
        val_failover_cluster_name = val

        val = dictionary['failover_cluster_protection_status']
        val_failover_cluster_protection_status = val

        val = dictionary['host_connection_id']
        val_host_connection_id = val

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

        val = dictionary['is_supported']
        val_is_supported = val

        val = dictionary['last_backup_timestamp']
        val_last_backup_timestamp = val

        val = dictionary['last_bulk_recovery_model_log_backup_timestamp']
        val_last_bulk_recovery_model_log_backup_timestamp = val

        val = dictionary['last_full_recovery_model_log_backup_timestamp']
        val_last_full_recovery_model_log_backup_timestamp = val

        val = dictionary['name']
        val_name = val

        val = dictionary['organizational_unit_id']
        val_organizational_unit_id = val

        val = dictionary['protection_info']
        val_protection_info = protection_info_.ProtectionInfo.from_dictionary(val)

        val = dictionary['recovery_model']
        val_recovery_model = val

        val = dictionary['size']
        val_size = val

        val = dictionary['status']
        val_status = val

        val = dictionary['type']
        val_p_type = val

        val = dictionary['unsupported_reason']
        val_unsupported_reason = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_account_native_id,  # type: ignore
            val_availability_group_id,  # type: ignore
            val_availability_group_name,  # type: ignore
            val_aws_region,  # type: ignore
            val_backup_status_info,  # type: ignore
            val_environment_id,  # type: ignore
            val_failover_cluster_id,  # type: ignore
            val_failover_cluster_name,  # type: ignore
            val_failover_cluster_protection_status,  # type: ignore
            val_host_connection_id,  # type: ignore
            val_host_endpoint,  # type: ignore
            val_host_id,  # type: ignore
            val_p_id,  # type: ignore
            val_instance_id,  # type: ignore
            val_instance_name,  # type: ignore
            val_is_supported,  # type: ignore
            val_last_backup_timestamp,  # type: ignore
            val_last_bulk_recovery_model_log_backup_timestamp,  # type: ignore
            val_last_full_recovery_model_log_backup_timestamp,  # type: ignore
            val_name,  # type: ignore
            val_organizational_unit_id,  # type: ignore
            val_protection_info,  # type: ignore
            val_recovery_model,  # type: ignore
            val_size,  # type: ignore
            val_status,  # type: ignore
            val_p_type,  # type: ignore
            val_unsupported_reason,  # type: ignore
        )
