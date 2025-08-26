#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import dynamo_db_table_restore_source as dynamo_db_table_restore_source_
from clumioapi.models import dynamo_db_table_restore_target as dynamo_db_table_restore_target_
import requests

T = TypeVar('T', bound='RestoreAwsDynamodbTableV1Request')


@dataclasses.dataclass
class RestoreAwsDynamodbTableV1Request:
    """Implementation of the 'RestoreAwsDynamodbTableV1Request' model.

        Attributes:
            Source:
                The dynamodb table restore backup or point-in-time restore options. only one of these fields should be set.

            Target:
                The configuration of the restored dynamodb table.
    for restore from snapshot, use the dynamodb table configurations present at time of snapshot obtained from
    [get /backups/aws/dynamodb-tables/{backup_id}](#operation/read-backup-aws-dynamodb-table) and for restoring point-in-time,
    use the current configuration of the table from [get /datasources/aws/dynamodb-tables/{table_id}](#operation/read-aws-dynamodb-table).
    the table properties are set to empty or to their default values if they are specified as `null`.

    """

    Source: dynamo_db_table_restore_source_.DynamoDBTableRestoreSource | None = None
    Target: dynamo_db_table_restore_target_.DynamoDBTableRestoreTarget | None = None

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
        val = dictionary.get('source', None)
        val_source = dynamo_db_table_restore_source_.DynamoDBTableRestoreSource.from_dictionary(val)

        val = dictionary.get('target', None)
        val_target = dynamo_db_table_restore_target_.DynamoDBTableRestoreTarget.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_source,
            val_target,
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
