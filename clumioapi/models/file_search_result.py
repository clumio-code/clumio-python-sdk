#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import list_file_versions_hateoas_links as list_file_versions_hateoas_links_

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
    _names: dict[str, str] = {
        'links': '_links',
        'path': 'path',
        'search_result_id': 'search_result_id',
    }

    def __init__(
        self,
        links: list_file_versions_hateoas_links_.ListFileVersionsHateoasLinks | None = None,
        path: str | None = None,
        search_result_id: str | None = None,
    ) -> None:
        """Constructor for the FileSearchResult class."""

        # Initialize members of the class
        self.links: list_file_versions_hateoas_links_.ListFileVersionsHateoasLinks | None = links
        self.path: str | None = path
        self.search_result_id: str | None = search_result_id

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
        val_links = list_file_versions_hateoas_links_.ListFileVersionsHateoasLinks.from_dictionary(
            val
        )

        val = dictionary.get('path', None)
        val_path = val

        val = dictionary.get('search_result_id', None)
        val_search_result_id = val

        # Return an object of this model
        return cls(
            val_links,
            val_path,
            val_search_result_id,
        )
