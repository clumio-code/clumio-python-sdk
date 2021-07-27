#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_first_link
from clumioapi.models import hateoas_next_link
from clumioapi.models import hateoas_self_link

T = TypeVar('T', bound='FileSearchListLinks')


class FileSearchListLinks:
    """Implementation of the 'FileSearchListLinks' model.

    URLs to pages related to the resource.

    Attributes:
        first:
            The HATEOAS link to the first page of results.
        next:
            The HATEOAS link to the next page of results.
        p_self:
            The HATEOAS link to this resource.
    """

    # Create a mapping from Model property names to API property names
    _names = {'first': '_first', 'next': '_next', 'p_self': '_self'}

    def __init__(
        self,
        first: hateoas_first_link.HateoasFirstLink = None,
        next: hateoas_next_link.HateoasNextLink = None,
        p_self: hateoas_self_link.HateoasSelfLink = None,
    ) -> None:
        """Constructor for the FileSearchListLinks class."""

        # Initialize members of the class
        self.first: hateoas_first_link.HateoasFirstLink = first
        self.next: hateoas_next_link.HateoasNextLink = next
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self

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

        # Return an object of this model
        return cls(first, next, p_self)
