#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import dynamo_db_grr_source_pitr_options as dynamo_db_grr_source_pitr_options_
import requests

T = TypeVar('T', bound='DynamoDBGrrSource')


@dataclasses.dataclass
class DynamoDBGrrSource:
    """Implementation of the 'DynamoDBGrrSource' model.

    The parameters for initiating a DynamoDB table backup query from a backup.

    Attributes:
        BackupId:
            Performs the operation on a dynamodb table within the specified backup.
            use the [get /backups/aws/dynamodb-tables](#operation/list-backup-aws-dynamodb-
            tables)
            endpoint to fetch valid values.

        ContinuousBackup:
            Dynamodbgrrsourcepitroptions represents the parameters required to initiate a
            point-in-time restore (pitr)
            operation for a dynamodb table. this struct is used to specify the target table
            and the specific point in time
            to which the table should be restored. only one of `timestamp` or
            `use_latest_restorable_time` should be set
            to indicate the desired restore time.

    """

    BackupId: str | None = None
    ContinuousBackup: dynamo_db_grr_source_pitr_options_.DynamoDBGrrSourcePitrOptions | None = None

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
        val = dictionary.get('backup_id', None)
        val_backup_id = val

        val = dictionary.get('continuous_backup', None)
        val_continuous_backup = (
            dynamo_db_grr_source_pitr_options_.DynamoDBGrrSourcePitrOptions.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_backup_id,
            val_continuous_backup,
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
