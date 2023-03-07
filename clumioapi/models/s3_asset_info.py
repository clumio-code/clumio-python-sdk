#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3AssetInfo')


class S3AssetInfo:
    """Implementation of the 'S3AssetInfo' model.

    Attributes:
        installed_template_version:
            The current version of the feature.
    """

    # Create a mapping from Model property names to API property names
    _names = {'installed_template_version': 'installed_template_version'}

    def __init__(self, installed_template_version: str = None) -> None:
        """Constructor for the S3AssetInfo class."""

        # Initialize members of the class
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
        installed_template_version = dictionary.get('installed_template_version')
        # Return an object of this model
        return cls(installed_template_version)
