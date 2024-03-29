#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ProtectionGroupRestoreSourcePitrOptions')


class ProtectionGroupRestoreSourcePitrOptions:
    """Implementation of the 'ProtectionGroupRestoreSourcePitrOptions' model.

    The parameters for initiating a point in time restore.<br>Note that only one of
    `backup_id` or `pitr` must be given.

    Attributes:
        protection_group_id:
            Clumio-assigned ID of protection group, representing the
            protection group to restore from. Use the
            [GET /datasources/protection-groups](#operation/list-protection-group)
            endpoint to fetch valid values.
        restore_end_timestamp:
            The end timestamp to be restored in RFC-3339 format.
            Clumio restores last objects modified before the given time.
            If `restore_end_timestamp` is given without `restore_start_timestamp`,
            it is the same as point in time restore.
        restore_start_timestamp:
            The start timestamp to be restored in RFC-3339 format.
            Clumio restores objects modified since the given time.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'protection_group_id': 'protection_group_id',
        'restore_end_timestamp': 'restore_end_timestamp',
        'restore_start_timestamp': 'restore_start_timestamp',
    }

    def __init__(
        self,
        protection_group_id: str = None,
        restore_end_timestamp: str = None,
        restore_start_timestamp: str = None,
    ) -> None:
        """Constructor for the ProtectionGroupRestoreSourcePitrOptions class."""

        # Initialize members of the class
        self.protection_group_id: str = protection_group_id
        self.restore_end_timestamp: str = restore_end_timestamp
        self.restore_start_timestamp: str = restore_start_timestamp

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
        protection_group_id = dictionary.get('protection_group_id')
        restore_end_timestamp = dictionary.get('restore_end_timestamp')
        restore_start_timestamp = dictionary.get('restore_start_timestamp')
        # Return an object of this model
        return cls(protection_group_id, restore_end_timestamp, restore_start_timestamp)
