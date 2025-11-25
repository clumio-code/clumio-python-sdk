#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    dynamo_db_restore_source_backup_options as dynamo_db_restore_source_backup_options_
from clumioapi.models import \
    dynamo_db_restore_source_pitr_options as dynamo_db_restore_source_pitr_options_
import requests

T = TypeVar('T', bound='DynamoDBTableRestoreSource')


@dataclasses.dataclass
class DynamoDBTableRestoreSource:
    """Implementation of the 'DynamoDBTableRestoreSource' model.

    The DynamoDB table restore backup or point-in-time restore options. Only one of
    these fields should be set.

    Attributes:
        ContinuousBackup:
            The parameters for initiating a dynamodb table point-in-time restore.
            only one of `timestamp` or `use_latest_restorable_time` should be set.

        SecurevaultBackup:
            The parameters for initiating a dynamodb table restore from a backup.

    """

    ContinuousBackup: (
        dynamo_db_restore_source_pitr_options_.DynamoDBRestoreSourcePitrOptions | None
    ) = None
    SecurevaultBackup: (
        dynamo_db_restore_source_backup_options_.DynamoDBRestoreSourceBackupOptions | None
    ) = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

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
        val = dictionary.get('continuous_backup', None)
        val_continuous_backup = (
            dynamo_db_restore_source_pitr_options_.DynamoDBRestoreSourcePitrOptions.from_dictionary(
                val
            )
        )

        val = dictionary.get('securevault_backup', None)
        val_securevault_backup = dynamo_db_restore_source_backup_options_.DynamoDBRestoreSourceBackupOptions.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_continuous_backup,
            val_securevault_backup,
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
