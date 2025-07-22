#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='BackupTierStat')


class BackupTierStat:
    """Implementation of the 'BackupTierStat' model.

    BackupTierStat

    Attributes:
        backup_tier:
            The backup tier name.
        total_backed_up_object_count:
            Cumulative count of all unexpired objects in each backup (any new or updated
            since
            the last backup) that have been backed up as part of this protection group
        total_backed_up_size_bytes:
            Cumulative size of all unexpired objects in each backup (any new or updated
            since
            the last backup) that have been backed up as part of this protection group
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'backup_tier': 'backup_tier',
        'total_backed_up_object_count': 'total_backed_up_object_count',
        'total_backed_up_size_bytes': 'total_backed_up_size_bytes',
    }

    def __init__(
        self, backup_tier: str, total_backed_up_object_count: int, total_backed_up_size_bytes: int
    ) -> None:
        """Constructor for the BackupTierStat class."""

        # Initialize members of the class
        self.backup_tier: str = backup_tier
        self.total_backed_up_object_count: int = total_backed_up_object_count
        self.total_backed_up_size_bytes: int = total_backed_up_size_bytes

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
        val = dictionary['backup_tier']
        val_backup_tier = val

        val = dictionary['total_backed_up_object_count']
        val_total_backed_up_object_count = val

        val = dictionary['total_backed_up_size_bytes']
        val_total_backed_up_size_bytes = val

        # Return an object of this model
        return cls(
            val_backup_tier,  # type: ignore
            val_total_backed_up_object_count,  # type: ignore
            val_total_backed_up_size_bytes,  # type: ignore
        )
