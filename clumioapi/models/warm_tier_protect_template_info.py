#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamodb_template_info as dynamodb_template_info_

T = TypeVar('T', bound='WarmTierProtectTemplateInfo')


class WarmTierProtectTemplateInfo:
    """Implementation of the 'WarmTierProtectTemplateInfo' model.

    Configuration information about the Warm-Tier Protect feature of the template.

    Attributes:
        asset_types_enabled:
            The AWS asset types supported with the available version of the template.
        available_template_version:
            The latest available version for the template.
        dynamodb:
            The latest available information for the DynamoDB feature.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'asset_types_enabled': 'asset_types_enabled',
        'available_template_version': 'available_template_version',
        'dynamodb': 'dynamodb',
    }

    def __init__(
        self,
        asset_types_enabled: Sequence[str] | None = None,
        available_template_version: str | None = None,
        dynamodb: dynamodb_template_info_.DynamodbTemplateInfo | None = None,
    ) -> None:
        """Constructor for the WarmTierProtectTemplateInfo class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] | None = asset_types_enabled
        self.available_template_version: str | None = available_template_version
        self.dynamodb: dynamodb_template_info_.DynamodbTemplateInfo | None = dynamodb

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
        val = dictionary.get('asset_types_enabled', None)
        val_asset_types_enabled = val

        val = dictionary.get('available_template_version', None)
        val_available_template_version = val

        val = dictionary.get('dynamodb', None)
        val_dynamodb = dynamodb_template_info_.DynamodbTemplateInfo.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_asset_types_enabled,
            val_available_template_version,
            val_dynamodb,
        )
