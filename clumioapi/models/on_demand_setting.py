#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import policy_advanced_settings as policy_advanced_settings_
from clumioapi.models import retention_backup_sla_param as retention_backup_sla_param_

T = TypeVar('T', bound='OnDemandSetting')


class OnDemandSetting:
    """Implementation of the 'OnDemandSetting' model.

    Settings for requesting on-demand backup directly.

    Attributes:
        advanced_settings:
            Additional operation-specific policy settings. For operation types which do not
            support additional settings, this field is `null`.
        backup_aws_region:
            The region in which this backup is stored. This might be used for cross-region
            backup.
        retention_duration:
            The retention time for this SLA. For example, to retain the backup for 1 month,
            set `unit="months"` and `value=1`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'advanced_settings': 'advanced_settings',
        'backup_aws_region': 'backup_aws_region',
        'retention_duration': 'retention_duration',
    }

    def __init__(
        self,
        advanced_settings: policy_advanced_settings_.PolicyAdvancedSettings,
        backup_aws_region: str,
        retention_duration: retention_backup_sla_param_.RetentionBackupSLAParam,
    ) -> None:
        """Constructor for the OnDemandSetting class."""

        # Initialize members of the class
        self.advanced_settings: policy_advanced_settings_.PolicyAdvancedSettings = advanced_settings
        self.backup_aws_region: str = backup_aws_region
        self.retention_duration: retention_backup_sla_param_.RetentionBackupSLAParam = (
            retention_duration
        )

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
        val = dictionary['advanced_settings']
        val_advanced_settings = policy_advanced_settings_.PolicyAdvancedSettings.from_dictionary(
            val
        )

        val = dictionary['backup_aws_region']
        val_backup_aws_region = val

        val = dictionary['retention_duration']
        val_retention_duration = (
            retention_backup_sla_param_.RetentionBackupSLAParam.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_advanced_settings,  # type: ignore
            val_backup_aws_region,  # type: ignore
            val_retention_duration,  # type: ignore
        )
