#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AWSEnvironmentEmbedded')


class AWSEnvironmentEmbedded:
    """Implementation of the 'AWSEnvironmentEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        read_aws_environments_backup_status_stats:
            Backup statistics for each AWS environment.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'read_aws_environments_backup_status_stats': 'read-aws-environments-backup-status-stats'
    }

    def __init__(self, read_aws_environments_backup_status_stats: object) -> None:
        """Constructor for the AWSEnvironmentEmbedded class."""

        # Initialize members of the class
        self.read_aws_environments_backup_status_stats: object = (
            read_aws_environments_backup_status_stats
        )

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

        # Extract variables from the dictionary
        val = dictionary['read-aws-environments-backup-status-stats']
        val_read_aws_environments_backup_status_stats = val

        # Return an object of this model
        return cls(
            val_read_aws_environments_backup_status_stats,  # type: ignore
        )
