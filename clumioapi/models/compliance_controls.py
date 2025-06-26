#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import asset_backup_control
from clumioapi.models import asset_protection_control
from clumioapi.models import policy_control

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
    _names = {
        'asset_backup': 'asset_backup',
        'asset_protection': 'asset_protection',
        'policy': 'policy',
    }

    def __init__(
        self,
        asset_backup: asset_backup_control.AssetBackupControl = None,
        asset_protection: asset_protection_control.AssetProtectionControl = None,
        policy: policy_control.PolicyControl = None,
    ) -> None:
        """Constructor for the ComplianceControls class."""

        # Initialize members of the class
        self.asset_backup: asset_backup_control.AssetBackupControl = asset_backup
        self.asset_protection: asset_protection_control.AssetProtectionControl = asset_protection
        self.policy: policy_control.PolicyControl = policy

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
        key = 'asset_backup'
        asset_backup = (
            asset_backup_control.AssetBackupControl.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'asset_protection'
        asset_protection = (
            asset_protection_control.AssetProtectionControl.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'policy'
        policy = (
            policy_control.PolicyControl.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(asset_backup, asset_protection, policy)
