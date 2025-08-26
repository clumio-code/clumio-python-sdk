#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='DynamoDBRestoreSourcePitrOptions')


@dataclasses.dataclass
class DynamoDBRestoreSourcePitrOptions:
    """Implementation of the 'DynamoDBRestoreSourcePitrOptions' model.

        The parameters for initiating a DynamoDB table point-in-time restore.Only one of
        `timestamp` or `use_latest_restorable_time` should be set.

        Attributes:
            TableId:
                The clumio-assigned id of the dynamodb table to be restored.
    use the [get /datasources/aws/dynamodb-tables](#operation/list-aws-dynamodb-tables)
    endpoint to fetch valid values.

            Timestamp:
                A point in time to be restored in rfc-3339 format.

            Type:
                The type of the backup. possible values - `clumio_pitr`, `aws_pitr`. the
    type will be assumed as `aws_pitr` if the field is left empty.

            UseLatestRestorableTime:
                Restore the table to the latest possible time.

    """

    TableId: str | None = None
    Timestamp: str | None = None
    Type: str | None = None
    UseLatestRestorableTime: bool | None = None

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
        val = dictionary.get('table_id', None)
        val_table_id = val

        val = dictionary.get('timestamp', None)
        val_timestamp = val

        val = dictionary.get('type', None)
        val_type = val

        val = dictionary.get('use_latest_restorable_time', None)
        val_use_latest_restorable_time = val

        # Return an object of this model
        return cls(
            val_table_id,
            val_timestamp,
            val_type,
            val_use_latest_restorable_time,
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
