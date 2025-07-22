#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='SetBucketPropertiesV1Request')


class SetBucketPropertiesV1Request:
    """Implementation of the 'SetBucketPropertiesV1Request' model.

    The set of properties that are being updated for the given bucket.

    Attributes:
        event_bridge_enabled:
            If true, enables continuous backup for the given bucket.
            If false, disables continuous backup for the given bucket.
            If not set, does not update EventBridge.
        event_bridge_notification_disabled:
            If true, tries to disable EventBridge notification for the given bucket.
            It may override the existing bucket notification configuration in the customer's
            account.
            This takes effect only when `event_bridge_enabled` is set to `false`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'event_bridge_enabled': 'event_bridge_enabled',
        'event_bridge_notification_disabled': 'event_bridge_notification_disabled',
    }

    def __init__(
        self, event_bridge_enabled: bool, event_bridge_notification_disabled: bool
    ) -> None:
        """Constructor for the SetBucketPropertiesV1Request class."""

        # Initialize members of the class
        self.event_bridge_enabled: bool = event_bridge_enabled
        self.event_bridge_notification_disabled: bool = event_bridge_notification_disabled

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
        val = dictionary['event_bridge_enabled']
        val_event_bridge_enabled = val

        val = dictionary['event_bridge_notification_disabled']
        val_event_bridge_notification_disabled = val

        # Return an object of this model
        return cls(
            val_event_bridge_enabled,  # type: ignore
            val_event_bridge_notification_disabled,  # type: ignore
        )
