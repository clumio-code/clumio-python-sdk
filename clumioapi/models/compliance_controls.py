#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import asset_backup_control as asset_backup_control_
from clumioapi.models import asset_protection_control as asset_protection_control_
from clumioapi.models import policy_control as policy_control_

T = TypeVar('T', bound='ComplianceControls')


class ComplianceControls:
    """Implementation of the 'ComplianceControls' model.

    The set of controls supported in compliance report.

    Attributes:
        asset_backup:
            The control for asset backup.
        asset_protection:
            The control for asset protection.
        policy:
            The control for policy.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'asset_backup': 'asset_backup',
        'asset_protection': 'asset_protection',
        'policy': 'policy',
    }

    def __init__(
        self,
        asset_backup: asset_backup_control_.AssetBackupControl | None = None,
        asset_protection: asset_protection_control_.AssetProtectionControl | None = None,
        policy: policy_control_.PolicyControl | None = None,
    ) -> None:
        """Constructor for the ComplianceControls class."""

        # Initialize members of the class
        self.asset_backup: asset_backup_control_.AssetBackupControl | None = asset_backup
        self.asset_protection: asset_protection_control_.AssetProtectionControl | None = (
            asset_protection
        )
        self.policy: policy_control_.PolicyControl | None = policy

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
        val = dictionary.get('asset_backup', None)
        val_asset_backup = asset_backup_control_.AssetBackupControl.from_dictionary(val)

        val = dictionary.get('asset_protection', None)
        val_asset_protection = asset_protection_control_.AssetProtectionControl.from_dictionary(val)

        val = dictionary.get('policy', None)
        val_policy = policy_control_.PolicyControl.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_asset_backup,
            val_asset_protection,
            val_policy,
        )
