#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import ebs_backup_advanced_setting as ebs_backup_advanced_setting_
from clumioapi.models import ec2_backup_advanced_setting as ec2_backup_advanced_setting_
from clumioapi.models import \
    ec2_mssql_database_backup_advanced_setting as ec2_mssql_database_backup_advanced_setting_
from clumioapi.models import \
    ec2_mssql_log_backup_advanced_setting as ec2_mssql_log_backup_advanced_setting_
from clumioapi.models import iceberg_backup_advanced_setting as iceberg_backup_advanced_setting_
from clumioapi.models import \
    mssql_database_backup_advanced_setting as mssql_database_backup_advanced_setting_
from clumioapi.models import mssql_log_backup_advanced_setting as mssql_log_backup_advanced_setting_
from clumioapi.models import \
    oracle_database_backup_advanced_setting as oracle_database_backup_advanced_setting_
from clumioapi.models import \
    oracle_log_backup_advanced_setting as oracle_log_backup_advanced_setting_
from clumioapi.models import \
    protection_group_backup_advanced_setting as protection_group_backup_advanced_setting_
from clumioapi.models import \
    protection_group_continuous_backup_advanced_setting as \
    protection_group_continuous_backup_advanced_setting_
from clumioapi.models import rds_config_sync_advanced_setting as rds_config_sync_advanced_setting_
from clumioapi.models import \
    rds_logical_backup_advanced_setting as rds_logical_backup_advanced_setting_
import requests

T = TypeVar('T', bound='PolicyAdvancedSettings')


