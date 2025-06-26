#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ScheduleSetting')


class ScheduleSetting:
    """Implementation of the 'ScheduleSetting' model.

    When the report will be generated and sent. If the schedule is not provided then
    adefault value will be used.

    Attributes:
        day_of_month:
            The day of the month when the report will be sent out. This is required for the
            'monthly'
            report frequency. It has to be >= 1 and <= 28, or '-1', which signifies end of
            month.
            If the day_of_month is set to -1 then the report will be sent out at the end of
            every month.
        day_of_week:
            Which day the report will be sent out. This is required for 'weekly' report
            frequency.
        frequency:
            The unit of frequency in which the report is generated.
        start_time:
            When the report will be send out. This field should follow the format "HH:MM"
            based
            on a 24-hour clock. Only values where HH ranges from 0 to 23 and MM ranges from
            0 to
            59 are allowed.
        timezone:
            The timezone for the report schedule. The timezone must be a valid location name
            from
            the IANA Time Zone database. For instance, it can be "America/New_York",
            "US/Central",
            "UTC", or similar. If empty, then the timezone is considered as UTC.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'day_of_month': 'day_of_month',
        'day_of_week': 'day_of_week',
        'frequency': 'frequency',
        'start_time': 'start_time',
        'timezone': 'timezone',
    }

    def __init__(
        self,
        day_of_month: int = None,
        day_of_week: str = None,
        frequency: str = None,
        start_time: str = None,
        timezone: str = None,
    ) -> None:
        """Constructor for the ScheduleSetting class."""

        # Initialize members of the class
        self.day_of_month: int = day_of_month
        self.day_of_week: str = day_of_week
        self.frequency: str = frequency
        self.start_time: str = start_time
        self.timezone: str = timezone

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
        day_of_month = dictionary.get('day_of_month')
        day_of_week = dictionary.get('day_of_week')
        frequency = dictionary.get('frequency')
        start_time = dictionary.get('start_time')
        timezone = dictionary.get('timezone')
        # Return an object of this model
        return cls(day_of_month, day_of_week, frequency, start_time, timezone)
