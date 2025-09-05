#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import object as object_
from clumioapi.models import \
    preview_protection_group_s3_asset_details_links as \
    preview_protection_group_s3_asset_details_links_
import requests

T = TypeVar('T', bound='PreviewProtectionGroupS3AssetDetailsResponse')


@dataclasses.dataclass
class PreviewProtectionGroupS3AssetDetailsResponse:
    """Implementation of the 'PreviewProtectionGroupS3AssetDetailsResponse' model.

        Attributes:
            Etag:
    The etag value.

            Links:
    Urls to pages related to the resource.

            Objects:
    The fetched objects as a result of the preview.

    """

    Etag: str | None = None
    Links: (
        preview_protection_group_s3_asset_details_links_.PreviewProtectionGroupS3AssetDetailsLinks
        | None
    ) = None
    Objects: Sequence[object_.Object] | None = None
    raw_response: Optional[requests.Response] = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self,
            dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v not in [None, {}]},
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
        val = dictionary.get('_etag', None)
        val_etag = val

        val = dictionary.get('_links', None)
        val_links = preview_protection_group_s3_asset_details_links_.PreviewProtectionGroupS3AssetDetailsLinks.from_dictionary(
            val
        )

        val = dictionary.get('objects', None)

        val_objects = []
        if val:
            for value in val:
                val_objects.append(object_.Object.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_etag,
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
