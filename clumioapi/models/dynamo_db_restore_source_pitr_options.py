#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='DynamoDBRestoreSourcePitrOptions')


class DynamoDBRestoreSourcePitrOptions:
    """Implementation of the 'DynamoDBRestoreSourcePitrOptions' model.

    The parameters for initiating a DynamoDB table point-in-time restore.Only one of
    `timestamp` or `use_latest_restorable_time` should be set.

    Attributes:
        table_id:
            The Clumio-assigned ID of the DynamoDB table to be restored.
            Use the [GET /datasources/aws/dynamodb-tables](#operation/list-aws-dynamodb-
            tables)
            endpoint to fetch valid values.
        timestamp:
            A point in time to be restored in RFC-3339 format.
        p_type:
            The type of the backup. Possible values - `clumio_pitr`, `aws_pitr`. The
            type will be assumed as `aws_pitr` if the field is left empty.
        use_latest_restorable_time:
            Restore the table to the latest possible time.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'table_id': 'table_id',
        'timestamp': 'timestamp',
        'p_type': 'type',
        'use_latest_restorable_time': 'use_latest_restorable_time',
    }

    def __init__(
        self,
        table_id: str | None = None,
        timestamp: str | None = None,
        p_type: str | None = None,
        use_latest_restorable_time: bool | None = None,
    ) -> None:
        """Constructor for the DynamoDBRestoreSourcePitrOptions class."""

        # Initialize members of the class
        self.table_id: str | None = table_id
        self.timestamp: str | None = timestamp
        self.p_type: str | None = p_type
        self.use_latest_restorable_time: bool | None = use_latest_restorable_time

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

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('table_id', None)
        val_table_id = val

        val = dictionary.get('timestamp', None)
        val_timestamp = val

        val = dictionary.get('type', None)
        val_p_type = val

        val = dictionary.get('use_latest_restorable_time', None)
        val_use_latest_restorable_time = val

        # Return an object of this model
        return cls(
            val_table_id,
            val_timestamp,
            val_p_type,
            val_use_latest_restorable_time,
        )
