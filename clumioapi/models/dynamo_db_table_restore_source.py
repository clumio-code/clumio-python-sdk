#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    dynamo_db_restore_source_backup_options as dynamo_db_restore_source_backup_options_
from clumioapi.models import \
    dynamo_db_restore_source_pitr_options as dynamo_db_restore_source_pitr_options_

T = TypeVar('T', bound='DynamoDBTableRestoreSource')


class DynamoDBTableRestoreSource:
    """Implementation of the 'DynamoDBTableRestoreSource' model.

    The DynamoDB table restore backup or point-in-time restore options. Only one of
    these fields should be set.

    Attributes:
        continuous_backup:
            The parameters for initiating a DynamoDB table point-in-time restore.
            Only one of `timestamp` or `use_latest_restorable_time` should be set.
        securevault_backup:
            The parameters for initiating a DynamoDB table restore from a backup.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'continuous_backup': 'continuous_backup',
        'securevault_backup': 'securevault_backup',
    }

    def __init__(
        self,
        continuous_backup: dynamo_db_restore_source_pitr_options_.DynamoDBRestoreSourcePitrOptions,
        securevault_backup: dynamo_db_restore_source_backup_options_.DynamoDBRestoreSourceBackupOptions,
    ) -> None:
        """Constructor for the DynamoDBTableRestoreSource class."""

        # Initialize members of the class
        self.continuous_backup: (
            dynamo_db_restore_source_pitr_options_.DynamoDBRestoreSourcePitrOptions
        ) = continuous_backup
        self.securevault_backup: (
            dynamo_db_restore_source_backup_options_.DynamoDBRestoreSourceBackupOptions
        ) = securevault_backup

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
        val = dictionary['continuous_backup']
        val_continuous_backup = (
            dynamo_db_restore_source_pitr_options_.DynamoDBRestoreSourcePitrOptions.from_dictionary(
                val
            )
        )

        val = dictionary['securevault_backup']
        val_securevault_backup = dynamo_db_restore_source_backup_options_.DynamoDBRestoreSourceBackupOptions.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_continuous_backup,  # type: ignore
            val_securevault_backup,  # type: ignore
        )
