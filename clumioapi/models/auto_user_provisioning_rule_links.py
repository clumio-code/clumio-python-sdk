#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_

T = TypeVar('T', bound='AutoUserProvisioningRuleLinks')


class AutoUserProvisioningRuleLinks:
    """Implementation of the 'AutoUserProvisioningRuleLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        delete_auto_user_provisioning_rule:
            A resource-specific HATEOAS link.
        update_auto_user_provisioning_rule:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'p_self': '_self',
        'delete_auto_user_provisioning_rule': 'delete-auto-user-provisioning-rule',
        'update_auto_user_provisioning_rule': 'update-auto-user-provisioning-rule',
    }

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink,
        delete_auto_user_provisioning_rule: hateoas_link_.HateoasLink,
        update_auto_user_provisioning_rule: hateoas_link_.HateoasLink,
    ) -> None:
        """Constructor for the AutoUserProvisioningRuleLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink = p_self
        self.delete_auto_user_provisioning_rule: hateoas_link_.HateoasLink = (
            delete_auto_user_provisioning_rule
        )
        self.update_auto_user_provisioning_rule: hateoas_link_.HateoasLink = (
            update_auto_user_provisioning_rule
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

        val = dictionary['delete-auto-user-provisioning-rule']
        val_delete_auto_user_provisioning_rule = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary['update-auto-user-provisioning-rule']
        val_update_auto_user_provisioning_rule = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_p_self,  # type: ignore
            val_delete_auto_user_provisioning_rule,  # type: ignore
            val_update_auto_user_provisioning_rule,  # type: ignore
        )
