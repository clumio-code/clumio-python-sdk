#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='EC2MSSQLPITROptions')


@dataclasses.dataclass
class EC2MSSQLPITROptions:
    """Implementation of the 'EC2MSSQLPITROptions' model.

        A database backup at a specific point-in-time to be restored.

        Attributes:
            DatabaseId:
                The clumio-assigned id of the mssql database to be restored.
    use the [get /datasources/aws/ec2-mssql/databases](#operation/list-ec2-mssql-databases)
    endpoint to fetch valid values.

            RestoreToLatest:
                If enabled, performs pitr till the latest possible time.
    either timestamp or restore_to_latest must be provided, but not both.

            Timestamp:
                The point in time to be restored in rfc-3339 format.
    either timestamp or restore_to_latest must be provided, but not both.

    """

    DatabaseId: str | None = None
    RestoreToLatest: bool | None = None
    Timestamp: str | None = None

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
        val = dictionary.get('database_id', None)
        val_database_id = val

        val = dictionary.get('restore_to_latest', None)
        val_restore_to_latest = val

        val = dictionary.get('timestamp', None)
        val_timestamp = val

        # Return an object of this model
        return cls(
            val_database_id,
            val_restore_to_latest,
            val_timestamp,
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
