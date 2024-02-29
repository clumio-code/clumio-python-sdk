#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link
from clumioapi.models import hateoas_self_link
from clumioapi.models import read_policy_definition_hateoas_link

T = TypeVar('T', bound='RuleLinks')


class RuleLinks:
    """Implementation of the 'RuleLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        delete_policy_rule:
            A resource-specific HATEOAS link.
        read_policy_definition:
            A HATEOAS link to the policy protecting this resource. Will be omitted for
            unprotected entities.
        update_policy_rule:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_self': '_self',
        'delete_policy_rule': 'delete-policy-rule',
        'read_policy_definition': 'read-policy-definition',
        'update_policy_rule': 'update-policy-rule',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        delete_policy_rule: hateoas_link.HateoasLink = None,
        read_policy_definition: read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink = None,
        update_policy_rule: hateoas_link.HateoasLink = None,
    ) -> None:
        """Constructor for the RuleLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.delete_policy_rule: hateoas_link.HateoasLink = delete_policy_rule
        self.read_policy_definition: (
            read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink
        ) = read_policy_definition
        self.update_policy_rule: hateoas_link.HateoasLink = update_policy_rule

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
        key = '_self'
        p_self = (
            hateoas_self_link.HateoasSelfLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'delete-policy-rule'
        delete_policy_rule = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'read-policy-definition'
        read_policy_definition = (
            read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'update-policy-rule'
        update_policy_rule = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(p_self, delete_policy_rule, read_policy_definition, update_policy_rule)
