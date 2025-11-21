#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import preview_s3_bucket_links as preview_s3_bucket_links_
import requests

T = TypeVar('T', bound='PreviewS3BucketResponse')


@dataclasses.dataclass
class PreviewS3BucketResponse:
    """Implementation of the 'PreviewS3BucketResponse' model.

    Attributes:
        Links:
            Urls to pages related to the resource.

        PreviewId:
            The identifier for the requested preview which is used to fetch results of the
            preview.

        TaskId:
            The clumio-assigned id of the task created by this preview request.
            the progress of the task can be monitored using the
            `get /tasks/{task_id}` endpoint.

    """

    Links: preview_s3_bucket_links_.PreviewS3BucketLinks | None = None
    PreviewId: str | None = None
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
        val = dictionary.get('_links', None)
        val_links = preview_s3_bucket_links_.PreviewS3BucketLinks.from_dictionary(val)

        val = dictionary.get('preview_id', None)
        val_preview_id = val

        val = dictionary.get('task_id', None)
        val_task_id = val

        # Return an object of this model
        return cls(
            val_links,
            val_preview_id,
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
