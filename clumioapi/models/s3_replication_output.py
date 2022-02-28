#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_replication_configuration

T = TypeVar('T', bound='S3ReplicationOutput')


class S3ReplicationOutput:
    """Implementation of the 'S3ReplicationOutput' model.

    The AWS replication output of the bucket.

    Attributes:
        replication_configuration:
            A container for replication rules with a maximum size
            of 2MB and a maximum of 1,000 rules.
    """

    # Create a mapping from Model property names to API property names
    _names = {'replication_configuration': 'replication_configuration'}

    def __init__(
        self,
        replication_configuration: s3_replication_configuration.S3ReplicationConfiguration = None,
    ) -> None:
        """Constructor for the S3ReplicationOutput class."""

        # Initialize members of the class
        self.replication_configuration: s3_replication_configuration.S3ReplicationConfiguration = (
            replication_configuration
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
        key = 'replication_configuration'
        replication_configuration = (
            s3_replication_configuration.S3ReplicationConfiguration.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(replication_configuration)
