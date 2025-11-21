#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import backup_status_info as backup_status_info_
from clumioapi.models import ec2_mssql_database_embedded as ec2_mssql_database_embedded_
from clumioapi.models import ec2_mssql_database_links as ec2_mssql_database_links_
from clumioapi.models import protection_info as protection_info_
import requests

T = TypeVar('T', bound='ReadEC2MSSQLDatabaseResponse')


@dataclasses.dataclass
class ReadEC2MSSQLDatabaseResponse:
    """Implementation of the 'ReadEC2MSSQLDatabaseResponse' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        AccountNativeId:
            The aws-assigned id of the account associated with the ec2 instance the database
            resides in.

        AvailabilityGroupId:
            The clumio-assigned id of the availability group. it is null in case of a
            standalone database.

        AvailabilityGroupName:
            The microsoft sql assigned name of the availability group. it is null in case of
            a standalone database.

        AwsRegion:
            The aws region associated with the ec2 instance the database resides in.

        BackupStatusInfo:
            The backup status information applied to this resource.

        EnvironmentId:
            The clumio-assigned id of the aws environment associated with the ec2 mssql
            database.

        FailoverClusterId:
            The clumio-assigned id of the failover cluster.

        FailoverClusterName:
            The microsoft sql assigned name of the failover cluster.

        FailoverClusterProtectionStatus:
            Failovercluster protection status is used to indicate the fci protection status
            associated with the
            fci database.

        HostConnectionId:
            The clumio-assigned id of the host connection containing the given database.

        HostEndpoint:
            The user-provided endpoint of the host containing the given database.

        HostId:
            The clumio-assigned id of the host containing the given database.

        Id:
            The clumio-assigned id of the database.

        InstanceId:
            The clumio-assigned id of the instance containing the given database.

        InstanceName:
            The name of the microsoft sql instance containing the given database.

        IsSupported:
            Is_supported is true if clumio supports backup of the database.

        LastBackupTimestamp:
            The timestamp of the last time this database was full backed up.
            represented in rfc-3339 format. if this database has never been backed up,
            this field has a value of `null`.

        LastBulkRecoveryModelLogBackupTimestamp:
            The timestamp of the last time this database was log backed up in bulk recovery
            model.
            represented in rfc-3339 format. if this database has never been backed up,
            this field has a value of `null`.

        LastFullRecoveryModelLogBackupTimestamp:
            The timestamp of the last time this database was log backed up in full recovery
            model.
            represented in rfc-3339 format. if this database has never been backed up,
            this field has a value of `null`.

        Name:
            The name of the database.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the database.

        ProtectionInfo:
            The protection policy applied to this resource. if the resource is not
            protected, then this field has a value of `null`.

        RecoveryModel:
            Recovery_model is the recovery model of the database. possible values include
            'simple_recovery_model',
            'bulk_recovery_model', and 'full_recovery_model'.

        Size:
            The size of the database.

        Status:
            The status of the database, possible values include 'active' and 'inactive'.

        Type:
            The type of the database. possible values include 'availability_group_database'
            and 'standalone_database'.

        UnsupportedReason:
            Unsupported_reason is the reason why clumio doesn't support backup of such
            database,
            possible values include 'filestream_enabled_database'.

    """

    Embedded: ec2_mssql_database_embedded_.EC2MSSQLDatabaseEmbedded | None = None
    Links: ec2_mssql_database_links_.EC2MSSQLDatabaseLinks | None = None
    AccountNativeId: str | None = None
    AvailabilityGroupId: str | None = None
    AvailabilityGroupName: str | None = None
    AwsRegion: str | None = None
    BackupStatusInfo: backup_status_info_.BackupStatusInfo | None = None
    EnvironmentId: str | None = None
    FailoverClusterId: str | None = None
    FailoverClusterName: str | None = None
    FailoverClusterProtectionStatus: str | None = None
    HostConnectionId: str | None = None
    HostEndpoint: str | None = None
    HostId: str | None = None
    Id: str | None = None
    InstanceId: str | None = None
    InstanceName: str | None = None
    IsSupported: bool | None = None
    LastBackupTimestamp: str | None = None
    LastBulkRecoveryModelLogBackupTimestamp: str | None = None
    LastFullRecoveryModelLogBackupTimestamp: str | None = None
    Name: str | None = None
    OrganizationalUnitId: str | None = None
    ProtectionInfo: protection_info_.ProtectionInfo | None = None
    RecoveryModel: str | None = None
    Size: float | None = None
    Status: str | None = None
    Type: str | None = None
    UnsupportedReason: str | None = None
    raw_response: Optional[requests.Response] = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val_id = val

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
        val_type = val

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
            val_id,
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
            val_type,
            val_unsupported_reason,
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
