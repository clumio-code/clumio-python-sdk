#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_replication_time_value

T = TypeVar('T', bound='S3ReplicationTime')


class S3ReplicationTime:
    """Implementation of the 'S3ReplicationTime' model.

    A container specifying S3 Replication Time Control (S3 RTC)related information.

    Attributes:
        status:
            Specifies whether the replication time is enabled.
        time:
            A container specifying the time value for S3 Replication Time
            Control (S3 RTC) and replication metrics EventThreshold.
    """

    # Create a mapping from Model property names to API property names
    _names = {'status': 'status', 'time': 'time'}

    def __init__(
        self, status: str = None, time: s3_replication_time_value.S3ReplicationTimeValue = None
    ) -> None:
        """Constructor for the S3ReplicationTime class."""

        # Initialize members of the class
        self.status: str = status
        self.time: s3_replication_time_value.S3ReplicationTimeValue = time

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
        status = dictionary.get('status')
        key = 'time'
        time = (
            s3_replication_time_value.S3ReplicationTimeValue.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(status, time)
