#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import object as object_
from clumioapi.models import \
    preview_protection_group_sync_links as preview_protection_group_sync_links_

T = TypeVar('T', bound='PreviewProtectionGroupSyncResponse')


class PreviewProtectionGroupSyncResponse:
    """Implementation of the 'PreviewProtectionGroupSyncResponse' model.

    Success (Sync)

    Attributes:
        links:
            URLs to pages related to the resource.
        objects:
            The fetched objects as a result of the preview.
            Note that this field is given only for sync request.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'links': '_links', 'objects': 'objects'}

    def __init__(
        self,
        links: preview_protection_group_sync_links_.PreviewProtectionGroupSyncLinks | None = None,
        objects: Sequence[object_.Object] | None = None,
    ) -> None:
        """Constructor for the PreviewProtectionGroupSyncResponse class."""

        # Initialize members of the class
        self.links: preview_protection_group_sync_links_.PreviewProtectionGroupSyncLinks | None = (
            links
        )
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
        val = dictionary.get('_links', None)
        val_links = (
            preview_protection_group_sync_links_.PreviewProtectionGroupSyncLinks.from_dictionary(
                val
            )
        )

        val = dictionary.get('objects', None)

        val_objects = None
        if val:
            val_objects = list()
            for value in val:
                val_objects.append(object_.Object.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_links,
            val_objects,
        )
