#
# Copyright 2023. Clumio, Inc.
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
    _names = {'key': 'key', 'value': 'value'}

    def __init__(self, key: str = None, value: str = None) -> None:
        """Constructor for the Tag class."""

        # Initialize members of the class
        self.key: str = key
        self.value: str = value

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
        key = dictionary.get('key')
        value = dictionary.get('value')
        # Return an object of this model
        return cls(key, value)
