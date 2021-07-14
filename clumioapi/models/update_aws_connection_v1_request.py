#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='UpdateAwsConnectionV1Request')


class UpdateAwsConnectionV1Request:
    """Implementation of the 'UpdateAwsConnectionV1Request' model.

    Attributes:
        description:
            An optional, user-provided description for this connection.
    """

    # Create a mapping from Model property names to API property names
    _names = {'description': 'description'}

    def __init__(self, description: str = None) -> None:
        """Constructor for the UpdateAwsConnectionV1Request class."""

        # Initialize members of the class
        self.description: str = description

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
        # Return an object of this model
        return cls(description)
