#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import read_task_hateoas_outer_embedded as read_task_hateoas_outer_embedded_
from clumioapi.models import restore_s3_bucket_links as restore_s3_bucket_links_
import requests

T = TypeVar('T', bound='RestoreS3BucketResponse')


@dataclasses.dataclass
class RestoreS3BucketResponse:
    """Implementation of the 'RestoreS3BucketResponse' model.

        Attributes:
            Embedded:
                Embedded responses related to the resource.

            Links:
                Urls to pages related to the resource.

            TaskId:
                The clumio-assigned id of the task created by this restore request.
    the progress of the task can be monitored using the
    `get /tasks/{task_id}` endpoint.

    """

    Embedded: read_task_hateoas_outer_embedded_.ReadTaskHateoasOuterEmbedded | None = None
    Links: restore_s3_bucket_links_.RestoreS3BucketLinks | None = None
    TaskId: str | None = None
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
        val = dictionary.get('_embedded', None)
        val_embedded = (
            read_task_hateoas_outer_embedded_.ReadTaskHateoasOuterEmbedded.from_dictionary(val)
        )

        val = dictionary.get('_links', None)
        val_links = restore_s3_bucket_links_.RestoreS3BucketLinks.from_dictionary(val)

        val = dictionary.get('task_id', None)
        val_task_id = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
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
