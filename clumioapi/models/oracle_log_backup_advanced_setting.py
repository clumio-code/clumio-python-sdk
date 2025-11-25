#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='OracleLogBackupAdvancedSetting')


@dataclasses.dataclass
class OracleLogBackupAdvancedSetting:
    """Implementation of the 'OracleLogBackupAdvancedSetting' model.

    Additional policy configuration settings for the `oracle_log_backup` operation.
    If this operation is not of type `oracle_log_backup`, then this field is omitted
    from the response.

    Attributes:
        AlternativeReplica:
            `primary`, `standby`, and `stop`.
            if `"stop"` is provided, then backups will not attempt to switch to a different
            replica when the preferred replica is unavailable.

        PreferredReplica:
            `primary`, and `standby`.
            recurring backup will first attempt to use either the primary replica or the
            secondary replica accordingly.

    """

    AlternativeReplica: str | None = None
    PreferredReplica: str | None = None

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
        val = dictionary.get('alternative_replica', None)
        val_alternative_replica = val

        val = dictionary.get('preferred_replica', None)
        val_preferred_replica = val

        # Return an object of this model
        return cls(
            val_alternative_replica,
            val_preferred_replica,
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
