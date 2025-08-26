#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import object as object_
from clumioapi.models import \
    preview_protection_group_s3_asset_details_links as \
    preview_protection_group_s3_asset_details_links_

T = TypeVar('T', bound='PreviewProtectionGroupS3AssetDetailsResponse')


class PreviewProtectionGroupS3AssetDetailsResponse:
    """Implementation of the 'PreviewProtectionGroupS3AssetDetailsResponse' model.

    Attributes:
        etag:
            The ETag value.
        links:
            URLs to pages related to the resource.
        objects:
            The fetched objects as a result of the preview.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'etag': '_etag', 'links': '_links', 'objects': 'objects'}

    def __init__(
        self,
        etag: str | None = None,
        links: (
            preview_protection_group_s3_asset_details_links_.PreviewProtectionGroupS3AssetDetailsLinks
            | None
        ) = None,
        objects: Sequence[object_.Object] | None = None,
    ) -> None:
        """Constructor for the PreviewProtectionGroupS3AssetDetailsResponse class."""

        # Initialize members of the class
        self.etag: str | None = etag
        self.links: (
            preview_protection_group_s3_asset_details_links_.PreviewProtectionGroupS3AssetDetailsLinks
            | None
        ) = links
        self.objects: Sequence[object_.Object] | None = objects

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

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('_etag', None)
        val_etag = val

        val = dictionary.get('_links', None)
        val_links = preview_protection_group_s3_asset_details_links_.PreviewProtectionGroupS3AssetDetailsLinks.from_dictionary(
            val
        )

        val = dictionary.get('objects', None)

        val_objects = None
        if val:
            val_objects = list()
            for value in val:
                val_objects.append(object_.Object.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_etag,
            val_links,
            val_objects,
        )
