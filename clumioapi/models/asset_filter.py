#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import asset_group_filter as asset_group_filter_
from clumioapi.models import tag as tag_

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
    _names: dict[str, str] = {'groups': 'groups', 'tag_op_mode': 'tag_op_mode', 'tags': 'tags'}

    def __init__(
        self,
        groups: Sequence[asset_group_filter_.AssetGroupFilter] | None = None,
        tag_op_mode: str | None = None,
        tags: Sequence[tag_.Tag] | None = None,
    ) -> None:
        """Constructor for the AssetFilter class."""

        # Initialize members of the class
        self.groups: Sequence[asset_group_filter_.AssetGroupFilter] | None = groups
        self.tag_op_mode: str | None = tag_op_mode
        self.tags: Sequence[tag_.Tag] | None = tags

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
        val = dictionary.get('groups', None)

        val_groups = None
        if val:
            val_groups = list()
            for value in val:
                val_groups.append(asset_group_filter_.AssetGroupFilter.from_dictionary(value))

        val = dictionary.get('tag_op_mode', None)
        val_tag_op_mode = val

        val = dictionary.get('tags', None)

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(tag_.Tag.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_groups,
            val_tag_op_mode,
            val_tags,
        )
