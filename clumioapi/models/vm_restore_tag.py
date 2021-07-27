#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='VMRestoreTag')


class VMRestoreTag:
    """Implementation of the 'VMRestoreTag' model.

    Attributes:
        tag_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the tag.
    """

    # Create a mapping from Model property names to API property names
    _names = {'tag_id': 'tag_id'}

    def __init__(self, tag_id: str = None) -> None:
        """Constructor for the VMRestoreTag class."""

        # Initialize members of the class
        self.tag_id: str = tag_id

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
        tag_id = dictionary.get('tag_id')
        # Return an object of this model
        return cls(tag_id)
