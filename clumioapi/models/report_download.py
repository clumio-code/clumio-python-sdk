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
        download_link: str,
        end_timestamp: str,
        expiration_timestamp: str,
        file_name: str,
        filters: str,
        p_id: str,
        start_timestamp: str,
        task_id: str,
        p_type: str,
    ) -> None:
        """Constructor for the ReportDownload class."""

        # Initialize members of the class
        self.download_link: str = download_link
        self.end_timestamp: str = end_timestamp
        self.expiration_timestamp: str = expiration_timestamp
        self.file_name: str = file_name
        self.filters: str = filters
        self.p_id: str = p_id
        self.start_timestamp: str = start_timestamp
        self.task_id: str = task_id
        self.p_type: str = p_type

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
        val = dictionary['download_link']
        val_download_link = val

        val = dictionary['end_timestamp']
        val_end_timestamp = val

        val = dictionary['expiration_timestamp']
        val_expiration_timestamp = val

        val = dictionary['file_name']
        val_file_name = val

        val = dictionary['filters']
        val_filters = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['start_timestamp']
        val_start_timestamp = val

        val = dictionary['task_id']
        val_task_id = val

        val = dictionary['type']
        val_p_type = val

        # Return an object of this model
        return cls(
            val_download_link,  # type: ignore
            val_end_timestamp,  # type: ignore
            val_expiration_timestamp,  # type: ignore
            val_file_name,  # type: ignore
            val_filters,  # type: ignore
            val_p_id,  # type: ignore
            val_start_timestamp,  # type: ignore
            val_task_id,  # type: ignore
            val_p_type,  # type: ignore
        )
