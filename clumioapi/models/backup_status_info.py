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
    _names = {
        'backup_status': 'backup_status',
        'last_failed_policy_start_timestamp': 'last_failed_policy_start_timestamp',
        'last_successful_policy_start_timestamp': 'last_successful_policy_start_timestamp',
        'operation_info_list': 'operation_info_list',
    }

    def __init__(
        self,
        backup_status: str = None,
        last_failed_policy_start_timestamp: str = None,
        last_successful_policy_start_timestamp: str = None,
        operation_info_list: Sequence[operation_info_.OperationInfo] = None,
    ) -> None:
        """Constructor for the BackupStatusInfo class."""

        # Initialize members of the class
        self.backup_status: str = backup_status
        self.last_failed_policy_start_timestamp: str = last_failed_policy_start_timestamp
        self.last_successful_policy_start_timestamp: str = last_successful_policy_start_timestamp
        self.operation_info_list: Sequence[operation_info_.OperationInfo] = operation_info_list

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
        val_backup_status = dictionary.get('backup_status')
        val_last_failed_policy_start_timestamp = dictionary.get(
            'last_failed_policy_start_timestamp'
        )
        val_last_successful_policy_start_timestamp = dictionary.get(
            'last_successful_policy_start_timestamp'
        )

        val_operation_info_list = None
        if dictionary.get('operation_info_list'):
            val_operation_info_list = list()
            for value in dictionary.get('operation_info_list'):
                val_operation_info_list.append(operation_info_.OperationInfo.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_backup_status,
            val_last_failed_policy_start_timestamp,
            val_last_successful_policy_start_timestamp,
            val_operation_info_list,
        )
