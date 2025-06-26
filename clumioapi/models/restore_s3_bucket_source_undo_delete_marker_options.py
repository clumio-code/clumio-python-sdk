#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='RestoreS3BucketSourceUndoDeleteMarkerOptions')


class RestoreS3BucketSourceUndoDeleteMarkerOptions:
    """Implementation of the 'RestoreS3BucketSourceUndoDeleteMarkerOptions' model.

    This field is required when the request type is 'Undo delete marker'.

    Attributes:
        start_timestamp:
            The start timestamp for undo delete marker in RFC-3339 format.
            Clumio undoes the delete markers created after the given timestamp.
    """

    # Create a mapping from Model property names to API property names
    _names = {'start_timestamp': 'start_timestamp'}

    def __init__(self, start_timestamp: str = None) -> None:
        """Constructor for the RestoreS3BucketSourceUndoDeleteMarkerOptions class."""

        # Initialize members of the class
        self.start_timestamp: str = start_timestamp

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
        start_timestamp = dictionary.get('start_timestamp')
        # Return an object of this model
        return cls(start_timestamp)
