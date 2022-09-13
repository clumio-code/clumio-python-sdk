#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ebs_backup_advanced_setting
from clumioapi.models import ec2_backup_advanced_setting
from clumioapi.models import mssql_database_backup_advanced_setting
from clumioapi.models import mssql_log_backup_advanced_setting
from clumioapi.models import protection_group_backup_advanced_setting

T = TypeVar('T', bound='PolicyAdvancedSettings')


class PolicyAdvancedSettings:
    """Implementation of the 'PolicyAdvancedSettings' model.

    Additional operation-specific policy settings. For operation types which do not
    support additional settings, this field is `null`.

    Attributes:
        aws_ebs_volume_backup:
            Backup tier to store the backup in. Valid values are: `` for standard, `lite`
        aws_ec2_instance_backup:
            Backup tier to store the backup in. Valid values are: `` for standard, `lite`
        ec2_mssql_database_backup:
            Additional policy configuration settings for the `mssql_database_backup`
            operation. If this operation is not of type `mssql_database_backup`, then this
            field is omitted from the response.
        ec2_mssql_log_backup:
            Additional policy configuration settings for the `mssql_log_backup` operation.
            If this operation is not of type `mssql_log_backup`, then this field is omitted
            from the response.
        mssql_database_backup:
            Additional policy configuration settings for the `mssql_database_backup`
            operation. If this operation is not of type `mssql_database_backup`, then this
            field is omitted from the response.
        mssql_log_backup:
            Additional policy configuration settings for the `mssql_log_backup` operation.
            If this operation is not of type `mssql_log_backup`, then this field is omitted
            from the response.
        protection_group_backup:
            Additional policy configuration settings for the `protection_group_backup`
            operation. If this operation is not of type `protection_group_backup`, then this
            field is omitted from the response.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'aws_ebs_volume_backup': 'aws_ebs_volume_backup',
        'aws_ec2_instance_backup': 'aws_ec2_instance_backup',
        'ec2_mssql_database_backup': 'ec2_mssql_database_backup',
        'ec2_mssql_log_backup': 'ec2_mssql_log_backup',
        'mssql_database_backup': 'mssql_database_backup',
        'mssql_log_backup': 'mssql_log_backup',
        'protection_group_backup': 'protection_group_backup',
    }

    def __init__(
        self,
        aws_ebs_volume_backup: ebs_backup_advanced_setting.EBSBackupAdvancedSetting = None,
        aws_ec2_instance_backup: ec2_backup_advanced_setting.EC2BackupAdvancedSetting = None,
        ec2_mssql_database_backup: mssql_database_backup_advanced_setting.MSSQLDatabaseBackupAdvancedSetting = None,
        ec2_mssql_log_backup: mssql_log_backup_advanced_setting.MSSQLLogBackupAdvancedSetting = None,
        mssql_database_backup: mssql_database_backup_advanced_setting.MSSQLDatabaseBackupAdvancedSetting = None,
        mssql_log_backup: mssql_log_backup_advanced_setting.MSSQLLogBackupAdvancedSetting = None,
        protection_group_backup: protection_group_backup_advanced_setting.ProtectionGroupBackupAdvancedSetting = None,
    ) -> None:
        """Constructor for the PolicyAdvancedSettings class."""

        # Initialize members of the class
        self.aws_ebs_volume_backup: ebs_backup_advanced_setting.EBSBackupAdvancedSetting = (
            aws_ebs_volume_backup
        )
        self.aws_ec2_instance_backup: ec2_backup_advanced_setting.EC2BackupAdvancedSetting = (
            aws_ec2_instance_backup
        )
        self.ec2_mssql_database_backup: mssql_database_backup_advanced_setting.MSSQLDatabaseBackupAdvancedSetting = (
            ec2_mssql_database_backup
        )
        self.ec2_mssql_log_backup: mssql_log_backup_advanced_setting.MSSQLLogBackupAdvancedSetting = (
            ec2_mssql_log_backup
        )
        self.mssql_database_backup: mssql_database_backup_advanced_setting.MSSQLDatabaseBackupAdvancedSetting = (
            mssql_database_backup
        )
        self.mssql_log_backup: mssql_log_backup_advanced_setting.MSSQLLogBackupAdvancedSetting = (
            mssql_log_backup
        )
        self.protection_group_backup: protection_group_backup_advanced_setting.ProtectionGroupBackupAdvancedSetting = (
            protection_group_backup
        )

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
        key = 'aws_ebs_volume_backup'
        aws_ebs_volume_backup = (
            ebs_backup_advanced_setting.EBSBackupAdvancedSetting.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'aws_ec2_instance_backup'
        aws_ec2_instance_backup = (
            ec2_backup_advanced_setting.EC2BackupAdvancedSetting.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'ec2_mssql_database_backup'
        ec2_mssql_database_backup = (
            mssql_database_backup_advanced_setting.MSSQLDatabaseBackupAdvancedSetting.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'ec2_mssql_log_backup'
        ec2_mssql_log_backup = (
            mssql_log_backup_advanced_setting.MSSQLLogBackupAdvancedSetting.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'mssql_database_backup'
        mssql_database_backup = (
            mssql_database_backup_advanced_setting.MSSQLDatabaseBackupAdvancedSetting.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'mssql_log_backup'
        mssql_log_backup = (
            mssql_log_backup_advanced_setting.MSSQLLogBackupAdvancedSetting.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'protection_group_backup'
        protection_group_backup = (
            protection_group_backup_advanced_setting.ProtectionGroupBackupAdvancedSetting.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(
            aws_ebs_volume_backup,
            aws_ec2_instance_backup,
            ec2_mssql_database_backup,
            ec2_mssql_log_backup,
            mssql_database_backup,
            mssql_log_backup,
            protection_group_backup,
        )
