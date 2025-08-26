#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='ProtectionGroupRestoreSourcePitrOptions')


@dataclasses.dataclass
class ProtectionGroupRestoreSourcePitrOptions:
    """Implementation of the 'ProtectionGroupRestoreSourcePitrOptions' model.

        The parameters for initiating a point in time restore.<br>Note that only one of
        `backup_id` or `pitr` must be given.

        Attributes:
            ProtectionGroupId:
                Clumio-assigned id of protection group, representing the
    protection group to restore from. use the
    [get /datasources/protection-groups](#operation/list-protection-group)
    endpoint to fetch valid values.

            RestoreEndTimestamp:
                The end timestamp to be restored in rfc-3339 format.
    clumio restores last objects modified before the given time.
    if `restore_end_timestamp` is given without `restore_start_timestamp`,
    it is the same as point in time restore.

            RestoreStartTimestamp:
                The start timestamp to be restored in rfc-3339 format.
    clumio restores objects modified since the given time.

    """

    ProtectionGroupId: str | None = None
    RestoreEndTimestamp: str | None = None
    RestoreStartTimestamp: str | None = None

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
        val = dictionary.get('protection_group_id', None)
        val_protection_group_id = val

        val = dictionary.get('restore_end_timestamp', None)
        val_restore_end_timestamp = val

        val = dictionary.get('restore_start_timestamp', None)
        val_restore_start_timestamp = val

        # Return an object of this model
        return cls(
            val_protection_group_id,
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
