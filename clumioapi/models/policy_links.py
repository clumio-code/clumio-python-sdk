#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link
from clumioapi.models import hateoas_self_link

T = TypeVar('T', bound='PolicyLinks')


class PolicyLinks:
    """Implementation of the 'PolicyLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        delete_policy_definition:
            A resource-specific HATEOAS link.
        update_policy_definition:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_self': '_self',
        'delete_policy_definition': 'delete-policy-definition',
        'update_policy_definition': 'update-policy-definition',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        delete_policy_definition: hateoas_link.HateoasLink = None,
        update_policy_definition: hateoas_link.HateoasLink = None,
    ) -> None:
        """Constructor for the PolicyLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.delete_policy_definition: hateoas_link.HateoasLink = delete_policy_definition
        self.update_policy_definition: hateoas_link.HateoasLink = update_policy_definition

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

        key = 'delete-policy-definition'
        delete_policy_definition = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'update-policy-definition'
        update_policy_definition = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(p_self, delete_policy_definition, update_policy_definition)
