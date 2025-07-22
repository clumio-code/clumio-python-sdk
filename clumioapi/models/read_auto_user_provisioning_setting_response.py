#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    auto_user_provisioning_setting_links as auto_user_provisioning_setting_links_

T = TypeVar('T', bound='ReadAutoUserProvisioningSettingResponse')


class ReadAutoUserProvisioningSettingResponse:
    """Implementation of the 'ReadAutoUserProvisioningSettingResponse' model.

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
        links: auto_user_provisioning_setting_links_.AutoUserProvisioningSettingLinks,
        is_enabled: bool,
    ) -> None:
        """Constructor for the ReadAutoUserProvisioningSettingResponse class."""

        # Initialize members of the class
        self.links: auto_user_provisioning_setting_links_.AutoUserProvisioningSettingLinks = links
        self.is_enabled: bool = is_enabled

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
        val = dictionary['_links']
        val_links = (
            auto_user_provisioning_setting_links_.AutoUserProvisioningSettingLinks.from_dictionary(
                val
            )
        )

        val = dictionary['is_enabled']
        val_is_enabled = val

        # Return an object of this model
        return cls(
            val_links,  # type: ignore
            val_is_enabled,  # type: ignore
        )
