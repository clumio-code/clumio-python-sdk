#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import template_configuration

T = TypeVar('T', bound='ReadAWSTemplatesV2Response')


class ReadAWSTemplatesV2Response:
    """Implementation of the 'ReadAWSTemplatesV2Response' model.

    Attributes:
        config:

    """

    # Create a mapping from Model property names to API property names
    _names = {'config': 'config'}

    def __init__(self, config: template_configuration.TemplateConfiguration = None) -> None:
        """Constructor for the ReadAWSTemplatesV2Response class."""

        # Initialize members of the class
        self.config: template_configuration.TemplateConfiguration = config

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
        key = 'config'
        config = (
            template_configuration.TemplateConfiguration.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(config)
