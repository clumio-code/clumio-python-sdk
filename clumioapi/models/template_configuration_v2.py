#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ebs_template_info
from clumioapi.models import rds_template_info

T = TypeVar('T', bound='TemplateConfigurationV2')


class TemplateConfigurationV2:
    """Implementation of the 'TemplateConfigurationV2' model.

    Attributes:
        asset_types_enabled:
            The AWS asset types supported with the available version of the template.
        available_template_version:
            The latest available version for the template.
        ebs:

        rds:

    """

    # Create a mapping from Model property names to API property names
    _names = {
        'asset_types_enabled': 'asset_types_enabled',
        'available_template_version': 'available_template_version',
        'ebs': 'ebs',
        'rds': 'rds',
    }

    def __init__(
        self,
        asset_types_enabled: Sequence[str] = None,
        available_template_version: str = None,
        ebs: ebs_template_info.EbsTemplateInfo = None,
        rds: rds_template_info.RdsTemplateInfo = None,
    ) -> None:
        """Constructor for the TemplateConfigurationV2 class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
        self.available_template_version: str = available_template_version
        self.ebs: ebs_template_info.EbsTemplateInfo = ebs
        self.rds: rds_template_info.RdsTemplateInfo = rds

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
        asset_types_enabled = dictionary.get('asset_types_enabled')
        available_template_version = dictionary.get('available_template_version')
        key = 'ebs'
        ebs = (
            ebs_template_info.EbsTemplateInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'rds'
        rds = (
            rds_template_info.RdsTemplateInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(asset_types_enabled, available_template_version, ebs, rds)
