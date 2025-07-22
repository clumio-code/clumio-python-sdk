#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    estimate_cost_s3_instant_access_endpoint_async_response_links as \
    estimate_cost_s3_instant_access_endpoint_async_response_links_

T = TypeVar('T', bound='EstimateCostS3InstantAccessEndpointAsyncResponse')


class EstimateCostS3InstantAccessEndpointAsyncResponse:
    """Implementation of the 'EstimateCostS3InstantAccessEndpointAsyncResponse' model.

    Success (Async)

    Attributes:
        links:
            URLs to pages related to the resource.
        estimate_id:
            The identifier for the requested estimate which is used to fetch results.
        task_id:
            The Clumio-assigned ID of the task created by this restore request.
            The progress of the task can be monitored using the
            `GET /tasks/{task_id}` endpoint.
            Note that this field is given only for async request.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'links': '_links', 'estimate_id': 'estimate_id', 'task_id': 'task_id'}

    def __init__(
        self,
        links: estimate_cost_s3_instant_access_endpoint_async_response_links_.EstimateCostS3InstantAccessEndpointAsyncResponseLinks,
        estimate_id: str,
        task_id: str,
    ) -> None:
        """Constructor for the EstimateCostS3InstantAccessEndpointAsyncResponse class."""

        # Initialize members of the class
        self.links: (
            estimate_cost_s3_instant_access_endpoint_async_response_links_.EstimateCostS3InstantAccessEndpointAsyncResponseLinks
        ) = links
        self.estimate_id: str = estimate_id
        self.task_id: str = task_id

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
        val = dictionary['_links']
        val_links = estimate_cost_s3_instant_access_endpoint_async_response_links_.EstimateCostS3InstantAccessEndpointAsyncResponseLinks.from_dictionary(
            val
        )

        val = dictionary['estimate_id']
        val_estimate_id = val

        val = dictionary['task_id']
        val_task_id = val

        # Return an object of this model
        return cls(
            val_links,  # type: ignore
            val_estimate_id,  # type: ignore
            val_task_id,  # type: ignore
        )
