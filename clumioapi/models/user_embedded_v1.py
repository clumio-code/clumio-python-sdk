#
# Copyright 2023. Clumio, A Commvault Company.
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
    _names: dict[str, str] = {'description': 'description', 'name': 'name'}

    def __init__(self, description: str, name: str) -> None:
        """Constructor for the UserEmbeddedV1 class."""

        # Initialize members of the class
        self.description: str = description
        self.name: str = name

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

        # Extract variables from the dictionary
        val = dictionary['description']
        val_description = val

        val = dictionary['name']
        val_name = val

        # Return an object of this model
        return cls(
            val_description,  # type: ignore
            val_name,  # type: ignore
        )
