#
# Copyright 2023. Clumio, Inc.
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
            The possible values include "activity" and "compliance".
    """

    # Create a mapping from Model property names to API property names
    _names = {
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
        download_link: str = None,
        end_timestamp: str = None,
        expiration_timestamp: str = None,
        file_name: str = None,
        filters: str = None,
        p_id: str = None,
        start_timestamp: str = None,
        task_id: str = None,
        p_type: str = None,
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
        download_link = dictionary.get('download_link')
        end_timestamp = dictionary.get('end_timestamp')
        expiration_timestamp = dictionary.get('expiration_timestamp')
        file_name = dictionary.get('file_name')
        filters = dictionary.get('filters')
        p_id = dictionary.get('id')
        start_timestamp = dictionary.get('start_timestamp')
        task_id = dictionary.get('task_id')
        p_type = dictionary.get('type')
        # Return an object of this model
        return cls(
            download_link,
            end_timestamp,
            expiration_timestamp,
            file_name,
            filters,
            p_id,
            start_timestamp,
            task_id,
            p_type,
        )
