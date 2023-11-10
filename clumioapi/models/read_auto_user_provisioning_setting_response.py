#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import auto_user_provisioning_setting_links

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
    _names = {'links': '_links', 'is_enabled': 'is_enabled'}

    def __init__(
        self,
        links: auto_user_provisioning_setting_links.AutoUserProvisioningSettingLinks = None,
        is_enabled: bool = None,
    ) -> None:
        """Constructor for the ReadAutoUserProvisioningSettingResponse class."""

        # Initialize members of the class
        self.links: auto_user_provisioning_setting_links.AutoUserProvisioningSettingLinks = links
        self.is_enabled: bool = is_enabled

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
        key = '_links'
        links = (
            auto_user_provisioning_setting_links.AutoUserProvisioningSettingLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        is_enabled = dictionary.get('is_enabled')
        # Return an object of this model
        return cls(links, is_enabled)
