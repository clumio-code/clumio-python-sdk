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
        links: template_links_.TemplateLinks,
        cloudformation_url: str,
        config: template_configuration_v2_.TemplateConfigurationV2,
        deployable_cloudformation_url: str,
        group_token: str,
        resources: categorised_resources_.CategorisedResources,
        terraform_url: str,
    ) -> None:
        """Constructor for the CreateAWSTemplateV2Response class."""

        # Initialize members of the class
        self.links: template_links_.TemplateLinks = links
        self.cloudformation_url: str = cloudformation_url
        self.config: template_configuration_v2_.TemplateConfigurationV2 = config
        self.deployable_cloudformation_url: str = deployable_cloudformation_url
        self.group_token: str = group_token
        self.resources: categorised_resources_.CategorisedResources = resources
        self.terraform_url: str = terraform_url

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

        # Extract variables from the dictionary
        val = dictionary['_links']
        val_links = template_links_.TemplateLinks.from_dictionary(val)

        val = dictionary['cloudformation_url']
        val_cloudformation_url = val

        val = dictionary['config']
        val_config = template_configuration_v2_.TemplateConfigurationV2.from_dictionary(val)

        val = dictionary['deployable_cloudformation_url']
        val_deployable_cloudformation_url = val

        val = dictionary['group_token']
        val_group_token = val

        val = dictionary['resources']
        val_resources = categorised_resources_.CategorisedResources.from_dictionary(val)

        val = dictionary['terraform_url']
        val_terraform_url = val

        # Return an object of this model
        return cls(
            val_links,  # type: ignore
            val_cloudformation_url,  # type: ignore
            val_config,  # type: ignore
            val_deployable_cloudformation_url,  # type: ignore
            val_group_token,  # type: ignore
            val_resources,  # type: ignore
            val_terraform_url,  # type: ignore
        )
