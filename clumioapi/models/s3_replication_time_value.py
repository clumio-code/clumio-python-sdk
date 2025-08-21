#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3ReplicationTimeValue')


class S3ReplicationTimeValue:
    """Implementation of the 'S3ReplicationTimeValue' model.

    A container specifying the time value for S3 Replication TimeControl (S3 RTC)
    and replication metrics EventThreshold.

    Attributes:
        minutes:
            Contains an integer specifying time in minutes.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'minutes': 'minutes'}

    def __init__(self, minutes: int | None = None) -> None:
        """Constructor for the S3ReplicationTimeValue class."""

        # Initialize members of the class
        self.minutes: int | None = minutes

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
        val = dictionary.get('minutes', None)
        val_minutes = val

        # Return an object of this model
        return cls(
            val_minutes,
        )
