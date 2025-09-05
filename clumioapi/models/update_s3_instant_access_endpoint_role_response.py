#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    s3_instant_access_endpoint_embedded as s3_instant_access_endpoint_embedded_
from clumioapi.models import s3_instant_access_endpoint_links as s3_instant_access_endpoint_links_

T = TypeVar('T', bound='UpdateS3InstantAccessEndpointRoleResponse')


class UpdateS3InstantAccessEndpointRoleResponse:
    """Implementation of the 'UpdateS3InstantAccessEndpointRoleResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'embedded': '_embedded', 'links': '_links'}

    def __init__(
        self,
        embedded: (
            s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded | None
        ) = None,
        links: s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks | None = None,
    ) -> None:
        """Constructor for the UpdateS3InstantAccessEndpointRoleResponse class."""

        # Initialize members of the class
        self.embedded: (
            s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded | None
        ) = embedded
        self.links: s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks | None = links

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
        val_embedded = (
            s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded.from_dictionary(
                val
            )
        )

        val = dictionary.get('_links', None)
        val_links = s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
        )
