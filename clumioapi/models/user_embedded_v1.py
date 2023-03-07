#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='UserEmbeddedV1')


class UserEmbeddedV1:
    """Implementation of the 'UserEmbeddedV1' model.

    Embedded responses related to the resource.

    Attributes:
        description:
            A description of the role.
        name:
            Unique name assigned to the role.
    """

    # Create a mapping from Model property names to API property names
    _names = {'description': 'description', 'name': 'name'}

    def __init__(self, description: str = None, name: str = None) -> None:
        """Constructor for the UserEmbeddedV1 class."""

        # Initialize members of the class
        self.description: str = description
        self.name: str = name

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
        description = dictionary.get('description')
        name = dictionary.get('name')
        # Return an object of this model
        return cls(description, name)
