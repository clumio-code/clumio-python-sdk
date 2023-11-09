#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='DynamodbTemplateInfo')


class DynamodbTemplateInfo:
    """Implementation of the 'DynamodbTemplateInfo' model.

    The latest available information for the DynamoDB feature.

    Attributes:
        available_template_version:
            The latest available feature version for the asset.
    """

    # Create a mapping from Model property names to API property names
    _names = {'available_template_version': 'available_template_version'}

    def __init__(self, available_template_version: str = None) -> None:
        """Constructor for the DynamodbTemplateInfo class."""

        # Initialize members of the class
        self.available_template_version: str = available_template_version

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
        available_template_version = dictionary.get('available_template_version')
        # Return an object of this model
        return cls(available_template_version)
