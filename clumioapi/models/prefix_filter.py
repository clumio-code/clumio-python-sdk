#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='PrefixFilter')


class PrefixFilter:
    """Implementation of the 'PrefixFilter' model.

    PrefixFilter

    Attributes:
        excluded_sub_prefixes:
            List of subprefixes to exclude from the prefix.
        prefix:
            Prefix to include.
    """

    # Create a mapping from Model property names to API property names
    _names = {'excluded_sub_prefixes': 'excluded_sub_prefixes', 'prefix': 'prefix'}

    def __init__(self, excluded_sub_prefixes: Sequence[str] = None, prefix: str = None) -> None:
        """Constructor for the PrefixFilter class."""

        # Initialize members of the class
        self.excluded_sub_prefixes: Sequence[str] = excluded_sub_prefixes
        self.prefix: str = prefix

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
        excluded_sub_prefixes = dictionary.get('excluded_sub_prefixes')
        prefix = dictionary.get('prefix')
        # Return an object of this model
        return cls(excluded_sub_prefixes, prefix)
