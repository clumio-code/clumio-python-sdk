#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='DiscoverTemplateInfoV2')


class DiscoverTemplateInfoV2:
    """Implementation of the 'DiscoverTemplateInfoV2' model.

    Attributes:
        asset_types_enabled:
            The AWS asset types supported with the available version of the template.
        available_template_version:
            The latest available version for the template.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'asset_types_enabled': 'asset_types_enabled',
        'available_template_version': 'available_template_version',
    }

    def __init__(
        self, asset_types_enabled: Sequence[str] = None, available_template_version: str = None
    ) -> None:
        """Constructor for the DiscoverTemplateInfoV2 class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
        self.available_template_version: str = available_template_version

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
        asset_types_enabled = dictionary.get('asset_types_enabled')
        available_template_version = dictionary.get('available_template_version')
        # Return an object of this model
        return cls(asset_types_enabled, available_template_version)
