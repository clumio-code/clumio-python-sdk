#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3InstantAccessSourcePitrOptions')


class S3InstantAccessSourcePitrOptions:
    """Implementation of the 'S3InstantAccessSourcePitrOptions' model.

    The parameters to initiate a point-in-time creation of S3 instant access
    endpoint.<br>Note that only one of either `backup_id` or `pitr` must be
    provided.

    Attributes:
        restore_end_timestamp:
            The end time of the period in which the objects must be restored in RFC-3339
            format.
            Objects modified before this given time will be restored.
            If `restore_end_timestamp` is provided without `restore_start_timestamp`, then
            it is the same
            as a point-in-time restore.
        restore_start_timestamp:
            The start time of the period in which the objects must be restored in RFC-3339
            format.
            Objects modified since the given time will be restored.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'restore_end_timestamp': 'restore_end_timestamp',
        'restore_start_timestamp': 'restore_start_timestamp',
    }

    def __init__(self, restore_end_timestamp: str, restore_start_timestamp: str) -> None:
        """Constructor for the S3InstantAccessSourcePitrOptions class."""

        # Initialize members of the class
        self.restore_end_timestamp: str = restore_end_timestamp
        self.restore_start_timestamp: str = restore_start_timestamp

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
        val = dictionary['restore_end_timestamp']
        val_restore_end_timestamp = val

        val = dictionary['restore_start_timestamp']
        val_restore_start_timestamp = val

        # Return an object of this model
        return cls(
            val_restore_end_timestamp,  # type: ignore
            val_restore_start_timestamp,  # type: ignore
        )
