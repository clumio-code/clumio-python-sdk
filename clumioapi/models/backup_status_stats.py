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
    _names = {
        'failure_count': 'failure_count',
        'no_backup_count': 'no_backup_count',
        'partial_success_count': 'partial_success_count',
        'success_count': 'success_count',
    }

    def __init__(
        self,
        failure_count: int = None,
        no_backup_count: int = None,
        partial_success_count: int = None,
        success_count: int = None,
    ) -> None:
        """Constructor for the BackupStatusStats class."""

        # Initialize members of the class
        self.failure_count: int = failure_count
        self.no_backup_count: int = no_backup_count
        self.partial_success_count: int = partial_success_count
        self.success_count: int = success_count

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
        failure_count = dictionary.get('failure_count')
        no_backup_count = dictionary.get('no_backup_count')
        partial_success_count = dictionary.get('partial_success_count')
        success_count = dictionary.get('success_count')
        # Return an object of this model
        return cls(failure_count, no_backup_count, partial_success_count, success_count)
