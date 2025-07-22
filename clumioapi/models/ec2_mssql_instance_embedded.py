#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='EC2MSSQLInstanceEmbedded')


class EC2MSSQLInstanceEmbedded:
    """Implementation of the 'EC2MSSQLInstanceEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        get_ec2_mssql_instance_backup_status_stats:
            Stats pertaining to the backup status of the EC2 MSSQL Instance.
        get_ec2_mssql_instance_stats:
            Stats pertaining to the EC2 MSSQL Instance.
        read_policy_definition:
            Embeds the associated policy of a protected resource in the response if
            requested using the `embed` query parameter. Unprotected resources will not have
            an associated policy.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'get_ec2_mssql_instance_backup_status_stats': 'get-ec2-mssql-instance-backup-status-stats',
        'get_ec2_mssql_instance_stats': 'get-ec2-mssql-instance-stats',
        'read_policy_definition': 'read-policy-definition',
    }

    def __init__(
        self,
        get_ec2_mssql_instance_backup_status_stats: object,
        get_ec2_mssql_instance_stats: object,
        read_policy_definition: object,
    ) -> None:
        """Constructor for the EC2MSSQLInstanceEmbedded class."""

        # Initialize members of the class
        self.get_ec2_mssql_instance_backup_status_stats: object = (
            get_ec2_mssql_instance_backup_status_stats
        )
        self.get_ec2_mssql_instance_stats: object = get_ec2_mssql_instance_stats
        self.read_policy_definition: object = read_policy_definition

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
        val = dictionary['get-ec2-mssql-instance-backup-status-stats']
        val_get_ec2_mssql_instance_backup_status_stats = val

        val = dictionary['get-ec2-mssql-instance-stats']
        val_get_ec2_mssql_instance_stats = val

        val = dictionary['read-policy-definition']
        val_read_policy_definition = val

        # Return an object of this model
        return cls(
            val_get_ec2_mssql_instance_backup_status_stats,  # type: ignore
            val_get_ec2_mssql_instance_stats,  # type: ignore
            val_read_policy_definition,  # type: ignore
        )
