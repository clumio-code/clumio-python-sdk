#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import categorised_resources as categorised_resources_
from clumioapi.models import template_configuration_v2 as template_configuration_v2_
from clumioapi.models import template_links as template_links_

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
    _names: dict[str, str] = {
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
        links: template_links_.TemplateLinks | None = None,
        cloudformation_url: str | None = None,
        config: template_configuration_v2_.TemplateConfigurationV2 | None = None,
        deployable_cloudformation_url: str | None = None,
        group_token: str | None = None,
        resources: categorised_resources_.CategorisedResources | None = None,
        terraform_url: str | None = None,
    ) -> None:
        """Constructor for the CreateAWSTemplateV2Response class."""

        # Initialize members of the class
        self.links: template_links_.TemplateLinks | None = links
        self.cloudformation_url: str | None = cloudformation_url
        self.config: template_configuration_v2_.TemplateConfigurationV2 | None = config
        self.deployable_cloudformation_url: str | None = deployable_cloudformation_url
        self.group_token: str | None = group_token
        self.resources: categorised_resources_.CategorisedResources | None = resources
        self.terraform_url: str | None = terraform_url

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
        val = dictionary.get('_links', None)
        val_links = template_links_.TemplateLinks.from_dictionary(val)

        val = dictionary.get('cloudformation_url', None)
        val_cloudformation_url = val

        val = dictionary.get('config', None)
        val_config = template_configuration_v2_.TemplateConfigurationV2.from_dictionary(val)

        val = dictionary.get('deployable_cloudformation_url', None)
        val_deployable_cloudformation_url = val

        val = dictionary.get('group_token', None)
        val_group_token = val

        val = dictionary.get('resources', None)
        val_resources = categorised_resources_.CategorisedResources.from_dictionary(val)

        val = dictionary.get('terraform_url', None)
        val_terraform_url = val

        # Return an object of this model
        return cls(
            val_links,
            val_cloudformation_url,
            val_config,
            val_deployable_cloudformation_url,
            val_group_token,
            val_resources,
            val_terraform_url,
        )
