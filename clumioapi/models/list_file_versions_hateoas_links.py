#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import list_file_versions_hateoas_link

T = TypeVar('T', bound='ListFileVersionsHateoasLinks')


class ListFileVersionsHateoasLinks:
    """Implementation of the 'ListFileVersionsHateoasLinks' model.

    URLs to pages related to the resource.

    Attributes:
        list_file_versions:
            A HATEOAS link to the file versions associated with this resource.
    """

    # Create a mapping from Model property names to API property names
    _names = {'list_file_versions': 'list-file-versions'}

    def __init__(
        self, list_file_versions: list_file_versions_hateoas_link.ListFileVersionsHateoasLink = None
    ) -> None:
        """Constructor for the ListFileVersionsHateoasLinks class."""

        # Initialize members of the class
        self.list_file_versions: list_file_versions_hateoas_link.ListFileVersionsHateoasLink = (
            list_file_versions
        )

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
        key = 'list-file-versions'
        list_file_versions = (
            list_file_versions_hateoas_link.ListFileVersionsHateoasLink.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(list_file_versions)
