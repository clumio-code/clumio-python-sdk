#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import object_v2
from clumioapi.models import preview_details_s3_bucket_links

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
    _names = {'links': '_links', 'objects': 'objects'}

    def __init__(
        self,
        links: preview_details_s3_bucket_links.PreviewDetailsS3BucketLinks = None,
        objects: Sequence[object_v2.ObjectV2] = None,
    ) -> None:
        """Constructor for the PreviewDetailsS3BucketResponse class."""

        # Initialize members of the class
        self.links: preview_details_s3_bucket_links.PreviewDetailsS3BucketLinks = links
        self.objects: Sequence[object_v2.ObjectV2] = objects

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
        key = '_links'
        links = (
            preview_details_s3_bucket_links.PreviewDetailsS3BucketLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        objects = None
        if dictionary.get('objects'):
            objects = list()
            for value in dictionary.get('objects'):
                objects.append(object_v2.ObjectV2.from_dictionary(value))

        # Return an object of this model
        return cls(links, objects)
