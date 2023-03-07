#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='EC2MSSQLTemplateInfo')


class EC2MSSQLTemplateInfo:
    """Implementation of the 'EC2MSSQLTemplateInfo' model.

    The latest available information for the EC2 MSSQL feature.

    Attributes:
        available_template_version:
            The latest available feature version for the asset.
    """

    # Create a mapping from Model property names to API property names
    _names = {'available_template_version': 'available_template_version'}

    def __init__(self, available_template_version: str = None) -> None:
        """Constructor for the EC2MSSQLTemplateInfo class."""

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
