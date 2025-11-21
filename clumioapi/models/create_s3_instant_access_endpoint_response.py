#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    create_s3_instant_access_endpoint_response_embedded as \
    create_s3_instant_access_endpoint_response_embedded_
from clumioapi.models import \
    create_s3_instant_access_endpoint_response_links as \
    create_s3_instant_access_endpoint_response_links_
import requests

T = TypeVar('T', bound='CreateS3InstantAccessEndpointResponse')


@dataclasses.dataclass
class CreateS3InstantAccessEndpointResponse:
    """Implementation of the 'CreateS3InstantAccessEndpointResponse' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        Id:
            The clumio-assigned id of the s3 instant access endpoint.

        TaskId:
            The clumio-assigned id of the task created by this instant access creation
            request.
            the progress of the task can be monitored using the `get /tasks/{task_id}`
            endpoint.

    """

    Embedded: (
        create_s3_instant_access_endpoint_response_embedded_.CreateS3InstantAccessEndpointResponseEmbedded
        | None
    ) = None
    Links: (
        create_s3_instant_access_endpoint_response_links_.CreateS3InstantAccessEndpointResponseLinks
        | None
    ) = None
    Id: str | None = None
    TaskId: str | None = None
    raw_response: Optional[requests.Response] = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('_embedded', None)
        val_embedded = create_s3_instant_access_endpoint_response_embedded_.CreateS3InstantAccessEndpointResponseEmbedded.from_dictionary(
            val
        )

        val = dictionary.get('_links', None)
        val_links = create_s3_instant_access_endpoint_response_links_.CreateS3InstantAccessEndpointResponseLinks.from_dictionary(
            val
        )

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('task_id', None)
        val_task_id = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_id,
            val_task_id,
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
