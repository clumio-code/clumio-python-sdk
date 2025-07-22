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
        etag: str,
        links: preview_details_protection_group_links_.PreviewDetailsProtectionGroupLinks,
        objects: Sequence[object_.Object],
    ) -> None:
        """Constructor for the PreviewDetailsProtectionGroupResponse class."""

        # Initialize members of the class
        self.etag: str = etag
        self.links: preview_details_protection_group_links_.PreviewDetailsProtectionGroupLinks = (
            links
        )
        self.objects: Sequence[object_.Object] = objects

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

        # Extract variables from the dictionary
        val = dictionary['_etag']
        val_etag = val

        val = dictionary['_links']
        val_links = preview_details_protection_group_links_.PreviewDetailsProtectionGroupLinks.from_dictionary(
            val
        )

        val = dictionary['objects']

        val_objects = None
        if val:
            val_objects = list()
            for value in val:
                val_objects.append(object_.Object.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_etag,  # type: ignore
            val_links,  # type: ignore
            val_objects,  # type: ignore
        )
