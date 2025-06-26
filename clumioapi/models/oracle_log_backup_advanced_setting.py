#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='OracleLogBackupAdvancedSetting')


class OracleLogBackupAdvancedSetting:
    """Implementation of the 'OracleLogBackupAdvancedSetting' model.

    Additional policy configuration settings for the `oracle_log_backup` operation.
    If this operation is not of type `oracle_log_backup`, then this field is omitted
    from the response.

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
    _names = {
        'alternative_replica': 'alternative_replica',
        'preferred_replica': 'preferred_replica',
    }

    def __init__(self, alternative_replica: str = None, preferred_replica: str = None) -> None:
        """Constructor for the OracleLogBackupAdvancedSetting class."""

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
