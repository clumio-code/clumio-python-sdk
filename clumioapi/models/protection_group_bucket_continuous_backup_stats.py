#
# Copyright 2023. Clumio, Inc.
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
    _names = {
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
        backup_end_time: str = None,
        backup_start_time: str = None,
        deleted_objects_count: int = None,
        deleted_objects_size: int = None,
        failed_continuous_backups_count: int = None,
        failed_objects_count: int = None,
        failed_objects_size: int = None,
        filtered_in_count: int = None,
        filtered_in_size: int = None,
        filtered_out_count: int = None,
        filtered_out_size: int = None,
        missing_objects_count: int = None,
        missing_objects_size: int = None,
        ongoing_continuous_backups_count: int = None,
        successful_continuous_backups_count: int = None,
        successful_objects_count: int = None,
        successful_objects_size: int = None,
        total_continuous_backups_count: int = None,
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
        backup_end_time = dictionary.get('backup_end_time')
        backup_start_time = dictionary.get('backup_start_time')
        deleted_objects_count = dictionary.get('deleted_objects_count')
        deleted_objects_size = dictionary.get('deleted_objects_size')
        failed_continuous_backups_count = dictionary.get('failed_continuous_backups_count')
        failed_objects_count = dictionary.get('failed_objects_count')
        failed_objects_size = dictionary.get('failed_objects_size')
        filtered_in_count = dictionary.get('filtered_in_count')
        filtered_in_size = dictionary.get('filtered_in_size')
        filtered_out_count = dictionary.get('filtered_out_count')
        filtered_out_size = dictionary.get('filtered_out_size')
        missing_objects_count = dictionary.get('missing_objects_count')
        missing_objects_size = dictionary.get('missing_objects_size')
        ongoing_continuous_backups_count = dictionary.get('ongoing_continuous_backups_count')
        successful_continuous_backups_count = dictionary.get('successful_continuous_backups_count')
        successful_objects_count = dictionary.get('successful_objects_count')
        successful_objects_size = dictionary.get('successful_objects_size')
        total_continuous_backups_count = dictionary.get('total_continuous_backups_count')
        # Return an object of this model
        return cls(
            backup_end_time,
            backup_start_time,
            deleted_objects_count,
            deleted_objects_size,
            failed_continuous_backups_count,
            failed_objects_count,
            failed_objects_size,
            filtered_in_count,
            filtered_in_size,
            filtered_out_count,
            filtered_out_size,
            missing_objects_count,
            missing_objects_size,
            ongoing_continuous_backups_count,
            successful_continuous_backups_count,
            successful_objects_count,
            successful_objects_size,
            total_continuous_backups_count,
        )
