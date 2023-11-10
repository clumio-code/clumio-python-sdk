#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import object
from clumioapi.models import preview_protection_group_sync_links

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
    _names = {'links': '_links', 'objects': 'objects'}

    def __init__(
        self,
        links: preview_protection_group_sync_links.PreviewProtectionGroupSyncLinks = None,
        objects: Sequence[object.Object] = None,
    ) -> None:
        """Constructor for the PreviewProtectionGroupSyncResponse class."""

        # Initialize members of the class
        self.links: preview_protection_group_sync_links.PreviewProtectionGroupSyncLinks = links
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
        key = '_links'
        links = (
            preview_protection_group_sync_links.PreviewProtectionGroupSyncLinks.from_dictionary(
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
        return cls(links, objects)
