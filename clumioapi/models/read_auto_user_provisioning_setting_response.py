#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    auto_user_provisioning_setting_links as auto_user_provisioning_setting_links_
import requests

T = TypeVar('T', bound='ReadAutoUserProvisioningSettingResponse')


@dataclasses.dataclass
class ReadAutoUserProvisioningSettingResponse:
    """Implementation of the 'ReadAutoUserProvisioningSettingResponse' model.

    Attributes:
        Links:
            Urls to pages related to the resource.

        IsEnabled:
            Whether auto user provisioning is enabled or not.

    """

    Links: auto_user_provisioning_setting_links_.AutoUserProvisioningSettingLinks | None = None
    IsEnabled: bool | None = None
    raw_response: Optional[requests.Response] = None

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
        val = dictionary.get('_links', None)
        val_links = (
            auto_user_provisioning_setting_links_.AutoUserProvisioningSettingLinks.from_dictionary(
                val
            )
        )

        val = dictionary.get('is_enabled', None)
        val_is_enabled = val

        # Return an object of this model
        return cls(
            val_links,
            val_is_enabled,
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
        model_instance.raw_response = response
        return model_instance
