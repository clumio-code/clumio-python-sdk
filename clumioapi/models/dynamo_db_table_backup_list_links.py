#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_first_link
from clumioapi.models import hateoas_last_link
from clumioapi.models import hateoas_next_link
from clumioapi.models import hateoas_prev_link
from clumioapi.models import hateoas_self_link

T = TypeVar('T', bound='DynamoDBTableBackupListLinks')


class DynamoDBTableBackupListLinks:
    """Implementation of the 'DynamoDBTableBackupListLinks' model.

    URLs to pages related to the resource.

    Attributes:
        first:
            The HATEOAS link to the first page of results.
        last:
            The HATEOAS link to the last page of results.
        p_next:
            The HATEOAS link to the next page of results.
        prev:
            The HATEOAS link to the previous page of results.
        p_self:
            The HATEOAS link to this resource.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'first': '_first',
        'last': '_last',
        'p_next': '_next',
        'prev': '_prev',
        'p_self': '_self',
    }

    def __init__(
        self,
        first: hateoas_first_link.HateoasFirstLink = None,
        last: hateoas_last_link.HateoasLastLink = None,
        p_next: hateoas_next_link.HateoasNextLink = None,
        prev: hateoas_prev_link.HateoasPrevLink = None,
        p_self: hateoas_self_link.HateoasSelfLink = None,
    ) -> None:
        """Constructor for the DynamoDBTableBackupListLinks class."""

        # Initialize members of the class
        self.first: hateoas_first_link.HateoasFirstLink = first
        self.last: hateoas_last_link.HateoasLastLink = last
        self.p_next: hateoas_next_link.HateoasNextLink = p_next
        self.prev: hateoas_prev_link.HateoasPrevLink = prev
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

        key = '_last'
        last = (
            hateoas_last_link.HateoasLastLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_next'
        p_next = (
            hateoas_next_link.HateoasNextLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_prev'
        prev = (
            hateoas_prev_link.HateoasPrevLink.from_dictionary(dictionary.get(key))
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
        return cls(first, last, p_next, prev, p_self)
