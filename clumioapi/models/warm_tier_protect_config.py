#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamodb_asset_info as dynamodb_asset_info_

T = TypeVar('T', bound='WarmTierProtectConfig')


class WarmTierProtectConfig:
    """Implementation of the 'WarmTierProtectConfig' model.

    The configuration of the Clumio Cloud Warm-Tier Protect product for this
    connection.

    Attributes:
        dynamodb:
            DynamodbAssetInfo
            The installed information for the DynamoDB feature.
        installed_template_version:
            The current version of the feature.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'dynamodb': 'dynamodb',
        'installed_template_version': 'installed_template_version',
    }

    def __init__(
        self, dynamodb: dynamodb_asset_info_.DynamodbAssetInfo, installed_template_version: str
    ) -> None:
        """Constructor for the WarmTierProtectConfig class."""

        # Initialize members of the class
        self.dynamodb: dynamodb_asset_info_.DynamodbAssetInfo = dynamodb
        self.installed_template_version: str = installed_template_version

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
        val = dictionary['dynamodb']
        val_dynamodb = dynamodb_asset_info_.DynamodbAssetInfo.from_dictionary(val)

        val = dictionary['installed_template_version']
        val_installed_template_version = val

        # Return an object of this model
        return cls(
            val_dynamodb,  # type: ignore
            val_installed_template_version,  # type: ignore
        )
