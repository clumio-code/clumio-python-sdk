#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamo_db_restore_source_backup_options
from clumioapi.models import dynamo_db_restore_source_pitr_options

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
    _names = {'continuous_backup': 'continuous_backup', 'securevault_backup': 'securevault_backup'}

    def __init__(
        self,
        continuous_backup: dynamo_db_restore_source_pitr_options.DynamoDBRestoreSourcePitrOptions = None,
        securevault_backup: dynamo_db_restore_source_backup_options.DynamoDBRestoreSourceBackupOptions = None,
    ) -> None:
        """Constructor for the DynamoDBTableRestoreSource class."""

        # Initialize members of the class
        self.continuous_backup: dynamo_db_restore_source_pitr_options.DynamoDBRestoreSourcePitrOptions = (
            continuous_backup
        )
        self.securevault_backup: dynamo_db_restore_source_backup_options.DynamoDBRestoreSourceBackupOptions = (
            securevault_backup
        )

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
        key = 'continuous_backup'
        continuous_backup = (
            dynamo_db_restore_source_pitr_options.DynamoDBRestoreSourcePitrOptions.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'securevault_backup'
        securevault_backup = (
            dynamo_db_restore_source_backup_options.DynamoDBRestoreSourceBackupOptions.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(continuous_backup, securevault_backup)
