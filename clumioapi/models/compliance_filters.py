#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import asset_filter as asset_filter_
from clumioapi.models import common_filter as common_filter_

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
    _names: dict[str, str] = {'asset': 'asset', 'common': 'common'}

    def __init__(
        self, asset: asset_filter_.AssetFilter, common: common_filter_.CommonFilter
    ) -> None:
        """Constructor for the ComplianceFilters class."""

        # Initialize members of the class
        self.asset: asset_filter_.AssetFilter = asset
        self.common: common_filter_.CommonFilter = common

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
        val = dictionary['asset']
        val_asset = asset_filter_.AssetFilter.from_dictionary(val)

        val = dictionary['common']
        val_common = common_filter_.CommonFilter.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_asset,  # type: ignore
            val_common,  # type: ignore
        )
