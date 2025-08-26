#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='RDSLogicalBackupAdvancedSetting')


class RDSLogicalBackupAdvancedSetting:
    """Implementation of the 'RDSLogicalBackupAdvancedSetting' model.

    Settings for determining if a RDS policy is created with standard or archive
    tier.

    Attributes:
        backup_tier:
            Backup tier to store the backup in. Valid values are: `standard`, `archive`
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'backup_tier': 'backup_tier'}

    def __init__(self, backup_tier: str | None = None) -> None:
        """Constructor for the RDSLogicalBackupAdvancedSetting class."""

        # Initialize members of the class
        self.backup_tier: str | None = backup_tier

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
        val = dictionary.get('backup_tier', None)
        val_backup_tier = val

        # Return an object of this model
        return cls(
            val_backup_tier,
        )
