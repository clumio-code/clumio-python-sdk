#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import create_s3_instant_access_endpoint_response_embedded
from clumioapi.models import create_s3_instant_access_endpoint_response_links

T = TypeVar('T', bound='CreateS3InstantAccessEndpointResponse')


class CreateS3InstantAccessEndpointResponse:
    """Implementation of the 'CreateS3InstantAccessEndpointResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        p_id:
            The Clumio-assigned ID of the S3 instant access endpoint.
        task_id:
            The Clumio-assigned ID of the task created by this instant access creation
            request.
            The progress of the task can be monitored using the `GET /tasks/{task_id}`
            endpoint.
    """

    # Create a mapping from Model property names to API property names
    _names = {'embedded': '_embedded', 'links': '_links', 'p_id': 'id', 'task_id': 'task_id'}

    def __init__(
        self,
        embedded: create_s3_instant_access_endpoint_response_embedded.CreateS3InstantAccessEndpointResponseEmbedded = None,
        links: create_s3_instant_access_endpoint_response_links.CreateS3InstantAccessEndpointResponseLinks = None,
        p_id: str = None,
        task_id: str = None,
    ) -> None:
        """Constructor for the CreateS3InstantAccessEndpointResponse class."""

        # Initialize members of the class
        self.embedded: create_s3_instant_access_endpoint_response_embedded.CreateS3InstantAccessEndpointResponseEmbedded = (
            embedded
        )
        self.links: create_s3_instant_access_endpoint_response_links.CreateS3InstantAccessEndpointResponseLinks = (
            links
        )
        self.p_id: str = p_id
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
        key = '_embedded'
        embedded = (
            create_s3_instant_access_endpoint_response_embedded.CreateS3InstantAccessEndpointResponseEmbedded.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            create_s3_instant_access_endpoint_response_links.CreateS3InstantAccessEndpointResponseLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        p_id = dictionary.get('id')
        task_id = dictionary.get('task_id')
        # Return an object of this model
        return cls(embedded, links, p_id, task_id)
