#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import estimate_cost_details_s3_instant_access_endpoint_response_links

T = TypeVar('T', bound='EstimateCostDetailsS3InstantAccessEndpointResponse')


class EstimateCostDetailsS3InstantAccessEndpointResponse:
    """Implementation of the 'EstimateCostDetailsS3InstantAccessEndpointResponse' model.

    Attributes:
        etag:
            The ETag value.
        links:
            URLs to pages related to the resource.
        estimated_cost:
            The estimated cost for instant access endpoint.
        total_object_count:
            The count of objects to be restored.
        total_object_size:
            The total size in bytes of objects to be restored.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'etag': '_etag',
        'links': '_links',
        'estimated_cost': 'estimated_cost',
        'total_object_count': 'total_object_count',
        'total_object_size': 'total_object_size',
    }

    def __init__(
        self,
        etag: str = None,
        links: estimate_cost_details_s3_instant_access_endpoint_response_links.EstimateCostDetailsS3InstantAccessEndpointResponseLinks = None,
        estimated_cost: float = None,
        total_object_count: int = None,
        total_object_size: int = None,
    ) -> None:
        """Constructor for the EstimateCostDetailsS3InstantAccessEndpointResponse class."""

        # Initialize members of the class
        self.etag: str = etag
        self.links: (
            estimate_cost_details_s3_instant_access_endpoint_response_links.EstimateCostDetailsS3InstantAccessEndpointResponseLinks
        ) = links
        self.estimated_cost: float = estimated_cost
        self.total_object_count: int = total_object_count
        self.total_object_size: int = total_object_size

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
        etag = dictionary.get('_etag')
        key = '_links'
        links = (
            estimate_cost_details_s3_instant_access_endpoint_response_links.EstimateCostDetailsS3InstantAccessEndpointResponseLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        estimated_cost = dictionary.get('estimated_cost')
        total_object_count = dictionary.get('total_object_count')
        total_object_size = dictionary.get('total_object_size')
        # Return an object of this model
        return cls(etag, links, estimated_cost, total_object_count, total_object_size)
