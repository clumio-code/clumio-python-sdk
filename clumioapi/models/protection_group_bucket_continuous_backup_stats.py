#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='ProtectionGroupBucketContinuousBackupStats')


@dataclasses.dataclass
class ProtectionGroupBucketContinuousBackupStats:
    """Implementation of the 'ProtectionGroupBucketContinuousBackupStats' model.

    ProtectionGroupBucketContinuousBackupStats

    Attributes:
        BackupEndTime:
            The end time for the continuous backup stats in rfc-3339 format.

        BackupStartTime:
            The start time for the continuous backup stats in rfc-3339 format.

        DeletedObjectsCount:
            The number of objects in the continuous backup task successfully deleted.

        DeletedObjectsSize:
            The total size in bytes of objects in the continuous backup task successfully
            deleted.

        FailedContinuousBackupsCount:
            The number of failed continuous backup task executions.

        FailedObjectsCount:
            The number of objects in the continuous backup task failed to be backed up.

        FailedObjectsSize:
            The total size in bytes of objects in the continuous backup task failed to be
            backed up.

        FilteredInCount:
            The number of included objects after the protection group filter.

        FilteredInSize:
            The total size in bytes of included objects after the protection group filter.

        FilteredOutCount:
            The number of excluded objects after the protection group filter.

        FilteredOutSize:
            The total size in bytes of excluded objects after the protection group filter.

        MissingObjectsCount:
            The number of objects in the continuous backup task missed to be backed up.

        MissingObjectsSize:
            The total size in bytes of objects in the continuous backup task missed to be
            backed up.

        OngoingContinuousBackupsCount:
            The number of ongoing continuous backup task executions.

        SuccessfulContinuousBackupsCount:
            The number of successful continuous backup task executions.

        SuccessfulObjectsCount:
            The number of objects in the continuous backup task successfully backed up.

        SuccessfulObjectsSize:
            The total size in bytes of objects in the continuous backup task successfully
            backed up.

        TotalContinuousBackupsCount:
            The number of total continuous backup task executions.

    """

    BackupEndTime: str | None = None
    BackupStartTime: str | None = None
    DeletedObjectsCount: int | None = None
    DeletedObjectsSize: int | None = None
    FailedContinuousBackupsCount: int | None = None
    FailedObjectsCount: int | None = None
    FailedObjectsSize: int | None = None
    FilteredInCount: int | None = None
    FilteredInSize: int | None = None
    FilteredOutCount: int | None = None
    FilteredOutSize: int | None = None
    MissingObjectsCount: int | None = None
    MissingObjectsSize: int | None = None
    OngoingContinuousBackupsCount: int | None = None
    SuccessfulContinuousBackupsCount: int | None = None
    SuccessfulObjectsCount: int | None = None
    SuccessfulObjectsSize: int | None = None
    TotalContinuousBackupsCount: int | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('backup_end_time', None)
        val_backup_end_time = val

        val = dictionary.get('backup_start_time', None)
        val_backup_start_time = val

        val = dictionary.get('deleted_objects_count', None)
        val_deleted_objects_count = val

        val = dictionary.get('deleted_objects_size', None)
        val_deleted_objects_size = val

        val = dictionary.get('failed_continuous_backups_count', None)
        val_failed_continuous_backups_count = val

        val = dictionary.get('failed_objects_count', None)
        val_failed_objects_count = val

        val = dictionary.get('failed_objects_size', None)
        val_failed_objects_size = val

        val = dictionary.get('filtered_in_count', None)
        val_filtered_in_count = val

        val = dictionary.get('filtered_in_size', None)
        val_filtered_in_size = val

        val = dictionary.get('filtered_out_count', None)
        val_filtered_out_count = val

        val = dictionary.get('filtered_out_size', None)
        val_filtered_out_size = val

        val = dictionary.get('missing_objects_count', None)
        val_missing_objects_count = val

        val = dictionary.get('missing_objects_size', None)
        val_missing_objects_size = val

        val = dictionary.get('ongoing_continuous_backups_count', None)
        val_ongoing_continuous_backups_count = val

        val = dictionary.get('successful_continuous_backups_count', None)
        val_successful_continuous_backups_count = val

        val = dictionary.get('successful_objects_count', None)
        val_successful_objects_count = val

        val = dictionary.get('successful_objects_size', None)
        val_successful_objects_size = val

        val = dictionary.get('total_continuous_backups_count', None)
        val_total_continuous_backups_count = val

        # Return an object of this model
        return cls(
            val_backup_end_time,
            val_backup_start_time,
            val_deleted_objects_count,
            val_deleted_objects_size,
            val_failed_continuous_backups_count,
            val_failed_objects_count,
            val_failed_objects_size,
            val_filtered_in_count,
            val_filtered_in_size,
            val_filtered_out_count,
            val_filtered_out_size,
            val_missing_objects_count,
            val_missing_objects_size,
            val_ongoing_continuous_backups_count,
            val_successful_continuous_backups_count,
            val_successful_objects_count,
            val_successful_objects_size,
            val_total_continuous_backups_count,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
