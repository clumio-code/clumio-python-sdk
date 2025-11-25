#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import categorised_resources as categorised_resources_
from clumioapi.models import template_configuration_v2 as template_configuration_v2_
from clumioapi.models import template_links as template_links_
import requests

T = TypeVar('T', bound='CreateAWSTemplateV2Response')


@dataclasses.dataclass
class CreateAWSTemplateV2Response:
    """Implementation of the 'CreateAWSTemplateV2Response' model.

    Attributes:
        Links:
            Urls to pages related to the resource.

        CloudformationUrl:
            The latest available url for the template.

        Config:
            The configuration of the given template.

        DeployableCloudformationUrl:
            The latest available url for the deployable template.

        GroupToken:
            Ignore.

        Resources:
            Categorised resources, based on the generated template, to be created manually
            by the user.

        TerraformUrl:
            The latest available url for the terraform template.

    """

    Links: template_links_.TemplateLinks | None = None
    CloudformationUrl: str | None = None
    Config: template_configuration_v2_.TemplateConfigurationV2 | None = None
    DeployableCloudformationUrl: str | None = None
    GroupToken: str | None = None
    Resources: categorised_resources_.CategorisedResources | None = None
    TerraformUrl: str | None = None
    raw_response: Optional[requests.Response] = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        model_instance.raw_response = response
        return model_instance
