#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
from clumioapi.models import \
    read_policy_definition_hateoas_link as read_policy_definition_hateoas_link_

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
    _names: dict[str, str] = {
        'p_self': '_self',
        'delete_policy_rule': 'delete-policy-rule',
        'read_policy_definition': 'read-policy-definition',
        'update_policy_rule': 'update-policy-rule',
    }

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink,
        delete_policy_rule: hateoas_link_.HateoasLink,
        read_policy_definition: read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink,
        update_policy_rule: hateoas_link_.HateoasLink,
    ) -> None:
        """Constructor for the RuleLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink = p_self
        self.delete_policy_rule: hateoas_link_.HateoasLink = delete_policy_rule
        self.read_policy_definition: (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink
        ) = read_policy_definition
        self.update_policy_rule: hateoas_link_.HateoasLink = update_policy_rule

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

        val = dictionary['delete-policy-rule']
        val_delete_policy_rule = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary['read-policy-definition']
        val_read_policy_definition = (
            read_policy_definition_hateoas_link_.ReadPolicyDefinitionHateoasLink.from_dictionary(
                val
            )
        )

        val = dictionary['update-policy-rule']
        val_update_policy_rule = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_p_self,  # type: ignore
            val_delete_policy_rule,  # type: ignore
            val_read_policy_definition,  # type: ignore
            val_update_policy_rule,  # type: ignore
        )
