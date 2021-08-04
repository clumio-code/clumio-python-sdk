#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ebs_asset_info
from clumioapi.models import rds_asset_info

T = TypeVar('T', bound='ProtectTemplateInfo')


class ProtectTemplateInfo:
    """Implementation of the 'ProtectTemplateInfo' model.

    The latest available CloudFormation template for Clumio Cloud Protect.

    Attributes:
        asset_types_enabled:
            The AWS asset types supported with the available version of the template.
        available_template_url:
            The latest available URL for the template.
        available_template_version:
            The latest available version for the template.
        ebs:
            The latest available information for the EBS/ EC2 feature.
        rds:
            The latest available information for the EBS/ EC2 feature.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'asset_types_enabled': 'asset_types_enabled',
        'available_template_url': 'available_template_url',
        'available_template_version': 'available_template_version',
        'ebs': 'ebs',
        'rds': 'rds',
    }

    def __init__(
        self,
        asset_types_enabled: Sequence[str] = None,
        available_template_url: str = None,
        available_template_version: str = None,
        ebs: ebs_asset_info.EbsAssetInfo = None,
        rds: rds_asset_info.RdsAssetInfo = None,
    ) -> None:
        """Constructor for the ProtectTemplateInfo class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
        self.available_template_url: str = available_template_url
        self.available_template_version: str = available_template_version
        self.ebs: ebs_asset_info.EbsAssetInfo = ebs
        self.rds: rds_asset_info.RdsAssetInfo = rds

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
        available_template_url = dictionary.get('available_template_url')
        available_template_version = dictionary.get('available_template_version')
        key = 'ebs'
        ebs = (
            ebs_asset_info.EbsAssetInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'rds'
        rds = (
            rds_asset_info.RdsAssetInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(
            asset_types_enabled, available_template_url, available_template_version, ebs, rds
        )
