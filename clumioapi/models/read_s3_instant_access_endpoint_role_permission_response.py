#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    s3_instant_access_endpoint_embedded as s3_instant_access_endpoint_embedded_
from clumioapi.models import s3_instant_access_endpoint_links as s3_instant_access_endpoint_links_

T = TypeVar('T', bound='ReadS3InstantAccessEndpointRolePermissionResponse')


class ReadS3InstantAccessEndpointRolePermissionResponse:
    """Implementation of the 'ReadS3InstantAccessEndpointRolePermissionResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        permissions:
            The permissions JSON string to be attached to the user's IAM role to allow
            access to the
            Instant Access endpoint.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'permissions': 'permissions',
    }

    def __init__(
        self,
        embedded: s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded,
        links: s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks,
        permissions: str,
    ) -> None:
        """Constructor for the ReadS3InstantAccessEndpointRolePermissionResponse class."""

        # Initialize members of the class
        self.embedded: s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded = (
            embedded
        )
        self.links: s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks = links
        self.permissions: str = permissions

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

        # Extract variables from the dictionary
        val = dictionary['_embedded']
        val_embedded = (
            s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded.from_dictionary(
                val
            )
        )

        val = dictionary['_links']
        val_links = s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks.from_dictionary(
            val
        )

        val = dictionary['permissions']
        val_permissions = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_permissions,  # type: ignore
        )
