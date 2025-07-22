#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

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

T = TypeVar('T', bound='PolicyAdvancedSettings')


class PolicyAdvancedSettings:
    """Implementation of the 'PolicyAdvancedSettings' model.

    Additional operation-specific policy settings. For operation types which do not
    support additional settings, this field is `null`.

    Attributes:
        aws_ebs_volume_backup:
            Advanced settings for EBS backup.
        aws_ec2_instance_backup:
            Advanced settings for EC2 backup.
        aws_iceberg_table_backup:
            IcebergBackupAdvancedSetting defines the advanced settings for Iceberg backup
            operations
        aws_rds_config_sync:
            Advanced settings for RDS PITR configuration sync.
        aws_rds_resource_granular_backup:
            Settings for determining if a RDS policy is created with standard or archive
            tier.
        ec2_mssql_database_backup:
            Additional policy configuration settings for the `ec2_mssql_database_backup`
            operation. If this operation is not of type `ec2_mssql_database_backup`, then
            this field is omitted from the response.
        ec2_mssql_log_backup:
            Additional policy configuration settings for the `ec2_mssql_log_backup`
            operation. If this operation is not of type `ec2_mssql_log_backup`, then this
            field is omitted from the response.
        mssql_database_backup:
            Additional policy configuration settings for the `mssql_database_backup`
            operation. If this operation is not of type `mssql_database_backup`, then this
            field is omitted from the response.
        mssql_log_backup:
            Additional policy configuration settings for the `mssql_log_backup` operation.
            If this operation is not of type `mssql_log_backup`, then this field is omitted
            from the response.
        oracle_database_backup:
            Additional policy configuration settings for the `oracle_database_backup`
            operation. If this operation is not of type `oracle_database_backup`, then this
            field is omitted from the response.
        oracle_log_backup:
            Additional policy configuration settings for the `oracle_log_backup` operation.
            If this operation is not of type `oracle_log_backup`, then this field is omitted
            from the response.
        protection_group_backup:
            Additional policy configuration settings for the `protection_group_backup`
            operation. If this operation is not of type `protection_group_backup`, then this
            field is omitted from the response.
        protection_group_continuous_backup:
            Additional policy configuration settings for the
            `protection_group_continuous_backup` operation. If this operation is not of type
            `protection_group_continuous_backup`, then this field is omitted from the
            response.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'aws_ebs_volume_backup': 'aws_ebs_volume_backup',
        'aws_ec2_instance_backup': 'aws_ec2_instance_backup',
        'aws_iceberg_table_backup': 'aws_iceberg_table_backup',
        'aws_rds_config_sync': 'aws_rds_config_sync',
        'aws_rds_resource_granular_backup': 'aws_rds_resource_granular_backup',
        'ec2_mssql_database_backup': 'ec2_mssql_database_backup',
        'ec2_mssql_log_backup': 'ec2_mssql_log_backup',
        'mssql_database_backup': 'mssql_database_backup',
        'mssql_log_backup': 'mssql_log_backup',
        'oracle_database_backup': 'oracle_database_backup',
        'oracle_log_backup': 'oracle_log_backup',
        'protection_group_backup': 'protection_group_backup',
        'protection_group_continuous_backup': 'protection_group_continuous_backup',
    }

    def __init__(
        self,
        aws_ebs_volume_backup: ebs_backup_advanced_setting_.EBSBackupAdvancedSetting,
        aws_ec2_instance_backup: ec2_backup_advanced_setting_.EC2BackupAdvancedSetting,
        aws_iceberg_table_backup: iceberg_backup_advanced_setting_.IcebergBackupAdvancedSetting,
        aws_rds_config_sync: rds_config_sync_advanced_setting_.RDSConfigSyncAdvancedSetting,
        aws_rds_resource_granular_backup: rds_logical_backup_advanced_setting_.RDSLogicalBackupAdvancedSetting,
        ec2_mssql_database_backup: ec2_mssql_database_backup_advanced_setting_.EC2MSSQLDatabaseBackupAdvancedSetting,
        ec2_mssql_log_backup: ec2_mssql_log_backup_advanced_setting_.EC2MSSQLLogBackupAdvancedSetting,
        mssql_database_backup: mssql_database_backup_advanced_setting_.MSSQLDatabaseBackupAdvancedSetting,
        mssql_log_backup: mssql_log_backup_advanced_setting_.MSSQLLogBackupAdvancedSetting,
        oracle_database_backup: oracle_database_backup_advanced_setting_.OracleDatabaseBackupAdvancedSetting,
        oracle_log_backup: oracle_log_backup_advanced_setting_.OracleLogBackupAdvancedSetting,
        protection_group_backup: protection_group_backup_advanced_setting_.ProtectionGroupBackupAdvancedSetting,
        protection_group_continuous_backup: protection_group_continuous_backup_advanced_setting_.ProtectionGroupContinuousBackupAdvancedSetting,
    ) -> None:
        """Constructor for the PolicyAdvancedSettings class."""

        # Initialize members of the class
        self.aws_ebs_volume_backup: ebs_backup_advanced_setting_.EBSBackupAdvancedSetting = (
            aws_ebs_volume_backup
        )
        self.aws_ec2_instance_backup: ec2_backup_advanced_setting_.EC2BackupAdvancedSetting = (
            aws_ec2_instance_backup
        )
        self.aws_iceberg_table_backup: (
            iceberg_backup_advanced_setting_.IcebergBackupAdvancedSetting
        ) = aws_iceberg_table_backup
        self.aws_rds_config_sync: rds_config_sync_advanced_setting_.RDSConfigSyncAdvancedSetting = (
            aws_rds_config_sync
        )
        self.aws_rds_resource_granular_backup: (
            rds_logical_backup_advanced_setting_.RDSLogicalBackupAdvancedSetting
        ) = aws_rds_resource_granular_backup
        self.ec2_mssql_database_backup: (
            ec2_mssql_database_backup_advanced_setting_.EC2MSSQLDatabaseBackupAdvancedSetting
        ) = ec2_mssql_database_backup
        self.ec2_mssql_log_backup: (
            ec2_mssql_log_backup_advanced_setting_.EC2MSSQLLogBackupAdvancedSetting
        ) = ec2_mssql_log_backup
        self.mssql_database_backup: (
            mssql_database_backup_advanced_setting_.MSSQLDatabaseBackupAdvancedSetting
        ) = mssql_database_backup
        self.mssql_log_backup: mssql_log_backup_advanced_setting_.MSSQLLogBackupAdvancedSetting = (
            mssql_log_backup
        )
        self.oracle_database_backup: (
            oracle_database_backup_advanced_setting_.OracleDatabaseBackupAdvancedSetting
        ) = oracle_database_backup
        self.oracle_log_backup: (
            oracle_log_backup_advanced_setting_.OracleLogBackupAdvancedSetting
        ) = oracle_log_backup
        self.protection_group_backup: (
            protection_group_backup_advanced_setting_.ProtectionGroupBackupAdvancedSetting
        ) = protection_group_backup
        self.protection_group_continuous_backup: (
            protection_group_continuous_backup_advanced_setting_.ProtectionGroupContinuousBackupAdvancedSetting
        ) = protection_group_continuous_backup

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
        val = dictionary['aws_ebs_volume_backup']
        val_aws_ebs_volume_backup = (
            ebs_backup_advanced_setting_.EBSBackupAdvancedSetting.from_dictionary(val)
        )

        val = dictionary['aws_ec2_instance_backup']
        val_aws_ec2_instance_backup = (
            ec2_backup_advanced_setting_.EC2BackupAdvancedSetting.from_dictionary(val)
        )

        val = dictionary['aws_iceberg_table_backup']
        val_aws_iceberg_table_backup = (
            iceberg_backup_advanced_setting_.IcebergBackupAdvancedSetting.from_dictionary(val)
        )

        val = dictionary['aws_rds_config_sync']
        val_aws_rds_config_sync = (
            rds_config_sync_advanced_setting_.RDSConfigSyncAdvancedSetting.from_dictionary(val)
        )

        val = dictionary['aws_rds_resource_granular_backup']
        val_aws_rds_resource_granular_backup = (
            rds_logical_backup_advanced_setting_.RDSLogicalBackupAdvancedSetting.from_dictionary(
                val
            )
        )

        val = dictionary['ec2_mssql_database_backup']
        val_ec2_mssql_database_backup = ec2_mssql_database_backup_advanced_setting_.EC2MSSQLDatabaseBackupAdvancedSetting.from_dictionary(
            val
        )

        val = dictionary['ec2_mssql_log_backup']
        val_ec2_mssql_log_backup = (
            ec2_mssql_log_backup_advanced_setting_.EC2MSSQLLogBackupAdvancedSetting.from_dictionary(
                val
            )
        )

        val = dictionary['mssql_database_backup']
        val_mssql_database_backup = mssql_database_backup_advanced_setting_.MSSQLDatabaseBackupAdvancedSetting.from_dictionary(
            val
        )

        val = dictionary['mssql_log_backup']
        val_mssql_log_backup = (
            mssql_log_backup_advanced_setting_.MSSQLLogBackupAdvancedSetting.from_dictionary(val)
        )

        val = dictionary['oracle_database_backup']
        val_oracle_database_backup = oracle_database_backup_advanced_setting_.OracleDatabaseBackupAdvancedSetting.from_dictionary(
            val
        )

        val = dictionary['oracle_log_backup']
        val_oracle_log_backup = (
            oracle_log_backup_advanced_setting_.OracleLogBackupAdvancedSetting.from_dictionary(val)
        )

        val = dictionary['protection_group_backup']
        val_protection_group_backup = protection_group_backup_advanced_setting_.ProtectionGroupBackupAdvancedSetting.from_dictionary(
            val
        )

        val = dictionary['protection_group_continuous_backup']
        val_protection_group_continuous_backup = protection_group_continuous_backup_advanced_setting_.ProtectionGroupContinuousBackupAdvancedSetting.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_aws_ebs_volume_backup,  # type: ignore
            val_aws_ec2_instance_backup,  # type: ignore
            val_aws_iceberg_table_backup,  # type: ignore
            val_aws_rds_config_sync,  # type: ignore
            val_aws_rds_resource_granular_backup,  # type: ignore
            val_ec2_mssql_database_backup,  # type: ignore
            val_ec2_mssql_log_backup,  # type: ignore
            val_mssql_database_backup,  # type: ignore
            val_mssql_log_backup,  # type: ignore
            val_oracle_database_backup,  # type: ignore
            val_oracle_log_backup,  # type: ignore
            val_protection_group_backup,  # type: ignore
            val_protection_group_continuous_backup,  # type: ignore
        )
