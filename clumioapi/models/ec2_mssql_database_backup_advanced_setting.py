#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='EC2MSSQLDatabaseBackupAdvancedSetting')


@dataclasses.dataclass
class EC2MSSQLDatabaseBackupAdvancedSetting:
    """Implementation of the 'EC2MSSQLDatabaseBackupAdvancedSetting' model.

    Additional policy configuration settings for the `ec2_mssql_database_backup`
    operation. If this operation is not of type `ec2_mssql_database_backup`, then
    this field is omitted from the response.

    Attributes:
        AlternativeReplica:
            The alternative replica for mssql database backups. this setting only applies to availability group databases. possible values include `"primary"`, `"sync_secondary"`, and `"stop"`. if `"stop"` is provided, then backups will not attempt to switch to a different replica when the preferred replica is unavailable. otherwise, recurring backups will attempt to use either the primary replica or the secondary replica accordingly.

        PreferredReplica:
            The primary preferred replica for mssql database backups. this setting only applies to availability group databases. possible values include `"primary"` and `"sync_secondary"`. recurring backup will first attempt to use either the primary replica or the secondary replica accordingly.

    """

    AlternativeReplica: str | None = None
    PreferredReplica: str | None = None

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
