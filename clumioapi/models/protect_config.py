#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ebs_asset_info as ebs_asset_info_
from clumioapi.models import rds_asset_info as rds_asset_info_

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
            EbsAssetInfo
            The installed information for the EBS feature.
        installed_template_version:
            The current version of the feature.
        rds:
            RdsAssetInfo
            The installed information for the RDS feature.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'asset_types_enabled': 'asset_types_enabled',
        'ebs': 'ebs',
        'installed_template_version': 'installed_template_version',
        'rds': 'rds',
    }

    def __init__(
        self,
        asset_types_enabled: Sequence[str],
        ebs: ebs_asset_info_.EbsAssetInfo,
        installed_template_version: str,
        rds: rds_asset_info_.RdsAssetInfo,
    ) -> None:
        """Constructor for the ProtectConfig class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
        self.ebs: ebs_asset_info_.EbsAssetInfo = ebs
        self.installed_template_version: str = installed_template_version
        self.rds: rds_asset_info_.RdsAssetInfo = rds

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
        val = dictionary['asset_types_enabled']
        val_asset_types_enabled = val

        val = dictionary['ebs']
        val_ebs = ebs_asset_info_.EbsAssetInfo.from_dictionary(val)

        val = dictionary['installed_template_version']
        val_installed_template_version = val

        val = dictionary['rds']
        val_rds = rds_asset_info_.RdsAssetInfo.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_asset_types_enabled,  # type: ignore
            val_ebs,  # type: ignore
            val_installed_template_version,  # type: ignore
            val_rds,  # type: ignore
        )
