#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import backup_sla as backup_sla_
from clumioapi.models import backup_window as backup_window_
from clumioapi.models import policy_advanced_settings as policy_advanced_settings_

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
    _names: dict[str, str] = {
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
        action_setting: str | None = None,
        advanced_settings: policy_advanced_settings_.PolicyAdvancedSettings | None = None,
        backup_aws_region: str | None = None,
        backup_window: backup_window_.BackupWindow | None = None,
        backup_window_tz: backup_window_.BackupWindow | None = None,
        next_start_time: int | None = None,
        previous_start_time: int | None = None,
        slas: Sequence[backup_sla_.BackupSLA] | None = None,
        timezone: str | None = None,
        p_type: str | None = None,
    ) -> None:
        """Constructor for the PolicyOperation class."""

        # Initialize members of the class
        self.action_setting: str | None = action_setting
        self.advanced_settings: policy_advanced_settings_.PolicyAdvancedSettings | None = (
            advanced_settings
        )
        self.backup_aws_region: str | None = backup_aws_region
        self.backup_window: backup_window_.BackupWindow | None = backup_window
        self.backup_window_tz: backup_window_.BackupWindow | None = backup_window_tz
        self.next_start_time: int | None = next_start_time
        self.previous_start_time: int | None = previous_start_time
        self.slas: Sequence[backup_sla_.BackupSLA] | None = slas
        self.timezone: str | None = timezone
        self.p_type: str | None = p_type

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
        val = dictionary.get('action_setting', None)
        val_action_setting = val

        val = dictionary.get('advanced_settings', None)
        val_advanced_settings = policy_advanced_settings_.PolicyAdvancedSettings.from_dictionary(
            val
        )

        val = dictionary.get('backup_aws_region', None)
        val_backup_aws_region = val

        val = dictionary.get('backup_window', None)
        val_backup_window = backup_window_.BackupWindow.from_dictionary(val)

        val = dictionary.get('backup_window_tz', None)
        val_backup_window_tz = backup_window_.BackupWindow.from_dictionary(val)

        val = dictionary.get('next_start_time', None)
        val_next_start_time = val

        val = dictionary.get('previous_start_time', None)
        val_previous_start_time = val

        val = dictionary.get('slas', None)

        val_slas = None
        if val:
            val_slas = list()
            for value in val:
                val_slas.append(backup_sla_.BackupSLA.from_dictionary(value))

        val = dictionary.get('timezone', None)
        val_timezone = val

        val = dictionary.get('type', None)
        val_p_type = val

        # Return an object of this model
        return cls(
            val_action_setting,
            val_advanced_settings,
            val_backup_aws_region,
            val_backup_window,
            val_backup_window_tz,
            val_next_start_time,
            val_previous_start_time,
            val_slas,
            val_timezone,
            val_p_type,
        )
