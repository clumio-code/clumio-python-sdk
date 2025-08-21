#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import object_v2 as object_v2_
from clumioapi.models import preview_details_s3_bucket_links as preview_details_s3_bucket_links_

T = TypeVar('T', bound='PreviewDetailsS3BucketResponse')


class PreviewDetailsS3BucketResponse:
    """Implementation of the 'PreviewDetailsS3BucketResponse' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        objects:
            The fetched objects as a result of the preview.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'links': '_links', 'objects': 'objects'}

    def __init__(
        self,
        links: preview_details_s3_bucket_links_.PreviewDetailsS3BucketLinks | None = None,
        objects: Sequence[object_v2_.ObjectV2] | None = None,
    ) -> None:
        """Constructor for the PreviewDetailsS3BucketResponse class."""

        # Initialize members of the class
        self.links: preview_details_s3_bucket_links_.PreviewDetailsS3BucketLinks | None = links
        self.objects: Sequence[object_v2_.ObjectV2] | None = objects

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
        val = dictionary.get('_links', None)
        val_links = preview_details_s3_bucket_links_.PreviewDetailsS3BucketLinks.from_dictionary(
            val
        )

        val = dictionary.get('objects', None)

        val_objects = None
        if val:
            val_objects = list()
            for value in val:
                val_objects.append(object_v2_.ObjectV2.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_links,
            val_objects,
        )
