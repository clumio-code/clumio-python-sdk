#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3AssetInfo')


class S3AssetInfo:
    """Implementation of the 'S3AssetInfo' model.

    S3AssetInfoThe installed information for the S3 feature.

    Attributes:
        installed_template_version:
            The current version of the feature.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'installed_template_version': 'installed_template_version'}

    def __init__(self, installed_template_version: str) -> None:
        """Constructor for the S3AssetInfo class."""

        # Initialize members of the class
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
        val = dictionary['installed_template_version']
        val_installed_template_version = val

        # Return an object of this model
        return cls(
            val_installed_template_version,  # type: ignore
        )
