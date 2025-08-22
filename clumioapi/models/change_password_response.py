#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_common_links as hateoas_common_links_

T = TypeVar('T', bound='ChangePasswordResponse')


class ChangePasswordResponse:
    """Implementation of the 'ChangePasswordResponse' model.

    Attributes:
        links:
            HateoasCommonLinks are the common fields for HATEOAS response.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'links': '_links'}

    def __init__(self, links: hateoas_common_links_.HateoasCommonLinks | None = None) -> None:
        """Constructor for the ChangePasswordResponse class."""

        # Initialize members of the class
        self.links: hateoas_common_links_.HateoasCommonLinks | None = links

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
        val = dictionary.get('_links', None)
        val_links = hateoas_common_links_.HateoasCommonLinks.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_links,
        )
