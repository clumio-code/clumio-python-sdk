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
        action_setting: str,
        advanced_settings: policy_advanced_settings_.PolicyAdvancedSettings,
        backup_aws_region: str,
        backup_window: backup_window_.BackupWindow,
        backup_window_tz: backup_window_.BackupWindow,
        next_start_time: int,
        previous_start_time: int,
        slas: Sequence[backup_sla_.BackupSLA],
        timezone: str,
        p_type: str,
    ) -> None:
        """Constructor for the PolicyOperation class."""

        # Initialize members of the class
        self.action_setting: str = action_setting
        self.advanced_settings: policy_advanced_settings_.PolicyAdvancedSettings = advanced_settings
        self.backup_aws_region: str = backup_aws_region
        self.backup_window: backup_window_.BackupWindow = backup_window
        self.backup_window_tz: backup_window_.BackupWindow = backup_window_tz
        self.next_start_time: int = next_start_time
        self.previous_start_time: int = previous_start_time
        self.slas: Sequence[backup_sla_.BackupSLA] = slas
        self.timezone: str = timezone
        self.p_type: str = p_type

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
        val = dictionary['action_setting']
        val_action_setting = val

        val = dictionary['advanced_settings']
        val_advanced_settings = policy_advanced_settings_.PolicyAdvancedSettings.from_dictionary(
            val
        )

        val = dictionary['backup_aws_region']
        val_backup_aws_region = val

        val = dictionary['backup_window']
        val_backup_window = backup_window_.BackupWindow.from_dictionary(val)

        val = dictionary['backup_window_tz']
        val_backup_window_tz = backup_window_.BackupWindow.from_dictionary(val)

        val = dictionary['next_start_time']
        val_next_start_time = val

        val = dictionary['previous_start_time']
        val_previous_start_time = val

        val = dictionary['slas']

        val_slas = None
        if val:
            val_slas = list()
            for value in val:
                val_slas.append(backup_sla_.BackupSLA.from_dictionary(value))

        val = dictionary['timezone']
        val_timezone = val

        val = dictionary['type']
        val_p_type = val

        # Return an object of this model
        return cls(
            val_action_setting,  # type: ignore
            val_advanced_settings,  # type: ignore
            val_backup_aws_region,  # type: ignore
            val_backup_window,  # type: ignore
            val_backup_window_tz,  # type: ignore
            val_next_start_time,  # type: ignore
            val_previous_start_time,  # type: ignore
            val_slas,  # type: ignore
            val_timezone,  # type: ignore
            val_p_type,  # type: ignore
        )
