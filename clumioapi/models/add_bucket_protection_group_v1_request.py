#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AddBucketProtectionGroupV1Request')


class AddBucketProtectionGroupV1Request:
    """Implementation of the 'AddBucketProtectionGroupV1Request' model.

    Attributes:
        bucket_id:

    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'bucket_id': 'bucket_id'}

    def __init__(self, bucket_id: str | None = None) -> None:
        """Constructor for the AddBucketProtectionGroupV1Request class."""

        # Initialize members of the class
        self.bucket_id: str | None = bucket_id

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
        val = dictionary.get('bucket_id', None)
        val_bucket_id = val

        # Return an object of this model
        return cls(
            val_bucket_id,
        )
