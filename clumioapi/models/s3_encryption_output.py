#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    s3_server_side_encryption_configuration as s3_server_side_encryption_configuration_

T = TypeVar('T', bound='S3EncryptionOutput')


class S3EncryptionOutput:
    """Implementation of the 'S3EncryptionOutput' model.

    The AWS encryption output of the bucket.

    Attributes:
        server_side_encryption_configuration:
            Specifies the default server-side-encryption configuration.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'server_side_encryption_configuration': 'server_side_encryption_configuration'
    }

    def __init__(
        self,
        server_side_encryption_configuration: (
            s3_server_side_encryption_configuration_.S3ServerSideEncryptionConfiguration | None
        ) = None,
    ) -> None:
        """Constructor for the S3EncryptionOutput class."""

        # Initialize members of the class
        self.server_side_encryption_configuration: (
            s3_server_side_encryption_configuration_.S3ServerSideEncryptionConfiguration | None
        ) = server_side_encryption_configuration

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
        val = dictionary.get('server_side_encryption_configuration', None)
        val_server_side_encryption_configuration = s3_server_side_encryption_configuration_.S3ServerSideEncryptionConfiguration.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_server_side_encryption_configuration,
        )
