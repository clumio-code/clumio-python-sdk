#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ProtectionGroupBucketContinuousBackupStats')


class ProtectionGroupBucketContinuousBackupStats:
    """Implementation of the 'ProtectionGroupBucketContinuousBackupStats' model.

    ProtectionGroupBucketContinuousBackupStats

    Attributes:
        backup_end_time:
            The end time for the continuous backup stats in RFC-3339 format.
        backup_start_time:
            The start time for the continuous backup stats in RFC-3339 format.
        deleted_objects_count:
            The number of objects in the continuous backup task successfully deleted.
        deleted_objects_size:
            The total size in bytes of objects in the continuous backup task successfully
            deleted.
        failed_continuous_backups_count:
            The number of failed continuous backup task executions.
        failed_objects_count:
            The number of objects in the continuous backup task failed to be backed up.
        failed_objects_size:
            The total size in bytes of objects in the continuous backup task failed to be
            backed up.
        filtered_in_count:
            The number of included objects after the protection group filter.
        filtered_in_size:
            The total size in bytes of included objects after the protection group filter.
        filtered_out_count:
            The number of excluded objects after the protection group filter.
        filtered_out_size:
            The total size in bytes of excluded objects after the protection group filter.
        missing_objects_count:
            The number of objects in the continuous backup task missed to be backed up.
        missing_objects_size:
            The total size in bytes of objects in the continuous backup task missed to be
            backed up.
        ongoing_continuous_backups_count:
            The number of ongoing continuous backup task executions.
        successful_continuous_backups_count:
            The number of successful continuous backup task executions.
        successful_objects_count:
            The number of objects in the continuous backup task successfully backed up.
        successful_objects_size:
            The total size in bytes of objects in the continuous backup task successfully
            backed up.
        total_continuous_backups_count:
            The number of total continuous backup task executions.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'backup_end_time': 'backup_end_time',
        'backup_start_time': 'backup_start_time',
        'deleted_objects_count': 'deleted_objects_count',
        'deleted_objects_size': 'deleted_objects_size',
        'failed_continuous_backups_count': 'failed_continuous_backups_count',
        'failed_objects_count': 'failed_objects_count',
        'failed_objects_size': 'failed_objects_size',
        'filtered_in_count': 'filtered_in_count',
        'filtered_in_size': 'filtered_in_size',
        'filtered_out_count': 'filtered_out_count',
        'filtered_out_size': 'filtered_out_size',
        'missing_objects_count': 'missing_objects_count',
        'missing_objects_size': 'missing_objects_size',
        'ongoing_continuous_backups_count': 'ongoing_continuous_backups_count',
        'successful_continuous_backups_count': 'successful_continuous_backups_count',
        'successful_objects_count': 'successful_objects_count',
        'successful_objects_size': 'successful_objects_size',
        'total_continuous_backups_count': 'total_continuous_backups_count',
    }

    def __init__(
        self,
        backup_end_time: str,
        backup_start_time: str,
        deleted_objects_count: int,
        deleted_objects_size: int,
        failed_continuous_backups_count: int,
        failed_objects_count: int,
        failed_objects_size: int,
        filtered_in_count: int,
        filtered_in_size: int,
        filtered_out_count: int,
        filtered_out_size: int,
        missing_objects_count: int,
        missing_objects_size: int,
        ongoing_continuous_backups_count: int,
        successful_continuous_backups_count: int,
        successful_objects_count: int,
        successful_objects_size: int,
        total_continuous_backups_count: int,
    ) -> None:
        """Constructor for the ProtectionGroupBucketContinuousBackupStats class."""

        # Initialize members of the class
        self.backup_end_time: str = backup_end_time
        self.backup_start_time: str = backup_start_time
        self.deleted_objects_count: int = deleted_objects_count
        self.deleted_objects_size: int = deleted_objects_size
        self.failed_continuous_backups_count: int = failed_continuous_backups_count
        self.failed_objects_count: int = failed_objects_count
        self.failed_objects_size: int = failed_objects_size
        self.filtered_in_count: int = filtered_in_count
        self.filtered_in_size: int = filtered_in_size
        self.filtered_out_count: int = filtered_out_count
        self.filtered_out_size: int = filtered_out_size
        self.missing_objects_count: int = missing_objects_count
        self.missing_objects_size: int = missing_objects_size
        self.ongoing_continuous_backups_count: int = ongoing_continuous_backups_count
        self.successful_continuous_backups_count: int = successful_continuous_backups_count
        self.successful_objects_count: int = successful_objects_count
        self.successful_objects_size: int = successful_objects_size
        self.total_continuous_backups_count: int = total_continuous_backups_count

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
        val = dictionary['backup_end_time']
        val_backup_end_time = val

        val = dictionary['backup_start_time']
        val_backup_start_time = val

        val = dictionary['deleted_objects_count']
        val_deleted_objects_count = val

        val = dictionary['deleted_objects_size']
        val_deleted_objects_size = val

        val = dictionary['failed_continuous_backups_count']
        val_failed_continuous_backups_count = val

        val = dictionary['failed_objects_count']
        val_failed_objects_count = val

        val = dictionary['failed_objects_size']
        val_failed_objects_size = val

        val = dictionary['filtered_in_count']
        val_filtered_in_count = val

        val = dictionary['filtered_in_size']
        val_filtered_in_size = val

        val = dictionary['filtered_out_count']
        val_filtered_out_count = val

        val = dictionary['filtered_out_size']
        val_filtered_out_size = val

        val = dictionary['missing_objects_count']
        val_missing_objects_count = val

        val = dictionary['missing_objects_size']
        val_missing_objects_size = val

        val = dictionary['ongoing_continuous_backups_count']
        val_ongoing_continuous_backups_count = val

        val = dictionary['successful_continuous_backups_count']
        val_successful_continuous_backups_count = val

        val = dictionary['successful_objects_count']
        val_successful_objects_count = val

        val = dictionary['successful_objects_size']
        val_successful_objects_size = val

        val = dictionary['total_continuous_backups_count']
        val_total_continuous_backups_count = val

        # Return an object of this model
        return cls(
            val_backup_end_time,  # type: ignore
            val_backup_start_time,  # type: ignore
            val_deleted_objects_count,  # type: ignore
            val_deleted_objects_size,  # type: ignore
            val_failed_continuous_backups_count,  # type: ignore
            val_failed_objects_count,  # type: ignore
            val_failed_objects_size,  # type: ignore
            val_filtered_in_count,  # type: ignore
            val_filtered_in_size,  # type: ignore
            val_filtered_out_count,  # type: ignore
            val_filtered_out_size,  # type: ignore
            val_missing_objects_count,  # type: ignore
            val_missing_objects_size,  # type: ignore
            val_ongoing_continuous_backups_count,  # type: ignore
            val_successful_continuous_backups_count,  # type: ignore
            val_successful_objects_count,  # type: ignore
            val_successful_objects_size,  # type: ignore
            val_total_continuous_backups_count,  # type: ignore
        )
