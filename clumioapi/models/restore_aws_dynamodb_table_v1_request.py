#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamo_db_table_restore_source
from clumioapi.models import dynamo_db_table_restore_target

T = TypeVar('T', bound='RestoreAwsDynamodbTableV1Request')


class RestoreAwsDynamodbTableV1Request:
    """Implementation of the 'RestoreAwsDynamodbTableV1Request' model.

    Attributes:
        source:
            The DynamoDB table restore backup or point-in-time restore options. Only one of
            these fields should be set.
        target:
            The configuration of the restored DynamoDB table.
            For restore from snapshot, use the DynamoDB table configurations present at time
            of snapshot obtained from
            [GET /backups/aws/dynamodb-tables/{backup_id}](#operation/read-backup-aws-
            dynamodb-table) and for restoring point-in-time,
            use the current configuration of the table from [GET /datasources/aws/dynamodb-
            tables/{table_id}](#operation/read-aws-dynamodb-table).
            The table properties are set to empty or to their default values if they are
            specified as `null`.
    """

    # Create a mapping from Model property names to API property names
    _names = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: dynamo_db_table_restore_source.DynamoDBTableRestoreSource = None,
        target: dynamo_db_table_restore_target.DynamoDBTableRestoreTarget = None,
    ) -> None:
        """Constructor for the RestoreAwsDynamodbTableV1Request class."""

        # Initialize members of the class
        self.source: dynamo_db_table_restore_source.DynamoDBTableRestoreSource = source
        self.target: dynamo_db_table_restore_target.DynamoDBTableRestoreTarget = target

    @classmethod
    def from_dictionary(cls: Type, dictionary: Mapping[str, Any]) -> Optional[T]:
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
        key = 'source'
        source = (
            dynamo_db_table_restore_source.DynamoDBTableRestoreSource.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'target'
        target = (
            dynamo_db_table_restore_target.DynamoDBTableRestoreTarget.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(source, target)
