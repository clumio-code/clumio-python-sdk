#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamo_db_table_restore_source as dynamo_db_table_restore_source_
from clumioapi.models import dynamo_db_table_restore_target as dynamo_db_table_restore_target_

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
    _names: dict[str, str] = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: dynamo_db_table_restore_source_.DynamoDBTableRestoreSource,
        target: dynamo_db_table_restore_target_.DynamoDBTableRestoreTarget,
    ) -> None:
        """Constructor for the RestoreAwsDynamodbTableV1Request class."""

        # Initialize members of the class
        self.source: dynamo_db_table_restore_source_.DynamoDBTableRestoreSource = source
        self.target: dynamo_db_table_restore_target_.DynamoDBTableRestoreTarget = target

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
        val = dictionary['source']
        val_source = dynamo_db_table_restore_source_.DynamoDBTableRestoreSource.from_dictionary(val)

        val = dictionary['target']
        val_target = dynamo_db_table_restore_target_.DynamoDBTableRestoreTarget.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_source,  # type: ignore
            val_target,  # type: ignore
        )
