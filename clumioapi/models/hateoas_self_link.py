#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='HateoasSelfLink')


class HateoasSelfLink:
    """Implementation of the 'HateoasSelfLink' model.

    The HATEOAS link to this resource.

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
    _names: dict[str, str] = {'href': 'href', 'templated': 'templated', 'p_type': 'type'}

    def __init__(self, href: str, templated: bool, p_type: str) -> None:
        """Constructor for the HateoasSelfLink class."""

        # Initialize members of the class
        self.href: str = href
        self.templated: bool = templated
        self.p_type: str = p_type

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
        val = dictionary['href']
        val_href = val

        val = dictionary['templated']
        val_templated = val

        val = dictionary['type']
        val_p_type = val

        # Return an object of this model
        return cls(
            val_href,  # type: ignore
            val_templated,  # type: ignore
            val_p_type,  # type: ignore
        )
