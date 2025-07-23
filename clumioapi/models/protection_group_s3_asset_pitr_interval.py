#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ProtectionGroupS3AssetPitrInterval')


class ProtectionGroupS3AssetPitrInterval:
    """Implementation of the 'ProtectionGroupS3AssetPitrInterval' model.

    Attributes:
        end_timestamp:
            The end time of the interval, represented in RFC3339 format.
        start_timestamp:
            The start time of the interval, represented in RFC3339 format.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'end_timestamp': 'end_timestamp',
        'start_timestamp': 'start_timestamp',
    }

    def __init__(
        self, end_timestamp: str | None = None, start_timestamp: str | None = None
    ) -> None:
        """Constructor for the ProtectionGroupS3AssetPitrInterval class."""

        # Initialize members of the class
        self.end_timestamp: str | None = end_timestamp
        self.start_timestamp: str | None = start_timestamp

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
        val = dictionary.get('end_timestamp', None)
        val_end_timestamp = val

        val = dictionary.get('start_timestamp', None)
        val_start_timestamp = val

        # Return an object of this model
        return cls(
            val_end_timestamp,
            val_start_timestamp,
        )
