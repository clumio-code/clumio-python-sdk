#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import object_v2 as object_v2_
from clumioapi.models import preview_details_s3_bucket_links as preview_details_s3_bucket_links_
import requests

T = TypeVar('T', bound='PreviewDetailsS3BucketResponse')


@dataclasses.dataclass
class PreviewDetailsS3BucketResponse:
    """Implementation of the 'PreviewDetailsS3BucketResponse' model.

    Attributes:
        Links:
            Urls to pages related to the resource.

        Objects:
            The fetched objects as a result of the preview.

    """

    Links: preview_details_s3_bucket_links_.PreviewDetailsS3BucketLinks | None = None
    Objects: Sequence[object_v2_.ObjectV2] | None = None
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
        val_links = preview_details_s3_bucket_links_.PreviewDetailsS3BucketLinks.from_dictionary(
            val
        )

        val = dictionary.get('objects', None)

        val_objects = []
        if val:
            for value in val:
                val_objects.append(object_v2_.ObjectV2.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_links,
            val_objects,
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
