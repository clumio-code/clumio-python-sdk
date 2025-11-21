#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='S3InstantAccessSourcePitrOptions')


@dataclasses.dataclass
class S3InstantAccessSourcePitrOptions:
    """Implementation of the 'S3InstantAccessSourcePitrOptions' model.

    The parameters to initiate a point-in-time creation of S3 instant access
    endpoint.<br>Note that only one of either `backup_id` or `pitr` must be
    provided.

    Attributes:
        RestoreEndTimestamp:
            The end time of the period in which the objects must be restored in rfc-3339
            format.
            objects modified before this given time will be restored.
            if `restore_end_timestamp` is provided without `restore_start_timestamp`, then
            it is the same
            as a point-in-time restore.

        RestoreStartTimestamp:
            The start time of the period in which the objects must be restored in rfc-3339
            format.
            objects modified since the given time will be restored.

    """

    RestoreEndTimestamp: str | None = None
    RestoreStartTimestamp: str | None = None

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
        val = dictionary.get('restore_end_timestamp', None)
        val_restore_end_timestamp = val

        val = dictionary.get('restore_start_timestamp', None)
        val_restore_start_timestamp = val

        # Return an object of this model
        return cls(
            val_restore_end_timestamp,
            val_restore_start_timestamp,
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
