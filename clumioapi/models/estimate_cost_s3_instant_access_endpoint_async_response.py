#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import estimate_cost_s3_instant_access_endpoint_async_response_links

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
    _names = {'links': '_links', 'estimate_id': 'estimate_id', 'task_id': 'task_id'}

    def __init__(
        self,
        links: estimate_cost_s3_instant_access_endpoint_async_response_links.EstimateCostS3InstantAccessEndpointAsyncResponseLinks = None,
        estimate_id: str = None,
        task_id: str = None,
    ) -> None:
        """Constructor for the EstimateCostS3InstantAccessEndpointAsyncResponse class."""

        # Initialize members of the class
        self.links: (
            estimate_cost_s3_instant_access_endpoint_async_response_links.EstimateCostS3InstantAccessEndpointAsyncResponseLinks
        ) = links
        self.estimate_id: str = estimate_id
        self.task_id: str = task_id

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
        key = '_links'
        links = (
            estimate_cost_s3_instant_access_endpoint_async_response_links.EstimateCostS3InstantAccessEndpointAsyncResponseLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        estimate_id = dictionary.get('estimate_id')
        task_id = dictionary.get('task_id')
        # Return an object of this model
        return cls(links, estimate_id, task_id)
