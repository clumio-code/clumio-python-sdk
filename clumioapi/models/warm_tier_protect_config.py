#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamodb_asset_info

T = TypeVar('T', bound='WarmTierProtectConfig')


class WarmTierProtectConfig:
    """Implementation of the 'WarmTierProtectConfig' model.

    The configuration of the Clumio Cloud Warm-Tier Protect product for this
    connection.

    Attributes:
        dynamodb:

        installed_template_version:
            The current version of the feature.
    """

    # Create a mapping from Model property names to API property names
    _names = {'dynamodb': 'dynamodb', 'installed_template_version': 'installed_template_version'}

    def __init__(
        self,
        dynamodb: dynamodb_asset_info.DynamodbAssetInfo = None,
        installed_template_version: str = None,
    ) -> None:
        """Constructor for the WarmTierProtectConfig class."""

        # Initialize members of the class
        self.dynamodb: dynamodb_asset_info.DynamodbAssetInfo = dynamodb
        self.installed_template_version: str = installed_template_version

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
        key = 'dynamodb'
        dynamodb = (
            dynamodb_asset_info.DynamodbAssetInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        installed_template_version = dictionary.get('installed_template_version')
        # Return an object of this model
        return cls(dynamodb, installed_template_version)
