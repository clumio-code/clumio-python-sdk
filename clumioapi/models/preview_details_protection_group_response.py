#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import object as object_
from clumioapi.models import \
    preview_details_protection_group_links as preview_details_protection_group_links_

T = TypeVar('T', bound='PreviewDetailsProtectionGroupResponse')


class PreviewDetailsProtectionGroupResponse:
    """Implementation of the 'PreviewDetailsProtectionGroupResponse' model.

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
            preview_details_protection_group_links_.PreviewDetailsProtectionGroupLinks | None
        ) = None,
        objects: Sequence[object_.Object] | None = None,
    ) -> None:
        """Constructor for the PreviewDetailsProtectionGroupResponse class."""

        # Initialize members of the class
        self.etag: str | None = etag
        self.links: (
            preview_details_protection_group_links_.PreviewDetailsProtectionGroupLinks | None
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
        val_links = preview_details_protection_group_links_.PreviewDetailsProtectionGroupLinks.from_dictionary(
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
