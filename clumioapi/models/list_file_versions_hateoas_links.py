#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import list_file_versions_hateoas_link as list_file_versions_hateoas_link_
import requests

T = TypeVar('T', bound='ListFileVersionsHateoasLinks')


@dataclasses.dataclass
class ListFileVersionsHateoasLinks:
    """Implementation of the 'ListFileVersionsHateoasLinks' model.

    URLs to pages related to the resource.

    Attributes:
        ListFileVersions:
            A hateoas link to the file versions associated with this resource.

    """

    ListFileVersions: list_file_versions_hateoas_link_.ListFileVersionsHateoasLink | None = None

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
        val = dictionary.get('list-file-versions', None)
        val_list_file_versions = (
            list_file_versions_hateoas_link_.ListFileVersionsHateoasLink.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_list_file_versions,
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
