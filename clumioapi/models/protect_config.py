#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ebs_asset_info
from clumioapi.models import rds_asset_info

T = TypeVar('T', bound='ProtectConfig')


class ProtectConfig:
    """Implementation of the 'ProtectConfig' model.

    The configuration of the Clumio Cloud Protect product for this connection.If
    this connection is not configured for Clumio Cloud Protect, then this field has
    avalue of `null`.

    Attributes:
        asset_types_enabled:
            The asset types supported on the current version of the feature
        ebs:
            The latest available information for the EBS/ EC2 feature.
        installed_template_version:
            The current version of the feature.
        rds:
            The latest available information for the EBS/ EC2 feature.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'asset_types_enabled': 'asset_types_enabled',
        'ebs': 'ebs',
        'installed_template_version': 'installed_template_version',
        'rds': 'rds',
    }

    def __init__(
        self,
        asset_types_enabled: Sequence[str] = None,
        ebs: ebs_asset_info.EbsAssetInfo = None,
        installed_template_version: str = None,
        rds: rds_asset_info.RdsAssetInfo = None,
    ) -> None:
        """Constructor for the ProtectConfig class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
        self.ebs: ebs_asset_info.EbsAssetInfo = ebs
        self.installed_template_version: str = installed_template_version
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
        key = 'ebs'
        ebs = (
            ebs_asset_info.EbsAssetInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        installed_template_version = dictionary.get('installed_template_version')
        key = 'rds'
        rds = (
            rds_asset_info.RdsAssetInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(asset_types_enabled, ebs, installed_template_version, rds)
