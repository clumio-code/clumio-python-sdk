#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    auto_user_provisioning_setting_links as auto_user_provisioning_setting_links_

T = TypeVar('T', bound='UpdateAutoUserProvisioningSettingResponse')


class UpdateAutoUserProvisioningSettingResponse:
    """Implementation of the 'UpdateAutoUserProvisioningSettingResponse' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        is_enabled:
            Whether auto user provisioning is enabled or not.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'links': '_links', 'is_enabled': 'is_enabled'}

    def __init__(
        self,
        links: auto_user_provisioning_setting_links_.AutoUserProvisioningSettingLinks | None = None,
        is_enabled: bool | None = None,
    ) -> None:
        """Constructor for the UpdateAutoUserProvisioningSettingResponse class."""

        # Initialize members of the class
        self.links: (
            auto_user_provisioning_setting_links_.AutoUserProvisioningSettingLinks | None
        ) = links
        self.is_enabled: bool | None = is_enabled

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
