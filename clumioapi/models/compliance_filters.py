#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import asset_filter as asset_filter_
from clumioapi.models import common_filter as common_filter_
import requests

T = TypeVar('T', bound='ComplianceFilters')


@dataclasses.dataclass
class ComplianceFilters:
    """Implementation of the 'ComplianceFilters' model.

    The set of filters supported in compliance report.

    Attributes:
        Asset:
            The filter for asset. this will be applied to asset backup and asset protection controls.

        Common:
            The common filter which will be applied to all controls.

    """

    Asset: asset_filter_.AssetFilter | None = None
    Common: common_filter_.CommonFilter | None = None

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
        val = dictionary.get('asset', None)
        val_asset = asset_filter_.AssetFilter.from_dictionary(val)

        val = dictionary.get('common', None)
        val_common = common_filter_.CommonFilter.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_asset,
            val_common,
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
