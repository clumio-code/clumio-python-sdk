#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import s3_replication_time_value as s3_replication_time_value_
import requests

T = TypeVar('T', bound='S3Metrics')


@dataclasses.dataclass
class S3Metrics:
    """Implementation of the 'S3Metrics' model.

    A container specifying replication metrics-related settingsenabling replication
    metrics and events.

    Attributes:
        EventThreshold:
            A container specifying the time value for s3 replication time
            control (s3 rtc) and replication metrics eventthreshold.

        Status:
            Specifies whether the replication metrics are enabled.

    """

    EventThreshold: s3_replication_time_value_.S3ReplicationTimeValue | None = None
    Status: str | None = None

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
        val = dictionary.get('event_threshold', None)
        val_event_threshold = s3_replication_time_value_.S3ReplicationTimeValue.from_dictionary(val)

        val = dictionary.get('status', None)
        val_status = val

        # Return an object of this model
        return cls(
            val_event_threshold,
            val_status,
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
