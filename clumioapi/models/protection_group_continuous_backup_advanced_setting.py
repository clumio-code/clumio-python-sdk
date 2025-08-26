#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ProtectionGroupContinuousBackupAdvancedSetting')


class ProtectionGroupContinuousBackupAdvancedSetting:
    """Implementation of the 'ProtectionGroupContinuousBackupAdvancedSetting' model.

    Additional policy configuration settings for the
    `protection_group_continuous_backup` operation. If this operation is not of type
    `protection_group_continuous_backup`, then this field is omitted from the
    response.

    Attributes:
        disable_eventbridge_notification:
            If true, tries to disable EventBridge notification for the given protection
            group, when continuous backup no longer conducts.
            It may override the existing S3 bucket notification configuration in the
            customer's account.
            This takes effect only when `event_bridge_enabled` is set to `false`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'disable_eventbridge_notification': 'disable_eventbridge_notification'
    }

    def __init__(self, disable_eventbridge_notification: bool | None = None) -> None:
        """Constructor for the ProtectionGroupContinuousBackupAdvancedSetting class."""

        # Initialize members of the class
        self.disable_eventbridge_notification: bool | None = disable_eventbridge_notification

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
        val = dictionary.get('disable_eventbridge_notification', None)
        val_disable_eventbridge_notification = val

        # Return an object of this model
        return cls(
            val_disable_eventbridge_notification,
        )
