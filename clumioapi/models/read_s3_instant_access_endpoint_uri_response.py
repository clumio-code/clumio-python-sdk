#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_instant_access_endpoint_embedded
from clumioapi.models import s3_instant_access_endpoint_links

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
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'bucket_alias': 'bucket_alias',
        'cloudfront_distribution_origin_domain': 'cloudfront_distribution_origin_domain',
        'endpoint_uri': 'endpoint_uri',
        'region': 'region',
    }

    def __init__(
        self,
        embedded: s3_instant_access_endpoint_embedded.S3InstantAccessEndpointEmbedded = None,
        links: s3_instant_access_endpoint_links.S3InstantAccessEndpointLinks = None,
        bucket_alias: str = None,
        cloudfront_distribution_origin_domain: str = None,
        endpoint_uri: str = None,
        region: str = None,
    ) -> None:
        """Constructor for the ReadS3InstantAccessEndpointUriResponse class."""

        # Initialize members of the class
        self.embedded: s3_instant_access_endpoint_embedded.S3InstantAccessEndpointEmbedded = (
            embedded
        )
        self.links: s3_instant_access_endpoint_links.S3InstantAccessEndpointLinks = links
        self.bucket_alias: str = bucket_alias
        self.cloudfront_distribution_origin_domain: str = cloudfront_distribution_origin_domain
        self.endpoint_uri: str = endpoint_uri
        self.region: str = region

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

        bucket_alias = dictionary.get('bucket_alias')
        cloudfront_distribution_origin_domain = dictionary.get(
            'cloudfront_distribution_origin_domain'
        )
        endpoint_uri = dictionary.get('endpoint_uri')
        region = dictionary.get('region')
        # Return an object of this model
        return cls(
            embedded,
            links,
            bucket_alias,
            cloudfront_distribution_origin_domain,
            endpoint_uri,
            region,
        )
