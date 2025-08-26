#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import dynamodb_asset_info as dynamodb_asset_info_
import requests

T = TypeVar('T', bound='WarmTierProtectConfig')


@dataclasses.dataclass
class WarmTierProtectConfig:
    """Implementation of the 'WarmTierProtectConfig' model.

        The configuration of the Clumio Cloud Warm-Tier Protect product for this
        connection.

        Attributes:
            Dynamodb:
                Dynamodbassetinfo
    the installed information for the dynamodb feature.

            InstalledTemplateVersion:
                The current version of the feature.

    """

    Dynamodb: dynamodb_asset_info_.DynamodbAssetInfo | None = None
    InstalledTemplateVersion: str | None = None

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
        val = dictionary.get('dynamodb', None)
        val_dynamodb = dynamodb_asset_info_.DynamodbAssetInfo.from_dictionary(val)

        val = dictionary.get('installed_template_version', None)
        val_installed_template_version = val

        # Return an object of this model
        return cls(
            val_dynamodb,
            val_installed_template_version,
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
