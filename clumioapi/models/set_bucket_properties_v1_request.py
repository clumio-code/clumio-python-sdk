#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='SetBucketPropertiesV1Request')


@dataclasses.dataclass
class SetBucketPropertiesV1Request:
    """Implementation of the 'SetBucketPropertiesV1Request' model.

    The set of properties that are being updated for the given bucket.

    Attributes:
        EventBridgeEnabled:
            If true, enables continuous backup for the given bucket.
            if false, disables continuous backup for the given bucket.
            if not set, does not update eventbridge.

        EventBridgeNotificationDisabled:
            If true, tries to disable eventbridge notification for the given bucket.
            it may override the existing bucket notification configuration in the customer's
            account.
            this takes effect only when `event_bridge_enabled` is set to `false`.

    """

    EventBridgeEnabled: bool | None = None
    EventBridgeNotificationDisabled: bool | None = None

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
        val = dictionary.get('event_bridge_enabled', None)
        val_event_bridge_enabled = val

        val = dictionary.get('event_bridge_notification_disabled', None)
        val_event_bridge_notification_disabled = val

        # Return an object of this model
        return cls(
            val_event_bridge_enabled,
            val_event_bridge_notification_disabled,
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
