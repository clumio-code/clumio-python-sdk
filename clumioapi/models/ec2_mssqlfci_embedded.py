#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='EC2MSSQLFCIEmbedded')


class EC2MSSQLFCIEmbedded:
    """Implementation of the 'EC2MSSQLFCIEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        get_ec2_mssql_failover_cluster_backup_status_stats:
            FCIBackupStatusStats contain information about the backup status of the
            databases in the cluster
        get_ec2_mssql_failover_cluster_hosts_info:
            ConnectedHostsInfo contains information about the hosts associated with the
            cluster
        get_ec2_mssql_failover_cluster_stats:
            FCIStats contain information about the compliant databases in the cluster
        read_policy_definition:
            Embeds the associated policy of a protected resource in the response if
            requested using the `embed` query parameter. Unprotected resources will not have
            an associated policy.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'get_ec2_mssql_failover_cluster_backup_status_stats': 'get-ec2-mssql-failover-cluster-backup-status-stats',
        'get_ec2_mssql_failover_cluster_hosts_info': 'get-ec2-mssql-failover-cluster-hosts-info',
        'get_ec2_mssql_failover_cluster_stats': 'get-ec2-mssql-failover-cluster-stats',
        'read_policy_definition': 'read-policy-definition',
    }

    def __init__(
        self,
        get_ec2_mssql_failover_cluster_backup_status_stats: object = None,
        get_ec2_mssql_failover_cluster_hosts_info: object = None,
        get_ec2_mssql_failover_cluster_stats: object = None,
        read_policy_definition: object = None,
    ) -> None:
        """Constructor for the EC2MSSQLFCIEmbedded class."""

        # Initialize members of the class
        self.get_ec2_mssql_failover_cluster_backup_status_stats: object = (
            get_ec2_mssql_failover_cluster_backup_status_stats
        )
        self.get_ec2_mssql_failover_cluster_hosts_info: object = (
            get_ec2_mssql_failover_cluster_hosts_info
        )
        self.get_ec2_mssql_failover_cluster_stats: object = get_ec2_mssql_failover_cluster_stats
        self.read_policy_definition: object = read_policy_definition

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
        get_ec2_mssql_failover_cluster_backup_status_stats = dictionary.get(
            'get-ec2-mssql-failover-cluster-backup-status-stats'
        )
        get_ec2_mssql_failover_cluster_hosts_info = dictionary.get(
            'get-ec2-mssql-failover-cluster-hosts-info'
        )
        get_ec2_mssql_failover_cluster_stats = dictionary.get(
            'get-ec2-mssql-failover-cluster-stats'
        )
        read_policy_definition = dictionary.get('read-policy-definition')
        # Return an object of this model
        return cls(
            get_ec2_mssql_failover_cluster_backup_status_stats,
            get_ec2_mssql_failover_cluster_hosts_info,
            get_ec2_mssql_failover_cluster_stats,
            read_policy_definition,
        )
