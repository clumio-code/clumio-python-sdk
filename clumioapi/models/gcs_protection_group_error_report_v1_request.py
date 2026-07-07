#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
import requests

T = TypeVar('T', bound='GcsProtectionGroupErrorReportV1Request')


@dataclasses.dataclass
class GcsProtectionGroupErrorReportV1Request:
    """Implementation of the 'GcsProtectionGroupErrorReportV1Request' model.

    Attributes:
        BackupId:
            Id of the failed backup id for which the error report will be generated.

        ErrorReportBucketName:
            Name of the gcs bucket where the generated error report will be stored.

        ErrorReportPrefix:
            Object prefix under which the generated error report will be stored.

        ErrorReportProjectId:
            Id of the gcp project where the generated error report will be stored.

        TaskId:
            Id of the failed task for which the error report will be generated.

    """

    BackupId: str | None = None
    ErrorReportBucketName: str | None = None
    ErrorReportPrefix: str | None = None
    ErrorReportProjectId: str | None = None
    TaskId: int | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return api_helper.to_dictionary(self)

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
        val = dictionary.get('backup_id', None)
        val_backup_id = val

        val = dictionary.get('error_report_bucket_name', None)
        val_error_report_bucket_name = val

        val = dictionary.get('error_report_prefix', None)
        val_error_report_prefix = val

        val = dictionary.get('error_report_project_id', None)
        val_error_report_project_id = val

        val = dictionary.get('task_id', None)
        val_task_id = val

        # Return an object of this model
        return cls(
            val_backup_id,
            val_error_report_bucket_name,
            val_error_report_prefix,
            val_error_report_project_id,
            val_task_id,
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
