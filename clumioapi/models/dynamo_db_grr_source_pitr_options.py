#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
import requests

T = TypeVar('T', bound='DynamoDBGrrSourcePitrOptions')


@dataclasses.dataclass
class DynamoDBGrrSourcePitrOptions:
    """Implementation of the 'DynamoDBGrrSourcePitrOptions' model.

    DynamoDBGrrSourcePitrOptions represents the parameters required to initiate a
    point-in-time restore (PITR)operation for a DynamoDB table. This struct is used
    to specify the target table and the specific point in timeto which the table
    should be restored. Only one of `timestamp` or `use_latest_restorable_time`
    should be setto indicate the desired restore time.

    Attributes:
        TableId:
            The clumio-assigned id of the dynamodb table to be restored.
            use the [get /datasources/aws/dynamodb-tables](#operation/list-aws-dynamodb-
            tables)
            endpoint to fetch valid values.

        Timestamp:
            A point in time to be restored in rfc-3339 format.

        UseLatestRestorableTime:
            Restore the table to the latest possible time.

    """

    TableId: str | None = None
    Timestamp: str | None = None
    UseLatestRestorableTime: bool | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return api_helper.to_dictionary(self)

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
        val = dictionary.get('table_id', None)
        val_table_id = val

        val = dictionary.get('timestamp', None)
        val_timestamp = val

        val = dictionary.get('use_latest_restorable_time', None)
        val_use_latest_restorable_time = val

        # Return an object of this model
        return cls(
            val_table_id,
            val_timestamp,
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
