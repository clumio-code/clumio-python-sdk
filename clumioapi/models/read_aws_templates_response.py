#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import discover_template_info, protect_template_info

T = TypeVar('T', bound='ReadAWSTemplatesResponse')


class ReadAWSTemplatesResponse:
    """Implementation of the 'ReadAWSTemplatesResponse' model.

    Attributes:
        discover:
            The latest available CloudFormation template for Clumio Discover.
        protect:
            The latest available CloudFormation template for Clumio Cloud Protect.
    """

    # Create a mapping from Model property names to API property names
    _names = {'discover': 'discover', 'protect': 'protect'}

    def __init__(
        self,
        discover: discover_template_info.DiscoverTemplateInfo = None,
        protect: protect_template_info.ProtectTemplateInfo = None,
    ) -> None:
        """Constructor for the ReadAWSTemplatesResponse class."""

        # Initialize members of the class
        self.discover: discover_template_info.DiscoverTemplateInfo = discover
        self.protect: protect_template_info.ProtectTemplateInfo = protect

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
        key = 'discover'
        discover = (
            discover_template_info.DiscoverTemplateInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'protect'
        protect = (
            protect_template_info.ProtectTemplateInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(discover, protect)
