#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import asset_filter
from clumioapi.models import common_filter

T = TypeVar('T', bound='ComplianceFilters')


class ComplianceFilters:
    """Implementation of the 'ComplianceFilters' model.

    The set of filters supported in compliance report.

    Attributes:
        asset:
            The filter for asset. This will be applied to asset backup and asset protection
            controls.
        common:
            The common filter which will be applied to all controls.
    """

    # Create a mapping from Model property names to API property names
    _names = {'asset': 'asset', 'common': 'common'}

    def __init__(
        self, asset: asset_filter.AssetFilter = None, common: common_filter.CommonFilter = None
    ) -> None:
        """Constructor for the ComplianceFilters class."""

        # Initialize members of the class
        self.asset: asset_filter.AssetFilter = asset
        self.common: common_filter.CommonFilter = common

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
        key = 'asset'
        asset = (
            asset_filter.AssetFilter.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'common'
        common = (
            common_filter.CommonFilter.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(asset, common)
