#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='BackupStatusStats')


class BackupStatusStats:
    """Implementation of the 'BackupStatusStats' model.

    Represents the aggregated stats for backup status.

    Attributes:
        failure_count:
            The total number of entities that have a backup status of `failure`.
        no_backup_count:
            The total number of entities that have a backup status of `no_backup`.
        partial_success_count:
            The total number of entities that have a backup status of `partial_success`.
        success_count:
            The total number of entities that have a backup status of `success`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'failure_count': 'failure_count',
        'no_backup_count': 'no_backup_count',
        'partial_success_count': 'partial_success_count',
        'success_count': 'success_count',
    }

    def __init__(
        self,
        failure_count: int | None = None,
        no_backup_count: int | None = None,
        partial_success_count: int | None = None,
        success_count: int | None = None,
    ) -> None:
        """Constructor for the BackupStatusStats class."""

        # Initialize members of the class
        self.failure_count: int | None = failure_count
        self.no_backup_count: int | None = no_backup_count
        self.partial_success_count: int | None = partial_success_count
        self.success_count: int | None = success_count

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
        val = dictionary.get('failure_count', None)
        val_failure_count = val

        val = dictionary.get('no_backup_count', None)
        val_no_backup_count = val

        val = dictionary.get('partial_success_count', None)
        val_partial_success_count = val

        val = dictionary.get('success_count', None)
        val_success_count = val

        # Return an object of this model
        return cls(
            val_failure_count,
            val_no_backup_count,
            val_partial_success_count,
            val_success_count,
        )
