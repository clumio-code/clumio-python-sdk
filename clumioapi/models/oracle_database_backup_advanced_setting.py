#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='OracleDatabaseBackupAdvancedSetting')


class OracleDatabaseBackupAdvancedSetting:
    """Implementation of the 'OracleDatabaseBackupAdvancedSetting' model.

    Additional policy configuration settings for the `oracle_database_backup`
    operation. If this operation is not of type `oracle_database_backup`, then this
    field is omitted from the response.

    Attributes:
        alternative_replica:
            The alternative replica for Oracle database backups. This setting only applies
            to Data Guard databases. Valid values are: `primary`, `standby`, and `stop`.
            If `"stop"` is provided, then backups will not attempt to switch to a different
            replica when the preferred replica is unavailable.
        preferred_replica:
            The primary preferred replica for Oracle database backups. This setting only
            applies to Data Guard databases. Valid values are: `primary`, and `standby`.
            Recurring backup will first attempt to use either the primary replica or the
            secondary replica accordingly.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'alternative_replica': 'alternative_replica',
        'preferred_replica': 'preferred_replica',
    }

    def __init__(
        self, alternative_replica: str | None = None, preferred_replica: str | None = None
    ) -> None:
        """Constructor for the OracleDatabaseBackupAdvancedSetting class."""

        # Initialize members of the class
        self.alternative_replica: str | None = alternative_replica
        self.preferred_replica: str | None = preferred_replica

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

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('alternative_replica', None)
        val_alternative_replica = val

        val = dictionary.get('preferred_replica', None)
        val_preferred_replica = val

        # Return an object of this model
        return cls(
            val_alternative_replica,
            val_preferred_replica,
        )
