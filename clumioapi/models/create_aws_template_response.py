#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import template_configuration

T = TypeVar('T', bound='CreateAWSTemplateResponse')


class CreateAWSTemplateResponse:
    """Implementation of the 'CreateAWSTemplateResponse' model.

    Attributes:
        available_template_url:
            The latest available URL for the template.
        config:

    """

    # Create a mapping from Model property names to API property names
    _names = {'available_template_url': 'available_template_url', 'config': 'config'}

    def __init__(
        self,
        available_template_url: str = None,
        config: template_configuration.TemplateConfiguration = None,
    ) -> None:
        """Constructor for the CreateAWSTemplateResponse class."""

        # Initialize members of the class
        self.available_template_url: str = available_template_url
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
        available_template_url = dictionary.get('available_template_url')
        key = 'config'
        config = (
            template_configuration.TemplateConfiguration.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(available_template_url, config)
