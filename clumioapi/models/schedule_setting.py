#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='ScheduleSetting')


@dataclasses.dataclass
class ScheduleSetting:
    """Implementation of the 'ScheduleSetting' model.

    When the report will be generated and sent. If the schedule is not provided then
    adefault value will be used.

    Attributes:
        DayOfMonth:
            The day of the month when the report will be sent out. this is required for the
            'monthly'
            report frequency. it has to be >= 1 and <= 28, or '-1', which signifies end of
            month.
            if the day_of_month is set to -1 then the report will be sent out at the end of
            every month.

        DayOfWeek:
            Which day the report will be sent out. this is required for 'weekly' report
            frequency.

        Frequency:
            The unit of frequency in which the report is generated.

        StartTime:
            When the report will be send out. this field should follow the format "hh:mm"
            based
            on a 24-hour clock. only values where hh ranges from 0 to 23 and mm ranges from
            0 to
            59 are allowed.

        Timezone:
            The timezone for the report schedule. the timezone must be a valid location name
            from
            the iana time zone database. for instance, it can be "america/new_york",
            "us/central",
            "utc", or similar. if empty, then the timezone is considered as utc.

    """

    DayOfMonth: int | None = None
    DayOfWeek: str | None = None
    Frequency: str | None = None
    StartTime: str | None = None
    Timezone: str | None = None

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
        val = dictionary.get('day_of_month', None)
        val_day_of_month = val

        val = dictionary.get('day_of_week', None)
        val_day_of_week = val

        val = dictionary.get('frequency', None)
        val_frequency = val

        val = dictionary.get('start_time', None)
        val_start_time = val

        val = dictionary.get('timezone', None)
        val_timezone = val

        # Return an object of this model
        return cls(
            val_day_of_month,
            val_day_of_week,
            val_frequency,
            val_start_time,
            val_timezone,
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
