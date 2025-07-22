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
        self, table_id: str, timestamp: str, p_type: str, use_latest_restorable_time: bool
    ) -> None:
        """Constructor for the DynamoDBRestoreSourcePitrOptions class."""

        # Initialize members of the class
        self.table_id: str = table_id
        self.timestamp: str = timestamp
        self.p_type: str = p_type
        self.use_latest_restorable_time: bool = use_latest_restorable_time

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

        # Extract variables from the dictionary
        val = dictionary['table_id']
        val_table_id = val

        val = dictionary['timestamp']
        val_timestamp = val

        val = dictionary['type']
        val_p_type = val

        val = dictionary['use_latest_restorable_time']
        val_use_latest_restorable_time = val

        # Return an object of this model
        return cls(
            val_table_id,  # type: ignore
            val_timestamp,  # type: ignore
            val_p_type,  # type: ignore
            val_use_latest_restorable_time,  # type: ignore
        )
