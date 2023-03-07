#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='EBSBackupAdvancedSetting')


class EBSBackupAdvancedSetting:
    """Implementation of the 'EBSBackupAdvancedSetting' model.

    Advanced settings for EBS backup.

    Attributes:
        backup_tier:
            Backup tier to store the backup in. Valid values are: (empty) equivalent to
            standard, `standard`, and `lite`.
    """

    # Create a mapping from Model property names to API property names
    _names = {'backup_tier': 'backup_tier'}

    def __init__(self, backup_tier: str = None) -> None:
        """Constructor for the EBSBackupAdvancedSetting class."""

        # Initialize members of the class
        self.backup_tier: str = backup_tier

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
        backup_tier = dictionary.get('backup_tier')
        # Return an object of this model
        return cls(backup_tier)
