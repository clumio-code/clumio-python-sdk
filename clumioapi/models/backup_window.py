#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='BackupWindow')


class BackupWindow:
    """Implementation of the 'BackupWindow' model.

    The start and end times of the customized backup window. Use of `backup_window`
    is deprecated, use `backup_window_tz` instead.

    Attributes:
        end_time:
            The time when the backup window closes. Specify the end time in the format
            `hh:mm`, where `hh` represents the hour of the day and `mm` represents the
            minute of the day, based on a 24 hour clock. Leave empty if you do not want to
            specify an end time. If the backup window closes while a backup is in progress,
            the entire backup process is aborted. Clumio will perform the next backup when
            the backup window re-opens.
        start_time:
            The time when the backup window opens. Specify the start time in the format
            `hh:mm`, where `hh` represents the hour of the day and `mm` represents the
            minute of the day based on the 24 hour clock.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'end_time': 'end_time', 'start_time': 'start_time'}

    def __init__(self, end_time: str, start_time: str) -> None:
        """Constructor for the BackupWindow class."""

        # Initialize members of the class
        self.end_time: str = end_time
        self.start_time: str = start_time

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
        val = dictionary['end_time']
        val_end_time = val

        val = dictionary['start_time']
        val_start_time = val

        # Return an object of this model
        return cls(
            val_end_time,  # type: ignore
            val_start_time,  # type: ignore
        )
