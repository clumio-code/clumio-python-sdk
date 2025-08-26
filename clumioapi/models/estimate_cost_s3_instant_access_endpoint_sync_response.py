#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    estimate_cost_s3_instant_access_endpoint_sync_response_links as \
    estimate_cost_s3_instant_access_endpoint_sync_response_links_
import requests

T = TypeVar('T', bound='EstimateCostS3InstantAccessEndpointSyncResponse')


@dataclasses.dataclass
class EstimateCostS3InstantAccessEndpointSyncResponse:
    """Implementation of the 'EstimateCostS3InstantAccessEndpointSyncResponse' model.

    Success (Sync)

    Attributes:
        Links:
            Urls to pages related to the resource.

        EstimatedCost:
            The estimated cost for instant access endpoint.

        TotalObjectCount:
            The count of objects to be restored.

        TotalObjectSize:
            The total size in bytes of objects to be restored.

    """

    Links: (
        estimate_cost_s3_instant_access_endpoint_sync_response_links_.EstimateCostS3InstantAccessEndpointSyncResponseLinks
        | None
    ) = None
    EstimatedCost: float | None = None
    TotalObjectCount: int | None = None
    TotalObjectSize: int | None = None
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
