#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import ec2_mssqlag_list_embedded as ec2_mssqlag_list_embedded_
from clumioapi.models import ec2_mssqlag_list_links as ec2_mssqlag_list_links_
import requests

T = TypeVar('T', bound='ListEC2MssqlAGsResponse')


@dataclasses.dataclass
class ListEC2MssqlAGsResponse:
    """Implementation of the 'ListEC2MssqlAGsResponse' model.

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
    "1"`).

            TotalCount:
    The total number of items, summed across all pages.

            TotalPagesCount:
    The total number of pages of results.

    """

    Embedded: ec2_mssqlag_list_embedded_.EC2MSSQLAGListEmbedded | None = None
    Links: ec2_mssqlag_list_links_.EC2MSSQLAGListLinks | None = None
    CurrentCount: int | None = None
    FilterApplied: str | None = None
    Limit: int | None = None
    Start: str | None = None
    TotalCount: int | None = None
    TotalPagesCount: int | None = None
    raw_response: Optional[requests.Response] = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self,
            dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v not in [None, {}]},
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
        val_embedded = ec2_mssqlag_list_embedded_.EC2MSSQLAGListEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = ec2_mssqlag_list_links_.EC2MSSQLAGListLinks.from_dictionary(val)

        val = dictionary.get('current_count', None)
        val_current_count = val

        val = dictionary.get('filter_applied', None)
        val_filter_applied = val

        val = dictionary.get('limit', None)
        val_limit = val

        val = dictionary.get('start', None)
        val_start = val

        val = dictionary.get('total_count', None)
        val_total_count = val

        val = dictionary.get('total_pages_count', None)
        val_total_pages_count = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_current_count,
            val_filter_applied,
            val_limit,
            val_start,
            val_total_count,
            val_total_pages_count,
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
