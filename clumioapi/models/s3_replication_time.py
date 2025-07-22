#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_replication_time_value as s3_replication_time_value_

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
    _names: dict[str, str] = {'status': 'status', 'time': 'time'}

    def __init__(
        self, status: str, time: s3_replication_time_value_.S3ReplicationTimeValue
    ) -> None:
        """Constructor for the S3ReplicationTime class."""

        # Initialize members of the class
        self.status: str = status
        self.time: s3_replication_time_value_.S3ReplicationTimeValue = time

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
        val = dictionary['status']
        val_status = val

        val = dictionary['time']
        val_time = s3_replication_time_value_.S3ReplicationTimeValue.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_status,  # type: ignore
            val_time,  # type: ignore
        )
