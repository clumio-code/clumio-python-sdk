#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3VersioningOutput')


class S3VersioningOutput:
    """Implementation of the 'S3VersioningOutput' model.

    The AWS versioning output of the bucket.

    Attributes:
        mfa_delete:
            Specifies whether MFA delete is enabled in the bucket versioning configuration.
        status:
            The versioning state of the bucket.
    """

    # Create a mapping from Model property names to API property names
    _names = {'mfa_delete': 'mfa_delete', 'status': 'status'}

    def __init__(self, mfa_delete: str = None, status: str = None) -> None:
        """Constructor for the S3VersioningOutput class."""

        # Initialize members of the class
        self.mfa_delete: str = mfa_delete
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
        mfa_delete = dictionary.get('mfa_delete')
        status = dictionary.get('status')
        # Return an object of this model
        return cls(mfa_delete, status)
