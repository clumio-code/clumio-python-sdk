#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import report_download_links

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
    _names = {'links': '_links', 'task_id': 'task_id'}

    def __init__(
        self, links: report_download_links.ReportDownloadLinks = None, task_id: str = None
    ) -> None:
        """Constructor for the CreateReportDownloadResponse class."""

        # Initialize members of the class
        self.links: report_download_links.ReportDownloadLinks = links
        self.task_id: str = task_id

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
        key = '_links'
        links = (
            report_download_links.ReportDownloadLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        task_id = dictionary.get('task_id')
        # Return an object of this model
        return cls(links, task_id)
