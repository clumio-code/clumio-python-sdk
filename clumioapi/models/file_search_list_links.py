#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_first_link as hateoas_first_link_
from clumioapi.models import hateoas_next_link as hateoas_next_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_

T = TypeVar('T', bound='FileSearchListLinks')


class FileSearchListLinks:
    """Implementation of the 'FileSearchListLinks' model.

    URLs to pages related to the resource.

    Attributes:
        first:
            The HATEOAS link to the first page of results.
        p_next:
            The HATEOAS link to the next page of results.
        p_self:
            The HATEOAS link to this resource.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'first': '_first', 'p_next': '_next', 'p_self': '_self'}

    def __init__(
        self,
        first: hateoas_first_link_.HateoasFirstLink | None = None,
        p_next: hateoas_next_link_.HateoasNextLink | None = None,
        p_self: hateoas_self_link_.HateoasSelfLink | None = None,
    ) -> None:
        """Constructor for the FileSearchListLinks class."""

        # Initialize members of the class
        self.first: hateoas_first_link_.HateoasFirstLink | None = first
        self.p_next: hateoas_next_link_.HateoasNextLink | None = p_next
        self.p_self: hateoas_self_link_.HateoasSelfLink | None = p_self

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

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('_first', None)
        val_first = hateoas_first_link_.HateoasFirstLink.from_dictionary(val)

        val = dictionary.get('_next', None)
        val_p_next = hateoas_next_link_.HateoasNextLink.from_dictionary(val)

        val = dictionary.get('_self', None)
        val_p_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_first,
            val_p_next,
            val_p_self,
        )