@dataclasses.dataclass
class PolicyAdvancedSettings:
    """Implementation of the 'PolicyAdvancedSettings' model.

    Additional operation-specific policy settings. For operation types which do not
    support additional settings, this field is `null`.

    Attributes:
        AwsEbsVolumeBackup:
            Advanced settings for ebs backup.

        AwsEc2InstanceBackup:
            Advanced settings for ec2 backup.

        AwsIcebergTableBackup:
            Icebergbackupadvancedsetting defines the advanced settings for iceberg backup operations.

        AwsRdsConfigSync:
            Advanced settings for rds pitr configuration sync.

        AwsRdsResourceGranularBackup:
            Settings for determining if a rds policy is created with standard or archive tier.

        Ec2MssqlDatabaseBackup:
            Additional policy configuration settings for the `ec2_mssql_database_backup` operation. if this operation is not of type `ec2_mssql_database_backup`, then this field is omitted from the response.

        Ec2MssqlLogBackup:
            Additional policy configuration settings for the `ec2_mssql_log_backup` operation. if this operation is not of type `ec2_mssql_log_backup`, then this field is omitted from the response.

        MssqlDatabaseBackup:
            Additional policy configuration settings for the `mssql_database_backup` operation. if this operation is not of type `mssql_database_backup`, then this field is omitted from the response.

        MssqlLogBackup:
            Additional policy configuration settings for the `mssql_log_backup` operation. if this operation is not of type `mssql_log_backup`, then this field is omitted from the response.

        OracleDatabaseBackup:
            Additional policy configuration settings for the `oracle_database_backup` operation. if this operation is not of type `oracle_database_backup`, then this field is omitted from the response.

        OracleLogBackup:
            Additional policy configuration settings for the `oracle_log_backup` operation. if this operation is not of type `oracle_log_backup`, then this field is omitted from the response.

        ProtectionGroupBackup:
            Additional policy configuration settings for the `protection_group_backup` operation. if this operation is not of type `protection_group_backup`, then this field is omitted from the response.

        ProtectionGroupContinuousBackup:
            Additional policy configuration settings for the `protection_group_continuous_backup` operation. if this operation is not of type `protection_group_continuous_backup`, then this field is omitted from the response.

    """

    AwsEbsVolumeBackup: ebs_backup_advanced_setting_.EBSBackupAdvancedSetting | None = None
    AwsEc2InstanceBackup: ec2_backup_advanced_setting_.EC2BackupAdvancedSetting | None = None
    AwsIcebergTableBackup: iceberg_backup_advanced_setting_.IcebergBackupAdvancedSetting | None = (
        None
    )
    AwsRdsConfigSync: rds_config_sync_advanced_setting_.RDSConfigSyncAdvancedSetting | None = None
    AwsRdsResourceGranularBackup: (
        rds_logical_backup_advanced_setting_.RDSLogicalBackupAdvancedSetting | None
    ) = None
    Ec2MssqlDatabaseBackup: (
        ec2_mssql_database_backup_advanced_setting_.EC2MSSQLDatabaseBackupAdvancedSetting | None
    ) = None
    Ec2MssqlLogBackup: (
        ec2_mssql_log_backup_advanced_setting_.EC2MSSQLLogBackupAdvancedSetting | None
    ) = None
    MssqlDatabaseBackup: (
        mssql_database_backup_advanced_setting_.MSSQLDatabaseBackupAdvancedSetting | None
    ) = None
    MssqlLogBackup: mssql_log_backup_advanced_setting_.MSSQLLogBackupAdvancedSetting | None = None
    OracleDatabaseBackup: (
        oracle_database_backup_advanced_setting_.OracleDatabaseBackupAdvancedSetting | None
    ) = None
    OracleLogBackup: oracle_log_backup_advanced_setting_.OracleLogBackupAdvancedSetting | None = (
        None
    )
    ProtectionGroupBackup: (
        protection_group_backup_advanced_setting_.ProtectionGroupBackupAdvancedSetting | None
    ) = None
    ProtectionGroupContinuousBackup: (
        protection_group_continuous_backup_advanced_setting_.ProtectionGroupContinuousBackupAdvancedSetting
        | None
    ) = None

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
        val = dictionary.get('aws_ebs_volume_backup', None)
        val_aws_ebs_volume_backup = (
            ebs_backup_advanced_setting_.EBSBackupAdvancedSetting.from_dictionary(val)
        )

        val = dictionary.get('aws_ec2_instance_backup', None)
        val_aws_ec2_instance_backup = (
            ec2_backup_advanced_setting_.EC2BackupAdvancedSetting.from_dictionary(val)
        )

        val = dictionary.get('aws_iceberg_table_backup', None)
        val_aws_iceberg_table_backup = (
            iceberg_backup_advanced_setting_.IcebergBackupAdvancedSetting.from_dictionary(val)
        )

        val = dictionary.get('aws_rds_config_sync', None)
        val_aws_rds_config_sync = (
            rds_config_sync_advanced_setting_.RDSConfigSyncAdvancedSetting.from_dictionary(val)
        )

        val = dictionary.get('aws_rds_resource_granular_backup', None)
        val_aws_rds_resource_granular_backup = (
            rds_logical_backup_advanced_setting_.RDSLogicalBackupAdvancedSetting.from_dictionary(
                val
            )
        )

        val = dictionary.get('ec2_mssql_database_backup', None)
        val_ec2_mssql_database_backup = ec2_mssql_database_backup_advanced_setting_.EC2MSSQLDatabaseBackupAdvancedSetting.from_dictionary(
            val
        )

        val = dictionary.get('ec2_mssql_log_backup', None)
        val_ec2_mssql_log_backup = (
            ec2_mssql_log_backup_advanced_setting_.EC2MSSQLLogBackupAdvancedSetting.from_dictionary(
                val
            )
        )

        val = dictionary.get('mssql_database_backup', None)
        val_mssql_database_backup = mssql_database_backup_advanced_setting_.MSSQLDatabaseBackupAdvancedSetting.from_dictionary(
            val
        )

        val = dictionary.get('mssql_log_backup', None)
        val_mssql_log_backup = (
            mssql_log_backup_advanced_setting_.MSSQLLogBackupAdvancedSetting.from_dictionary(val)
        )

        val = dictionary.get('oracle_database_backup', None)
        val_oracle_database_backup = oracle_database_backup_advanced_setting_.OracleDatabaseBackupAdvancedSetting.from_dictionary(
            val
        )

        val = dictionary.get('oracle_log_backup', None)
        val_oracle_log_backup = (
            oracle_log_backup_advanced_setting_.OracleLogBackupAdvancedSetting.from_dictionary(val)
        )

        val = dictionary.get('protection_group_backup', None)
        val_protection_group_backup = protection_group_backup_advanced_setting_.ProtectionGroupBackupAdvancedSetting.from_dictionary(
            val
        )

        val = dictionary.get('protection_group_continuous_backup', None)
        val_protection_group_continuous_backup = protection_group_continuous_backup_advanced_setting_.ProtectionGroupContinuousBackupAdvancedSetting.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_aws_ebs_volume_backup,
            val_aws_ec2_instance_backup,
            val_aws_iceberg_table_backup,
            val_aws_rds_config_sync,
            val_aws_rds_resource_granular_backup,
            val_ec2_mssql_database_backup,
            val_ec2_mssql_log_backup,
            val_mssql_database_backup,
            val_mssql_log_backup,
            val_oracle_database_backup,
            val_oracle_log_backup,
            val_protection_group_backup,
            val_protection_group_continuous_backup,
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
