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
        embedded: s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded,
        links: s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks,
        bucket_alias: str,
        cloudfront_distribution_origin_domain: str,
        endpoint_uri: str,
        region: str,
    ) -> None:
        """Constructor for the ReadS3InstantAccessEndpointUriResponse class."""

        # Initialize members of the class
        self.embedded: s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded = (
            embedded
        )
        self.links: s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks = links
        self.bucket_alias: str = bucket_alias
        self.cloudfront_distribution_origin_domain: str = cloudfront_distribution_origin_domain
        self.endpoint_uri: str = endpoint_uri
        self.region: str = region

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

        val = dictionary['bucket_alias']
        val_bucket_alias = val

        val = dictionary['cloudfront_distribution_origin_domain']
        val_cloudfront_distribution_origin_domain = val

        val = dictionary['endpoint_uri']
        val_endpoint_uri = val

        val = dictionary['region']
        val_region = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_bucket_alias,  # type: ignore
            val_cloudfront_distribution_origin_domain,  # type: ignore
            val_endpoint_uri,  # type: ignore
            val_region,  # type: ignore
        )
