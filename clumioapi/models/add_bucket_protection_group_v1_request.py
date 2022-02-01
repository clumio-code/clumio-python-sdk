#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AddBucketProtectionGroupV1Request')


class AddBucketProtectionGroupV1Request:
    """Implementation of the 'AddBucketProtectionGroupV1Request' model.

    Attributes:
        bucket_id:

    """

    # Create a mapping from Model property names to API property names
    _names = {'bucket_id': 'bucket_id'}

    def __init__(self, bucket_id: str = None) -> None:
        """Constructor for the AddBucketProtectionGroupV1Request class."""

        # Initialize members of the class
        self.bucket_id: str = bucket_id

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
        bucket_id = dictionary.get('bucket_id')
        # Return an object of this model
        return cls(bucket_id)
