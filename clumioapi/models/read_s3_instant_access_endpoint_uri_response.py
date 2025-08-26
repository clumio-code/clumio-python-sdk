#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    s3_instant_access_endpoint_embedded as s3_instant_access_endpoint_embedded_
from clumioapi.models import s3_instant_access_endpoint_links as s3_instant_access_endpoint_links_
import requests

T = TypeVar('T', bound='ReadS3InstantAccessEndpointUriResponse')


@dataclasses.dataclass
class ReadS3InstantAccessEndpointUriResponse:
    """Implementation of the 'ReadS3InstantAccessEndpointUriResponse' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        BucketAlias:
            An alias of the endpoint bucket.

        CloudfrontDistributionOriginDomain:
            An origin domain form of the endpoint uri for cloudfront distribution.

        EndpointUri:
            The uri of the endpoint.

        Region:
            The aws region the endpoint is located in.

    """

    Embedded: s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded | None = None
    Links: s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks | None = None
    BucketAlias: str | None = None
    CloudfrontDistributionOriginDomain: str | None = None
    EndpointUri: str | None = None
    Region: str | None = None
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
