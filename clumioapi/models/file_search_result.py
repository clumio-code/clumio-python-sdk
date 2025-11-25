#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import list_file_versions_hateoas_links as list_file_versions_hateoas_links_
import requests

T = TypeVar('T', bound='FileSearchResult')


@dataclasses.dataclass
class FileSearchResult:
    """Implementation of the 'FileSearchResult' model.

    Attributes:
        Links:
            Urls to pages related to the resource.

        Path:
            The full file path.

        SearchResultId:
            The clumio-assigned id representing a collection of one or more versions of the
            same
            file backed up at different times. this id cannot be used to restore the
            file. to restore the file, use the
            [get /backups/files/search/{search_result_id}/versions](#operation/list-file-
            versions)
            endpoint to retrieve particular versions of this file that can be restored.
            then, use the backup id, filesystem id, and file path as parameters for the
            [post /restores/files](#operation/restore-files) endpoint.

    """

    Links: list_file_versions_hateoas_links_.ListFileVersionsHateoasLinks | None = None
    Path: str | None = None
    SearchResultId: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
