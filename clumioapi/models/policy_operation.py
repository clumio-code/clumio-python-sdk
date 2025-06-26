#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import backup_sla
from clumioapi.models import backup_window
from clumioapi.models import policy_advanced_settings

T = TypeVar('T', bound='PolicyOperation')


class PolicyOperation:
    """Implementation of the 'PolicyOperation' model.

    Attributes:
        action_setting:
            Determines whether the protection policy should take action now or during the
            specified backup window.
            If set to `immediate`, Clumio starts the backup process right away. If set to
            `window`, Clumio starts the backup process when the backup window
            (`backup_window_tz`) opens.
            If set to `window` and `operation in ("aws_rds_resource_aws_snapshot",
            "mssql_log_backup", "ec2_mssql_log_backup")`,
            the backup window will not be determined by Clumio's backup window.
        advanced_settings:
            Additional operation-specific policy settings. For operation types which do not
            support additional settings, this field is `null`.
        backup_aws_region:
            The region in which this backup is stored. This might be used for cross-region
            backup.
        backup_window:
            The start and end times of the customized backup window. Use of `backup_window`
            is deprecated, use `backup_window_tz` instead.
        backup_window_tz:
            The start and end times of the customized backup window. Use of `backup_window`
            is deprecated, use `backup_window_tz` instead.
        next_start_time:
            The next start time of this operation in unix time.
        previous_start_time:
            The previous start time of this operation in unix time.
        slas:
            The service level agreement (SLA) for the policy. A policy can include one or
            more SLAs. For example, a policy can retain daily backups for a month each, and
            monthly backups for a year each.
        timezone:
            The timezone for the operation. The timezone must be a valid location name from
            the IANA Time Zone database.
            For instance, "America/New_York", "US/Central", "UTC".
        p_type:
            The operation to be performed for this SLA set. Each SLA set corresponds to one
            and only one operation.
            Refer to the Policy Operation table for a complete list of policy operations.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'action_setting': 'action_setting',
        'advanced_settings': 'advanced_settings',
        'backup_aws_region': 'backup_aws_region',
        'backup_window': 'backup_window',
        'backup_window_tz': 'backup_window_tz',
        'next_start_time': 'next_start_time',
        'previous_start_time': 'previous_start_time',
        'slas': 'slas',
        'timezone': 'timezone',
        'p_type': 'type',
    }

    def __init__(
        self,
        action_setting: str = None,
        advanced_settings: policy_advanced_settings.PolicyAdvancedSettings = None,
        backup_aws_region: str = None,
        backup_window: backup_window.BackupWindow = None,
        backup_window_tz: backup_window.BackupWindow = None,
        next_start_time: int = None,
        previous_start_time: int = None,
        slas: Sequence[backup_sla.BackupSLA] = None,
        timezone: str = None,
        p_type: str = None,
    ) -> None:
        """Constructor for the PolicyOperation class."""

        # Initialize members of the class
        self.action_setting: str = action_setting
        self.advanced_settings: policy_advanced_settings.PolicyAdvancedSettings = advanced_settings
        self.backup_aws_region: str = backup_aws_region
        self.backup_window: backup_window.BackupWindow = backup_window
        self.backup_window_tz: backup_window.BackupWindow = backup_window_tz
        self.next_start_time: int = next_start_time
        self.previous_start_time: int = previous_start_time
        self.slas: Sequence[backup_sla.BackupSLA] = slas
        self.timezone: str = timezone
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
        action_setting = dictionary.get('action_setting')
        key = 'advanced_settings'
        advanced_settings = (
            policy_advanced_settings.PolicyAdvancedSettings.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        backup_aws_region = dictionary.get('backup_aws_region')
        key = 'backup_window'
        p_backup_window = (
            backup_window.BackupWindow.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'backup_window_tz'
        backup_window_tz = (
            backup_window.BackupWindow.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        next_start_time = dictionary.get('next_start_time')
        previous_start_time = dictionary.get('previous_start_time')
        slas = None
        if dictionary.get('slas'):
            slas = list()
            for value in dictionary.get('slas'):
                slas.append(backup_sla.BackupSLA.from_dictionary(value))

        timezone = dictionary.get('timezone')
        p_type = dictionary.get('type')
        # Return an object of this model
        return cls(
            action_setting,
            advanced_settings,
            backup_aws_region,
            p_backup_window,
            backup_window_tz,
            next_start_time,
            previous_start_time,
            slas,
            timezone,
            p_type,
        )
