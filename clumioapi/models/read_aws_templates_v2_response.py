#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import template_configuration

T = TypeVar('T', bound='ReadAWSTemplatesV2Response')


class ReadAWSTemplatesV2Response:
    """Implementation of the 'ReadAWSTemplatesV2Response' model.

    Attributes:
        cloudformation_url:
            The latest available URL for the template.
        config:

        terraform_url:
            The latest available URL for the terraform template.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'cloudformation_url': 'cloudformation_url',
        'config': 'config',
        'terraform_url': 'terraform_url',
    }

    def __init__(
        self,
        cloudformation_url: str = None,
        config: template_configuration.TemplateConfiguration = None,
        terraform_url: str = None,
    ) -> None:
        """Constructor for the ReadAWSTemplatesV2Response class."""

        # Initialize members of the class
        self.cloudformation_url: str = cloudformation_url
        self.config: template_configuration.TemplateConfiguration = config
        self.terraform_url: str = terraform_url

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
        cloudformation_url = dictionary.get('cloudformation_url')
        key = 'config'
        config = (
            template_configuration.TemplateConfiguration.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        terraform_url = dictionary.get('terraform_url')
        # Return an object of this model
        return cls(cloudformation_url, config, terraform_url)
