#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamodb_template_info

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
    _names = {
        'asset_types_enabled': 'asset_types_enabled',
        'available_template_version': 'available_template_version',
        'dynamodb': 'dynamodb',
    }

    def __init__(
        self,
        asset_types_enabled: Sequence[str] = None,
        available_template_version: str = None,
        dynamodb: dynamodb_template_info.DynamodbTemplateInfo = None,
    ) -> None:
        """Constructor for the WarmTierProtectTemplateInfo class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
        self.available_template_version: str = available_template_version
        self.dynamodb: dynamodb_template_info.DynamodbTemplateInfo = dynamodb

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
        key = 'dynamodb'
        dynamodb = (
            dynamodb_template_info.DynamodbTemplateInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(asset_types_enabled, available_template_version, dynamodb)
