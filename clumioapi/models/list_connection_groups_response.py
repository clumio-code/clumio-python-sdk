#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    aws_connection_group_list_embedded as aws_connection_group_list_embedded_
from clumioapi.models import connection_group_list_links as connection_group_list_links_
import requests

T = TypeVar('T', bound='ListConnectionGroupsResponse')


@dataclasses.dataclass
class ListConnectionGroupsResponse:
    """Implementation of the 'ListConnectionGroupsResponse' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        CurrentCount:
            The number of items listed on the current page.

        FilterApplied:
            The filter used in the request. the filter includes both manually-specified and system-generated filters.

        Limit:
            The maximum number of items displayed per page in the response.

        Start:
            The page token used to get this response.

    """

    Embedded: aws_connection_group_list_embedded_.AWSConnectionGroupListEmbedded | None = None
    Links: connection_group_list_links_.ConnectionGroupListLinks | None = None
    CurrentCount: int | None = None
    FilterApplied: str | None = None
    Limit: int | None = None
    Start: str | None = None
    raw_response: Optional[requests.Response] = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
        val = dictionary.get('_embedded', None)
        val_embedded = (
            aws_connection_group_list_embedded_.AWSConnectionGroupListEmbedded.from_dictionary(val)
        )

        val = dictionary.get('_links', None)
        val_links = connection_group_list_links_.ConnectionGroupListLinks.from_dictionary(val)

        val = dictionary.get('current_count', None)
        val_current_count = val

        val = dictionary.get('filter_applied', None)
        val_filter_applied = val

        val = dictionary.get('limit', None)
        val_limit = val

        val = dictionary.get('start', None)
        val_start = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_current_count,
            val_filter_applied,
            val_limit,
            val_start,
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
        model_instance.raw_response = response
        return model_instance
