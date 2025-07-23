#
# Copyright 2023. Clumio, A Commvault Company.
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
    _names: dict[str, str] = {'owner': 'owner'}

    def __init__(self, owner: str | None = None) -> None:
        """Constructor for the S3AccessControlTranslation class."""

        # Initialize members of the class
        self.owner: str | None = owner

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
        val = dictionary.get('owner', None)
        val_owner = val

        # Return an object of this model
        return cls(
            val_owner,
        )
