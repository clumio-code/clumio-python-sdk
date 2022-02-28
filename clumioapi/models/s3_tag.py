#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3Tag')


class S3Tag:
    """Implementation of the 'S3Tag' model.

    A container of a key value name pair.

    Attributes:
        key:
            Name of the object key.
        value:
            Value of the tag.
    """

    # Create a mapping from Model property names to API property names
    _names = {'key': 'key', 'value': 'value'}

    def __init__(self, key: str = None, value: str = None) -> None:
        """Constructor for the S3Tag class."""

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
