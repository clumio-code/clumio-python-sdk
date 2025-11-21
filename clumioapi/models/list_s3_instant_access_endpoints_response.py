#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    s3_instant_access_endpoint_list_embedded as s3_instant_access_endpoint_list_embedded_
from clumioapi.models import \
    s3_instant_access_endpoint_list_links as s3_instant_access_endpoint_list_links_
import requests

T = TypeVar('T', bound='ListS3InstantAccessEndpointsResponse')


@dataclasses.dataclass
class ListS3InstantAccessEndpointsResponse:
    """Implementation of the 'ListS3InstantAccessEndpointsResponse' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        CurrentCount:
            The number of items listed on the current page.

        Limit:
            The maximum number of items displayed per page in the response.

        Start:
            The page token used to get this response.

    """

    Embedded: (
        s3_instant_access_endpoint_list_embedded_.S3InstantAccessEndpointListEmbedded | None
    ) = None
    Links: s3_instant_access_endpoint_list_links_.S3InstantAccessEndpointListLinks | None = None
    CurrentCount: int | None = None
    Limit: int | None = None
    Start: str | None = None
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
        val_embedded = s3_instant_access_endpoint_list_embedded_.S3InstantAccessEndpointListEmbedded.from_dictionary(
            val
        )

        val = dictionary.get('_links', None)
        val_links = (
            s3_instant_access_endpoint_list_links_.S3InstantAccessEndpointListLinks.from_dictionary(
                val
            )
        )

        val = dictionary.get('current_count', None)
        val_current_count = val

        val = dictionary.get('limit', None)
        val_limit = val

        val = dictionary.get('start', None)
        val_start = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_current_count,
            val_limit,
            val_start,
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
