#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='ReportDownload')


@dataclasses.dataclass
class ReportDownload:
    """Implementation of the 'ReportDownload' model.

    Attributes:
        DownloadLink:
            The link to the actual csv report.

        EndTimestamp:
            The time when the request was completed.

        ExpirationTimestamp:
            The time when this report csv will expire and not be available for download.

        FileName:
            The name of csv file.

        Filters:
            The filters applied to the report when download was initiated.

        Id:
            The id of the report that uniquely identifies the report.

        StartTimestamp:
            The time when the request was made.

        TaskId:
            The clumio-assigned id of the task which generated the restored file.

        Type:
            ["activity"].

    """

    DownloadLink: str | None = None
    EndTimestamp: str | None = None
    ExpirationTimestamp: str | None = None
    FileName: str | None = None
    Filters: str | None = None
    Id: str | None = None
    StartTimestamp: str | None = None
    TaskId: str | None = None
    Type: str | None = None

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
        val = dictionary.get('download_link', None)
        val_download_link = val

        val = dictionary.get('end_timestamp', None)
        val_end_timestamp = val

        val = dictionary.get('expiration_timestamp', None)
        val_expiration_timestamp = val

        val = dictionary.get('file_name', None)
        val_file_name = val

        val = dictionary.get('filters', None)
        val_filters = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('start_timestamp', None)
        val_start_timestamp = val

        val = dictionary.get('task_id', None)
        val_task_id = val

        val = dictionary.get('type', None)
        val_type = val

        # Return an object of this model
        return cls(
            val_download_link,
            val_end_timestamp,
            val_expiration_timestamp,
            val_file_name,
            val_filters,
            val_id,
            val_start_timestamp,
            val_task_id,
            val_type,
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
