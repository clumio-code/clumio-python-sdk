#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_server_side_encryption_configuration

T = TypeVar('T', bound='S3EncryptionOutput')


class S3EncryptionOutput:
    """Implementation of the 'S3EncryptionOutput' model.

    The AWS encryption output of the bucket.

    Attributes:
        server_side_encryption_configuration:
            Specifies the default server-side-encryption configuration.
    """

    # Create a mapping from Model property names to API property names
    _names = {'server_side_encryption_configuration': 'server_side_encryption_configuration'}

    def __init__(
        self,
        server_side_encryption_configuration: s3_server_side_encryption_configuration.S3ServerSideEncryptionConfiguration = None,
    ) -> None:
        """Constructor for the S3EncryptionOutput class."""

        # Initialize members of the class
        self.server_side_encryption_configuration: s3_server_side_encryption_configuration.S3ServerSideEncryptionConfiguration = (
            server_side_encryption_configuration
        )

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
        key = 'server_side_encryption_configuration'
        server_side_encryption_configuration = (
            s3_server_side_encryption_configuration.S3ServerSideEncryptionConfiguration.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(server_side_encryption_configuration)
