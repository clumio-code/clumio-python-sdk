#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='EC2MSSQLAGEmbedded')


class EC2MSSQLAGEmbedded:
    """Implementation of the 'EC2MSSQLAGEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        get_mssql_ec2_availability_group_backup_status_stats:
            availability group level backup status stats
        get_mssql_ec2_availability_group_stats:
            availability group level protection stats
        read_policy_definition:
            Embeds the associated policy of a protected resource in the response if
            requested using the `embed` query parameter. Unprotected resources will not have
            an associated policy.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'get_mssql_ec2_availability_group_backup_status_stats': 'get-mssql-ec2-availability-group-backup-status-stats',
        'get_mssql_ec2_availability_group_stats': 'get-mssql-ec2-availability-group-stats',
        'read_policy_definition': 'read-policy-definition',
    }

    def __init__(
        self,
        get_mssql_ec2_availability_group_backup_status_stats: object | None = None,
        get_mssql_ec2_availability_group_stats: object | None = None,
        read_policy_definition: object | None = None,
    ) -> None:
        """Constructor for the EC2MSSQLAGEmbedded class."""

        # Initialize members of the class
        self.get_mssql_ec2_availability_group_backup_status_stats: object | None = (
            get_mssql_ec2_availability_group_backup_status_stats
        )
        self.get_mssql_ec2_availability_group_stats: object | None = (
            get_mssql_ec2_availability_group_stats
        )
        self.read_policy_definition: object | None = read_policy_definition

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
        val = dictionary.get('get-mssql-ec2-availability-group-backup-status-stats', None)
        val_get_mssql_ec2_availability_group_backup_status_stats = val

        val = dictionary.get('get-mssql-ec2-availability-group-stats', None)
        val_get_mssql_ec2_availability_group_stats = val

        val = dictionary.get('read-policy-definition', None)
        val_read_policy_definition = val

        # Return an object of this model
        return cls(
            val_get_mssql_ec2_availability_group_backup_status_stats,
            val_get_mssql_ec2_availability_group_stats,
            val_read_policy_definition,
        )
