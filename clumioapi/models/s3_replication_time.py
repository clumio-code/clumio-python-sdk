#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import s3_replication_time_value as s3_replication_time_value_
import requests

T = TypeVar('T', bound='S3ReplicationTime')


@dataclasses.dataclass
class S3ReplicationTime:
    """Implementation of the 'S3ReplicationTime' model.

        A container specifying S3 Replication Time Control (S3 RTC)related information.

        Attributes:
            Status:
                Specifies whether the replication time is enabled.

            Time:
                A container specifying the time value for s3 replication time
    control (s3 rtc) and replication metrics eventthreshold.

    """

    Status: str | None = None
    Time: s3_replication_time_value_.S3ReplicationTimeValue | None = None

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
        val = dictionary.get('status', None)
        val_status = val

        val = dictionary.get('time', None)
        val_time = s3_replication_time_value_.S3ReplicationTimeValue.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_status,
            val_time,
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
