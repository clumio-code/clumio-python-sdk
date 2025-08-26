#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import report_download_links as report_download_links_

T = TypeVar('T', bound='CreateReportDownloadResponse')


class CreateReportDownloadResponse:
    """Implementation of the 'CreateReportDownloadResponse' model.

    Attributes:
        links:
            _links provides URLs to the related resources of a report CSV download
        task_id:
            The Clumio-assigned ID of the task created by the request.
            The progress of the task can be monitored using the
            [`GET /tasks/{task_id}`](#operation/list-tasks) endpoint.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'links': '_links', 'task_id': 'task_id'}

    def __init__(
        self,
        links: report_download_links_.ReportDownloadLinks | None = None,
        task_id: str | None = None,
    ) -> None:
        """Constructor for the CreateReportDownloadResponse class."""

        # Initialize members of the class
        self.links: report_download_links_.ReportDownloadLinks | None = links
        self.task_id: str | None = task_id

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
        val = dictionary.get('_links', None)
        val_links = report_download_links_.ReportDownloadLinks.from_dictionary(val)

        val = dictionary.get('task_id', None)
        val_task_id = val

        # Return an object of this model
        return cls(
            val_links,
            val_task_id,
        )
