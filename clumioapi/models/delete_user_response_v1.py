#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_common_links

T = TypeVar('T', bound='DeleteUserResponseV1')


class DeleteUserResponseV1:
    """Implementation of the 'DeleteUserResponseV1' model.

    Attributes:
        links:
            HateoasCommonLinks are the common fields for HATEOAS response.
    """

    # Create a mapping from Model property names to API property names
    _names = {'links': '_links'}

    def __init__(self, links: hateoas_common_links.HateoasCommonLinks = None) -> None:
        """Constructor for the DeleteUserResponseV1 class."""

        # Initialize members of the class
        self.links: hateoas_common_links.HateoasCommonLinks = links

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
            hateoas_common_links.HateoasCommonLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(links)
