#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import operation_info as operation_info_

T = TypeVar('T', bound='BackupStatusInfo')


class BackupStatusInfo:
    """Implementation of the 'BackupStatusInfo' model.

    The backup status information applied to this resource.

    Attributes:
        backup_status:
            BackupStatus is the status of the backup. Possible values are
            `success`, `partial_success`, `failure`, `no_backup`, and `unknown`. This value
            depends on `lookback_days`. If not specified, then this field has a value of
            `unknown`.
        last_failed_policy_start_timestamp:
            The last failed policy start time. Represented in RFC-3339 format.
        last_successful_policy_start_timestamp:
            The last successful policy start time. Represented in RFC-3339 format.
        operation_info_list:
            The policy operation information of the backups.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'backup_status': 'backup_status',
        'last_failed_policy_start_timestamp': 'last_failed_policy_start_timestamp',
        'last_successful_policy_start_timestamp': 'last_successful_policy_start_timestamp',
        'operation_info_list': 'operation_info_list',
    }

    def __init__(
        self,
        backup_status: str | None = None,
        last_failed_policy_start_timestamp: str | None = None,
        last_successful_policy_start_timestamp: str | None = None,
        operation_info_list: Sequence[operation_info_.OperationInfo] | None = None,
    ) -> None:
        """Constructor for the BackupStatusInfo class."""

        # Initialize members of the class
        self.backup_status: str | None = backup_status
        self.last_failed_policy_start_timestamp: str | None = last_failed_policy_start_timestamp
        self.last_successful_policy_start_timestamp: str | None = (
            last_successful_policy_start_timestamp
        )
        self.operation_info_list: Sequence[operation_info_.OperationInfo] | None = (
            operation_info_list
        )

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
        val = dictionary.get('backup_status', None)
        val_backup_status = val

        val = dictionary.get('last_failed_policy_start_timestamp', None)
        val_last_failed_policy_start_timestamp = val

        val = dictionary.get('last_successful_policy_start_timestamp', None)
        val_last_successful_policy_start_timestamp = val

        val = dictionary.get('operation_info_list', None)

        val_operation_info_list = None
        if val:
            val_operation_info_list = list()
            for value in val:
                val_operation_info_list.append(operation_info_.OperationInfo.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_backup_status,
            val_last_failed_policy_start_timestamp,
            val_last_successful_policy_start_timestamp,
            val_operation_info_list,
        )
