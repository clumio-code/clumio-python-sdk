#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='IcebergOnGlueTemplateInfo')


class IcebergOnGlueTemplateInfo:
    """Implementation of the 'IcebergOnGlueTemplateInfo' model.

    IcebergOnGlueTemplateInfo is the latest available information for the
    IcebergOnGlue feature.

    Attributes:
        available_template_version:
            The latest available feature version for the asset.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'available_template_version': 'available_template_version'}

    def __init__(self, available_template_version: str | None = None) -> None:
        """Constructor for the IcebergOnGlueTemplateInfo class."""

        # Initialize members of the class
        self.available_template_version: str | None = available_template_version

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
        val = dictionary.get('available_template_version', None)
        val_available_template_version = val

        # Return an object of this model
        return cls(
            val_available_template_version,
        )
