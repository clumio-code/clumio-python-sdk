#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3AccessControlTranslation')


class S3AccessControlTranslation:
    """Implementation of the 'S3AccessControlTranslation' model.

    A container for information about access control for replicas.

    Attributes:
        owner:
            Specifies the replica ownership.
    """

    # Create a mapping from Model property names to API property names
    _names = {'owner': 'owner'}

    def __init__(self, owner: str = None) -> None:
        """Constructor for the S3AccessControlTranslation class."""

        # Initialize members of the class
        self.owner: str = owner

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
        owner = dictionary.get('owner')
        # Return an object of this model
        return cls(owner)
