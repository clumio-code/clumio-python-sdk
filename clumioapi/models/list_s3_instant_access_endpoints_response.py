#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_instant_access_endpoint_list_embedded
from clumioapi.models import s3_instant_access_endpoint_list_links

T = TypeVar('T', bound='ListS3InstantAccessEndpointsResponse')


class ListS3InstantAccessEndpointsResponse:
    """Implementation of the 'ListS3InstantAccessEndpointsResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
    """

    # Create a mapping from Model property names to API property names
    _names = {'embedded': '_embedded', 'links': '_links'}

    def __init__(
        self,
        embedded: s3_instant_access_endpoint_list_embedded.S3InstantAccessEndpointListEmbedded = None,
        links: s3_instant_access_endpoint_list_links.S3InstantAccessEndpointListLinks = None,
    ) -> None:
        """Constructor for the ListS3InstantAccessEndpointsResponse class."""

        # Initialize members of the class
        self.embedded: s3_instant_access_endpoint_list_embedded.S3InstantAccessEndpointListEmbedded = (
            embedded
        )
        self.links: s3_instant_access_endpoint_list_links.S3InstantAccessEndpointListLinks = links

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
        key = '_embedded'
        embedded = (
            s3_instant_access_endpoint_list_embedded.S3InstantAccessEndpointListEmbedded.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            s3_instant_access_endpoint_list_links.S3InstantAccessEndpointListLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(embedded, links)
