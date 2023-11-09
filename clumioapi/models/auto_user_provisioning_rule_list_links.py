#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_first_link
from clumioapi.models import hateoas_link
from clumioapi.models import hateoas_next_link
from clumioapi.models import hateoas_self_link

T = TypeVar('T', bound='AutoUserProvisioningRuleListLinks')


class AutoUserProvisioningRuleListLinks:
    """Implementation of the 'AutoUserProvisioningRuleListLinks' model.

    URLs to pages related to the resource.

    Attributes:
        first:
            The HATEOAS link to the first page of results.
        p_next:
            The HATEOAS link to the next page of results.
        p_self:
            The HATEOAS link to this resource.
        create_auto_user_provisioning_rule:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'first': '_first',
        'p_next': '_next',
        'p_self': '_self',
        'create_auto_user_provisioning_rule': 'create-auto-user-provisioning-rule',
    }

    def __init__(
        self,
        first: hateoas_first_link.HateoasFirstLink = None,
        p_next: hateoas_next_link.HateoasNextLink = None,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        create_auto_user_provisioning_rule: hateoas_link.HateoasLink = None,
    ) -> None:
        """Constructor for the AutoUserProvisioningRuleListLinks class."""

        # Initialize members of the class
        self.first: hateoas_first_link.HateoasFirstLink = first
        self.p_next: hateoas_next_link.HateoasNextLink = p_next
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.create_auto_user_provisioning_rule: hateoas_link.HateoasLink = (
            create_auto_user_provisioning_rule
        )

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
        key = '_first'
        first = (
            hateoas_first_link.HateoasFirstLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_next'
        p_next = (
            hateoas_next_link.HateoasNextLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_self'
        p_self = (
            hateoas_self_link.HateoasSelfLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'create-auto-user-provisioning-rule'
        create_auto_user_provisioning_rule = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(first, p_next, p_self, create_auto_user_provisioning_rule)
