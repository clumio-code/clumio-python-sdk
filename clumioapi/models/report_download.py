#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ReportDownload')


class ReportDownload:
    """Implementation of the 'ReportDownload' model.

    Attributes:
        download_link:
            The link to the actual CSV report.
        end_timestamp:
            The time when the request was completed.
        expiration_timestamp:
            The time when this report CSV will expire and not be available for download.
        file_name:
            The name of CSV file.
        filters:
            The filters applied to the report when download was initiated.
        p_id:
            The id of the report that uniquely identifies the report.
        start_timestamp:
            The time when the request was made.
        task_id:
            The Clumio-assigned ID of the task which generated the restored file.
        p_type:
            The type of report this CSV Download is associated with.
            The possible values: ["activity"].
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'download_link': 'download_link',
        'end_timestamp': 'end_timestamp',
        'expiration_timestamp': 'expiration_timestamp',
        'file_name': 'file_name',
        'filters': 'filters',
        'p_id': 'id',
        'start_timestamp': 'start_timestamp',
        'task_id': 'task_id',
        'p_type': 'type',
    }

    def __init__(
        self,
        download_link: str | None = None,
        end_timestamp: str | None = None,
        expiration_timestamp: str | None = None,
        file_name: str | None = None,
        filters: str | None = None,
        p_id: str | None = None,
        start_timestamp: str | None = None,
        task_id: str | None = None,
        p_type: str | None = None,
    ) -> None:
        """Constructor for the ReportDownload class."""

        # Initialize members of the class
        self.download_link: str | None = download_link
        self.end_timestamp: str | None = end_timestamp
        self.expiration_timestamp: str | None = expiration_timestamp
        self.file_name: str | None = file_name
        self.filters: str | None = filters
        self.p_id: str | None = p_id
        self.start_timestamp: str | None = start_timestamp
        self.task_id: str | None = task_id
        self.p_type: str | None = p_type

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
        val_p_id = val

        val = dictionary.get('start_timestamp', None)
        val_start_timestamp = val

        val = dictionary.get('task_id', None)
        val_task_id = val

        val = dictionary.get('type', None)
        val_p_type = val

        # Return an object of this model
        return cls(
            val_download_link,
            val_end_timestamp,
            val_expiration_timestamp,
            val_file_name,
            val_filters,
            val_p_id,
            val_start_timestamp,
            val_task_id,
            val_p_type,
        )
