#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import operation_info as operation_info_
import requests

T = TypeVar('T', bound='BackupStatusInfo')


@dataclasses.dataclass
class BackupStatusInfo:
    """Implementation of the 'BackupStatusInfo' model.

    The backup status information applied to this resource.

    Attributes:
        BackupStatus:
            Backupstatus is the status of the backup. possible values are
            `success`, `partial_success`, `failure`, `no_backup`, and `unknown`. this value
            depends on `lookback_days`. if not specified, then this field has a value of
            `unknown`.

        LastFailedPolicyStartTimestamp:
            The last failed policy start time. represented in rfc-3339 format.

        LastSuccessfulPolicyStartTimestamp:
            The last successful policy start time. represented in rfc-3339 format.

        OperationInfoList:
            The policy operation information of the backups.

    """

    BackupStatus: str | None = None
    LastFailedPolicyStartTimestamp: str | None = None
    LastSuccessfulPolicyStartTimestamp: str | None = None
    OperationInfoList: Sequence[operation_info_.OperationInfo] | None = None

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
        val = dictionary.get('backup_status', None)
        val_backup_status = val

        val = dictionary.get('last_failed_policy_start_timestamp', None)
        val_last_failed_policy_start_timestamp = val

        val = dictionary.get('last_successful_policy_start_timestamp', None)
        val_last_successful_policy_start_timestamp = val

        val = dictionary.get('operation_info_list', None)

        val_operation_info_list = []
        if val:
            for value in val:
                val_operation_info_list.append(operation_info_.OperationInfo.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_backup_status,
            val_last_failed_policy_start_timestamp,
            val_last_successful_policy_start_timestamp,
            val_operation_info_list,
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
