#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='BackupWindow')


@dataclasses.dataclass
class BackupWindow:
    """Implementation of the 'BackupWindow' model.

    The start and end times of the customized backup window. Use of `backup_window`
    is deprecated, use `backup_window_tz` instead.

    Attributes:
        EndTime:
            The time when the backup window closes. specify the end time in the format `hh:mm`, where `hh` represents the hour of the day and `mm` represents the minute of the day, based on a 24 hour clock. leave empty if you do not want to specify an end time. if the backup window closes while a backup is in progress, the entire backup process is aborted. clumio will perform the next backup when the backup window re-opens.

        StartTime:
            The time when the backup window opens. specify the start time in the format `hh:mm`, where `hh` represents the hour of the day and `mm` represents the minute of the day based on the 24 hour clock.

    """

    EndTime: str | None = None
    StartTime: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
        val = dictionary.get('end_time', None)
        val_end_time = val

        val = dictionary.get('start_time', None)
        val_start_time = val

        # Return an object of this model
        return cls(
            val_end_time,
            val_start_time,
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
