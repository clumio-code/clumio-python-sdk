#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='SetBucketPropertiesV1Request')


class SetBucketPropertiesV1Request:
    """Implementation of the 'SetBucketPropertiesV1Request' model.

    The set of properties that are being updated for the given bucket.

    Attributes:
        event_bridge_enabled:
            True if enabling the bucket for continuous backup, false if disabling
    """

    # Create a mapping from Model property names to API property names
    _names = {'event_bridge_enabled': 'event_bridge_enabled'}

    def __init__(self, event_bridge_enabled: bool = None) -> None:
        """Constructor for the SetBucketPropertiesV1Request class."""

        # Initialize members of the class
        self.event_bridge_enabled: bool = event_bridge_enabled

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
        event_bridge_enabled = dictionary.get('event_bridge_enabled')
        # Return an object of this model
        return cls(event_bridge_enabled)
