#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import template_configuration_v2
from clumioapi.models import template_links

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
    _names = {'links': '_links', 'config': 'config'}

    def __init__(
        self,
        links: template_links.TemplateLinks = None,
        config: template_configuration_v2.TemplateConfigurationV2 = None,
    ) -> None:
        """Constructor for the ReadAWSTemplatesV2Response class."""

        # Initialize members of the class
        self.links: template_links.TemplateLinks = links
        self.config: template_configuration_v2.TemplateConfigurationV2 = config

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

        key = 'config'
        config = (
            template_configuration_v2.TemplateConfigurationV2.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(links, config)
