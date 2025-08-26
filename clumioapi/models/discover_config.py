#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='DiscoverConfig')


class DiscoverConfig:
    """Implementation of the 'DiscoverConfig' model.

    The configuration of the Clumio Discover product for this connection.If this
    connection is not configured for Clumio Discover, then this field has avalue of
    `null`.

    Attributes:
        asset_types_enabled:
            The asset types supported on the current version of the feature
        installed_template_version:
            The current version of the feature.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'asset_types_enabled': 'asset_types_enabled',
        'installed_template_version': 'installed_template_version',
    }

    def __init__(
        self,
        asset_types_enabled: Sequence[str] | None = None,
        installed_template_version: str | None = None,
    ) -> None:
        """Constructor for the DiscoverConfig class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] | None = asset_types_enabled
        self.installed_template_version: str | None = installed_template_version

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

        val = dictionary.get('installed_template_version', None)
        val_installed_template_version = val

        # Return an object of this model
        return cls(
            val_asset_types_enabled,
            val_installed_template_version,
        )
