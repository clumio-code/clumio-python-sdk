#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_self_link
from clumioapi.models import read_task_hateoas_links

T = TypeVar('T', bound='MoveHostsLinks')


class MoveHostsLinks:
    """Implementation of the 'MoveHostsLinks' model.

    URLs to pages related to the resource.

    Attributes:
        links:
            Embedded responses related to the resource.
        p_self:
            The HATEOAS link to this resource.
    """

    # Create a mapping from Model property names to API property names
    _names = {'links': '_links', 'p_self': '_self'}

    def __init__(
        self,
        links: read_task_hateoas_links.ReadTaskHateoasLinks = None,
        p_self: hateoas_self_link.HateoasSelfLink = None,
    ) -> None:
        """Constructor for the MoveHostsLinks class."""

        # Initialize members of the class
        self.links: read_task_hateoas_links.ReadTaskHateoasLinks = links
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
        key = '_links'
        links = (
            read_task_hateoas_links.ReadTaskHateoasLinks.from_dictionary(dictionary.get(key))
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
        return cls(links, p_self)
