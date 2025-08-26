#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3ExistingObjectReplication')


class S3ExistingObjectReplication:
    """Implementation of the 'S3ExistingObjectReplication' model.

    Configuration to replicate existing source bucket objects.

    Attributes:
        status:
            Specifies whether the existing object replication is enabled.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'status': 'status'}

    def __init__(self, status: str | None = None) -> None:
        """Constructor for the S3ExistingObjectReplication class."""

        # Initialize members of the class
        self.status: str | None = status

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
        val = dictionary.get('status', None)
        val_status = val

        # Return an object of this model
        return cls(
            val_status,
        )
