#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='DynamoDBRestoreSourceBackupOptions')


class DynamoDBRestoreSourceBackupOptions:
    """Implementation of the 'DynamoDBRestoreSourceBackupOptions' model.

    The parameters for initiating a DynamoDB table restore from a backup.

    Attributes:
        backup_id:
            The Clumio-assigned ID of the DynamoDB table backup to be restored. Use the
            [GET /backups/aws/dynamodb-tables](#operation/list-backup-aws-dynamodb-tables)
            endpoint to fetch valid values.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'backup_id': 'backup_id'}

    def __init__(self, backup_id: str) -> None:
        """Constructor for the DynamoDBRestoreSourceBackupOptions class."""

        # Initialize members of the class
        self.backup_id: str = backup_id

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
        val = dictionary['backup_id']
        val_backup_id = val

        # Return an object of this model
        return cls(
            val_backup_id,  # type: ignore
        )
