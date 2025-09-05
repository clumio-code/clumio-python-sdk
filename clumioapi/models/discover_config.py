#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='DiscoverConfig')


@dataclasses.dataclass
class DiscoverConfig:
    """Implementation of the 'DiscoverConfig' model.

        The configuration of the Clumio Discover product for this connection.If this
        connection is not configured for Clumio Discover, then this field has avalue of
        `null`.

        Attributes:
            AssetTypesEnabled:
    The asset types supported on the current version of the feature.

            InstalledTemplateVersion:
    The current version of the feature.

    """

    AssetTypesEnabled: Sequence[str] | None = None
    InstalledTemplateVersion: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self,
            dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v not in [None, {}]},
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
        val = dictionary.get('asset_types_enabled', None)
        val_asset_types_enabled = val

        val = dictionary.get('installed_template_version', None)
        val_installed_template_version = val

        # Return an object of this model
        return cls(
            val_asset_types_enabled,
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
