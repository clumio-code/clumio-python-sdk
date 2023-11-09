#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import object
from clumioapi.models import preview_protection_group_s3_asset_details_links

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
    _names = {'etag': '_etag', 'links': '_links', 'objects': 'objects'}

    def __init__(
        self,
        etag: str = None,
        links: preview_protection_group_s3_asset_details_links.PreviewProtectionGroupS3AssetDetailsLinks = None,
        objects: Sequence[object.Object] = None,
    ) -> None:
        """Constructor for the PreviewProtectionGroupS3AssetDetailsResponse class."""

        # Initialize members of the class
        self.etag: str = etag
        self.links: preview_protection_group_s3_asset_details_links.PreviewProtectionGroupS3AssetDetailsLinks = (
            links
        )
        self.objects: Sequence[object.Object] = objects

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
        etag = dictionary.get('_etag')
        key = '_links'
        links = (
            preview_protection_group_s3_asset_details_links.PreviewProtectionGroupS3AssetDetailsLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        objects = None
        if dictionary.get('objects'):
            objects = list()
            for value in dictionary.get('objects'):
                objects.append(object.Object.from_dictionary(value))

        # Return an object of this model
        return cls(etag, links, objects)
