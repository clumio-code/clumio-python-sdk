#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='EC2MSSQLDatabaseBackupAdvancedSetting')


class EC2MSSQLDatabaseBackupAdvancedSetting:
    """Implementation of the 'EC2MSSQLDatabaseBackupAdvancedSetting' model.

    Additional policy configuration settings for the `ec2_mssql_database_backup`
    operation. If this operation is not of type `ec2_mssql_database_backup`, then
    this field is omitted from the response.

    Attributes:
        alternative_replica:
            The alternative replica for MSSQL database backups. This setting only applies to
            Availability Group databases. Possible values include `"primary"`,
            `"sync_secondary"`, and `"stop"`. If `"stop"` is provided, then backups will not
            attempt to switch to a different replica when the preferred replica is
            unavailable. Otherwise, recurring backups will attempt to use either the primary
            replica or the secondary replica accordingly.
        preferred_replica:
            The primary preferred replica for MSSQL database backups. This setting only
            applies to Availability Group databases. Possible values include `"primary"` and
            `"sync_secondary"`. Recurring backup will first attempt to use either the
            primary replica or the secondary replica accordingly.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'alternative_replica': 'alternative_replica',
        'preferred_replica': 'preferred_replica',
    }

    def __init__(self, alternative_replica: str = None, preferred_replica: str = None) -> None:
        """Constructor for the EC2MSSQLDatabaseBackupAdvancedSetting class."""

        # Initialize members of the class
        self.alternative_replica: str = alternative_replica
        self.preferred_replica: str = preferred_replica

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
        alternative_replica = dictionary.get('alternative_replica')
        preferred_replica = dictionary.get('preferred_replica')
        # Return an object of this model
        return cls(alternative_replica, preferred_replica)
