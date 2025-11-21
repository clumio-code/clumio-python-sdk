#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='ProtectionGroupContinuousBackupAdvancedSetting')


@dataclasses.dataclass
class ProtectionGroupContinuousBackupAdvancedSetting:
    """Implementation of the 'ProtectionGroupContinuousBackupAdvancedSetting' model.

    Additional policy configuration settings for the
    `protection_group_continuous_backup` operation. If this operation is not of type
    `protection_group_continuous_backup`, then this field is omitted from the
    response.

    Attributes:
        DisableEventbridgeNotification:
            If true, tries to disable eventbridge notification for the given protection
            group, when continuous backup no longer conducts.
            it may override the existing s3 bucket notification configuration in the
            customer's account.
            this takes effect only when `event_bridge_enabled` is set to `false`.

    """

    DisableEventbridgeNotification: bool | None = None

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
        val = dictionary.get('disable_eventbridge_notification', None)
        val_disable_eventbridge_notification = val

        # Return an object of this model
        return cls(
            val_disable_eventbridge_notification,
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
