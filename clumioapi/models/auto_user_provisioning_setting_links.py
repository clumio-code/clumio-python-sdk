#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_

T = TypeVar('T', bound='AutoUserProvisioningSettingLinks')


class AutoUserProvisioningSettingLinks:
    """Implementation of the 'AutoUserProvisioningSettingLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        update_auto_user_provisioning_setting:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'p_self': '_self',
        'update_auto_user_provisioning_setting': 'update-auto-user-provisioning-setting',
    }

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink,
        update_auto_user_provisioning_setting: hateoas_link_.HateoasLink,
    ) -> None:
        """Constructor for the AutoUserProvisioningSettingLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink = p_self
        self.update_auto_user_provisioning_setting: hateoas_link_.HateoasLink = (
            update_auto_user_provisioning_setting
        )

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
        val = dictionary['_self']
        val_p_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary['update-auto-user-provisioning-setting']
        val_update_auto_user_provisioning_setting = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_p_self,  # type: ignore
            val_update_auto_user_provisioning_setting,  # type: ignore
        )
