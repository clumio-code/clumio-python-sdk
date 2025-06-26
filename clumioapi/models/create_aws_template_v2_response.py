#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import categorised_resources
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
        deployable_cloudformation_url:
            The latest available URL for the deployable template.
        group_token:
            swagger: ignore
        resources:
            Categorised Resources, based on the generated template, to be created manually
            by the user
        terraform_url:
            The latest available URL for the terraform template.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'links': '_links',
        'cloudformation_url': 'cloudformation_url',
        'config': 'config',
        'deployable_cloudformation_url': 'deployable_cloudformation_url',
        'group_token': 'group_token',
        'resources': 'resources',
        'terraform_url': 'terraform_url',
    }

    def __init__(
        self,
        links: template_links.TemplateLinks = None,
        cloudformation_url: str = None,
        config: template_configuration_v2.TemplateConfigurationV2 = None,
        deployable_cloudformation_url: str = None,
        group_token: str = None,
        resources: categorised_resources.CategorisedResources = None,
        terraform_url: str = None,
    ) -> None:
        """Constructor for the CreateAWSTemplateV2Response class."""

        # Initialize members of the class
        self.links: template_links.TemplateLinks = links
        self.cloudformation_url: str = cloudformation_url
        self.config: template_configuration_v2.TemplateConfigurationV2 = config
        self.deployable_cloudformation_url: str = deployable_cloudformation_url
        self.group_token: str = group_token
        self.resources: categorised_resources.CategorisedResources = resources
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

        deployable_cloudformation_url = dictionary.get('deployable_cloudformation_url')
        group_token = dictionary.get('group_token')
        key = 'resources'
        resources = (
            categorised_resources.CategorisedResources.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        terraform_url = dictionary.get('terraform_url')
        # Return an object of this model
        return cls(
            links,
            cloudformation_url,
            config,
            deployable_cloudformation_url,
            group_token,
            resources,
            terraform_url,
        )
