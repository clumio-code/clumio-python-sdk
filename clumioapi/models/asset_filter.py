#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import asset_group_filter as asset_group_filter_
from clumioapi.models import tag as tag_
import requests

T = TypeVar('T', bound='AssetFilter')


@dataclasses.dataclass
class AssetFilter:
    """Implementation of the 'AssetFilter' model.

    The filter for asset. This will be applied to asset backup and asset protection
    controls.

    Attributes:
        Groups:
            The asset groups to be filtered.

        TagOpMode:
            The tag filter operation to be applied to the given tags. this is supported for aws assets only.

        Tags:
            The asset tags to be filtered. this is supported for aws assets only.

    """

    Groups: Sequence[asset_group_filter_.AssetGroupFilter] | None = None
    TagOpMode: str | None = None
    Tags: Sequence[tag_.Tag] | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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

        val_groups = []
        if val:
            for value in val:
                val_groups.append(asset_group_filter_.AssetGroupFilter.from_dictionary(value))

        val = dictionary.get('tag_op_mode', None)
        val_tag_op_mode = val

        val = dictionary.get('tags', None)

        val_tags = []
        if val:
            for value in val:
                val_tags.append(tag_.Tag.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_groups,
            val_tag_op_mode,
            val_tags,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
