#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='StreamSpecification')


class StreamSpecification:
    """Implementation of the 'StreamSpecification' model.

    Represents the DynamoDB Streams configuration for a table in DynamoDB.and the
    data type (`S` for string, `N` for number, `B` for binary).

    Attributes:
        enabled:
            Indicates whether DynamoDB Streams is enabled (true) or disabled (false)
            on the table.
        view_type:
            When an item in the table is modified, ViewType determines what information
            is written to the stream for this table. Valid values for ViewType
            are:

            KEYS_ONLY - Only the key attributes of the modified item are written
            to the stream.

            NEW_IMAGE - The entire item, as it appears after it was modified, is
            written to the stream.

            OLD_IMAGE - The entire item, as it appeared before it was modified,
            is written to the stream.

            NEW_AND_OLD_IMAGES - Both the new and the old item images of the item
            are written to the stream.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'enabled': 'enabled', 'view_type': 'view_type'}

    def __init__(self, enabled: bool | None = None, view_type: str | None = None) -> None:
        """Constructor for the StreamSpecification class."""

        # Initialize members of the class
        self.enabled: bool | None = enabled
        self.view_type: str | None = view_type

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
        val = dictionary.get('enabled', None)
        val_enabled = val

        val = dictionary.get('view_type', None)
        val_view_type = val

        # Return an object of this model
        return cls(
            val_enabled,
            val_view_type,
        )
