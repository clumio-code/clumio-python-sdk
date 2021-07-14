#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='CreateReportDownloadResponse')


class CreateReportDownloadResponse:
    """Implementation of the 'CreateReportDownloadResponse' model.

    Attributes:
        task_id:
            The Clumio-assigned ID of the task created by the request.
            The progress of the task can be monitored using the
            [`GET /tasks/{task_id}`](#operation/list-tasks) endpoint.
    """

    # Create a mapping from Model property names to API property names
    _names = {'task_id': 'task_id'}

    def __init__(self, task_id: str = None) -> None:
        """Constructor for the CreateReportDownloadResponse class."""

        # Initialize members of the class
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
        task_id = dictionary.get('task_id')
        # Return an object of this model
        return cls(task_id)
