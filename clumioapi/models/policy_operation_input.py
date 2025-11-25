#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import backup_sla as backup_sla_
from clumioapi.models import backup_window as backup_window_
from clumioapi.models import policy_advanced_settings as policy_advanced_settings_
import requests

T = TypeVar('T', bound='PolicyOperationInput')


@dataclasses.dataclass
class PolicyOperationInput:
    """Implementation of the 'PolicyOperationInput' model.

    Attributes:
        ActionSetting:
            Determines whether the protection policy should take action now or during the
            specified backup window.
            if set to `immediate`, clumio starts the backup process right away. if set to
            `window`, clumio starts the backup process when the backup window
            (`backup_window_tz`) opens.
            if set to `window` and `operation in ("aws_rds_resource_aws_snapshot",
            "mssql_log_backup", "ec2_mssql_log_backup")`,
            the backup window will not be determined by clumio's backup window.

        AdvancedSettings:
            Additional operation-specific policy settings. for operation types which do not
            support additional settings, this field is `null`.

        BackupAwsRegion:
            The region in which this backup is stored. this might be used for cross-region
            backup.

        BackupWindow:
            The start and end times of the customized backup window. use of `backup_window`
            is deprecated, use `backup_window_tz` instead.

        BackupWindowTz:
            The start and end times of the customized backup window. use of `backup_window`
            is deprecated, use `backup_window_tz` instead.

        Slas:
            The service level agreement (sla) for the policy. a policy can include one or
            more slas. for example, a policy can retain daily backups for a month each, and
            monthly backups for a year each.

        Timezone:
            The timezone for the operation. the timezone must be a valid location name from
            the iana time zone database.
            for instance, "america/new_york", "us/central", "utc".

        Type:
            The operation to be performed for this sla set. each sla set corresponds to one
            and only one operation.
            refer to the policy operation table for a complete list of policy operations.

    """

    ActionSetting: str | None = None
    AdvancedSettings: policy_advanced_settings_.PolicyAdvancedSettings | None = None
    BackupAwsRegion: str | None = None
    BackupWindow: backup_window_.BackupWindow | None = None
    BackupWindowTz: backup_window_.BackupWindow | None = None
    Slas: Sequence[backup_sla_.BackupSLA] | None = None
    Timezone: str | None = None
    Type: str | None = None

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

        val = dictionary.get('slas', None)

        val_slas = []
        if val:
            for value in val:
                val_slas.append(backup_sla_.BackupSLA.from_dictionary(value))

        val = dictionary.get('timezone', None)
        val_timezone = val

        val = dictionary.get('type', None)
        val_type = val

        # Return an object of this model
        return cls(
            val_action_setting,
            val_advanced_settings,
            val_backup_aws_region,
            val_backup_window,
            val_backup_window_tz,
            val_slas,
            val_timezone,
            val_type,
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
