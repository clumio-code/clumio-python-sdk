#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='Tag')


class Tag:
    """Implementation of the 'Tag' model.

    The asset tags to be filtered. This is supported for AWS assets only.

    Attributes:
        key:
            The key of tag to filter.
        value:
            The value of tag to filter.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'key': 'key', 'value': 'value'}

    def __init__(self, key: str | None = None, value: str | None = None) -> None:
        """Constructor for the Tag class."""

        # Initialize members of the class
        self.key: str | None = key
        self.value: str | None = value

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
        val = dictionary.get('key', None)
        val_key = val

        val = dictionary.get('value', None)
        val_value = val

        # Return an object of this model
        return cls(
            val_key,
            val_value,
        )
