#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import template_configuration_v2 as template_configuration_v2_
from clumioapi.models import template_links as template_links_

T = TypeVar('T', bound='ReadAWSTemplatesV2Response')


class ReadAWSTemplatesV2Response:
    """Implementation of the 'ReadAWSTemplatesV2Response' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        config:
            The configuration of the given template
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'links': '_links', 'config': 'config'}

    def __init__(
        self,
        links: template_links_.TemplateLinks | None = None,
        config: template_configuration_v2_.TemplateConfigurationV2 | None = None,
    ) -> None:
        """Constructor for the ReadAWSTemplatesV2Response class."""

        # Initialize members of the class
        self.links: template_links_.TemplateLinks | None = links
        self.config: template_configuration_v2_.TemplateConfigurationV2 | None = config

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

        val = dictionary.get('config', None)
        val_config = template_configuration_v2_.TemplateConfigurationV2.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_links,
            val_config,
        )
