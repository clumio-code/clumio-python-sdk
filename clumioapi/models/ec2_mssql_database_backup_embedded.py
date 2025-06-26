#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='EC2MSSQLDatabaseBackupEmbedded')


class EC2MSSQLDatabaseBackupEmbedded:
    """Implementation of the 'EC2MSSQLDatabaseBackupEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        read_aws_environment:
            Embed information for AWS Environment details
    """

    # Create a mapping from Model property names to API property names
    _names = {'read_aws_environment': 'read-aws-environment'}

    def __init__(self, read_aws_environment: object = None) -> None:
        """Constructor for the EC2MSSQLDatabaseBackupEmbedded class."""

        # Initialize members of the class
        self.read_aws_environment: object = read_aws_environment

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
        read_aws_environment = dictionary.get('read-aws-environment')
        # Return an object of this model
        return cls(read_aws_environment)
