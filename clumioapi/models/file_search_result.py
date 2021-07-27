#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import list_file_versions_hateoas_links

T = TypeVar('T', bound='FileSearchResult')


class FileSearchResult:
    """Implementation of the 'FileSearchResult' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        path:
            The full file path.
        search_result_id:
            The Clumio-assigned ID representing a collection of one or more versions of the
            same
            file backed up at different times. This ID cannot be used to restore the
            file. To restore the file, use the
            [GET /backups/files/search/{search_result_id}/versions](#operation/list-file-
            versions)
            endpoint to retrieve particular versions of this file that can be restored.
            Then, use the backup ID, filesystem ID, and file path as parameters for the
            [POST /restores/files](#operation/restore-files) endpoint.
    """

    # Create a mapping from Model property names to API property names
    _names = {'links': '_links', 'path': 'path', 'search_result_id': 'search_result_id'}

    def __init__(
        self,
        links: list_file_versions_hateoas_links.ListFileVersionsHateoasLinks = None,
        path: str = None,
        search_result_id: str = None,
    ) -> None:
        """Constructor for the FileSearchResult class."""

        # Initialize members of the class
        self.links: list_file_versions_hateoas_links.ListFileVersionsHateoasLinks = links
        self.path: str = path
        self.search_result_id: str = search_result_id

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
            list_file_versions_hateoas_links.ListFileVersionsHateoasLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        path = dictionary.get('path')
        search_result_id = dictionary.get('search_result_id')
        # Return an object of this model
        return cls(links, path, search_result_id)
