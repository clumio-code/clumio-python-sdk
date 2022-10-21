#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_first_link, hateoas_link, hateoas_next_link, hateoas_self_link

T = TypeVar('T', bound='PolicyListLinks')


class PolicyListLinks:
    """Implementation of the 'PolicyListLinks' model.

    URLs to pages related to the resource.

    Attributes:
        first:
            The HATEOAS link to the first page of results.
        next:
            The HATEOAS link to the next page of results.
        p_self:
            The HATEOAS link to this resource.
        create_policy_definition:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'first': '_first',
        'next': '_next',
        'p_self': '_self',
        'create_policy_definition': 'create-policy-definition',
    }

    def __init__(
        self,
        first: hateoas_first_link.HateoasFirstLink = None,
        next: hateoas_next_link.HateoasNextLink = None,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        create_policy_definition: hateoas_link.HateoasLink = None,
    ) -> None:
        """Constructor for the PolicyListLinks class."""

        # Initialize members of the class
        self.first: hateoas_first_link.HateoasFirstLink = first
        self.next: hateoas_next_link.HateoasNextLink = next
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.create_policy_definition: hateoas_link.HateoasLink = create_policy_definition

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
        next = (
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

        key = 'create-policy-definition'
        create_policy_definition = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(first, next, p_self, create_policy_definition)
