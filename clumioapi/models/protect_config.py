#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ProtectConfig')


class ProtectConfig:
    """Implementation of the 'ProtectConfig' model.

    The configuration of the Clumio Cloud Protect product for this connection.If
    this connection is not configured for Clumio Cloud Protect, then this field has
    avalue of `null`.

    Attributes:
        asset_types_enabled:
            The asset types supported on the current version of the feature
        installed_template_version:
            The current version of the feature
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'asset_types_enabled': 'asset_types_enabled',
        'installed_template_version': 'installed_template_version',
    }

    def __init__(
        self, asset_types_enabled: Sequence[str] = None, installed_template_version: str = None
    ) -> None:
        """Constructor for the ProtectConfig class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
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
        asset_types_enabled = dictionary.get('asset_types_enabled')
        installed_template_version = dictionary.get('installed_template_version')
        # Return an object of this model
        return cls(asset_types_enabled, installed_template_version)
