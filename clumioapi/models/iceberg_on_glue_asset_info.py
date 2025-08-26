#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='IcebergOnGlueAssetInfo')


class IcebergOnGlueAssetInfo:
    """Implementation of the 'IcebergOnGlueAssetInfo' model.

    IcebergOnGlueAssetInfoThe installed information for the Iceberg on AWS Glue
    feature.

    Attributes:
        installed_template_version:
            The current version of the feature.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'installed_template_version': 'installed_template_version'}

    def __init__(self, installed_template_version: str | None = None) -> None:
        """Constructor for the IcebergOnGlueAssetInfo class."""

        # Initialize members of the class
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
        val = dictionary.get('installed_template_version', None)
        val_installed_template_version = val

        # Return an object of this model
        return cls(
            val_installed_template_version,
        )
