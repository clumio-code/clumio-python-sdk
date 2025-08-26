#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import policy_advanced_settings as policy_advanced_settings_
from clumioapi.models import retention_backup_sla_param as retention_backup_sla_param_
import requests

T = TypeVar('T', bound='OnDemandSetting')


@dataclasses.dataclass
class OnDemandSetting:
    """Implementation of the 'OnDemandSetting' model.

    Settings for requesting on-demand backup directly.

    Attributes:
        AdvancedSettings:
            Additional operation-specific policy settings. for operation types which do not support additional settings, this field is `null`.

        BackupAwsRegion:
            The region in which this backup is stored. this might be used for cross-region backup.

        RetentionDuration:
            The retention time for this sla. for example, to retain the backup for 1 month, set `unit="months"` and `value=1`.

    """

    AdvancedSettings: policy_advanced_settings_.PolicyAdvancedSettings | None = None
    BackupAwsRegion: str | None = None
    RetentionDuration: retention_backup_sla_param_.RetentionBackupSLAParam | None = None

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
        val = dictionary.get('advanced_settings', None)
        val_advanced_settings = policy_advanced_settings_.PolicyAdvancedSettings.from_dictionary(
            val
        )

        val = dictionary.get('backup_aws_region', None)
        val_backup_aws_region = val

        val = dictionary.get('retention_duration', None)
        val_retention_duration = (
            retention_backup_sla_param_.RetentionBackupSLAParam.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_advanced_settings,
            val_backup_aws_region,
            val_retention_duration,
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
