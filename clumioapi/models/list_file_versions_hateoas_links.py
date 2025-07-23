#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import list_file_versions_hateoas_link as list_file_versions_hateoas_link_

T = TypeVar('T', bound='ListFileVersionsHateoasLinks')


class ListFileVersionsHateoasLinks:
    """Implementation of the 'ListFileVersionsHateoasLinks' model.

    URLs to pages related to the resource.

    Attributes:
        list_file_versions:
            A HATEOAS link to the file versions associated with this resource.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'list_file_versions': 'list-file-versions'}

    def __init__(
        self,
        list_file_versions: (
            list_file_versions_hateoas_link_.ListFileVersionsHateoasLink | None
        ) = None,
    ) -> None:
        """Constructor for the ListFileVersionsHateoasLinks class."""

        # Initialize members of the class
        self.list_file_versions: (
            list_file_versions_hateoas_link_.ListFileVersionsHateoasLink | None
        ) = list_file_versions

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
        val = dictionary.get('list-file-versions', None)
        val_list_file_versions = (
            list_file_versions_hateoas_link_.ListFileVersionsHateoasLink.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_list_file_versions,
        )
