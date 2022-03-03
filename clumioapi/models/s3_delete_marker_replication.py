#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3DeleteMarkerReplication')


class S3DeleteMarkerReplication:
    """Implementation of the 'S3DeleteMarkerReplication' model.

    Specifies whether Amazon S3 replicates delete markers.

    Attributes:
        status:
            Indicates whether to replicate delete markers.
    """

    # Create a mapping from Model property names to API property names
    _names = {'status': 'status'}

    def __init__(self, status: str = None) -> None:
        """Constructor for the S3DeleteMarkerReplication class."""

        # Initialize members of the class
        self.status: str = status

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
        status = dictionary.get('status')
        # Return an object of this model
        return cls(status)
