#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_instant_access_endpoint_embedded
from clumioapi.models import s3_instant_access_endpoint_links

T = TypeVar('T', bound='DeleteS3InstantAccessEndpointRoleResponse')


class DeleteS3InstantAccessEndpointRoleResponse:
    """Implementation of the 'DeleteS3InstantAccessEndpointRoleResponse' model.

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
        embedded: s3_instant_access_endpoint_embedded.S3InstantAccessEndpointEmbedded = None,
        links: s3_instant_access_endpoint_links.S3InstantAccessEndpointLinks = None,
    ) -> None:
        """Constructor for the DeleteS3InstantAccessEndpointRoleResponse class."""

        # Initialize members of the class
        self.embedded: s3_instant_access_endpoint_embedded.S3InstantAccessEndpointEmbedded = (
            embedded
        )
        self.links: s3_instant_access_endpoint_links.S3InstantAccessEndpointLinks = links

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
            s3_instant_access_endpoint_embedded.S3InstantAccessEndpointEmbedded.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            s3_instant_access_endpoint_links.S3InstantAccessEndpointLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(embedded, links)
