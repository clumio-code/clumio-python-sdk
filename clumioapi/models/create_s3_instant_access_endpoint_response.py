#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    create_s3_instant_access_endpoint_response_embedded as \
    create_s3_instant_access_endpoint_response_embedded_
from clumioapi.models import \
    create_s3_instant_access_endpoint_response_links as \
    create_s3_instant_access_endpoint_response_links_

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
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'p_id': 'id',
        'task_id': 'task_id',
    }

    def __init__(
        self,
        embedded: create_s3_instant_access_endpoint_response_embedded_.CreateS3InstantAccessEndpointResponseEmbedded,
        links: create_s3_instant_access_endpoint_response_links_.CreateS3InstantAccessEndpointResponseLinks,
        p_id: str,
        task_id: str,
    ) -> None:
        """Constructor for the CreateS3InstantAccessEndpointResponse class."""

        # Initialize members of the class
        self.embedded: (
            create_s3_instant_access_endpoint_response_embedded_.CreateS3InstantAccessEndpointResponseEmbedded
        ) = embedded
        self.links: (
            create_s3_instant_access_endpoint_response_links_.CreateS3InstantAccessEndpointResponseLinks
        ) = links
        self.p_id: str = p_id
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
        val = dictionary['_embedded']
        val_embedded = create_s3_instant_access_endpoint_response_embedded_.CreateS3InstantAccessEndpointResponseEmbedded.from_dictionary(
            val
        )

        val = dictionary['_links']
        val_links = create_s3_instant_access_endpoint_response_links_.CreateS3InstantAccessEndpointResponseLinks.from_dictionary(
            val
        )

        val = dictionary['id']
        val_p_id = val

        val = dictionary['task_id']
        val_task_id = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_p_id,  # type: ignore
            val_task_id,  # type: ignore
        )
