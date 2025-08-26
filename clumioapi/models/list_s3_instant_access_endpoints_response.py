#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    s3_instant_access_endpoint_list_embedded as s3_instant_access_endpoint_list_embedded_
from clumioapi.models import \
    s3_instant_access_endpoint_list_links as s3_instant_access_endpoint_list_links_

T = TypeVar('T', bound='ListS3InstantAccessEndpointsResponse')


class ListS3InstantAccessEndpointsResponse:
    """Implementation of the 'ListS3InstantAccessEndpointsResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        current_count:
            The number of items listed on the current page.
        limit:
            The maximum number of items displayed per page in the response.
        start:
            The page token used to get this response.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'current_count': 'current_count',
        'limit': 'limit',
        'start': 'start',
    }

    def __init__(
        self,
        embedded: (
            s3_instant_access_endpoint_list_embedded_.S3InstantAccessEndpointListEmbedded | None
        ) = None,
        links: (
            s3_instant_access_endpoint_list_links_.S3InstantAccessEndpointListLinks | None
        ) = None,
        current_count: int | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> None:
        """Constructor for the ListS3InstantAccessEndpointsResponse class."""

        # Initialize members of the class
        self.embedded: (
            s3_instant_access_endpoint_list_embedded_.S3InstantAccessEndpointListEmbedded | None
        ) = embedded
        self.links: (
            s3_instant_access_endpoint_list_links_.S3InstantAccessEndpointListLinks | None
        ) = links
        self.current_count: int | None = current_count
        self.limit: int | None = limit
        self.start: str | None = start

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
        val = dictionary.get('_embedded', None)
        val_embedded = s3_instant_access_endpoint_list_embedded_.S3InstantAccessEndpointListEmbedded.from_dictionary(
            val
        )

        val = dictionary.get('_links', None)
        val_links = (
            s3_instant_access_endpoint_list_links_.S3InstantAccessEndpointListLinks.from_dictionary(
                val
            )
        )

        val = dictionary.get('current_count', None)
        val_current_count = val

        val = dictionary.get('limit', None)
        val_limit = val

        val = dictionary.get('start', None)
        val_start = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_current_count,
            val_limit,
            val_start,
        )
