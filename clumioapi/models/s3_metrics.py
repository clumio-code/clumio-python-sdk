#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_replication_time_value

T = TypeVar('T', bound='S3Metrics')


class S3Metrics:
    """Implementation of the 'S3Metrics' model.

    A container specifying replication metrics-related settingsenabling replication
    metrics and events.

    Attributes:
        event_threshold:
            A container specifying the time value for S3 Replication Time
            Control (S3 RTC) and replication metrics EventThreshold.
        status:
            Specifies whether the replication metrics are enabled.
    """

    # Create a mapping from Model property names to API property names
    _names = {'event_threshold': 'event_threshold', 'status': 'status'}

    def __init__(
        self,
        event_threshold: s3_replication_time_value.S3ReplicationTimeValue = None,
        status: str = None,
    ) -> None:
        """Constructor for the S3Metrics class."""

        # Initialize members of the class
        self.event_threshold: s3_replication_time_value.S3ReplicationTimeValue = event_threshold
        self.status: str = status

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
        key = 'event_threshold'
        event_threshold = (
            s3_replication_time_value.S3ReplicationTimeValue.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        status = dictionary.get('status')
        # Return an object of this model
        return cls(event_threshold, status)
