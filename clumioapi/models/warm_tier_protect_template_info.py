#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import dynamodb_template_info as dynamodb_template_info_
import requests

T = TypeVar('T', bound='WarmTierProtectTemplateInfo')


@dataclasses.dataclass
class WarmTierProtectTemplateInfo:
    """Implementation of the 'WarmTierProtectTemplateInfo' model.

    Configuration information about the Warm-Tier Protect feature of the template.

    Attributes:
        AssetTypesEnabled:
            The aws asset types supported with the available version of the template.

        AvailableTemplateVersion:
            The latest available version for the template.

        Dynamodb:
            The latest available information for the dynamodb feature.

    """

    AssetTypesEnabled: Sequence[str] | None = None
    AvailableTemplateVersion: str | None = None
    Dynamodb: dynamodb_template_info_.DynamodbTemplateInfo | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
