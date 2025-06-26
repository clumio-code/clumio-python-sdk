#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='RestoreS3BucketSourcePitrOptions')


class RestoreS3BucketSourcePitrOptions:
    """Implementation of the 'RestoreS3BucketSourcePitrOptions' model.

    This field is required when the request type is 'Rollback'. The parameters for
    initiating a point in time restore.

    Attributes:
        restore_end_timestamp:
            The end timestamp to be restored in RFC-3339 format.
            Clumio restores objects modified before the given timestamp.
    """

    # Create a mapping from Model property names to API property names
    _names = {'restore_end_timestamp': 'restore_end_timestamp'}

    def __init__(self, restore_end_timestamp: str = None) -> None:
        """Constructor for the RestoreS3BucketSourcePitrOptions class."""

        # Initialize members of the class
        self.restore_end_timestamp: str = restore_end_timestamp

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
        restore_end_timestamp = dictionary.get('restore_end_timestamp')
        # Return an object of this model
        return cls(restore_end_timestamp)
