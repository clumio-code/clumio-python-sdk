#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import tag2

T = TypeVar('T', bound='Tag2ListEmbedded')


class Tag2ListEmbedded:
    """Implementation of the 'Tag2ListEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        items:
            A collection of requested items.
    """

    # Create a mapping from Model property names to API property names
    _names = {'items': 'items'}

    def __init__(self, items: Sequence[tag2.Tag2] = None) -> None:
        """Constructor for the Tag2ListEmbedded class."""

        # Initialize members of the class
        self.items: Sequence[tag2.Tag2] = items

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
        items = None
        if dictionary.get('items'):
            items = list()
            for value in dictionary.get('items'):
                items.append(tag2.Tag2.from_dictionary(value))

        # Return an object of this model
        return cls(items)
