#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import template_configuration_v2
from clumioapi.models import template_links

T = TypeVar('T', bound='CreateAWSTemplateV2Response')


class CreateAWSTemplateV2Response:
    """Implementation of the 'CreateAWSTemplateV2Response' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        cloudformation_url:
            The latest available URL for the template.
        config:
            The configuration of the given template
        terraform_url:
            The latest available URL for the terraform template.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'links': '_links',
        'cloudformation_url': 'cloudformation_url',
        'config': 'config',
        'terraform_url': 'terraform_url',
    }

    def __init__(
        self,
        links: template_links.TemplateLinks = None,
        cloudformation_url: str = None,
        config: template_configuration_v2.TemplateConfigurationV2 = None,
        terraform_url: str = None,
    ) -> None:
        """Constructor for the CreateAWSTemplateV2Response class."""

        # Initialize members of the class
        self.links: template_links.TemplateLinks = links
        self.cloudformation_url: str = cloudformation_url
        self.config: template_configuration_v2.TemplateConfigurationV2 = config
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
        key = '_links'
        links = (
            template_links.TemplateLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        cloudformation_url = dictionary.get('cloudformation_url')
        key = 'config'
        config = (
            template_configuration_v2.TemplateConfigurationV2.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        terraform_url = dictionary.get('terraform_url')
        # Return an object of this model
        return cls(links, cloudformation_url, config, terraform_url)
