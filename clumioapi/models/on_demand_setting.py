#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import policy_advanced_settings, retention_backup_sla_param

T = TypeVar('T', bound='OnDemandSetting')


class OnDemandSetting:
    """Implementation of the 'OnDemandSetting' model.

    Settings for requesting on-demand backup directly

    Attributes:
        advanced_settings:
            Additional operation-specific policy settings. For operation types which do not
            support additional settings, this field is `null`.
        backup_aws_region:
            Specifies the destination vault for AWS backups.
        retention_duration:
            The retention time for this SLA. For example, to retain the backup for 1 month,
            set `unit="months"` and `value=1`.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'advanced_settings': 'advanced_settings',
        'backup_aws_region': 'backup_aws_region',
        'retention_duration': 'retention_duration',
    }

    def __init__(
        self,
        advanced_settings: policy_advanced_settings.PolicyAdvancedSettings = None,
        backup_aws_region: str = None,
        retention_duration: retention_backup_sla_param.RetentionBackupSLAParam = None,
    ) -> None:
        """Constructor for the OnDemandSetting class."""

        # Initialize members of the class
        self.advanced_settings: policy_advanced_settings.PolicyAdvancedSettings = advanced_settings
        self.backup_aws_region: str = backup_aws_region
        self.retention_duration: retention_backup_sla_param.RetentionBackupSLAParam = (
            retention_duration
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
        key = 'advanced_settings'
        advanced_settings = (
            policy_advanced_settings.PolicyAdvancedSettings.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        backup_aws_region = dictionary.get('backup_aws_region')
        key = 'retention_duration'
        retention_duration = (
            retention_backup_sla_param.RetentionBackupSLAParam.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(advanced_settings, backup_aws_region, retention_duration)
