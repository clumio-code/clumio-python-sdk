#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='UnprotectEntitiesHateoasLink')


class UnprotectEntitiesHateoasLink:
    """Implementation of the 'UnprotectEntitiesHateoasLink' model.

    A HATEOAS link to unprotect the entities.

    Attributes:
        href:
            The URI for the referenced operation.
        templated:
            Determines whether the "href" link is a URI template. If set to `true`, the
            "href" link is a URI template.
        p_type:
            The HTTP method to be used with the "href" link for the referenced operation.
    """

    # Create a mapping from Model property names to API property names
    _names = {'href': 'href', 'templated': 'templated', 'p_type': 'type'}

    def __init__(self, href: str = None, templated: bool = None, p_type: str = None) -> None:
        """Constructor for the UnprotectEntitiesHateoasLink class."""

        # Initialize members of the class
        self.href: str = href
        self.templated: bool = templated
        self.p_type: str = p_type

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
        href = dictionary.get('href')
        templated = dictionary.get('templated')
        p_type = dictionary.get('type')
        # Return an object of this model
        return cls(href, templated, p_type)
