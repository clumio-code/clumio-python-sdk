#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    s3_instant_access_endpoint_embedded as s3_instant_access_endpoint_embedded_
from clumioapi.models import s3_instant_access_endpoint_links as s3_instant_access_endpoint_links_

T = TypeVar('T', bound='ReadS3InstantAccessEndpointUriResponse')


class ReadS3InstantAccessEndpointUriResponse:
    """Implementation of the 'ReadS3InstantAccessEndpointUriResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        bucket_alias:
            An alias of the endpoint bucket.
        cloudfront_distribution_origin_domain:
            An Origin Domain form of the endpoint URI for CloudFront distribution.
        endpoint_uri:
            The URI of the endpoint.
        region:
            The AWS region the endpoint is located in.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'bucket_alias': 'bucket_alias',
        'cloudfront_distribution_origin_domain': 'cloudfront_distribution_origin_domain',
        'endpoint_uri': 'endpoint_uri',
        'region': 'region',
    }

    def __init__(
        self,
        embedded: (
            s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded | None
        ) = None,
        links: s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks | None = None,
        bucket_alias: str | None = None,
        cloudfront_distribution_origin_domain: str | None = None,
        endpoint_uri: str | None = None,
        region: str | None = None,
    ) -> None:
        """Constructor for the ReadS3InstantAccessEndpointUriResponse class."""

        # Initialize members of the class
        self.embedded: (
            s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded | None
        ) = embedded
        self.links: s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks | None = links
        self.bucket_alias: str | None = bucket_alias
        self.cloudfront_distribution_origin_domain: str | None = (
            cloudfront_distribution_origin_domain
        )
        self.endpoint_uri: str | None = endpoint_uri
        self.region: str | None = region

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

        val = dictionary.get('bucket_alias', None)
        val_bucket_alias = val

        val = dictionary.get('cloudfront_distribution_origin_domain', None)
        val_cloudfront_distribution_origin_domain = val

        val = dictionary.get('endpoint_uri', None)
        val_endpoint_uri = val

        val = dictionary.get('region', None)
        val_region = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_bucket_alias,
            val_cloudfront_distribution_origin_domain,
            val_endpoint_uri,
            val_region,
        )
