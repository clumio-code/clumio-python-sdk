#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    estimate_cost_s3_instant_access_endpoint_sync_response_links as \
    estimate_cost_s3_instant_access_endpoint_sync_response_links_

T = TypeVar('T', bound='EstimateCostS3InstantAccessEndpointSyncResponse')


class EstimateCostS3InstantAccessEndpointSyncResponse:
    """Implementation of the 'EstimateCostS3InstantAccessEndpointSyncResponse' model.

    Success (Sync)

    Attributes:
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
    _names: dict[str, str] = {
        'links': '_links',
        'estimated_cost': 'estimated_cost',
        'total_object_count': 'total_object_count',
        'total_object_size': 'total_object_size',
    }

    def __init__(
        self,
        links: (
            estimate_cost_s3_instant_access_endpoint_sync_response_links_.EstimateCostS3InstantAccessEndpointSyncResponseLinks
            | None
        ) = None,
        estimated_cost: float | None = None,
        total_object_count: int | None = None,
        total_object_size: int | None = None,
    ) -> None:
        """Constructor for the EstimateCostS3InstantAccessEndpointSyncResponse class."""

        # Initialize members of the class
        self.links: (
            estimate_cost_s3_instant_access_endpoint_sync_response_links_.EstimateCostS3InstantAccessEndpointSyncResponseLinks
            | None
        ) = links
        self.estimated_cost: float | None = estimated_cost
        self.total_object_count: int | None = total_object_count
        self.total_object_size: int | None = total_object_size

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
        val = dictionary.get('_links', None)
        val_links = estimate_cost_s3_instant_access_endpoint_sync_response_links_.EstimateCostS3InstantAccessEndpointSyncResponseLinks.from_dictionary(
            val
        )

        val = dictionary.get('estimated_cost', None)
        val_estimated_cost = val

        val = dictionary.get('total_object_count', None)
        val_total_object_count = val

        val = dictionary.get('total_object_size', None)
        val_total_object_size = val

        # Return an object of this model
        return cls(
            val_links,
            val_estimated_cost,
            val_total_object_count,
            val_total_object_size,
        )
