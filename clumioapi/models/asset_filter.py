#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import asset_group_filter
from clumioapi.models import tag

T = TypeVar('T', bound='AssetFilter')


class AssetFilter:
    """Implementation of the 'AssetFilter' model.

    The filter for asset. This will be applied to asset backup and asset protection
    controls.

    Attributes:
        groups:
            The asset groups to be filtered.
        tag_op_mode:
            The tag filter operation to be applied to the given tags. This is supported for
            AWS assets only.
        tags:
            The asset tags to be filtered. This is supported for AWS assets only.
    """

    # Create a mapping from Model property names to API property names
    _names = {'groups': 'groups', 'tag_op_mode': 'tag_op_mode', 'tags': 'tags'}

    def __init__(
        self,
        groups: Sequence[asset_group_filter.AssetGroupFilter] = None,
        tag_op_mode: str = None,
        tags: Sequence[tag.Tag] = None,
    ) -> None:
        """Constructor for the AssetFilter class."""

        # Initialize members of the class
        self.groups: Sequence[asset_group_filter.AssetGroupFilter] = groups
        self.tag_op_mode: str = tag_op_mode
        self.tags: Sequence[tag.Tag] = tags

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
        groups = None
        if dictionary.get('groups'):
            groups = list()
            for value in dictionary.get('groups'):
                groups.append(asset_group_filter.AssetGroupFilter.from_dictionary(value))

        tag_op_mode = dictionary.get('tag_op_mode')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(tag.Tag.from_dictionary(value))

        # Return an object of this model
        return cls(groups, tag_op_mode, tags)
